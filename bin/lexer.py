# Last modify Marcello 09/11/2013 

import ply.lex as lex
import ply.yacc as yacc

class Datalog():
    
    #Names of the tokens
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

    
    #Define the rules for the parsing
    t_TURNSTILE = r'\:\-'
    t_DOT = r'\.'
    t_LEFT_PAR  = r'\('
    t_RIGHT_PAR  = r'\)'
    t_COMMA = '\,'
    t_EQUALS  = r'='
    t_NAME = r'\"?[a-z][a-zA-Z0-9_]*\"?'  #?????????
    t_VAR = r'[A-Z][a-zA-Z0-9_]*'
    t_USCORE = r'_'
    def t_NUMBER(t):
        r'\d+'
        try:
            t.value = double(t.value)
        except ValueError:
            print ("Number value too large", t.value)
            t.value = 0
        print ("parsed number %s.2" % repr(t.value))
        return t

    
    # Rule to track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.line_number += len(t.value)
    
    
    # Rule to ignore spaces and tabs
    t_ignore  = ' \t'

    
    # Rule to skip illegals characters
    def t_error(t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    
    # Build the lexer
    lexer = lex.lex()

    
#DEBUGGING part
# if __name__ == '__main__':
    
    # string_to_parse = 'V(x,y) :- R(x,y) and S(y,_,"abc")'
    
    # datalog = Datalog()
    # datalog.lexer.input(string_to_parse)

    # while True:
        # parsed = datalog.lexer.token()
        # if not parsed: break      # No more input
        # print parsed.type, parsed.value, parsed.lineno, and parsed.lexpos
        # print (parsed)