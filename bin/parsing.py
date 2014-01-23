""" 
Parser for Datalog queries
Last modify:
	Marcello 24/01/2013

Python Lex & Yacc tutorial:
http://www.dabeaz.com/ply/ply.html
"""

import ply.lex as lex
import ply.yacc as yacc
import os

from dataStructures import * 

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
        'NUMBER',       #0-9
        'CONSTANT',      #something  
        'VARIABLE',     #X
        'UNDERSCORE',   #_
        'OPERATOR',     #>           
    ] + list(reserved.values())
 
    # Tokens' regular expressions 
    t_TURNSTILE = r'\:\-'
    t_DOT = r'\.'
    t_LEFT_PAR  = r'\('
    t_RIGHT_PAR  = r'\)'
    t_COMMA = r'\,'
    t_VARIABLE = r'[A-Z][a-z]*'
    t_CONSTANT = r'[a-z0-9][a-zA-Z0-9]*'
    t_UNDERSCORE = r'_'
    t_OPERATOR = r'[!<>=](=)?'
    t_NUMBER = r'\d+'
       
    def t_AND(self, t):
        r'[a-z][a-z]*'
        t.type = self.reserved.get(t.value,'CONSTANT')    # Check for reserved words
        return t
        
    def t_NOT(self, t):
        r'[a-z][a-z]*'
        t.type = self.reserved.get(t.value,'CONSTANT')    # Check for reserved words
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
        '''block : CONSTANT LEFT_PAR atomlist RIGHT_PAR'''
        p[0] = Predicate(p[1], p[3], False)
        
    def p_negatedblock(self, p):
        '''block : NOT CONSTANT LEFT_PAR atomlist RIGHT_PAR'''
        p[0] = Predicate(p[2], p[4], True)
    
    def p_atomlist1(self, p):
        '''atomlist : atomlist COMMA atom'''
        p[0] = p[1] + [p[3]]
     
    def p_atomlist2(self, p):
        '''atomlist : atom'''
        p[0] = [p[1]]
    
    def p_atomvariable(self, p):
        '''atom : VARIABLE 
            | UNDERSCORE'''
        p[0] = p[1]
    
    def p_atomconstant(self, p):
        '''atom : CONSTANT'''
        p[0] = "\'" + p[1] + "\'"
      
    def p_constraintvariable(self, p):
        '''constraint : VARIABLE OPERATOR VARIABLE'''
        p[0] = Constraint(p[1], p[2], p[3]) 
        
    def p_constraintconstant(self, p):
        '''constraint : VARIABLE OPERATOR CONSTANT'''
        p[0] = Constraint(p[1], p[2], "\'"+p[3]+"\'")   
 
    # def p_recursion(self, p):
       #  '''query : block recursive_query DOT'''
       #  p[0] = Tree(p[1], p[-1], 'query')
    
    def p_error(self, p):
        if p and p.value:
            print ("Syntax error at '%s'" % p.value)
        else:
            print ("Syntax error")
        