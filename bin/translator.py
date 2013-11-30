import psycopg2
import sys
def getTranslation(sql_session, parsing_result):
	viewName=''
	#selectStat='CREATE OR REPLACE VIEW Ephrem AS  SELECT "Actor"."Name", "Actor"."LastName", "Actor".title_movie  FROM "Actor";'
	selectStat=Translated(parsing_result)
	whereClouse=''
	#print (selectStat)
	if('CREATE' in selectStat):
	 CreateViews(sql_session,selectStat)
	else:
	 DisplayData(selectStat,sql_session)
	print('Succssfully Done !')
	
	
              
    #
 
    

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
        #print (Query)	

		#Creat view here
def CreateViews(sqlsession,selectStat):

     
     sqlsession.execute(selectStat)
      
     sqlsession.commit()
def DisplayData(sql,Con):
  
 cursr.execute(sql)
  
 print(R) 
   
def QueryType(selectStat):
 #print('Query type called here')
 if(selectStat):
  if (selectStat.head):
   resultHead=selectStat.head
    
   # get the first part of the query 
   viewname=resultHead.name
   
    
   terms=repr(resultHead.terms)
   Term=GetTerms(terms,'')
   Term=Term[1:len(Term)-1]
       
 Qr='Select '+ ' '+ Term + ' From '+ viewname
 Qr=Qr.replace("'",'')
  
 return Qr
  
 
 

	 # get the datalog header names and number attributes to create view
def GetHeaderName(resultHead):

	#get name of the header
	 name=repr(resultHead.name)
	 #name=name[1:len(name)-1]
	 #get list of attributs names
	 Term=""
	 terms=repr(resultHead.terms)
	 Term=GetTerms(terms,'')
	 Term=Term[1:len(Term)-1] 
	 
	 Q='CREATE OR REPLACE VIEW '+name+' AS  SELECT ' + Term +' From '
	 #print('Header '+Q)
	 return Q
def GetTerms(terms,trm):

 Term=""
 if(trm==''):
  i=0
  while i<len(terms):
   Term=Term+terms[i]
   i=i+1
#remove the last comma
 else:
  i=0
  while i<len(terms):
   Term=Term+trm[0]+'.'+terms[i]
   i=i+1
  
  
  #Term=Term[1: len(Term)-1]
  
 return Term

	 #Length of the body to check if there are more than one predicates in the body
def BodyLength(requestBody):
 #print(len(requestBody))
 return len(requestBody)
 
 #multiple body or Predicates
def MultipleBody(requestBody):
	body=""
	names=""
	criteria=""
	TempRequestBody=requestBody
 # get name of the predicates in the body
	for bodyNames in requestBody:
		names=names+repr(bodyNames.name)+","
	AllTerms=""
	for bodyAtt in TempRequestBody:
		AllTerms=AllTerms +repr(bodyAtt.name)+','
	AllTerms=AllTerms[:len(AllTerms)-1]
  
	return AllTerms
 #print("all attributs in the body"+ AllTerms)
  
	 
def GetPredicateBody(resultBody):
	B=""
	#for predicate with only one predicate in the body
	if(BodyLength(resultBody)==1):
		B=repr(resultBody[0].name)
		#print('B is the only one using indexing')
		#print(B)
	else:
		print('More than two predicates not implemented Comming soooooooon')
		#for predicates with multiple predicate n the body going on.. not done
		B=MultipleBody(resultBody)
		#print('One or more predicates here ')
		#print(B)
	return B
	



def Translated(results):
	if(results):
		 
		 if(results.type):
			 type=results.type
		 if(type=='query'):
		     QueryPrct=results
		     #print('\n----------------TYPE-------------------------------------------\n'+type)
			 
		     return QueryType(QueryPrct)
		    
			 
			 
			 #print(type)
		 if (results.head):
			 resultHead=results.head
			 # get the first part of the query
			 PreQuery=GetHeaderName(resultHead)
			 #print(PreQuery)
		 if (results.body):
		     resultBody=results.body
		     PostQuery=GetPredicateBody(resultBody)
		     
		 TotalQuery=PreQuery+' ' +PostQuery
		 TotalQuery=TotalQuery.replace("'",'')
		 #print (TotalQuery)
	return TotalQuery
			 			 		
		
	  
