import ply.lex as lex

tokens = (
   'LOAD',
   'USING',
   'AS',
   'STRING',
   'SEMICOLON',
   'SCHEMA'
)

t_LOAD = r'(?i)load'
t_USING = r'(?i)using'
t_AS = r'(?i)as'
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_STRING(t):
    r"'.*?'"
    t.value = t.value[1:-1].strip()
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def parse(s, l):
    l.input(s)
    s = ""
    while True:
        tok = l.token()
        if not tok: break
        s = "%s, %s" % (s, tok.value)

    return s

def lexer():
    return lex.lex(debug=1)
