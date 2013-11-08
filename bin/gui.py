# Last modify Marcello 09/11/2013 

import optparse
from connect import connect
from datalogQuery import datalogQuery


# This is for defining execution options from command line
# In this example I've found if you write 
# "python gui.py --person Marcello" it returns "Hello Marcello"
def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world")
    options, arguments = p.parse_args()
    print ('Hello %s' % options.person)

    

#This is a function we should implement later with an eventual query to test DB status...
def status():
    print('\n### Status goes here ###')
    

    
#Also the help has to be done later
def help():
    print ('\n### Help goes here ###')
   

   
#Main section of the gui.py
if __name__ == '__main__':
    
    options = {
            '1' : connect,
            '2' : status,
            '3' : datalogQuery,
            '4' : help,
            'q' : quit
        }
        
    print ('''
---------------------------------
       Welcome to YADI 2
---------------------------------- ''')
    
    choice_text = '''
What would you like to do?
 1. connect to a database
 2. check the status of a database
 3. a Datalog query
 4. I need help...
 q. quit :(

> '''

    while True:
        choice = input(choice_text)
        if choice in options:
            options[choice]()
        else:
            print ('Option unavailable\n')
        