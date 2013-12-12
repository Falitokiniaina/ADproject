import psycopg2
import sys
from Myalchemy import Myalchemy
 

def CleaningViews(connection_string,sql_sessionl):
     print('Cleaning...')
	 
     postgresalchemy = Myalchemy(connection_string)    	
     print('---------------------------\n')
     viewObjects=postgresalchemy.getAllViews()
     hasViews=0
     for v in viewObjects:
          dropView='DROP VIEW '+ v
          sql_sessionl.execute(dropView)
          hasViews=hasViews+1		  
          print('\n Cleaning ...')
     		  
     if hasViews>0 :
          sql_sessionl.commit()
     print('Cleaning Done. ')
