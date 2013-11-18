""" 
Datalog query console
Last modify:
	Marcello 12/11/2013
"""

from parseQuery import *


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
        
        results = datalog.getParsingOf(string_to_parse)
      
        # Get the type of request (query or rule)
        # Depending on the type we do a SELECT or a CREATE VIEW
        requestType =  results.type
        print("Got type >>> " +  requestType)
        
        # Get the head. 
        # Head contain the name of the view.
        # If type of request is query we get data from this view.
        # If type of request is rule we create a new view.
        requestHead = results.head
        print("Got head > " + repr(requestHead))
     
        # Get the body. Body is a list of predicates and constraint we need for the WHERE clause
        requestBody = results.body
        print("Got body > " + repr(requestBody))
        
        # Get a predicate from the body
        # We need to loop the predicates in order to create the WHERE clause
        for predicate in requestBody:
            print("\nGot a predicate.\n    Name >>>"+ repr(predicate.name))
            # To use the terms use
            print("    Terms >>>" + repr(predicate.terms))
      
       
# Ephrem Berhe
# Transform string into columns name separatd with commas.
def getTermList(TermList):
    for term in TermList:
        if(term !='_'):
            Terms += term +","
    return Terms

    
def getConstantList(ConstantList):
    if len(ConstantList)==0:
        return ""
    else: 
        for cont in ConstantList:
            Constats += cont +","
            LastConst = " Where " + Constats	   
    return LastConst

    for rslt in results:
        Query="CREATE VIEW "+rslt.predicate+" AS SELECT " + getTermList(rslt.terms) + " From "+ rslt.predicate + getConstantList(ConstantList)	
        print (Query)	

