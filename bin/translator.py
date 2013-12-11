import psycopg2
import sys

### GLOBAL VARIABLES ###
db_schema = None


def getTranslation(schema, parsing_result):
    if not parsing_result: return None
    global db_schema
    db_schema = schema
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
       statement = statement + db_schema[predicate.name][index] + ', '
    statement = statement[:-2] + ' FROM ' + predicate.name + ';'
    return statement

    
    
### CREATE VIEW ###  
def CreateViews(results):
    # q(X,Y):-actor(X,Y,Z) and movie(Z,_).
    # CREATE VIEW q AS SELECT actor.name, actor.lastname FROM actor 
    # JOIN movie ON actor.title=movie.title 
    statement = 'CREATE VIEW '+ results.head.name +' AS SELECT ' + CreateViews_SelectPart(results) + 'FROM '
    for predicate in results.body:
        statement = statement + predicate.name + ', '
    statement = statement[:-2] + ' WHERE ' + CreateViews_WherePart(results) + ';'
    return statement    
        
#Build the select clause for a view 
def CreateViews_SelectPart(Tree):
    toSelect = ''
    allTheTerms = []
    for toSearch in Tree.head.terms:
        for predicate in Tree.body:
            if toSearch in predicate.terms:
                if toSearch not in allTheTerms:
                    allTheTerms.append(toSearch)
                    index = predicate.terms.index(toSearch)
                    toSelect = toSelect + predicate.name + '.' + db_schema[predicate.name][index] + ', '
    return toSelect[:-2] + ' '  
    
#Build the where clause 
def CreateViews_WherePart(Tree):
    where = ''
    allTheTerms = [] 
    for predicate in Tree.body:
        for term in predicate.terms:
            if term not in allTheTerms:
                allTheTerms.append(term)
                #print(term+ '    ')
                listOcc = getPredicatesContainingTerm(Tree, term)
                lastElm =  listOcc.pop()
                indexLastElm = lastElm.terms.index(term)
                for elm in listOcc:
                    index = elm.terms.index(term)
                    where = where + elm.name + '.' +  db_schema[elm.name][index] + '=' + lastElm.name + '.' +  db_schema[lastElm.name][indexLastElm] + ' and '
    return where[:-5] + ' '
    
#returns a list of tables where term occour
def getPredicatesContainingTerm(Tree, term):
    listOcc = []
    for predicate in Tree.body:
        if term in predicate.terms:
            listOcc.append(predicate)
    return listOcc 