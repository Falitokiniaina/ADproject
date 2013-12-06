""" 
Parser for Datalog queries
Last modify:
	Marcello and Fali 12/11/2013

Python Lex & Yacc tutorial:
http://www.dabeaz.com/ply/ply.html
"""

import ply.lex as lex
import ply.yacc as yacc
import os


# Superclass for Datalog parser
class Parser:

    tokens = ()
    precedence = ()
    results = {} 
    
    # Config Lex and Yacc
    def __init__(self, **kw):
        #self.debug = kw.get('debug', 0)
        self.results = {}
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[1] + "_" + self.__class__.__name__
        except:
            modname = "parser"+"_"+self.__class__.__name__
        # self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        #print self.debugfile, self.tabmodule
        # Build the lexer and parser
        lex.lex(
                module=self
                #debug=self.debug
                )
        yacc.yacc(
                module=self,
                #debug=self.debug,
                #debugfile=self.debugfile,
                tabmodule=self.tabmodule
                )
        
        
    # Run is called only when this class is used standalone     
    def run(self):
        while 1:
            try:
                string_to_parse = input('\nInsert Datalog query:\n> ')
            except EOFError:
                break
            if not 	string_to_parse: 
                continue
            self.results = yacc.parse(string_to_parse)
            
            # TESTS
            # print(repr(self.results))    
            
            # Get the type of request (query or rule)
            # Depending on the type we do a SELECT or a CREATE VIEW
            self.requestType = self.results.type
            print("Got type >>> " + self.requestType)
            
            # Get the head. 
            # Head contain the name of the view.
            # If type of request is query we get data from this view.
            # If type of request is rule we create a new view.
            self.requestHead = self.results.head
            print("Got head > " + repr(self.requestHead))
         
            # Get the body. Body is a list of predicates and constraint we need for the WHERE clause
            self.requestBody = self.results.body
            print("Got body > " + repr(self.requestBody))
            
            # Get a predicate from the body
            # We need to loop the predicates in order to create the WHERE clause
            for predicate in self.requestBody:
                print("\nGot a predicate.\n    Name >>>"+ repr(predicate.name))
                # To use the terms use
                print("    Terms >>>" + repr(predicate.terms))
            
         
         
    # Parse a string
    def getParsingOf(self, string_to_parse):
        self.results = {}
        if not string_to_parse: 
            return "Error: empty string"
        self.results = yacc.parse(string_to_parse)
        return self.results
     
     
