# Last modify Marcello 09/11/2013 

from lexer import Datalog

def datalogQuery():

    #DEBUG
    #string_to_parse = 'V(x,y) :- R(x,y) and S(y,_,"abc")'

    datalog = Datalog()
    
    while True:
    
        string_to_parse = input('\nInsert Datalog query:\n> ')
        datalog.lexer.input(string_to_parse)
        
        tok = datalog.lexer.token()
        if tok: 
            print (tok)
            
        while True:
            tok = datalog.lexer.token()
            if not tok: 
                # No more input
                break
            else:
                #print tok.type, tok.value, tok.lineno, and tok.lexpos
                print (tok)

    