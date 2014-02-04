""" 
Graphical (?) interface for YADI2
Last modify:
	Marcello 12/11/2013
"""

import sys, traceback
import optparse
from dbConnect import getConnection
from dbStatus import *
from loopTree import printParsing
from translator import getTranslation
from scripting import *
from parsing import Datalog
from Myalchemy import Myalchemy
from utility import *



### GLOBAL VARIABLES ###
import globvar
""" Usage:
        globvar.sql_session
        globvar.connection_string
        globvar.db_schema 
"""



### FUNCTIONS ###
# This is for execution options from command line
# In this example I've found, if you write 
# "python gui.py --person Marcello" it returns "Hello Marcello"
def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world")
    options, arguments = p.parse_args()
    print ('Hello %s' % options.person)


#Clean the views and quit the application
 # def cleaning():
    #CleaningViews()
    # quit()


#This function returns a connection object
def connect():	
    getConnection()
    if globvar.sql_session:
        updateDbSchemaVar()
        #print(db_schema['actor'][0]) -> name
        #print(db_schema['actor'][1]) -> lastname
        #print(db_schema['movies'][0]) -> title
        #print(db_schema['Q'][0]) -> Key Error
        CleaningViews()
      
      
#This function returns the status of the connection and prints out the schema
def status():
    getStatus()
   
    
    
#This function asks the user for a datalog query 
def datalog():
    if not globvar.sql_session or not globvar.db_schema:
        print ('\nPlease connect to a database.')
        return     
    while 1:
        try:
            string_to_parse = input('\nInsert Datalog query or rule (q to quit)\n> ')
        except EOFError:
            break
        if not string_to_parse: 
            continue
        if string_to_parse == 'q':
            break
        execute(string_to_parse)
       
       

# Display the scripting menu
def script():
    if not globvar.sql_session:
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
    if not parsing_results or parsing_results == "error":
        print("\nParsing error. Please check datalog query format.")
        return False
    
    #Check safety
    if parsing_results.type=='rule':
        if CheckRelationName(parsing_results)=="Error":
            print("\nThere are no such relations in the database.")
            return False     
        elif CheckSafeRule(parsing_results)=="Error":
            print("\nThe rule is not safe.")
            return False
    elif parsing_results.type=='query' and CheckQueryName(parsing_results)=="Error":
        print("\nThere are no rules with such name.")
        return False
    
    # relationExist=CheckRelationName(parsing_results)
   
    # print(relationExist)
    # if 	relationExist=="Error":
        # print("\n There are no relations found in the database")
        # return False
	
	#Check if the query is safe
    # errorResult=SafeRule(parsing_results)
     
    # if errorResult=="Error":
        # print("\n Rule not safe.")
        # return False
	
    #Print parsing for debug 
    printParsing(parsing_results)
    
    
    #Translation into SQL 
    translation_results = getTranslation(parsing_results)
    if not translation_results:
        print("\nTranslation error.")
        return False
    #Print translation for debug
    print("\nSQL: " + translation_results)
  
    
    #Execute query in Postgresql
    try:
        postgres_results = globvar.sql_session.execute(translation_results)   
    except:
        print("Error:", sys.exc_info()[0])
        #traceback.print_exc(file=sys.stdout) 
        return False
    finally:
        globvar.sql_session.commit()     
     
     
    #Update globvar.db_schema variable if type=rule 
    if parsing_results.type=='rule':    
        updateDbSchemaVar()
        
     
    #Print results if type=query    
    if parsing_results.type=='query' and postgres_results:
        print('\n')
        try:
            flag = True
            count = 0
            for row in postgres_results:
                #Header
                if flag:
                    for column, value in row.items():
                        count = count + 1
                    print('-'*20*count)
                    for column, value in row.items():
                        print('{0: <20}'.format(column), end="")
                    print('')
                    print('-'*20*count)
                    flag=False
                #Content
                for column, value in row.items():
                    print('{0: <20}'.format(value), end="")
                print('')
            #Footer
            print('-'*20*count)
        except:
            print("Error:", sys.exc_info()[0])
            #traceback.print_exc(file=sys.stdout) 
            return False
    print('\nDone!\n')

        
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
    if not globvar.sql_session:
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
