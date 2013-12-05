import psycopg2
import sys
def getTranslation(sql_session, parsing_result):
 CreateViews(sql_session, parsing_result)
 print('View Succssfully Created !')
	
	
def CountBody(requestBody):
 Count=0;
 for predicate in requestBody:
  Count=Count+1
 return Count
def GetTableName(requestBody):
 TableName=""
 for predicate in requestBody:
  TableName=predicate.name
 return TableName

	# new codes
def ExecuteQuery(sqlsession,selectStat):
    sqlsession.execute(selectStat)
    sqlsession.commit()
	 
def CreateViews(sqlcon, results):
   if results:
        requestType =  results.type
        
        
        # Get the head. 
        # Head contain the name of the view.
        # If type of request is query we get data from this view.
        # If type of request is rule we create a new view.
        requestHead = results.head
        # Head is  one predicate 
        #print("\----------------------------------------- New One")
        ViewName=requestHead.name
        HeadTerms="" 
        for term in requestHead.terms:
             HeadTerms=HeadTerms + term +','
        HeadTerms=HeadTerms[:len(HeadTerms)-1]
        CreateView= 'CREATE VIEW '+' '+ ViewName +' ' +' AS Select '+HeadTerms +' From '
		
        
        requestBody = results.body
        TotalBody=CountBody(requestBody)
        if(TotalBody==1):
            #print('One Header Only')
            FromTable=GetTableName(requestBody)
            CreateView=CreateView +' '+ FromTable
            ExecuteQuery(sqlcon,CreateView)
	     
        #print(CreateView)
		
        #print("\nBODY")
        #for predicate in requestBody:
         #   print("    Name: "+ predicate.name)
          #  print("    Is negated? " + repr(predicate.isNegated))  # use repr() to print a boolean value! 
           # print("    Terms: ") 
            #for term in predicate.terms:
             #   print("        " + term)
            #print("\n")
   
    
			 			 		
		
	  
