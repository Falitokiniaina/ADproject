""" 
Datalog query console
Last modify:
	Marcello 12/11/2013
"""


### LOOPS FOR ACCESSING THE TREE###
def printParsing(parsing_results):
  
    #Do parsing
    # datalog = Datalog()
    # parsing_results = datalog.getParsingOf(string_to_parse)

    if not parsing_results:
        print("\nParsing error. Please check datalog query format.")
        return False
    else:
        # Get the type of request (query or rule)
        # Depending on the type we do a SELECT or a CREATE VIEW
        #if parsing_results:
        requestType =  parsing_results.type
        print("\nTYPE") 
        print("    " + requestType)
        
        # Get the head. 
        # Head contain the name of the view.
        # If type of request is query we get data from this view.
        # If type of request is rule we create a new view.
        requestHead = parsing_results.head
        # Head is not iterable...only one predicate is there
        print("\nHEAD")
        print("    Name: "+ requestHead.name)
        print("    Terms: ") 
        for term in requestHead.terms:
            print("        " + term)
     
        # Get the body. Body is a list of predicates and constraint we need for the WHERE clause    
        # We need to loop the predicates in order to create the WHERE clause
        requestBody = parsing_results.body
        print("\nBODY")
        for predicate in requestBody:
            print("    Name: "+ predicate.name)
            print("    Is negated? " + repr(predicate.isNegated))  # use repr() to print a boolean value! 
            print("    Terms: ") 
            for term in predicate.terms:
                print("        " + term)
            print("\n")

        return parsing_results