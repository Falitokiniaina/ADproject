def getTranslation(sql_session, parsing_result):
    #do something here
    print('\n###Eprhems code here###')
    

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
