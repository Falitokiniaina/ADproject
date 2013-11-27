""" 
Connection to database postgreSQL
Last modify:
	Marcello and Fali 12/11/2013
"""

import sys, traceback
import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base


# Default parameters are:
# hostname = 'localhost'
# port = '5432'
# username = 'postgres'
# password = 'root'
# dbname = 'adb'
# connection_string = 'postgresql+psycopg2://' + username + ':' + password + '@' + hostname + ':' + port + '/' + dbname

def getConnection(connection_string):
   
    try:
        engine = sqlalchemy.create_engine(connection_string)
        engine.connect()
        Session = sessionmaker(bind=engine)
        session = Session()
        print('\nConnected!\n')
        return session
        
    except:
        print('\nConnection error.\n')
        return None
        #DEBUG
        #traceback.print_exc(file=sys.stdout)  