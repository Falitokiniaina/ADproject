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
    
    
    # Parse a string
    def getParsingOf(self, string_to_parse):
        self.parts = {}
        if not string_to_parse: 
            return "Error: empty string"
        yacc.parse(string_to_parse)
        return self.parts
    
    
    # Config Lex and Yacc
    def __init__(self, **kw):
        #self.debug = kw.get('debug', 0)
        self.parts = {}
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[1] + "_" + self.__class__.__name__
        except:
            modname = "parser"+"_"+self.__class__.__name__
        # self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        #print self.debugfile, self.tabmodule
        # Build the lexer and parser
        lex.lex(
                module=self,
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
            yacc.parse(string_to_parse)
            # TESTS
            print (self.parts)

            
         
# Datalog parser class  
class Datalog(Parser):
    
    ### TOKENIZER RULES ####
    # Tokens' names
    tokens = (
        'TURNSTILE',
        'DOT',
        'LEFT_PAR',
        'RIGHT_PAR',
        'COMMA',
        'EQUALS',
        'NUMBER',
        'NAME',
        'VAR',
        'USCORE'
    )
 
    # Tokens' regular expressions 
    t_TURNSTILE = r'\:\-'
    t_DOT = r'\.'
    t_LEFT_PAR  = r'\('
    t_RIGHT_PAR  = r'\)'
    t_COMMA = '\,'
    t_EQUALS  = r'='
    t_NAME = r'\"?[a-z][a-zA-Z0-9_]*\"?'
    t_VAR = r'[A-Z][a-zA-Z0-9_]*'
    t_USCORE = r'_'
    
    # Recognize numbers
    def t_NUMBER(self, t):
        r'\d+'
        try:
            t.value = float(t.value)
        except ValueError:
            print ("Number value too large", t.value)
            t.value = 0
        print ("parsed number %s.2" % repr(t.value))
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
        '''statement : block 
                | predicate'''
	
    def p_block_select(self, p):
        '''block : variable TURNSTILE'''
        self.parts['head'] = p[1]
    
    def p_block_predicate(self, p):
        '''predicate : variable DOT'''
        self.parts['predicate'] = p[1]		
	
    def p_variable_single(self, p):
        '''variable : VAR'''
        p[0] = p[1]
        #print ('variable ')
	
    def p_variable_multi(self, p):
        '''variable : VAR COMMA variable '''
        p[0] = p[1] + ',' + p[3]
        #print ('multivar: ', p[0])
			
    def p_variable_block(self, p):
        '''variable : VAR LEFT_PAR variable RIGHT_PAR'''
        p[0] = p[1] + p[2] + p[3] + p[4]
        #print ('block: ', p[0])
	
    def p_error(self, p):
        print ("Syntax error at '%s'" % p.value)

    # TEST Lex and Yacc
    def runTests(self, string_to_parse):
        print("\n### STRING TO PARSE ###\n%s" % string_to_parse)
        print("\n### TOKENS ###")
        lex.input(string_to_parse)
        while True:
            tok = lex.token()
            if not tok: 
                # No more input
                break
            else:
                # This prints type, value, lineno, tok.lexpos
                print (tok)
        print("\n### SINTAX TREE ###")
        self.getParsingOf(string_to_parse)
        print(self.parts)
         
         
# For standalone use  
if __name__ == '__main__':
    datalog = Datalog()
    datalog.run()