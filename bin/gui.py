""" 
Graphical (?) interface for YADI2
Last modify:
	Marcello 12/11/2013
"""

import sys, traceback
import optparse
from dbConnect import getConnection
from dbStatus import getStatus
from loopTree import printParsing
from translator import getTranslation
from scripting import *
from parsing import Datalog
from Myalchemy import Myalchemy



### GLOBAL VARIABLES ###
sql_session = None
connection_string = None
db_schema = None



### FUNCTIONS ###
# This is for execution options from command line
# In this example I've found, if you write 
# "python gui.py --person Marcello" it returns "Hello Marcello"
def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world")
    options, arguments = p.parse_args()
    print ('Hello %s' % options.person)



#This function returns a connection object
def connect():		
    hostname = 'localhost'
    port = '5432'
    username = 'postgres'
    password = 'root'
    dbname = 'adb'
    global connection_string
    connection_string = 'postgresql+psycopg2://' + username + ':' + password + '@' + hostname + ':' + port + '/' + dbname
    print('\nDefault connection string is:\n%s\n' % connection_string)
    answer = input("Would you like to use this setting? [Y/N] > ")   
    if answer.lower()=='n':
        while True:
            #Input connection parameters
            hostname = input('\nPlease enter the PostgreSQL server name or IP address:\n> ')
            port = input('\nPort:\n> ')
            username = input('\nUsername:\n> ')
            password = input('\nPassword:\n> ')
            dbname = input('\nDatabase name:\n> ')      
            if hostname and port and username and password and dbname:              	      	            	
                connection_string = 'postgresql+psycopg2://' + username + ':' + password + '@' + hostname + ':' + port + '/' + dbname 
                print('\nNew connection string:\n%s\n' % connection_string)
                break
            else:
                print ('\nAll fields are mandatory.')
    global sql_session
    sql_session = getConnection(connection_string)
    if sql_session:
        postgresalchemy = Myalchemy(connection_string)    	
        global db_schema
        db_schema = postgresalchemy.getDBSchema()
        #print(db['actor'][0]) -> name
        #print(db['actor'][1]) -> lastname
        #print(db['movies'][0]) -> title
        #print(db['Q'][0]) -> Key Error
        
      
#This function returns the status of the connection and prints out the schema
def status():
    getStatus(sql_session,connection_string)
   
    
    
#This function asks the user for a datalog query 
def datalog():
    if not sql_session or not db_schema:
        print ('\nPlease connect to a database.')
        return     
    while 1:
        try:
            string_to_parse = input('\nInsert Datalog query or rule.\n> ')
        except EOFError:
            break
        if not string_to_parse: 
            continue
        execute(string_to_parse)
       
       

# Display the scripting menu
def script():
    if not sql_session:
        print ('\nPlease connect to a database.')
        return
    options = {
            '1' : listScript,
            '2' : writeScript,
            '3' : displayScript,
            '4' : runScript
        }
    choice_text = '''
Scripting menu:
 1. list existing files
 2. write a script
 3. display a script
 4. execute a script
 b. back
 
> '''
    while True:
       choice = input(choice_text)
       if choice=='b': break
       if choice in options:
            options[choice]()
       else:
           print ('Option unavailable\n')  
    


# Run a script file line by line
def runScript():
    path = input('Enter file to run:\n> ')
    path = "script_files/"+path
    try:
        file = open(path, "r")
        for line in file:
            if line.strip():
                print("Executing " + line)
                execute(line.strip())
        file.close()        
    except FileNotFoundError:
        print("File not found!")
    except:
        print("Unexpected error:", sys.exc_info()[0])

   

# The function which does all the job
def execute(string_to_parse):
    
    #Parsing
    datalog = Datalog()
    parsing_results = datalog.getParsingOf(string_to_parse)
    if parsing_results == "error":
        print("\nParsing error. Please check datalog query format.")
        return False
    #Print parsing for debug 
    printParsing(parsing_results)
    
    
    #Translation into SQL 
    translation_results = getTranslation(db_schema, parsing_results)
    if not translation_results:
        print("\nTranslation error.")
        return False
    #Print translation for debug
    print("SQL: " + translation_results)
  
    
    #Execute query in Postgresql
    try:
        postgres_results = sql_session.execute(translation_results)   
    except:
        print("Error:", sys.exc_info()[0])
        traceback.print_exc(file=sys.stdout) 
        return False
    finally:
        sql_session.commit()     
     
    #Print results    
    if parsing_results.type=='query' and postgres_results:
        try:
            for row in postgres_results:
                print (row)
        except:
            print("Error:", sys.exc_info()[0])
            traceback.print_exc(file=sys.stdout) 
            return False
    print('Done!\n')

        
# The help has to be done later
def help():
    print ('\n### Help goes here ###') 
  
    
### MAIN SECTION ###
if __name__ == '__main__':

    #welcome message
    print ('''
---------------------------------
       Welcome to YADI 2
---------------------------------''')


    #connection 
    if not sql_session:
        connect()
     
    
    #user menu
    options = {
            '1' : connect,
            '2' : status,
            '3' : datalog,
            '4' : script,
            '5' : help,
            'q' : quit
        }
        
    choice_text = '''
What would you like to do?
 1. connect to a database
 2. check the status of the database
 3. Datalog query
 4. run a script file
 5. I need help...
 q. quit :(

> '''
  
    while True:
        choice = input(choice_text)
        if choice in options:
            options[choice]()
        else:
            print ('Option unavailable\n')
