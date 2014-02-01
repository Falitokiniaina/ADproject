import psycopg2
import sys
from Myalchemy import Myalchemy
 
import globvar

def CleaningViews():

     print('Cleaning...')
	 
     postgresalchemy = Myalchemy(globvar.connection_string)    	
     print('---------------------------\n')
     viewObjects=postgresalchemy.getAllViews()
     hasViews=0
     for v in viewObjects:
          dropView='DROP VIEW '+ v
          globvar.sql_session.execute(dropView)
          hasViews=hasViews+1		  
          print('\n Cleaning ...')
     		  
     if hasViews>0 :
          globvar.sql_session.commit()
     print('Cleaning Done. ')

def SafeRule(parsing_result):
     if not parsing_result: return None
     if parsing_result.type=='rule':
          statement = CheckSafeRule(parsing_result)
     return statement
	
def CheckSafeRule(results):

     Error="Error"
     Headpredicate = results.head
     BodyPredicate=results.body
     for Hterm in Headpredicate.terms:
          Error="Error"
          for prdBody in BodyPredicate:
               for Bterm in  prdBody.terms:
                    if(Hterm == Bterm):
                         Error=""
                            	
          
     return Error

def CheckRelationName(results):
     postgresalchemy = Myalchemy(globvar.connection_string)    	
     Error="Error"
     S=""
     BodyPredicate=results.body
     tblObjects=postgresalchemy.getAllTables()
     for prdBody in BodyPredicate:
              Error="Error"
              for tbl in tblObjects:
                   if prdBody.name == str(tbl) :
                        Error=""
                        break
     return Error
