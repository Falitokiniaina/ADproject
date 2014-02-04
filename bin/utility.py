import psycopg2
import sys
from Myalchemy import Myalchemy
 
import globvar
import dataStructures

def CleaningViews():

     print('Cleaning views...')
	 
     postgresalchemy = Myalchemy(globvar.connection_string)    	
     #print('---------------------------\n')
     viewObjects=postgresalchemy.getAllViews()
     hasViews=0
     for v in viewObjects:
          dropView='DROP VIEW '+ v
          globvar.sql_session.execute(dropView)
          hasViews=hasViews+1		  
          #print('\n Cleaning ...')
     		  
     if hasViews>0 :
          globvar.sql_session.commit()
     print('Cleaning done! ')

# def SafeRule(parsing_result):
     # if not parsing_result: return None
     # elif parsing_result.type=='rule':
          # return CheckSafeRule(parsing_result)
     # elif parsing_result.type=='query':
          # return CheckQueryName(parsing_result)
     # else: return None
	
def CheckSafeRule(results):
     Error="Error"
     if results.body and results.head:
         Headpredicate = results.head
         BodyPredicate = results.body
         for Hterm in Headpredicate.terms:
            Error="Error"
            for prdBody in BodyPredicate:
                if isinstance(prdBody, dataStructures.Predicate):
                    for Bterm in  prdBody.terms:
                        if(Hterm == Bterm):
                            Error=""
                            break
     return Error

def CheckRelationName(results):
     postgresalchemy = Myalchemy(globvar.connection_string)    	
     Error="Error"
     if results.body:
         BodyPredicate=results.body
         tblObjects=postgresalchemy.getAllTables()
         for prdBody in BodyPredicate:
            if isinstance(prdBody, dataStructures.Predicate):
                Error="Error"
                for tbl in tblObjects:
                   if prdBody.name == str(tbl) :
                        Error=""
                        break
     return Error

def CheckQueryName(results):
     postgresalchemy = Myalchemy(globvar.connection_string)    	
     Error="Error"
     if results.head:
         HeadPredicate=results.head
         tblObjects=postgresalchemy.getAllTables()
         if isinstance(HeadPredicate, dataStructures.Predicate):
            for tbl in tblObjects:
               if HeadPredicate.name == str(tbl) :
                    Error=""
                    break
     return Error