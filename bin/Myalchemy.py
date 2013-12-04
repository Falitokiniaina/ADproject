#!/usr/bin/env python
# -*- coding: utf-8 -*-

# yum install python-sqlalchemy

#datas = {
#    "host": "localhost", 
#    "port": "5432",
#    "type": "postgresql", 
#    "user": "postgres",
#    "pass": "postgres",
#    "name": "adb",
#}

from sqlalchemy import MetaData, create_engine
from sqlalchemy.schema import Table

class Myalchemy(object):    
    """ This class allows to interact with the DB"""
    
    #def __init__(self, datas):    
        #self.url = "%(type)s://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s" % datas
    def __init__(self, connection_string):
        self.url = connection_string
        self.meta = MetaData()
        self.engine = create_engine(self.url)
        self.meta.reflect(bind=self.engine)
        self.connection = self.engine.connect()
        
    def __del__(self):
        self.connection.close()    
                    
    def getAllTables(self):
        """ Returns the list of the tables of the DB"""        
        return self.meta.sorted_tables        

    def getTable(self, table_name):
        """ Returns the object table corresponding to the table table_name """        
        return Table(table_name, self.meta, autoload=True)

    def getAttrOfTable(self, table_name):
        """ Returns the attributes of the table table_name """        
        table = self.getTable(table_name)
        attrs = []
        for attr in Table(table_name, self.meta, autoload=True).c:
            attrs.append(attr.name)
        return attrs
    
    def getPrimaryOfTable(self, table_name):
        """ Returns the primary key of a table """        
        table = self.getTable(table_name)
        for attr in table.c:
            if attr.primary_key:
                return attr.name

    def getForeignOfTable(self, table_name):
        """ Returns the foreign keys of a table """            
        table = self.getTable(table_name)
        foreigns = []
        for attr in table.foreign_keys:
            parent = (attr.column.table.name, attr.column.name)
            child = (attr.parent.table.name, attr.parent.name)
            foreigns.append((attr.name, child, parent))
        return foreigns
    
    def getAllOfTable(self, table_name):
        """ Returns all the elements of a table"""                
        table = self.getTable(table_name)
        result = self.engine.execute(table.select())
        return result.fetchall()
    
    def getCountOfTable(self, table_name):
        """ Returns the number of elements of a table """        
        table = self.getTable(table_name)
        result = self.engine.execute(table.count())
        return result.fetchone()[0]
    
    def getRowOfTableWithPrimaryVal(self, table_name, row_id_val):
        """ Returns the number of elements of a table"""        
        table = self.getTable(table_name)
        row_id_name = self.getPrimaryOfTable(table_name)[1]
        for attr in table.c:
            if attr.name == row_id_name:
                result = self.engine.execute(table.select(attr == row_id_val))
        return result.fetchone()        