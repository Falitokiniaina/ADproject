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
        requestType =  results.type
        print("\nTYPE") 
        print("    " + requestType)
        
        # Get the head. 
        # Head contain the name of the view.
        # If type of request is query we get data from this view.
        # If type of request is rule we create a new view.
        requestHead = results.head
        # Head is not iterable...only one predicate is there
        print("\nHEAD")
        print("    Name: "+ requestHead.name)
        print("    Terms: ") 
        for term in requestHead.terms:
            print("        " + term)
     
        # Get the body. Body is a list of predicates and constraint we need for the WHERE clause    
        # We need to loop the predicates in order to create the WHERE clause
        requestBody = results.body
        print("\nBODY")
        for predicate in requestBody:
            print("    Name: "+ predicate.name)
            print("    Is negated? " + repr(predicate.isNegated))  # use repr() to print a boolean value! 
            print("    Terms: ") 
            for term in predicate.terms:
                print("        " + term)
            print("\n")

        return results
    
    else:
        return "error" 