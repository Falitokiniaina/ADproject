import psycopg2
import sys

import globvar
import dataStructures

def getTranslation(parsing_result):
    if not parsing_result: return None
    if parsing_result.type=='rule':
        statement = CreateViews(parsing_result)
    elif parsing_result.type=='query':
        statement = CreateSelect(parsing_result)
    return statement
        
        
### CREATE SELECT ###  
def CreateSelect(results):
    # t(X,Y).
    # SELECT t.name, t.lastname FROM t 
    predicate = results.head
    statement = 'SELECT '
    for term in predicate.terms:
       index = predicate.terms.index(term)
       statement = statement + globvar.db_schema[predicate.name][index] + ', '
    statement = statement[:-2] + ' FROM ' + predicate.name + ';'
    return statement

    
    
### CREATE VIEW ###  
def CreateViews(results):
    # q(X,Y):-actor(X,Y,Z) and movie(Z,_).
    # CREATE VIEW q AS SELECT actor.name, actor.lastname FROM actor 
    # JOIN movie ON actor.title=movie.title 
    statement = 'CREATE VIEW '+ results.head.name +' AS SELECT ' + CreateViews_SelectPart(results) + ' FROM '
    for item in results.body:
        if isinstance(item, dataStructures.Predicate):
            statement = statement + item.name + ', '
    statement = statement[:-2]
    wherePart = CreateViews_WherePart(results)
    if wherePart:
        statement = statement + ' WHERE ' + wherePart + ';'
    return statement    
        
#Build the select clause for a view 
def CreateViews_SelectPart(Tree):
    toSelect = ''
    allTheTerms = []
    for toSearch in Tree.head.terms:
        for item in Tree.body:
            if isinstance(item, dataStructures.Predicate):
                if toSearch in item.terms:
                    if toSearch not in allTheTerms:
                        allTheTerms.append(toSearch)
                        index = item.terms.index(toSearch)
                        toSelect = toSelect + item.name + '.' + globvar.db_schema[item.name][index] + ', '
    return toSelect[:-2]  
    
#Build the where clause 
def CreateViews_WherePart(Tree):
    where = ''
    allTheTerms = [] 
    for item in Tree.body:
        
        #if the item in the body is a constraint like "termX operator termY"
        if isinstance(item, dataStructures.Constraint):
            listOccX = getPredicatesContainingTerm(Tree, item.termX)
            operator = item.operator
            
            #if termY is a constant for example X=marcello, the parser puts quotes
            if item.termY.startswith("'"):
                for elmX in listOccX:
                    indexX = elmX.terms.index(item.termX)
                    where = where + elmX.name + '.' + globvar.db_schema[elmX.name][indexX] + operator + item.termY + ' and '
            
            #else if termY is a variable for example X=Y, we have to loop the tree and search for the predicates that contain termY
            else:
                listOccY = getPredicatesContainingTerm(Tree, item.termY)
                for elmX in listOccX:
                    for elmY in listOccY:
                        indexX = elmX.terms.index(item.termX)
                        indexY = elmY.terms.index(item.termY)
                        where = where + elmX.name + '.' +  globvar.db_schema[elmX.name][indexX] + operator + elmY.name + '.' +  globvar.db_schema[elmY.name][indexY] + ' and '
        
        
        #else if the item in the body is a predicate for example actor(X,Y)
        elif isinstance(item, dataStructures.Predicate):           
           for term in item.terms:
                
                #if term is a constant for example actor(X,marcello), the parser puts quotes
                if term.startswith("'"):
                    index = item.terms.index(term)
                    where = where + item.name + '.' + globvar.db_schema[item.name][index] + '=' + term + ' and '
                
                #if term is a free variable _ it should be ignored
                elif term == "_":
                    break
                
                #else if term is a variable for example actor(X,Y), we have to loop the tree and search for the predicates that contain term 
                elif term not in allTheTerms:
                    allTheTerms.append(term)
                    #print(term+ '    ')
                    listOcc = getPredicatesContainingTerm(Tree, term)
                    lastElm =  listOcc.pop()
                    indexLastElm = lastElm.terms.index(term)
                    for elm in listOcc:
                        index = elm.terms.index(term)
                        where = where + elm.name + '.' +  globvar.db_schema[elm.name][index] + '=' + lastElm.name + '.' +  globvar.db_schema[lastElm.name][indexLastElm] + ' and '
    return where[:-5]
   
#returns a list of tables where term occour
def getPredicatesContainingTerm(Tree, term):
    listOcc = []
    for item in Tree.body:
        if isinstance(item, dataStructures.Predicate):
            if term in item.terms:
                listOcc.append(item)
    return listOcc 