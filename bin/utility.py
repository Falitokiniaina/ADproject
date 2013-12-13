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