# Datalog parser class  
class Datalog(Parser):
    
    ### TOKENIZER RULES ####
    # Tokens' names
    reserved = {'and' : 'AND', 'not' : 'NOT'}
    tokens = [
        'TURNSTILE',    #:-
        'DOT',          #.
        'LEFT_PAR',     #(
        'RIGHT_PAR',    #)
        'COMMA',        #,
        'EQUALS',       #=
        'NUMBER',       #0-9
        'VARIABLE',     #x
        'PREDICATE',    #Student
        'UNDERSCORE',   #_
        #'MINUS',         #-
        'OPERATOR',     #>
        'CONSTANT'      #"something"             
    ] + list(reserved.values())
 
    # Tokens' regular expressions 
    t_TURNSTILE = r'\:\-'
    t_DOT = r'\.'
    t_LEFT_PAR  = r'\('
    t_RIGHT_PAR  = r'\)'
    t_COMMA = '\,'
    t_EQUALS  = r'='
    t_VARIABLE = r'[a-z][a-z]*'
    t_PREDICATE = r'[A-Z][a-zA-Z0-9_]*'
    t_UNDERSCORE = r'_'
    #t_MINUS = r'-'
    t_OPERATOR = r'[!<>=](=)?'
    t_CONSTANT = r'"[^\"]*"'
    t_NUMBER = r'\d+'
       
    def t_AND(self, t):
        r'[a-z][a-z]*'
        t.type = self.reserved.get(t.value,'VARIABLE')    # Check for reserved words
        return t
        
    def t_NOT(self, t):
        r'[a-z][a-z]*'
        t.type = self.reserved.get(t.value,'VARIABLE')    # Check for reserved words
        return t
   
    # Keep track of line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.line_number += len(t.value)
     
    # Ignore spaces and tabs
    t_ignore  = ' \t'
    
    # Skip illegals characters
    def t_error(self, t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

       
    ### PARSER RULES ###
    # def p_entrypoint(self, p):
        # '''entrypoint : statementlist'''
        # p[0] = AST(p[1])
    
    # def p_statementlist1(self, p):
        # '''statementlist : statementlist statement'''
        # p[0] = p[1] + [p[2]]
    
    # def p_statementlist2(self, p):
        # '''statementlist : statement'''
        # p[0] = [p[1]]
    
    def p_statement(self, p):
        '''statement : rule 
                | query'''
        #p[0] = p[1]	             
        p[0] = p[1]
    
    def p_rule(self, p):
        '''rule : head TURNSTILE body DOT'''
        p[0] = Tree(p[1], p[3], 'rule')
    
    def p_query(self, p):
        '''query : block DOT'''
        p[0] = Tree(p[1], {}, 'query')
	
    def p_head(self, p):
        '''head : block'''
        p[0] = p[1]
    
    def p_body(self, p):
        '''body : blocklist'''
        p[0] = p[1]	        
                   
    def p_blocklist1(self, p):
        '''blocklist : blocklist AND block'''
        p[0] = p[1] + [p[3]]
    
    def p_blocklist2(self, p):
        '''blocklist : blocklist AND constraint'''
        p[0] = p[1] + [p[3]]
    
    def p_blocklist3(self, p):
        '''blocklist : block'''
        p[0] = [p[1]]
  
    def p_block(self, p):
        '''block : PREDICATE LEFT_PAR atomlist RIGHT_PAR'''
        p[0] = Predicate(p[1], p[3], False)
        
    def p_negatedblock(self, p):
        '''block : NOT PREDICATE LEFT_PAR atomlist RIGHT_PAR'''
        p[0] = Predicate(p[2], p[4], True)
    
    def p_atomlist1(self, p):
        '''atomlist : atomlist COMMA atom'''
        p[0] = p[1] + [p[3]]
     
    def p_atomlist2(self, p):
        '''atomlist : atom'''
        p[0] = [p[1]]
    
    def p_atom(self, p):
        '''atom : VARIABLE
            | CONSTANT
            | UNDERSCORE'''
        p[0] = p[1]
    
    def p_constraint(self, p):
        '''constraint : VARIABLE OPERATOR NUMBER'''
        # p[0] = Constraint(p[1] + p[2] + p[3])
        p[0] = Predicate("constraint", p[1] + p[2] + p[3], False) # no negation on the constraints 
 
    
    def p_error(self, p):
        if p and p.value:
            print ("Syntax error at '%s'" % p.value)
        else:
            print ("Syntax error")
        
    # TEST Lex and Yacc
    # def runTests(self, string_to_parse):
        # print("\n### STRING TO PARSE ###\n%s" % string_to_parse)
        # print("\n### TOKENS ###")
        # lex.input(string_to_parse)
        # while True:
            # tok = lex.token()
            # if not tok: 
                # No more input
                # break
            # else:
                # This prints type, value, lineno, tok.lexpos
                # print (tok)
        # print("\n### SINTAX TREE ###")
        # self.getParsingOf(string_to_parse)
        # print(self.p)
         
        
class Tree(object):
    def __init__(self, head={}, body={}, type=""):
        self.head = head 
        self.body = body
        self.type = type
    def __repr__(self):
        return "%r" % (self.__dict__)
        
class Predicate(object):
    def __init__(self, name="", terms={}, isNegated=""):
        self.name = name
        self.terms = terms
        self.isNegated = isNegated
    def __repr__(self):
        return "%r" % (self.__dict__)
    
    
# class Constraint(object):
    # def __init__(self, constraint):
        # self.constraint = constraint
    # def __repr__(self):
        # return "%r" % (self.__dict__)
        
         
# For standalone use  
if __name__ == '__main__':
    datalog = Datalog()
    datalog.run()