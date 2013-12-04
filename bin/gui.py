""" 
Graphical (?) interface for YADI2
Last modify:
	Marcello 12/11/2013
"""

import optparse
from connect import getConnection
from datalogQuery import datalogQuery
from translator import getTranslation
import sys
sys.path.append('../faly_files/')
from read_file import scriptFile
from checkConnect import checkConnect


### GLOBAL VARIABLES ###
sql_session = None
connection_string = None



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
    
    if answer.lower()=='y':
        while True:
            #insert parameters
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
    
    
    
#This function asks for a datalog query, parses it and returns the results 
def datalog():
    if not sql_session:
        print ('\nPlease connect to a database.')
        return
        
    while 1:
        try:
            string_to_parse = input('\nInsert Datalog query or rule.\n> ')
        except EOFError:
            break
        if not string_to_parse: 
            continue
        
        parsing_results = datalogQuery(string_to_parse)
        
        if parsing_results == "error":
            print("\nParsing error. Please check datalog query format.")
        else: 
            getTranslation(sql_session, parsing_results)
            ## PRINT FUNCTION HERE##
        
      
    
#This is a function we should implement later with an eventual query to test DB status...
def status():
    #print('\n### Status goes here ###') -> in checkConnect.py
    checkConnect(sql_session,connection_string)
    
#Also the help has to be done later
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
            '4' : help,
            '5' : scriptFile,
            'q' : quit
        }
        
    choice_text = '''
What would you like to do?
 1. connect to a database
 2. check the status of a database
 3. a Datalog query
 4. I need help...
 5. script Files,
 q. quit :(

> '''
  
    while True:
        choice = input(choice_text)
        if choice in options:
            options[choice]()
        else:
            print ('Option unavailable\n')
