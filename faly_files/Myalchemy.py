#!/usr/bin/env python
# -*- coding: utf-8 -*-

# yum install python-sqlalchemy

#datas = {
#    "host": "localhost", 
#    "port": "3306",
#    "type": "mysql", 
#    "user": "root",
#    "pass": "",
#    "name": "msn",
#}

from sqlalchemy import MetaData, create_engine
from sqlalchemy.schema import Table

class Myalchemy(object):
    """Cette classe permet d interrgair avec une base de donnees"""
    
    def __init__(self, datas):
        self.url = "%(type)s://%(user)s:%(pass)s@%(host)s:%(port)s/%(name)s" % datas
        self.meta = MetaData()
        self.engine = create_engine(self.url)
        self.meta.reflect(bind=self.engine)
        self.connection = self.engine.connect()
        
    def __del__(self):
        self.connection.close()
    
    def getAllTables(self):
        """Retourne la liste des tables de la base"""
        #return self.meta.sorted_tables
        for table in self.meta.sorted_tables:
            print (table)

    def getTable(self, table_name):
        """Retourne l objet table correspondant a la table table_name"""
        return Table(table_name, self.meta, autoload=True)

    def getAttrOfTable(self, table_name):
        """Retourne les attributs de la table table_name"""
        table = self.getTable(table_name)
        attrs = []
        for attr in Table(table_name, self.meta, autoload=True).c:
            attrs.append(attr.name)
        return attrs
    
    def getPrimaryOfTable(self, table_name):
        """Retourne la cle primaire d'une table"""
        table = self.getTable(table_name)
        for attr in table.c:
            if attr.primary_key:
                return attr.name

    def getForeignOfTable(self, table_name):
        """Retourne les cles etrangeres d'une table"""
        table = self.getTable(table_name)
        foreigns = []
        for attr in table.foreign_keys:
            parent = (attr.column.table.name, attr.column.name)
            child = (attr.parent.table.name, attr.parent.name)
            foreigns.append((attr.name, child, parent))
        return foreigns
    
    def getAllOfTable(self, table_name):
        """Retourne tout les elements d une table"""
        table = self.getTable(table_name)
        result = self.engine.execute(table.select())
        return result.fetchall()
    
    def getCountOfTable(self, table_name):
        """Retourne le nombre d elements d une table"""
        table = self.getTable(table_name)
        result = self.engine.execute(table.count())
        return result.fetchone()[0]
    
    def getRowOfTableWithPrimaryVal(self, table_name, row_id_val):
        """Retourne le nombre d elements d une table"""
        table = self.getTable(table_name)
        row_id_name = self.getPrimaryOfTable(table_name)[1]
        for attr in table.c:
            if attr.name == row_id_name:
                result = self.engine.execute(table.select(attr == row_id_val))
        return result.fetchone()        