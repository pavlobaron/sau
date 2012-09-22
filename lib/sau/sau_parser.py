import ply.lex as lex
import ply.yacc as yacc

#------------ lexer rules -----------------

tokens = (
   'AND',
   'ANY',
   'ALL',
   'ARRANGE',
   'AS',
   'ASC',
   'AVG',
   'BAG',
   'BINSTORAGE',
   'BY',
   'BYTEARRAY',
   'CACHE',
   'CAT',
   'CD',
   'CHARARRAY',
   'COGROUP',
   'CONCAT',
   'COPYFROMLOCAL',
   'COPYTOLOCAL',
   'COUNT',
   'CP',
   'CROSS',
   'DECLARE',
   'DEFAULT',
   'DEFINE',
   'DESC',
   'DESCRIBE',
   'DIFF',
   'DISTINCT',
   'DOUBLE',
   'DU',
   'DUMP',
   'E_L',
   'E_U',
   'EVAL',
   'EXEC',
   'EXPLAIN',
   'F_L',
   'F_U',
   'FILTER',
   'FLOAT',
   'FLATTEN',
   'FOREACH',
   'FULL',
   'GENERATE',
   'GROUP',
   'HELP',
   'IF',
   'ILLUSTRATE',
   'INNER',
   'INPUT',
   'INT',
   'INTO',
   'IS',
   'JOIN',
   'KILL',
   'L_L',
   'L_U',
   'LEFT',
   'LIMIT',
   'LOAD',
   'LONG',
   'LS',
   'MAP',
   'MATCHES',
   'MAX',
   'MIN',
   'MKDIR',
   'MV',
   'NOT',
   'NULL',
   'OR',
   'ORDER',
   'OUTER',
   'OUTPUT',
   'PARALLEL',
   'PIG',
   'PIGDUMP',
   'PIGSTORAGE',
   'PWD',
   'QUIT',
   'REGISTER',
   'RIGHT',
   'RM',
   'RMF',
   'RUN',
   'SAMPLE',
   'SET',
   'SHIP',
   'SIZE',
   'SPLIT',
   'STDERR',
   'STDIN',
   'STDOUT',
   'STORE',
   'STREAM',
   'SUM',
   'TEXTLOADER',
   'TOKENIZE',
   'THROUGH',
   'TUPLE',
   'UNION',
   'USING',
   'PATH',
   'SCOL'
)

