""" 
Datalog query console
Last modify:
	Marcello 12/11/2013
"""

from parseQuery import *


# For every input it calls the parser and show test results (for now)
def datalogQuery(string_to_parse = ''):

    datalog = Datalog()
    results = datalog.getParsingOf(string_to_parse)
  
  
    ### LOOPS FOR ACCESSING THE TREE### 
    # Get the type of request (query or rule)
    # Depending on the type we do a SELECT or a CREATE VIEW
    if results:
        if results.type:
            requestType =  results.type
            print("Got type >>> " +  requestType)
        
        # Get the head. 
        # Head contain the name of the view.
        # If type of request is query we get data from this view.
        # If type of request is rule we create a new view.
        if results.head:
            requestHead = results.head
            print("Got head > " + repr(requestHead))
     
        # Get the body. Body is a list of predicates and constraint we need for the WHERE clause
        if results.body:
            requestBody = results.body
            print("Got body > " + repr(requestBody))
        
        # Get a predicate from the body
        # We need to loop the predicates in order to create the WHERE clause
            for predicate in requestBody:
                print("\nGot a predicate.\n    Name >>>"+ repr(predicate.name))
                # To use the terms use
                print("    Terms >>>" + repr(predicate.terms))

        return results