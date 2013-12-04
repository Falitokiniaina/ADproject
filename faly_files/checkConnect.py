import sys
sys.path.append('../faly_files/')
from Myalchemy import Myalchemy

def checkConnect(sql_session,connection_string):
    #print('\n### Status goes here ###')
    #try:
        if  sql_session:
            print("connection ok \n DB schema: \n")
           # datas = {
           #     "host": "localhost", 
           #     "port": "5432",
           #     "type": "postgresql+psycopg2", 
           #     "user": "postgres",
           #     "pass": "postgres",
           #     "name": "adb",
           # }            
            postgresalchemy = Myalchemy(connection_string)            
            alltables = postgresalchemy.getAllTables()
            print (alltables)
            
            print("\n TABLES")
            for table in alltables:
                print("\n")                
                print (table)    
                print (postgresalchemy.getAttrOfTable(str(table)))
                print (postgresalchemy.getAllOfTable(str(table)))
                                     
            #print (postgresalchemy.getAttrOfTable("actor"))
            #print (postgresalchemy.getTable("actor"))
            #print (postgresalchemy.getAllOfTable("actor"))
            #print (postgresalchemy.getCountOfTable("actor"))
            #print (postgresalchemy.getRowOfTableWithPrimaryVal("actor", 1))        
            
        else:
            print ("not connected!")
   # except:
    #    print("Unexpected error:", sys.exc_info()[0])  
        