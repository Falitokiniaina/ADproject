""" 
Datalog query console
Last modify:
	Marcello 12/11/2013
"""

from parseQuery import Datalog


# For every input it calls the parser and show test results (for now)
def datalogQuery():

    datalog = Datalog()
    
    while 1:
        try:
            string_to_parse = input('\nInsert Datalog query:\n> ')
        except EOFError:
            break
        if not string_to_parse: 
            continue
        
        #TEST
        datalog.runTests(string_to_parse)
        
        # To get actual results uncomment this
        #results = datalog.getParsingOf(string_to_parse)