t_AS = r'(?i)as'
t_AND = r'(?i)AND'
t_ANY = r'(?i)ANY'
t_ALL = r'(?i)ALL'
t_ARRANGE = r'(?i)ARRANGE'
t_ASC = r'(?i)ASC'
t_AVG = r'(?i)AVG'
t_BAG = r'(?i)BAG'
t_BINSTORAGE = r'BinStorage'
t_BY = r'(?i)BY'
t_BYTEARRAY = r'(?i)BYTEARRAY'
t_CACHE = r'(?i)CACHE'
t_CAT = r'(?i)CAT'
t_CD = r'(?i)CD'
t_CHARARRAY = r'(?i)CHARARRAY'
t_COGROUP = r'(?i)COGROUP'
t_CONCAT = r'(?i)CONCAT'
t_COPYFROMLOCAL = r'copyFromLocal'
t_COPYTOLOCAL = r'copyToLocal'
t_COUNT = r'(?i)COUNT'
t_CP = r'(?i)CP'
t_CROSS = r'(?i)CROSS'
t_DECLARE = r'%(?i)declare'
t_DEFAULT = r'%(?i)default'
t_DEFINE = r'(?i)DEFINE'
t_DESC = r'(?i)DESC'
t_DESCRIBE = r'(?i)DESCRIBE'
t_DIFF = r'(?i)DIFF'
t_DISTINCT = r'(?i)DISTINCT'
t_DOUBLE = r'(?i)DOUBLE'
t_DU = r'(?i)DU'
t_DUMP = r'(?i)DUMP'
t_E_L = r'e'
t_E_U = r'E'
t_EVAL = r'(?i)EVAL'
t_EXEC = r'(?i)EXEC'
t_EXPLAIN = r'(?i)EXPLAIN'
t_F_L = r'f'
t_F_U = r'F'
t_FILTER = r'(?i)FILTER'
t_FLATTEN = r'(?i)FLATTEN'
t_FLOAT = r'(?i)float'
t_FOREACH = r'(?i)FOREACH'
t_FULL = r'(?i)FULL'
t_GENERATE = r'(?i)GENERATE'
t_GROUP = r'(?i)GROUP'
t_HELP = r'(?i)HELP'
t_IF = r'(?i)IF'
t_ILLUSTRATE = r'(?i)ILLUSTRATE'
t_INNER = r'(?i)INNER'
t_INPUT = r'(?i)INPUT'
t_INT = r'(?i)INT'
t_INTO = r'(?i)INTO'
t_IS = r'(?i)IS'
t_JOIN = r'(?i)JOIN'
t_KILL = r'(?i)KILL'
t_L_L = r'l'
t_L_U = r'L'
t_LEFT = r'(?i)LEFT'
t_LIMIT = r'(?i)LIMIT'
t_LOAD = r'(?i)LOAD'
t_LONG = r'(?i)LONG'
t_LS = r'(?i)LS'
t_MAP = r'(?i)MAP'
t_MATCHES = r'(?i)MATCHES'
t_MAX = r'(?i)MAX'
t_MIN = r'(?i)MIN'
t_MKDIR = r'(?i)MKDIR'
t_MV = r'(?i)MV'
t_NOT = r'(?i)NOT'
t_NULL = r'(?i)NULL'
t_OR = r'(?i)OR'
t_ORDER = r'(?i)ORDER'
t_OUTER = r'(?i)OUTER'
t_OUTPUT = r'(?i)OUTPUT'
t_PARALLEL = r'(?i)PARALLEL'
t_PIG = r'(?i)PIG'
t_PIGDUMP = r'(?i)PigDump'
t_PIGSTORAGE = r'(?i)PigStorage'
t_PWD = r'(?i)PWD'
t_QUIT = r'(?i)QUIT'
t_REGISTER = r'(?i)REGISTER'
t_RIGHT = r'(?i)RIGHT'
t_RM = r'(?i)RM'
t_RMF = r'(?i)RMF'
t_RUN = r'(?i)RUN'
t_SAMPLE = r'(?i)SAMPLE'
t_SET = r'(?i)SET'
t_SHIP = r'(?i)SHIP'
t_SIZE = r'(?i)SIZE'
t_SPLIT = r'(?i)SPLIT'
t_STDERR = r'(?i)STDERR'
t_STDIN = r'(?i)STDIN'
t_STDOUT = r'(?i)STDOUT'
t_STORE = r'(?i)STORE'
t_STREAM = r'(?i)STREAM'
t_SUM = r'(?i)SUM'
t_TEXTLOADER = r'(?i)TextLoader'
t_TOKENIZE = r'(?i)TOKENIZE'
t_THROUGH = r'(?i)THROUGH'
t_TUPLE = r'(?i)TUPLE'
t_UNION = r'(?i)UNION'
t_USING = r'(?i)USING'
t_PATH = r"'[a-zA-Z0-9_\-./]+?'"
t_SCOL = r';'

t_ignore = ' \t\n'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex(debug=1)

#-------------- parser rules ---------------

literals = ['=',
            '!=',
            '<',
            '>',
            '<=',
            '>=',
            '+',
            '-',
            '*',
            '/',
            '%',
            '?',
            '$',
            '.',
            '#',
            '::',
            ':',
            '(',
            ')',
            '[',
            ']',
            '{',
            '}']

def p_error(p):
    print "Syntax error in input: %s" % str(p)

def p_expressoin_load(p):
    'expression : LOAD expression SCOL'
    p[0] = ('load', p[2], None, None)

def p_expression_path(p):
    'expression : PATH'
    p[0] = p[1][1:-1]

def parse(cmd):
    return yacc.yacc().parse(cmd, lexer=lexer, debug=1)
