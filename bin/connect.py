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


def connect(
    hostname = 'localhost',
	port = '5432',
    username = 'postgres',
    password = 'root',
    dbname = 'adb'
	):

    connection_string = 'postgresql+psycopg2://' + username + ':' + password + '@' + hostname + ':' + port + '/' + dbname
    
    print('\nDefault connection string is:\n%s\n' % connection_string)
    answer = input('Would you like to change that settings? [Y/N]\n> ')
    
    if answer.lower()=='y':
        while True:
            #insert parameters
            hostname = input('\nPlease enter the PostgreSQL server name or IP address:\n> ')
            port = input('\nPort:\n> ')
            username = input('\nUsername:\n> ')
            password = input('\nPassword:\n> ')
            dbname = input('\nDatabase name:\n> ')
           
            if hostname and port and username and password and dbname:
                connection_string = 'postgresql+psycopg2://' + username + ':' + password + '@' + hostname + ':' + port + '/' + dbname 
                print('\nNew connection string:\n%s\n' % connection_string)
                break
            else:
                print ('\nAll fields are mandatory.')
        
    try:
        engine = sqlalchemy.create_engine(connection_string)
        engine.connect()
        Session = sessionmaker(bind=engine)
        session = Session()
        print('\nConnected!\n')
    
    except:
        print('\nConnection error.\n')
        #DEBUG
        #traceback.print_exc(file=sys.stdout)