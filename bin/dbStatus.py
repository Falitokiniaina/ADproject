from Myalchemy import Myalchemy

def getStatus(sql_session, connection_string):
    #print('\n### Status goes here ###')
    #try:
        if  sql_session:
            print("You are connected to:\n" + connection_string)
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
            print("\nDB SCHEMA")
            #print (alltables)
            for table in alltables:        
                print(50*"-")
                print ("Table name: ")
                print (table)    
                print ("Column names: ")
                print (postgresalchemy.getAttrOfTable(str(table)))
                #print (postgresalchemy.getAllOfTable(str(table)))
            
            print(50*"-")                        
            #print (postgresalchemy.getAttrOfTable("actor"))
            #print (postgresalchemy.getTable("actor"))
            #print (postgresalchemy.getAllOfTable("actor"))
            #print (postgresalchemy.getCountOfTable("actor"))
            #print (postgresalchemy.getRowOfTableWithPrimaryVal("actor", 1))        
            
        else:
            print ("You are not connected!")
   # except:
    #    print("Unexpected error:", sys.exc_info()[0])  
        