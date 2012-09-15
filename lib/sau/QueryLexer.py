# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 QueryLexer.g 2012-09-15 22:26:59

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
STAR=104
LETTER=86
NOT=37
DOUBLENUMBER=99
EOF=-1
CACHE=59
STDOUT=64
STR_OP_NE=75
TUPLE=51
IMPORT=5
DCOLON=89
FULL=69
USING=28
RIGHT_BRACKET=115
DOUBLE=46
STR_OP_EQ=70
VOID=4
GENERATE=38
STREAM=54
INTO=22
STORE=56
STR_OP_LTE=74
OTHERWISE=24
QUOTEDSTRING=101
POUND=116
ASC=40
PERIOD=92
ROLLUP=15
LOAD=8
STDIN=63
SEMI_COLON=109
INT=43
BYTEARRAY=49
NUM_OP_GTE=83
GROUP=34
WS=106
CUBE=14
SPECIALCHAR=87
LEFT_CURLY=112
SL_COMMENT=107
FLOATINGPOINT=93
OR=36
CHARARRAY=48
FILTER=9
FLOATNUMBER=100
LEFT_PAREN=110
FOREACH=10
STR_OP_GT=71
MULTILINE_QUOTEDSTRING=102
FALSE=78
DISTINCT=16
QMARK=122
OUTPUT=61
DOLLAR=95
COGROUP=17
RIGHT_CURLY=113
INNER=29
ONSCHEMA=31
NUM_OP_LTE=81
ORDER=11
LIMIT=65
SPLIT=21
LEFT_BRACKET=114
STR_OP_GTE=73
PARALLEL=32
INPUT=60
FLOAT=45
STR_OP_MATCHES=76
AND=35
ID=88
DEFINE=7
CROSS=19
IF=23
ML_COMMENT=108
AS=26
RIGHT_PAREN=111
RANK=12
SAMPLE=66
BOOLEAN=42
COMMA=118
PARTITION=33
IS=53
LEFT=67
EQUAL=117
ALL=25
DENSE=13
PLUS=98
DIGIT=85
IDENTIFIER_L=90
NUM_OP_GT=82
RETURNS=6
STDERROR=62
NUM_OP_NE=84
INTEGER=91
OUTER=30
BY=27
PERCENT=121
DOUBLE_PERIOD=119
DATETIME=47
RIGHT=68
LONGINTEGER=94
MINUS=97
DOLLARVAR=96
STR_OP_LT=72
TRUE=77
JOIN=18
UNION=20
COLON=105
BAG=50
EXECCOMMAND=103
FLATTEN=39
MAP=52
THROUGH=55
NUM_OP_LT=80
MAPREDUCE=57
SHIP=58
DIV=120
DESC=41
LONG=44
NUM_OP_EQ=79


class QueryLexer(Lexer):

    grammarFileName = "QueryLexer.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(QueryLexer, self).__init__(input, state)


        self.dfa2 = self.DFA2(
            self, 2,
            eot = self.DFA2_eot,
            eof = self.DFA2_eof,
            min = self.DFA2_min,
            max = self.DFA2_max,
            accept = self.DFA2_accept,
            special = self.DFA2_special,
            transition = self.DFA2_transition
            )

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
            )




              



    # $ANTLR start "VOID"
    def mVOID(self, ):

        try:
            _type = VOID
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:27:9: ( 'VOID' )
            # QueryLexer.g:27:11: 'VOID'
            pass 
            self.match("VOID")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VOID"



    # $ANTLR start "IMPORT"
    def mIMPORT(self, ):

        try:
            _type = IMPORT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:30:9: ( 'IMPORT' )
            # QueryLexer.g:30:11: 'IMPORT'
            pass 
            self.match("IMPORT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORT"



    # $ANTLR start "RETURNS"
    def mRETURNS(self, ):

        try:
            _type = RETURNS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:33:9: ( 'RETURNS' )
            # QueryLexer.g:33:11: 'RETURNS'
            pass 
            self.match("RETURNS")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RETURNS"



    # $ANTLR start "DEFINE"
    def mDEFINE(self, ):

        try:
            _type = DEFINE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:36:8: ( 'DEFINE' )
            # QueryLexer.g:36:10: 'DEFINE'
            pass 
            self.match("DEFINE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DEFINE"



    # $ANTLR start "LOAD"
    def mLOAD(self, ):

        try:
            _type = LOAD
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:39:8: ( 'LOAD' )
            # QueryLexer.g:39:10: 'LOAD'
            pass 
            self.match("LOAD")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LOAD"



    # $ANTLR start "FILTER"
    def mFILTER(self, ):

        try:
            _type = FILTER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:42:8: ( 'FILTER' )
            # QueryLexer.g:42:10: 'FILTER'
            pass 
            self.match("FILTER")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FILTER"



    # $ANTLR start "FOREACH"
    def mFOREACH(self, ):

        try:
            _type = FOREACH
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:45:9: ( 'FOREACH' )
            # QueryLexer.g:45:11: 'FOREACH'
            pass 
            self.match("FOREACH")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FOREACH"



    # $ANTLR start "ORDER"
    def mORDER(self, ):

        try:
            _type = ORDER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:48:9: ( 'ORDER' )
            # QueryLexer.g:48:12: 'ORDER'
            pass 
            self.match("ORDER")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ORDER"



    # $ANTLR start "RANK"
    def mRANK(self, ):

        try:
            _type = RANK
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:51:8: ( 'RANK' )
            # QueryLexer.g:51:11: 'RANK'
            pass 
            self.match("RANK")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RANK"



    # $ANTLR start "DENSE"
    def mDENSE(self, ):

        try:
            _type = DENSE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:54:9: ( 'DENSE' )
            # QueryLexer.g:54:12: 'DENSE'
            pass 
            self.match("DENSE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DENSE"



    # $ANTLR start "CUBE"
    def mCUBE(self, ):

        try:
            _type = CUBE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:57:9: ( 'CUBE' )
            # QueryLexer.g:57:11: 'CUBE'
            pass 
            self.match("CUBE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CUBE"



    # $ANTLR start "ROLLUP"
    def mROLLUP(self, ):

        try:
            _type = ROLLUP
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:60:8: ( 'ROLLUP' )
            # QueryLexer.g:60:10: 'ROLLUP'
            pass 
            self.match("ROLLUP")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ROLLUP"



    # $ANTLR start "DISTINCT"
    def mDISTINCT(self, ):

        try:
            _type = DISTINCT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:63:10: ( 'DISTINCT' )
            # QueryLexer.g:63:12: 'DISTINCT'
            pass 
            self.match("DISTINCT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DISTINCT"



    # $ANTLR start "COGROUP"
    def mCOGROUP(self, ):

        try:
            _type = COGROUP
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:66:9: ( 'COGROUP' )
            # QueryLexer.g:66:11: 'COGROUP'
            pass 
            self.match("COGROUP")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COGROUP"



    # $ANTLR start "JOIN"
    def mJOIN(self, ):

        try:
            _type = JOIN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:69:6: ( 'JOIN' )
            # QueryLexer.g:69:8: 'JOIN'
            pass 
            self.match("JOIN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "JOIN"



    # $ANTLR start "CROSS"
    def mCROSS(self, ):

        try:
            _type = CROSS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:72:7: ( 'CROSS' )
            # QueryLexer.g:72:9: 'CROSS'
            pass 
            self.match("CROSS")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CROSS"



    # $ANTLR start "UNION"
    def mUNION(self, ):

        try:
            _type = UNION
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:75:7: ( 'UNION' )
            # QueryLexer.g:75:9: 'UNION'
            pass 
            self.match("UNION")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "UNION"



    # $ANTLR start "SPLIT"
    def mSPLIT(self, ):

        try:
            _type = SPLIT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:78:7: ( 'SPLIT' )
            # QueryLexer.g:78:9: 'SPLIT'
            pass 
            self.match("SPLIT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SPLIT"



    # $ANTLR start "INTO"
    def mINTO(self, ):

        try:
            _type = INTO
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:81:6: ( 'INTO' )
            # QueryLexer.g:81:8: 'INTO'
            pass 
            self.match("INTO")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTO"



    # $ANTLR start "IF"
    def mIF(self, ):

        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:84:4: ( 'IF' )
            # QueryLexer.g:84:6: 'IF'
            pass 
            self.match("IF")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IF"



    # $ANTLR start "OTHERWISE"
    def mOTHERWISE(self, ):

        try:
            _type = OTHERWISE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:87:11: ( 'OTHERWISE' )
            # QueryLexer.g:87:13: 'OTHERWISE'
            pass 
            self.match("OTHERWISE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OTHERWISE"



    # $ANTLR start "ALL"
    def mALL(self, ):

        try:
            _type = ALL
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:90:5: ( 'ALL' )
            # QueryLexer.g:90:7: 'ALL'
            pass 
            self.match("ALL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALL"



    # $ANTLR start "AS"
    def mAS(self, ):

        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:93:4: ( 'AS' )
            # QueryLexer.g:93:6: 'AS'
            pass 
            self.match("AS")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS"



    # $ANTLR start "BY"
    def mBY(self, ):

        try:
            _type = BY
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:96:4: ( 'BY' )
            # QueryLexer.g:96:6: 'BY'
            pass 
            self.match("BY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BY"



    # $ANTLR start "USING"
    def mUSING(self, ):

        try:
            _type = USING
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:99:7: ( 'USING' )
            # QueryLexer.g:99:9: 'USING'
            pass 
            self.match("USING")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "USING"



    # $ANTLR start "INNER"
    def mINNER(self, ):

        try:
            _type = INNER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:102:7: ( 'INNER' )
            # QueryLexer.g:102:9: 'INNER'
            pass 
            self.match("INNER")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INNER"



    # $ANTLR start "OUTER"
    def mOUTER(self, ):

        try:
            _type = OUTER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:105:7: ( 'OUTER' )
            # QueryLexer.g:105:9: 'OUTER'
            pass 
            self.match("OUTER")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTER"



    # $ANTLR start "ONSCHEMA"
    def mONSCHEMA(self, ):

        try:
            _type = ONSCHEMA
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:108:10: ( 'ONSCHEMA' )
            # QueryLexer.g:108:12: 'ONSCHEMA'
            pass 
            self.match("ONSCHEMA")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ONSCHEMA"



    # $ANTLR start "PARALLEL"
    def mPARALLEL(self, ):

        try:
            _type = PARALLEL
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:111:10: ( 'PARALLEL' )
            # QueryLexer.g:111:12: 'PARALLEL'
            pass 
            self.match("PARALLEL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARALLEL"



    # $ANTLR start "PARTITION"
    def mPARTITION(self, ):

        try:
            _type = PARTITION
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:114:11: ( 'PARTITION' )
            # QueryLexer.g:114:13: 'PARTITION'
            pass 
            self.match("PARTITION")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PARTITION"



    # $ANTLR start "GROUP"
    def mGROUP(self, ):

        try:
            _type = GROUP
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:117:7: ( 'GROUP' )
            # QueryLexer.g:117:9: 'GROUP'
            pass 
            self.match("GROUP")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GROUP"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:120:5: ( 'AND' )
            # QueryLexer.g:120:7: 'AND'
            pass 
            self.match("AND")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:123:4: ( 'OR' )
            # QueryLexer.g:123:6: 'OR'
            pass 
            self.match("OR")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:126:5: ( 'NOT' )
            # QueryLexer.g:126:7: 'NOT'
            pass 
            self.match("NOT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "GENERATE"
    def mGENERATE(self, ):

        try:
            _type = GENERATE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:129:10: ( 'GENERATE' )
            # QueryLexer.g:129:12: 'GENERATE'
            pass 
            self.match("GENERATE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GENERATE"



    # $ANTLR start "FLATTEN"
    def mFLATTEN(self, ):

        try:
            _type = FLATTEN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:132:9: ( 'FLATTEN' )
            # QueryLexer.g:132:11: 'FLATTEN'
            pass 
            self.match("FLATTEN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLATTEN"



    # $ANTLR start "ASC"
    def mASC(self, ):

        try:
            _type = ASC
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:135:5: ( 'ASC' )
            # QueryLexer.g:135:7: 'ASC'
            pass 
            self.match("ASC")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASC"



    # $ANTLR start "DESC"
    def mDESC(self, ):

        try:
            _type = DESC
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:138:6: ( 'DESC' )
            # QueryLexer.g:138:8: 'DESC'
            pass 
            self.match("DESC")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DESC"



    # $ANTLR start "BOOLEAN"
    def mBOOLEAN(self, ):

        try:
            _type = BOOLEAN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:141:9: ( 'BOOLEAN' )
            # QueryLexer.g:141:11: 'BOOLEAN'
            pass 
            self.match("BOOLEAN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOOLEAN"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:144:5: ( 'INT' )
            # QueryLexer.g:144:7: 'INT'
            pass 
            self.match("INT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "LONG"
    def mLONG(self, ):

        try:
            _type = LONG
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:147:6: ( 'LONG' )
            # QueryLexer.g:147:8: 'LONG'
            pass 
            self.match("LONG")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LONG"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:150:7: ( 'FLOAT' )
            # QueryLexer.g:150:9: 'FLOAT'
            pass 
            self.match("FLOAT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "DOUBLE"
    def mDOUBLE(self, ):

        try:
            _type = DOUBLE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:153:8: ( 'DOUBLE' )
            # QueryLexer.g:153:10: 'DOUBLE'
            pass 
            self.match("DOUBLE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE"



    # $ANTLR start "DATETIME"
    def mDATETIME(self, ):

        try:
            _type = DATETIME
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:156:10: ( 'DATETIME' )
            # QueryLexer.g:156:12: 'DATETIME'
            pass 
            self.match("DATETIME")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DATETIME"



    # $ANTLR start "CHARARRAY"
    def mCHARARRAY(self, ):

        try:
            _type = CHARARRAY
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:159:11: ( 'CHARARRAY' )
            # QueryLexer.g:159:13: 'CHARARRAY'
            pass 
            self.match("CHARARRAY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CHARARRAY"



    # $ANTLR start "BYTEARRAY"
    def mBYTEARRAY(self, ):

        try:
            _type = BYTEARRAY
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:162:11: ( 'BYTEARRAY' )
            # QueryLexer.g:162:13: 'BYTEARRAY'
            pass 
            self.match("BYTEARRAY")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BYTEARRAY"



    # $ANTLR start "BAG"
    def mBAG(self, ):

        try:
            _type = BAG
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:165:5: ( 'BAG' )
            # QueryLexer.g:165:7: 'BAG'
            pass 
            self.match("BAG")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BAG"



    # $ANTLR start "TUPLE"
    def mTUPLE(self, ):

        try:
            _type = TUPLE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:168:7: ( 'TUPLE' )
            # QueryLexer.g:168:9: 'TUPLE'
            pass 
            self.match("TUPLE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TUPLE"



    # $ANTLR start "MAP"
    def mMAP(self, ):

        try:
            _type = MAP
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:171:5: ( 'MAP' )
            # QueryLexer.g:171:7: 'MAP'
            pass 
            self.match("MAP")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAP"



    # $ANTLR start "IS"
    def mIS(self, ):

        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:174:4: ( 'IS' )
            # QueryLexer.g:174:6: 'IS'
            pass 
            self.match("IS")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IS"



    # $ANTLR start "STREAM"
    def mSTREAM(self, ):

        try:
            _type = STREAM
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:177:8: ( 'STREAM' )
            # QueryLexer.g:177:10: 'STREAM'
            pass 
            self.match("STREAM")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STREAM"



    # $ANTLR start "THROUGH"
    def mTHROUGH(self, ):

        try:
            _type = THROUGH
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:180:9: ( 'THROUGH' )
            # QueryLexer.g:180:11: 'THROUGH'
            pass 
            self.match("THROUGH")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THROUGH"



    # $ANTLR start "STORE"
    def mSTORE(self, ):

        try:
            _type = STORE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:183:7: ( 'STORE' )
            # QueryLexer.g:183:9: 'STORE'
            pass 
            self.match("STORE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STORE"



    # $ANTLR start "MAPREDUCE"
    def mMAPREDUCE(self, ):

        try:
            _type = MAPREDUCE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:186:11: ( 'MAPREDUCE' )
            # QueryLexer.g:186:13: 'MAPREDUCE'
            pass 
            self.match("MAPREDUCE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MAPREDUCE"



    # $ANTLR start "SHIP"
    def mSHIP(self, ):

        try:
            _type = SHIP
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:189:6: ( 'SHIP' )
            # QueryLexer.g:189:8: 'SHIP'
            pass 
            self.match("SHIP")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SHIP"



    # $ANTLR start "CACHE"
    def mCACHE(self, ):

        try:
            _type = CACHE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:192:7: ( 'CACHE' )
            # QueryLexer.g:192:9: 'CACHE'
            pass 
            self.match("CACHE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CACHE"



    # $ANTLR start "INPUT"
    def mINPUT(self, ):

        try:
            _type = INPUT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:195:7: ( 'INPUT' )
            # QueryLexer.g:195:9: 'INPUT'
            pass 
            self.match("INPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INPUT"



    # $ANTLR start "OUTPUT"
    def mOUTPUT(self, ):

        try:
            _type = OUTPUT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:198:8: ( 'OUTPUT' )
            # QueryLexer.g:198:10: 'OUTPUT'
            pass 
            self.match("OUTPUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OUTPUT"



    # $ANTLR start "STDERROR"
    def mSTDERROR(self, ):

        try:
            _type = STDERROR
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:201:10: ( 'STDERR' )
            # QueryLexer.g:201:12: 'STDERR'
            pass 
            self.match("STDERR")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STDERROR"



    # $ANTLR start "STDIN"
    def mSTDIN(self, ):

        try:
            _type = STDIN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:204:7: ( 'STDIN' )
            # QueryLexer.g:204:9: 'STDIN'
            pass 
            self.match("STDIN")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STDIN"



    # $ANTLR start "STDOUT"
    def mSTDOUT(self, ):

        try:
            _type = STDOUT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:207:8: ( 'STDOUT' )
            # QueryLexer.g:207:10: 'STDOUT'
            pass 
            self.match("STDOUT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STDOUT"



    # $ANTLR start "LIMIT"
    def mLIMIT(self, ):

        try:
            _type = LIMIT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:210:7: ( 'LIMIT' )
            # QueryLexer.g:210:9: 'LIMIT'
            pass 
            self.match("LIMIT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LIMIT"



    # $ANTLR start "SAMPLE"
    def mSAMPLE(self, ):

        try:
            _type = SAMPLE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:213:8: ( 'SAMPLE' )
            # QueryLexer.g:213:10: 'SAMPLE'
            pass 
            self.match("SAMPLE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SAMPLE"



    # $ANTLR start "LEFT"
    def mLEFT(self, ):

        try:
            _type = LEFT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:216:6: ( 'LEFT' )
            # QueryLexer.g:216:8: 'LEFT'
            pass 
            self.match("LEFT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT"



    # $ANTLR start "RIGHT"
    def mRIGHT(self, ):

        try:
            _type = RIGHT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:219:7: ( 'RIGHT' )
            # QueryLexer.g:219:9: 'RIGHT'
            pass 
            self.match("RIGHT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT"



    # $ANTLR start "FULL"
    def mFULL(self, ):

        try:
            _type = FULL
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:222:6: ( 'FULL' )
            # QueryLexer.g:222:8: 'FULL'
            pass 
            self.match("FULL")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FULL"



    # $ANTLR start "STR_OP_EQ"
    def mSTR_OP_EQ(self, ):

        try:
            _type = STR_OP_EQ
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:225:11: ( 'EQ' )
            # QueryLexer.g:225:13: 'EQ'
            pass 
            self.match("EQ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_EQ"



    # $ANTLR start "STR_OP_GT"
    def mSTR_OP_GT(self, ):

        try:
            _type = STR_OP_GT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:228:11: ( 'GT' )
            # QueryLexer.g:228:13: 'GT'
            pass 
            self.match("GT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_GT"



    # $ANTLR start "STR_OP_LT"
    def mSTR_OP_LT(self, ):

        try:
            _type = STR_OP_LT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:231:11: ( 'LT' )
            # QueryLexer.g:231:13: 'LT'
            pass 
            self.match("LT")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_LT"



    # $ANTLR start "STR_OP_GTE"
    def mSTR_OP_GTE(self, ):

        try:
            _type = STR_OP_GTE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:234:12: ( 'GTE' )
            # QueryLexer.g:234:14: 'GTE'
            pass 
            self.match("GTE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_GTE"



    # $ANTLR start "STR_OP_LTE"
    def mSTR_OP_LTE(self, ):

        try:
            _type = STR_OP_LTE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:237:12: ( 'LTE' )
            # QueryLexer.g:237:14: 'LTE'
            pass 
            self.match("LTE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_LTE"



    # $ANTLR start "STR_OP_NE"
    def mSTR_OP_NE(self, ):

        try:
            _type = STR_OP_NE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:240:11: ( 'NEQ' )
            # QueryLexer.g:240:13: 'NEQ'
            pass 
            self.match("NEQ")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_NE"



    # $ANTLR start "STR_OP_MATCHES"
    def mSTR_OP_MATCHES(self, ):

        try:
            _type = STR_OP_MATCHES
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:243:16: ( 'MATCHES' )
            # QueryLexer.g:243:18: 'MATCHES'
            pass 
            self.match("MATCHES")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STR_OP_MATCHES"



    # $ANTLR start "TRUE"
    def mTRUE(self, ):

        try:
            _type = TRUE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:246:6: ( 'TRUE' )
            # QueryLexer.g:246:8: 'TRUE'
            pass 
            self.match("TRUE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TRUE"



    # $ANTLR start "FALSE"
    def mFALSE(self, ):

        try:
            _type = FALSE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:249:7: ( 'FALSE' )
            # QueryLexer.g:249:9: 'FALSE'
            pass 
            self.match("FALSE")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FALSE"



    # $ANTLR start "NUM_OP_EQ"
    def mNUM_OP_EQ(self, ):

        try:
            _type = NUM_OP_EQ
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:252:11: ( '==' )
            # QueryLexer.g:252:13: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_EQ"



    # $ANTLR start "NUM_OP_LT"
    def mNUM_OP_LT(self, ):

        try:
            _type = NUM_OP_LT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:255:11: ( '<' )
            # QueryLexer.g:255:13: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_LT"



    # $ANTLR start "NUM_OP_LTE"
    def mNUM_OP_LTE(self, ):

        try:
            _type = NUM_OP_LTE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:258:12: ( '<=' )
            # QueryLexer.g:258:14: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_LTE"



    # $ANTLR start "NUM_OP_GT"
    def mNUM_OP_GT(self, ):

        try:
            _type = NUM_OP_GT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:261:11: ( '>' )
            # QueryLexer.g:261:13: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_GT"



    # $ANTLR start "NUM_OP_GTE"
    def mNUM_OP_GTE(self, ):

        try:
            _type = NUM_OP_GTE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:264:12: ( '>=' )
            # QueryLexer.g:264:14: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_GTE"



    # $ANTLR start "NUM_OP_NE"
    def mNUM_OP_NE(self, ):

        try:
            _type = NUM_OP_NE
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:267:11: ( '!=' )
            # QueryLexer.g:267:13: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NUM_OP_NE"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # QueryLexer.g:270:16: ( '0' .. '9' )
            # QueryLexer.g:270:18: '0' .. '9'
            pass 
            self.matchRange(48, 57)




        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # QueryLexer.g:273:17: ( 'A' .. 'Z' )
            # QueryLexer.g:273:19: 'A' .. 'Z'
            pass 
            self.matchRange(65, 90)




        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "SPECIALCHAR"
    def mSPECIALCHAR(self, ):

        try:
            # QueryLexer.g:276:22: ( '_' )
            # QueryLexer.g:276:24: '_'
            pass 
            self.match(95)




        finally:

            pass

    # $ANTLR end "SPECIALCHAR"



    # $ANTLR start "ID"
    def mID(self, ):

        try:
            # QueryLexer.g:279:12: ( LETTER ( DIGIT | LETTER | SPECIALCHAR )* )
            # QueryLexer.g:279:14: LETTER ( DIGIT | LETTER | SPECIALCHAR )*
            pass 
            self.mLETTER()
            # QueryLexer.g:279:21: ( DIGIT | LETTER | SPECIALCHAR )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or (65 <= LA1_0 <= 90) or LA1_0 == 95) :
                    alt1 = 1


                if alt1 == 1:
                    # QueryLexer.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop1




        finally:

            pass

    # $ANTLR end "ID"



    # $ANTLR start "DCOLON"
    def mDCOLON(self, ):

        try:
            _type = DCOLON
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:282:8: ( '::' )
            # QueryLexer.g:282:10: '::'
            pass 
            self.match("::")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DCOLON"



    # $ANTLR start "IDENTIFIER_L"
    def mIDENTIFIER_L(self, ):

        try:
            _type = IDENTIFIER_L
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:285:14: ( ( ID DCOLON )=> ( ID DCOLON IDENTIFIER_L ) | ID )
            alt2 = 2
            alt2 = self.dfa2.predict(self.input)
            if alt2 == 1:
                # QueryLexer.g:285:16: ( ID DCOLON )=> ( ID DCOLON IDENTIFIER_L )
                pass 
                # QueryLexer.g:285:33: ( ID DCOLON IDENTIFIER_L )
                # QueryLexer.g:285:35: ID DCOLON IDENTIFIER_L
                pass 
                self.mID()
                self.mDCOLON()
                self.mIDENTIFIER_L()





            elif alt2 == 2:
                # QueryLexer.g:286:14: ID
                pass 
                self.mID()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER_L"



    # $ANTLR start "FLOATINGPOINT"
    def mFLOATINGPOINT(self, ):

        try:
            # QueryLexer.g:289:24: ( INTEGER ( PERIOD INTEGER )? | PERIOD INTEGER )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if ((48 <= LA4_0 <= 57)) :
                alt4 = 1
            elif (LA4_0 == 46) :
                alt4 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae

            if alt4 == 1:
                # QueryLexer.g:289:26: INTEGER ( PERIOD INTEGER )?
                pass 
                self.mINTEGER()
                # QueryLexer.g:289:34: ( PERIOD INTEGER )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 46) :
                    alt3 = 1
                if alt3 == 1:
                    # QueryLexer.g:289:36: PERIOD INTEGER
                    pass 
                    self.mPERIOD()
                    self.mINTEGER()





            elif alt4 == 2:
                # QueryLexer.g:289:56: PERIOD INTEGER
                pass 
                self.mPERIOD()
                self.mINTEGER()



        finally:

            pass

    # $ANTLR end "FLOATINGPOINT"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:292:8: ( ( DIGIT )+ )
            # QueryLexer.g:292:10: ( DIGIT )+
            pass 
            # QueryLexer.g:292:10: ( DIGIT )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57)) :
                    alt5 = 1


                if alt5 == 1:
                    # QueryLexer.g:292:12: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt5 >= 1:
                        break #loop5

                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "LONGINTEGER"
    def mLONGINTEGER(self, ):

        try:
            _type = LONGINTEGER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:295:12: ( INTEGER ( 'L' )? )
            # QueryLexer.g:295:14: INTEGER ( 'L' )?
            pass 
            self.mINTEGER()
            # QueryLexer.g:295:22: ( 'L' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 76) :
                alt6 = 1
            if alt6 == 1:
                # QueryLexer.g:295:24: 'L'
                pass 
                self.match(76)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LONGINTEGER"



    # $ANTLR start "DOLLARVAR"
    def mDOLLARVAR(self, ):

        try:
            _type = DOLLARVAR
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:298:11: ( DOLLAR INTEGER )
            # QueryLexer.g:298:13: DOLLAR INTEGER
            pass 
            self.mDOLLAR()
            self.mINTEGER()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOLLARVAR"



    # $ANTLR start "DOUBLENUMBER"
    def mDOUBLENUMBER(self, ):

        try:
            _type = DOUBLENUMBER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:301:14: ( FLOATINGPOINT ( 'E' ( MINUS | PLUS )? INTEGER )? )
            # QueryLexer.g:301:16: FLOATINGPOINT ( 'E' ( MINUS | PLUS )? INTEGER )?
            pass 
            self.mFLOATINGPOINT()
            # QueryLexer.g:301:30: ( 'E' ( MINUS | PLUS )? INTEGER )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 69) :
                alt8 = 1
            if alt8 == 1:
                # QueryLexer.g:301:32: 'E' ( MINUS | PLUS )? INTEGER
                pass 
                self.match(69)
                # QueryLexer.g:301:36: ( MINUS | PLUS )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 43 or LA7_0 == 45) :
                    alt7 = 1
                if alt7 == 1:
                    # QueryLexer.g:
                    pass 
                    if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                self.mINTEGER()






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLENUMBER"



    # $ANTLR start "FLOATNUMBER"
    def mFLOATNUMBER(self, ):

        try:
            _type = FLOATNUMBER
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:304:13: ( DOUBLENUMBER ( 'F' )? )
            # QueryLexer.g:304:15: DOUBLENUMBER ( 'F' )?
            pass 
            self.mDOUBLENUMBER()
            # QueryLexer.g:304:28: ( 'F' )?
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 70) :
                alt9 = 1
            if alt9 == 1:
                # QueryLexer.g:304:30: 'F'
                pass 
                self.match(70)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOATNUMBER"



    # $ANTLR start "QUOTEDSTRING"
    def mQUOTEDSTRING(self, ):

        try:
            _type = QUOTEDSTRING
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:307:14: ( '\\'' ( (~ ( '\\'' | '\\\\' | '\\n' | '\\r' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )* '\\'' )
            # QueryLexer.g:307:17: '\\'' ( (~ ( '\\'' | '\\\\' | '\\n' | '\\r' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )* '\\''
            pass 
            self.match(39)
            # QueryLexer.g:307:22: ( (~ ( '\\'' | '\\\\' | '\\n' | '\\r' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )*
            while True: #loop10
                alt10 = 4
                LA10_0 = self.input.LA(1)

                if ((0 <= LA10_0 <= 9) or (11 <= LA10_0 <= 12) or (14 <= LA10_0 <= 38) or (40 <= LA10_0 <= 91) or (93 <= LA10_0 <= 65535)) :
                    alt10 = 1
                elif (LA10_0 == 92) :
                    LA10_3 = self.input.LA(2)

                    if (LA10_3 == 39 or LA10_3 == 66 or LA10_3 == 70 or LA10_3 == 78 or LA10_3 == 82 or LA10_3 == 84 or LA10_3 == 92) :
                        alt10 = 2
                    elif (LA10_3 == 85) :
                        alt10 = 3




                if alt10 == 1:
                    # QueryLexer.g:307:26: (~ ( '\\'' | '\\\\' | '\\n' | '\\r' ) )
                    pass 
                    # QueryLexer.g:307:26: (~ ( '\\'' | '\\\\' | '\\n' | '\\r' ) )
                    # QueryLexer.g:307:28: ~ ( '\\'' | '\\\\' | '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                elif alt10 == 2:
                    # QueryLexer.g:308:26: ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) ) )
                    pass 
                    # QueryLexer.g:308:26: ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) ) )
                    # QueryLexer.g:308:28: '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) )
                    pass 
                    self.match(92)
                    # QueryLexer.g:308:33: ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' ) )
                    # QueryLexer.g:308:35: ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' )
                    pass 
                    if self.input.LA(1) == 39 or self.input.LA(1) == 66 or self.input.LA(1) == 70 or self.input.LA(1) == 78 or self.input.LA(1) == 82 or self.input.LA(1) == 84 or self.input.LA(1) == 92:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse









                elif alt10 == 3:
                    # QueryLexer.g:309:26: ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) )
                    pass 
                    # QueryLexer.g:309:26: ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) )
                    # QueryLexer.g:309:28: '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' )
                    pass 
                    self.match("\\U")
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                else:
                    break #loop10
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUOTEDSTRING"



    # $ANTLR start "MULTILINE_QUOTEDSTRING"
    def mMULTILINE_QUOTEDSTRING(self, ):

        try:
            _type = MULTILINE_QUOTEDSTRING
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:317:24: ( '\\'' ( (~ ( '\\'' | '\\\\' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )* '\\'' )
            # QueryLexer.g:317:27: '\\'' ( (~ ( '\\'' | '\\\\' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )* '\\''
            pass 
            self.match(39)
            # QueryLexer.g:317:32: ( (~ ( '\\'' | '\\\\' ) ) | ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) ) ) | ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ) )*
            while True: #loop11
                alt11 = 4
                LA11_0 = self.input.LA(1)

                if ((0 <= LA11_0 <= 38) or (40 <= LA11_0 <= 91) or (93 <= LA11_0 <= 65535)) :
                    alt11 = 1
                elif (LA11_0 == 92) :
                    LA11_3 = self.input.LA(2)

                    if (LA11_3 == 39 or LA11_3 == 66 or LA11_3 == 70 or LA11_3 == 78 or LA11_3 == 82 or LA11_3 == 84 or LA11_3 == 92 or LA11_3 == 110 or LA11_3 == 114) :
                        alt11 = 2
                    elif (LA11_3 == 85) :
                        alt11 = 3




                if alt11 == 1:
                    # QueryLexer.g:317:36: (~ ( '\\'' | '\\\\' ) )
                    pass 
                    # QueryLexer.g:317:36: (~ ( '\\'' | '\\\\' ) )
                    # QueryLexer.g:317:38: ~ ( '\\'' | '\\\\' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                elif alt11 == 2:
                    # QueryLexer.g:318:36: ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) ) )
                    pass 
                    # QueryLexer.g:318:36: ( '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) ) )
                    # QueryLexer.g:318:38: '\\\\' ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) )
                    pass 
                    self.match(92)
                    # QueryLexer.g:318:43: ( ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' ) )
                    # QueryLexer.g:318:45: ( 'N' | 'T' | 'B' | 'R' | 'F' | '\\\\' | '\\'' | 'n' | 'r' )
                    pass 
                    if self.input.LA(1) == 39 or self.input.LA(1) == 66 or self.input.LA(1) == 70 or self.input.LA(1) == 78 or self.input.LA(1) == 82 or self.input.LA(1) == 84 or self.input.LA(1) == 92 or self.input.LA(1) == 110 or self.input.LA(1) == 114:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse









                elif alt11 == 3:
                    # QueryLexer.g:319:36: ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) )
                    pass 
                    # QueryLexer.g:319:36: ( '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) )
                    # QueryLexer.g:319:38: '\\\\U' ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' ) ( '0' .. '9' | 'A' .. 'F' )
                    pass 
                    self.match("\\U")
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse

                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                else:
                    break #loop11
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MULTILINE_QUOTEDSTRING"



    # $ANTLR start "EXECCOMMAND"
    def mEXECCOMMAND(self, ):

        try:
            _type = EXECCOMMAND
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:327:13: ( '`' (~ ( '`' ) )* '`' )
            # QueryLexer.g:327:15: '`' (~ ( '`' ) )* '`'
            pass 
            self.match(96)
            # QueryLexer.g:327:19: (~ ( '`' ) )*
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((0 <= LA12_0 <= 95) or (97 <= LA12_0 <= 65535)) :
                    alt12 = 1


                if alt12 == 1:
                    # QueryLexer.g:327:21: ~ ( '`' )
                    pass 
                    if (0 <= self.input.LA(1) <= 95) or (97 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop12
            self.match(96)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXECCOMMAND"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:330:6: ( '*' )
            # QueryLexer.g:330:8: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:333:7: ( ':' )
            # QueryLexer.g:333:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "DOLLAR"
    def mDOLLAR(self, ):

        try:
            _type = DOLLAR
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:336:8: ( '$' )
            # QueryLexer.g:336:10: '$'
            pass 
            self.match(36)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOLLAR"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:339:5: ( ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' ) )
            # QueryLexer.g:339:8: ( ' ' | '\\r' | '\\t' | '\\u000C' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            if self._state.backtracking == 0:
                _channel = HIDDEN; 




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "SL_COMMENT"
    def mSL_COMMENT(self, ):

        try:
            _type = SL_COMMENT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:342:12: ( '--' (~ ( '\\r' | '\\n' ) )* )
            # QueryLexer.g:342:14: '--' (~ ( '\\r' | '\\n' ) )*
            pass 
            self.match("--")
            # QueryLexer.g:342:19: (~ ( '\\r' | '\\n' ) )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if ((0 <= LA13_0 <= 9) or (11 <= LA13_0 <= 12) or (14 <= LA13_0 <= 65535)) :
                    alt13 = 1


                if alt13 == 1:
                    # QueryLexer.g:342:21: ~ ( '\\r' | '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop13
            if self._state.backtracking == 0:
                _channel = HIDDEN; 




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SL_COMMENT"



    # $ANTLR start "ML_COMMENT"
    def mML_COMMENT(self, ):

        try:
            _type = ML_COMMENT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:345:12: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # QueryLexer.g:345:14: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")
            # QueryLexer.g:345:19: ( options {greedy=false; } : . )*
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 42) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == 47) :
                        alt14 = 2
                    elif ((0 <= LA14_1 <= 46) or (48 <= LA14_1 <= 65535)) :
                        alt14 = 1


                elif ((0 <= LA14_0 <= 41) or (43 <= LA14_0 <= 65535)) :
                    alt14 = 1


                if alt14 == 1:
                    # QueryLexer.g:345:49: .
                    pass 
                    self.matchAny()


                else:
                    break #loop14
            self.match("*/")
            if self._state.backtracking == 0:
                _channel = HIDDEN; 




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ML_COMMENT"



    # $ANTLR start "SEMI_COLON"
    def mSEMI_COLON(self, ):

        try:
            _type = SEMI_COLON
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:348:12: ( ';' )
            # QueryLexer.g:348:14: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI_COLON"



    # $ANTLR start "LEFT_PAREN"
    def mLEFT_PAREN(self, ):

        try:
            _type = LEFT_PAREN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:351:12: ( '(' )
            # QueryLexer.g:351:14: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT_PAREN"



    # $ANTLR start "RIGHT_PAREN"
    def mRIGHT_PAREN(self, ):

        try:
            _type = RIGHT_PAREN
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:354:13: ( ')' )
            # QueryLexer.g:354:15: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT_PAREN"



    # $ANTLR start "LEFT_CURLY"
    def mLEFT_CURLY(self, ):

        try:
            _type = LEFT_CURLY
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:357:12: ( '{' )
            # QueryLexer.g:357:14: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT_CURLY"



    # $ANTLR start "RIGHT_CURLY"
    def mRIGHT_CURLY(self, ):

        try:
            _type = RIGHT_CURLY
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:360:13: ( '}' )
            # QueryLexer.g:360:15: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT_CURLY"



    # $ANTLR start "LEFT_BRACKET"
    def mLEFT_BRACKET(self, ):

        try:
            _type = LEFT_BRACKET
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:363:14: ( '[' )
            # QueryLexer.g:363:16: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT_BRACKET"



    # $ANTLR start "RIGHT_BRACKET"
    def mRIGHT_BRACKET(self, ):

        try:
            _type = RIGHT_BRACKET
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:366:15: ( ']' )
            # QueryLexer.g:366:17: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT_BRACKET"



    # $ANTLR start "POUND"
    def mPOUND(self, ):

        try:
            _type = POUND
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:369:7: ( '#' )
            # QueryLexer.g:369:9: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "POUND"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:372:7: ( '=' )
            # QueryLexer.g:372:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:375:7: ( ',' )
            # QueryLexer.g:375:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "PERIOD"
    def mPERIOD(self, ):

        try:
            _type = PERIOD
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:378:8: ( '.' )
            # QueryLexer.g:378:10: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERIOD"



    # $ANTLR start "DOUBLE_PERIOD"
    def mDOUBLE_PERIOD(self, ):

        try:
            _type = DOUBLE_PERIOD
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:381:15: ( '..' )
            # QueryLexer.g:381:17: '..'
            pass 
            self.match("..")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_PERIOD"



    # $ANTLR start "DIV"
    def mDIV(self, ):

        try:
            _type = DIV
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:384:5: ( '/' )
            # QueryLexer.g:384:7: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DIV"



    # $ANTLR start "PERCENT"
    def mPERCENT(self, ):

        try:
            _type = PERCENT
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:387:9: ( '%' )
            # QueryLexer.g:387:11: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENT"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:390:6: ( '+' )
            # QueryLexer.g:390:8: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:393:7: ( '-' )
            # QueryLexer.g:393:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "QMARK"
    def mQMARK(self, ):

        try:
            _type = QMARK
            _channel = DEFAULT_CHANNEL

            # QueryLexer.g:396:7: ( '?' )
            # QueryLexer.g:396:9: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QMARK"



    def mTokens(self):
        # QueryLexer.g:1:8: ( VOID | IMPORT | RETURNS | DEFINE | LOAD | FILTER | FOREACH | ORDER | RANK | DENSE | CUBE | ROLLUP | DISTINCT | COGROUP | JOIN | CROSS | UNION | SPLIT | INTO | IF | OTHERWISE | ALL | AS | BY | USING | INNER | OUTER | ONSCHEMA | PARALLEL | PARTITION | GROUP | AND | OR | NOT | GENERATE | FLATTEN | ASC | DESC | BOOLEAN | INT | LONG | FLOAT | DOUBLE | DATETIME | CHARARRAY | BYTEARRAY | BAG | TUPLE | MAP | IS | STREAM | THROUGH | STORE | MAPREDUCE | SHIP | CACHE | INPUT | OUTPUT | STDERROR | STDIN | STDOUT | LIMIT | SAMPLE | LEFT | RIGHT | FULL | STR_OP_EQ | STR_OP_GT | STR_OP_LT | STR_OP_GTE | STR_OP_LTE | STR_OP_NE | STR_OP_MATCHES | TRUE | FALSE | NUM_OP_EQ | NUM_OP_LT | NUM_OP_LTE | NUM_OP_GT | NUM_OP_GTE | NUM_OP_NE | DCOLON | IDENTIFIER_L | INTEGER | LONGINTEGER | DOLLARVAR | DOUBLENUMBER | FLOATNUMBER | QUOTEDSTRING | MULTILINE_QUOTEDSTRING | EXECCOMMAND | STAR | COLON | DOLLAR | WS | SL_COMMENT | ML_COMMENT | SEMI_COLON | LEFT_PAREN | RIGHT_PAREN | LEFT_CURLY | RIGHT_CURLY | LEFT_BRACKET | RIGHT_BRACKET | POUND | EQUAL | COMMA | PERIOD | DOUBLE_PERIOD | DIV | PERCENT | PLUS | MINUS | QMARK )
        alt15 = 114
        alt15 = self.dfa15.predict(self.input)
        if alt15 == 1:
            # QueryLexer.g:1:10: VOID
            pass 
            self.mVOID()


        elif alt15 == 2:
            # QueryLexer.g:1:15: IMPORT
            pass 
            self.mIMPORT()


        elif alt15 == 3:
            # QueryLexer.g:1:22: RETURNS
            pass 
            self.mRETURNS()


        elif alt15 == 4:
            # QueryLexer.g:1:30: DEFINE
            pass 
            self.mDEFINE()


        elif alt15 == 5:
            # QueryLexer.g:1:37: LOAD
            pass 
            self.mLOAD()


        elif alt15 == 6:
            # QueryLexer.g:1:42: FILTER
            pass 
            self.mFILTER()


        elif alt15 == 7:
            # QueryLexer.g:1:49: FOREACH
            pass 
            self.mFOREACH()


        elif alt15 == 8:
            # QueryLexer.g:1:57: ORDER
            pass 
            self.mORDER()


        elif alt15 == 9:
            # QueryLexer.g:1:63: RANK
            pass 
            self.mRANK()


        elif alt15 == 10:
            # QueryLexer.g:1:68: DENSE
            pass 
            self.mDENSE()


        elif alt15 == 11:
            # QueryLexer.g:1:74: CUBE
            pass 
            self.mCUBE()


        elif alt15 == 12:
            # QueryLexer.g:1:79: ROLLUP
            pass 
            self.mROLLUP()


        elif alt15 == 13:
            # QueryLexer.g:1:86: DISTINCT
            pass 
            self.mDISTINCT()


        elif alt15 == 14:
            # QueryLexer.g:1:95: COGROUP
            pass 
            self.mCOGROUP()


        elif alt15 == 15:
            # QueryLexer.g:1:103: JOIN
            pass 
            self.mJOIN()


        elif alt15 == 16:
            # QueryLexer.g:1:108: CROSS
            pass 
            self.mCROSS()


        elif alt15 == 17:
            # QueryLexer.g:1:114: UNION
            pass 
            self.mUNION()


        elif alt15 == 18:
            # QueryLexer.g:1:120: SPLIT
            pass 
            self.mSPLIT()


        elif alt15 == 19:
            # QueryLexer.g:1:126: INTO
            pass 
            self.mINTO()


        elif alt15 == 20:
            # QueryLexer.g:1:131: IF
            pass 
            self.mIF()


        elif alt15 == 21:
            # QueryLexer.g:1:134: OTHERWISE
            pass 
            self.mOTHERWISE()


        elif alt15 == 22:
            # QueryLexer.g:1:144: ALL
            pass 
            self.mALL()


        elif alt15 == 23:
            # QueryLexer.g:1:148: AS
            pass 
            self.mAS()


        elif alt15 == 24:
            # QueryLexer.g:1:151: BY
            pass 
            self.mBY()


        elif alt15 == 25:
            # QueryLexer.g:1:154: USING
            pass 
            self.mUSING()


        elif alt15 == 26:
            # QueryLexer.g:1:160: INNER
            pass 
            self.mINNER()


        elif alt15 == 27:
            # QueryLexer.g:1:166: OUTER
            pass 
            self.mOUTER()


        elif alt15 == 28:
            # QueryLexer.g:1:172: ONSCHEMA
            pass 
            self.mONSCHEMA()


        elif alt15 == 29:
            # QueryLexer.g:1:181: PARALLEL
            pass 
            self.mPARALLEL()


        elif alt15 == 30:
            # QueryLexer.g:1:190: PARTITION
            pass 
            self.mPARTITION()


        elif alt15 == 31:
            # QueryLexer.g:1:200: GROUP
            pass 
            self.mGROUP()


        elif alt15 == 32:
            # QueryLexer.g:1:206: AND
            pass 
            self.mAND()


        elif alt15 == 33:
            # QueryLexer.g:1:210: OR
            pass 
            self.mOR()


        elif alt15 == 34:
            # QueryLexer.g:1:213: NOT
            pass 
            self.mNOT()


        elif alt15 == 35:
            # QueryLexer.g:1:217: GENERATE
            pass 
            self.mGENERATE()


        elif alt15 == 36:
            # QueryLexer.g:1:226: FLATTEN
            pass 
            self.mFLATTEN()


        elif alt15 == 37:
            # QueryLexer.g:1:234: ASC
            pass 
            self.mASC()


        elif alt15 == 38:
            # QueryLexer.g:1:238: DESC
            pass 
            self.mDESC()


        elif alt15 == 39:
            # QueryLexer.g:1:243: BOOLEAN
            pass 
            self.mBOOLEAN()


        elif alt15 == 40:
            # QueryLexer.g:1:251: INT
            pass 
            self.mINT()


        elif alt15 == 41:
            # QueryLexer.g:1:255: LONG
            pass 
            self.mLONG()


        elif alt15 == 42:
            # QueryLexer.g:1:260: FLOAT
            pass 
            self.mFLOAT()


        elif alt15 == 43:
            # QueryLexer.g:1:266: DOUBLE
            pass 
            self.mDOUBLE()


        elif alt15 == 44:
            # QueryLexer.g:1:273: DATETIME
            pass 
            self.mDATETIME()


        elif alt15 == 45:
            # QueryLexer.g:1:282: CHARARRAY
            pass 
            self.mCHARARRAY()


        elif alt15 == 46:
            # QueryLexer.g:1:292: BYTEARRAY
            pass 
            self.mBYTEARRAY()


        elif alt15 == 47:
            # QueryLexer.g:1:302: BAG
            pass 
            self.mBAG()


        elif alt15 == 48:
            # QueryLexer.g:1:306: TUPLE
            pass 
            self.mTUPLE()


        elif alt15 == 49:
            # QueryLexer.g:1:312: MAP
            pass 
            self.mMAP()


        elif alt15 == 50:
            # QueryLexer.g:1:316: IS
            pass 
            self.mIS()


        elif alt15 == 51:
            # QueryLexer.g:1:319: STREAM
            pass 
            self.mSTREAM()


        elif alt15 == 52:
            # QueryLexer.g:1:326: THROUGH
            pass 
            self.mTHROUGH()


        elif alt15 == 53:
            # QueryLexer.g:1:334: STORE
            pass 
            self.mSTORE()


        elif alt15 == 54:
            # QueryLexer.g:1:340: MAPREDUCE
            pass 
            self.mMAPREDUCE()


        elif alt15 == 55:
            # QueryLexer.g:1:350: SHIP
            pass 
            self.mSHIP()


        elif alt15 == 56:
            # QueryLexer.g:1:355: CACHE
            pass 
            self.mCACHE()


        elif alt15 == 57:
            # QueryLexer.g:1:361: INPUT
            pass 
            self.mINPUT()


        elif alt15 == 58:
            # QueryLexer.g:1:367: OUTPUT
            pass 
            self.mOUTPUT()


        elif alt15 == 59:
            # QueryLexer.g:1:374: STDERROR
            pass 
            self.mSTDERROR()


        elif alt15 == 60:
            # QueryLexer.g:1:383: STDIN
            pass 
            self.mSTDIN()


        elif alt15 == 61:
            # QueryLexer.g:1:389: STDOUT
            pass 
            self.mSTDOUT()


        elif alt15 == 62:
            # QueryLexer.g:1:396: LIMIT
            pass 
            self.mLIMIT()


        elif alt15 == 63:
            # QueryLexer.g:1:402: SAMPLE
            pass 
            self.mSAMPLE()


        elif alt15 == 64:
            # QueryLexer.g:1:409: LEFT
            pass 
            self.mLEFT()


        elif alt15 == 65:
            # QueryLexer.g:1:414: RIGHT
            pass 
            self.mRIGHT()


        elif alt15 == 66:
            # QueryLexer.g:1:420: FULL
            pass 
            self.mFULL()


        elif alt15 == 67:
            # QueryLexer.g:1:425: STR_OP_EQ
            pass 
            self.mSTR_OP_EQ()


        elif alt15 == 68:
            # QueryLexer.g:1:435: STR_OP_GT
            pass 
            self.mSTR_OP_GT()


        elif alt15 == 69:
            # QueryLexer.g:1:445: STR_OP_LT
            pass 
            self.mSTR_OP_LT()


        elif alt15 == 70:
            # QueryLexer.g:1:455: STR_OP_GTE
            pass 
            self.mSTR_OP_GTE()


        elif alt15 == 71:
            # QueryLexer.g:1:466: STR_OP_LTE
            pass 
            self.mSTR_OP_LTE()


        elif alt15 == 72:
            # QueryLexer.g:1:477: STR_OP_NE
            pass 
            self.mSTR_OP_NE()


        elif alt15 == 73:
            # QueryLexer.g:1:487: STR_OP_MATCHES
            pass 
            self.mSTR_OP_MATCHES()


        elif alt15 == 74:
            # QueryLexer.g:1:502: TRUE
            pass 
            self.mTRUE()


        elif alt15 == 75:
            # QueryLexer.g:1:507: FALSE
            pass 
            self.mFALSE()


        elif alt15 == 76:
            # QueryLexer.g:1:513: NUM_OP_EQ
            pass 
            self.mNUM_OP_EQ()


        elif alt15 == 77:
            # QueryLexer.g:1:523: NUM_OP_LT
            pass 
            self.mNUM_OP_LT()


        elif alt15 == 78:
            # QueryLexer.g:1:533: NUM_OP_LTE
            pass 
            self.mNUM_OP_LTE()


        elif alt15 == 79:
            # QueryLexer.g:1:544: NUM_OP_GT
            pass 
            self.mNUM_OP_GT()


        elif alt15 == 80:
            # QueryLexer.g:1:554: NUM_OP_GTE
            pass 
            self.mNUM_OP_GTE()


        elif alt15 == 81:
            # QueryLexer.g:1:565: NUM_OP_NE
            pass 
            self.mNUM_OP_NE()


        elif alt15 == 82:
            # QueryLexer.g:1:575: DCOLON
            pass 
            self.mDCOLON()


        elif alt15 == 83:
            # QueryLexer.g:1:582: IDENTIFIER_L
            pass 
            self.mIDENTIFIER_L()


        elif alt15 == 84:
            # QueryLexer.g:1:595: INTEGER
            pass 
            self.mINTEGER()


        elif alt15 == 85:
            # QueryLexer.g:1:603: LONGINTEGER
            pass 
            self.mLONGINTEGER()


        elif alt15 == 86:
            # QueryLexer.g:1:615: DOLLARVAR
            pass 
            self.mDOLLARVAR()


        elif alt15 == 87:
            # QueryLexer.g:1:625: DOUBLENUMBER
            pass 
            self.mDOUBLENUMBER()


        elif alt15 == 88:
            # QueryLexer.g:1:638: FLOATNUMBER
            pass 
            self.mFLOATNUMBER()


        elif alt15 == 89:
            # QueryLexer.g:1:650: QUOTEDSTRING
            pass 
            self.mQUOTEDSTRING()


        elif alt15 == 90:
            # QueryLexer.g:1:663: MULTILINE_QUOTEDSTRING
            pass 
            self.mMULTILINE_QUOTEDSTRING()


        elif alt15 == 91:
            # QueryLexer.g:1:686: EXECCOMMAND
            pass 
            self.mEXECCOMMAND()


        elif alt15 == 92:
            # QueryLexer.g:1:698: STAR
            pass 
            self.mSTAR()


        elif alt15 == 93:
            # QueryLexer.g:1:703: COLON
            pass 
            self.mCOLON()


        elif alt15 == 94:
            # QueryLexer.g:1:709: DOLLAR
            pass 
            self.mDOLLAR()


        elif alt15 == 95:
            # QueryLexer.g:1:716: WS
            pass 
            self.mWS()


        elif alt15 == 96:
            # QueryLexer.g:1:719: SL_COMMENT
            pass 
            self.mSL_COMMENT()


        elif alt15 == 97:
            # QueryLexer.g:1:730: ML_COMMENT
            pass 
            self.mML_COMMENT()


        elif alt15 == 98:
            # QueryLexer.g:1:741: SEMI_COLON
            pass 
            self.mSEMI_COLON()


        elif alt15 == 99:
            # QueryLexer.g:1:752: LEFT_PAREN
            pass 
            self.mLEFT_PAREN()


        elif alt15 == 100:
            # QueryLexer.g:1:763: RIGHT_PAREN
            pass 
            self.mRIGHT_PAREN()


        elif alt15 == 101:
            # QueryLexer.g:1:775: LEFT_CURLY
            pass 
            self.mLEFT_CURLY()


        elif alt15 == 102:
            # QueryLexer.g:1:786: RIGHT_CURLY
            pass 
            self.mRIGHT_CURLY()


        elif alt15 == 103:
            # QueryLexer.g:1:798: LEFT_BRACKET
            pass 
            self.mLEFT_BRACKET()


        elif alt15 == 104:
            # QueryLexer.g:1:811: RIGHT_BRACKET
            pass 
            self.mRIGHT_BRACKET()


        elif alt15 == 105:
            # QueryLexer.g:1:825: POUND
            pass 
            self.mPOUND()


        elif alt15 == 106:
            # QueryLexer.g:1:831: EQUAL
            pass 
            self.mEQUAL()


        elif alt15 == 107:
            # QueryLexer.g:1:837: COMMA
            pass 
            self.mCOMMA()


        elif alt15 == 108:
            # QueryLexer.g:1:843: PERIOD
            pass 
            self.mPERIOD()


        elif alt15 == 109:
            # QueryLexer.g:1:850: DOUBLE_PERIOD
            pass 
            self.mDOUBLE_PERIOD()


        elif alt15 == 110:
            # QueryLexer.g:1:864: DIV
            pass 
            self.mDIV()


        elif alt15 == 111:
            # QueryLexer.g:1:868: PERCENT
            pass 
            self.mPERCENT()


        elif alt15 == 112:
            # QueryLexer.g:1:876: PLUS
            pass 
            self.mPLUS()


        elif alt15 == 113:
            # QueryLexer.g:1:881: MINUS
            pass 
            self.mMINUS()


        elif alt15 == 114:
            # QueryLexer.g:1:887: QMARK
            pass 
            self.mQMARK()






    # $ANTLR start "synpred1_QueryLexer"
    def synpred1_QueryLexer_fragment(self, ):
        # QueryLexer.g:285:16: ( ID DCOLON )
        # QueryLexer.g:285:18: ID DCOLON
        pass 
        self.mID()
        self.mDCOLON()


    # $ANTLR end "synpred1_QueryLexer"



    def synpred1_QueryLexer(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_QueryLexer_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\1\uffff\1\2\1\uffff\1\2\1\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\101\1\60\1\uffff\1\60\1\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\132\1\137\1\uffff\1\137\1\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1"
        )

    DFA2_special = DFA.unpack(
        u"\1\uffff\1\0\1\uffff\1\1\1\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\32\1"),
        DFA.unpack(u"\12\3\1\4\6\uffff\32\3\4\uffff\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\3\1\4\6\uffff\32\3\4\uffff\1\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    class DFA2(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA2_1 = input.LA(1)

                 
                index2_1 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA2_1 <= 57) or (65 <= LA2_1 <= 90) or LA2_1 == 95):
                    s = 3

                elif (LA2_1 == 58) and (self.synpred1_QueryLexer()):
                    s = 4

                else:
                    s = 2

                 
                input.seek(index2_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA2_3 = input.LA(1)

                 
                index2_3 = input.index()
                input.rewind()
                s = -1
                if ((48 <= LA2_3 <= 57) or (65 <= LA2_3 <= 90) or LA2_3 == 95):
                    s = 3

                elif (LA2_3 == 58) and (self.synpred1_QueryLexer()):
                    s = 4

                else:
                    s = 2

                 
                input.seek(index2_3)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 2, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\1\uffff\23\31\1\147\1\151\1\153\1\uffff\1\155\1\uffff\1\156\1"
        u"\163\1\166\4\uffff\1\175\1\177\14\uffff\3\31\1\u0085\1\u0086\13"
        u"\31\1\u0096\5\31\1\u009e\20\31\1\u00b2\1\31\1\u00b5\5\31\1\u00bc"
        u"\6\31\1\u00c4\21\uffff\1\u00c8\10\uffff\2\31\1\u00cf\2\31\2\uffff"
        u"\16\31\1\u00e0\1\uffff\7\31\1\uffff\21\31\1\u00fc\1\u00fd\1\uffff"
        u"\1\u00fe\1\31\1\uffff\1\31\1\u0101\3\31\1\u0106\1\uffff\1\u0107"
        u"\1\u0108\3\31\1\u010d\1\31\1\uffff\1\u00c8\1\uffff\1\u00c8\4\uffff"
        u"\1\u0110\1\31\1\u0112\1\uffff\3\31\1\u0116\4\31\1\u011b\3\31\1"
        u"\u011f\1\u0120\1\31\1\u0122\1\uffff\4\31\1\u0127\6\31\1\u012e\4"
        u"\31\1\u0133\10\31\1\u013c\1\31\3\uffff\2\31\1\uffff\4\31\3\uffff"
        u"\2\31\1\u0146\1\31\1\uffff\1\31\2\uffff\1\31\1\uffff\1\u014b\1"
        u"\u014c\1\31\1\uffff\1\31\1\u014f\1\31\1\u0151\1\uffff\3\31\2\uffff"
        u"\1\u0155\1\uffff\3\31\1\u0159\1\uffff\1\u015a\1\u015b\1\31\1\u015d"
        u"\2\31\1\uffff\1\31\1\u0161\1\31\1\u0163\1\uffff\1\u0164\1\u0165"
        u"\1\u0166\1\31\1\u0168\1\31\1\u016a\1\31\1\uffff\5\31\1\u0171\1"
        u"\31\1\u0173\1\31\1\uffff\2\31\1\uffff\1\u0178\2\uffff\1\31\1\u017a"
        u"\1\uffff\1\u017b\1\uffff\1\31\1\u017d\1\31\1\uffff\1\u017f\2\31"
        u"\3\uffff\1\31\1\uffff\1\u0183\2\31\1\uffff\1\31\4\uffff\1\u0187"
        u"\1\uffff\1\u0188\1\uffff\1\u0189\1\u018a\4\31\1\uffff\1\31\1\uffff"
        u"\3\31\2\uffff\1\u0194\2\uffff\1\31\1\uffff\1\31\1\uffff\1\u0197"
        u"\1\u0198\1\31\1\uffff\1\31\1\u019b\1\31\4\uffff\1\31\1\u019e\3"
        u"\31\1\u01a2\1\31\1\u01a4\2\uffff\1\u01a5\1\u01a6\2\uffff\1\31\1"
        u"\u01a8\1\uffff\2\31\1\uffff\1\u01ab\1\31\1\u01ad\1\uffff\1\31\3"
        u"\uffff\1\u01af\1\uffff\1\u01b0\1\u01b1\1\uffff\1\u01b2\1\uffff"
        u"\1\u01b3\5\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\u01b4\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\11\1\117\1\106\2\101\1\105\1\101\1\116\1\101\1\117\1\116\1\101"
        u"\1\114\2\101\2\105\1\110\1\101\1\121\3\75\1\uffff\1\72\1\uffff"
        u"\1\56\1\60\1\56\1\0\3\uffff\1\55\1\52\14\uffff\1\111\1\120\1\116"
        u"\2\60\1\124\1\116\1\114\1\107\1\106\1\123\1\125\1\124\1\101\1\115"
        u"\1\106\1\60\1\114\1\122\1\101\2\114\1\60\1\110\1\124\1\123\1\102"
        u"\1\107\1\117\1\101\1\103\3\111\1\114\1\104\1\111\1\115\1\114\1"
        u"\60\1\104\1\60\1\117\1\107\1\122\1\117\1\116\1\60\1\124\1\121\1"
        u"\120\1\122\1\125\1\120\1\60\11\uffff\1\60\1\53\6\uffff\1\60\1\0"
        u"\1\47\6\uffff\1\104\1\117\1\60\1\105\1\125\2\uffff\1\125\1\113"
        u"\1\114\1\110\1\111\1\123\1\103\1\124\1\102\1\105\1\104\1\107\1"
        u"\111\1\124\1\60\1\uffff\1\124\1\105\1\124\1\101\1\114\1\123\1\105"
        u"\1\uffff\2\105\1\103\1\105\1\122\1\123\1\122\1\110\1\116\1\117"
        u"\1\116\1\111\1\105\1\122\1\105\2\120\2\60\1\uffff\1\60\1\105\1"
        u"\uffff\1\114\1\60\1\101\1\125\1\105\1\60\1\uffff\2\60\1\114\1\117"
        u"\1\105\1\60\1\103\1\uffff\3\60\1\uffff\1\0\1\60\1\uffff\1\60\1"
        u"\122\1\60\1\uffff\1\122\1\124\1\122\1\60\1\125\1\124\1\116\1\105"
        u"\1\60\1\111\1\114\1\124\2\60\1\124\1\60\1\uffff\1\105\1\101\2\124"
        u"\1\60\1\105\3\122\1\125\1\110\1\60\1\117\1\123\1\101\1\105\1\60"
        u"\1\116\1\107\1\124\1\101\1\105\1\122\1\116\1\125\1\60\1\114\3\uffff"
        u"\1\101\1\105\1\uffff\1\114\1\111\1\120\1\122\3\uffff\1\105\1\125"
        u"\1\60\1\105\1\uffff\1\110\1\60\1\uffff\1\124\1\uffff\2\60\1\116"
        u"\1\uffff\1\120\1\60\1\105\1\60\1\uffff\1\116\1\105\1\111\2\uffff"
        u"\1\60\1\uffff\1\122\1\103\1\105\1\60\1\uffff\2\60\1\127\1\60\1"
        u"\124\1\105\1\uffff\1\125\1\60\1\122\1\60\1\uffff\3\60\1\115\1\60"
        u"\1\122\1\60\1\124\1\uffff\1\105\1\122\1\101\1\114\1\124\1\60\1"
        u"\101\1\60\1\107\1\uffff\1\104\1\105\2\60\2\uffff\1\123\1\60\1\uffff"
        u"\1\60\1\uffff\1\103\1\60\1\115\1\uffff\1\60\1\110\1\116\3\uffff"
        u"\1\111\1\uffff\1\60\1\115\1\120\1\uffff\1\122\4\uffff\1\60\1\uffff"
        u"\1\60\1\uffff\2\60\1\122\1\116\1\105\1\111\1\uffff\1\124\1\uffff"
        u"\1\110\1\125\1\123\1\60\1\uffff\1\60\2\uffff\1\124\1\uffff\1\105"
        u"\1\uffff\2\60\1\123\1\uffff\1\101\1\60\1\101\4\uffff\1\101\1\60"
        u"\1\114\1\117\1\105\1\60\1\103\1\60\1\0\1\uffff\2\60\2\uffff\1\105"
        u"\1\60\1\uffff\2\131\1\uffff\1\60\1\116\1\60\1\uffff\1\105\3\uffff"
        u"\1\60\1\uffff\2\60\1\uffff\1\60\1\uffff\1\60\5\uffff"
        )

    DFA15_max = DFA.unpack(
        u"\1\175\1\117\1\123\2\117\1\124\3\125\1\117\1\123\1\124\1\123\1"
        u"\131\1\101\1\124\1\117\1\125\1\101\1\121\3\75\1\uffff\1\72\1\uffff"
        u"\1\114\2\71\1\uffff\3\uffff\1\55\1\52\14\uffff\1\111\1\120\1\124"
        u"\2\137\1\124\1\116\1\114\1\107\2\123\1\125\1\124\1\116\1\115\1"
        u"\106\1\137\1\114\1\122\1\117\2\114\1\137\1\110\1\124\1\123\1\102"
        u"\1\107\1\117\1\101\1\103\3\111\1\114\1\122\1\111\1\115\1\114\1"
        u"\137\1\104\1\137\1\117\1\107\1\122\1\117\1\116\1\137\1\124\1\121"
        u"\1\120\1\122\1\125\1\124\1\137\11\uffff\2\71\6\uffff\1\106\1\uffff"
        u"\1\162\6\uffff\1\104\1\117\1\137\1\105\1\125\2\uffff\1\125\1\113"
        u"\1\114\1\110\1\111\1\123\1\103\1\124\1\102\1\105\1\104\1\107\1"
        u"\111\1\124\1\137\1\uffff\1\124\1\105\1\124\1\101\1\114\1\123\1"
        u"\105\1\uffff\1\105\1\120\1\103\1\105\1\122\1\123\1\122\1\110\1"
        u"\116\1\117\1\116\1\111\1\105\1\122\1\117\2\120\2\137\1\uffff\1"
        u"\137\1\105\1\uffff\1\114\1\137\1\124\1\125\1\105\1\137\1\uffff"
        u"\2\137\1\114\1\117\1\105\1\137\1\103\1\uffff\1\106\1\71\1\106\1"
        u"\uffff\1\uffff\1\106\1\uffff\1\137\1\122\1\137\1\uffff\1\122\1"
        u"\124\1\122\1\137\1\125\1\124\1\116\1\105\1\137\1\111\1\114\1\124"
        u"\2\137\1\124\1\137\1\uffff\1\105\1\101\2\124\1\137\1\105\3\122"
        u"\1\125\1\110\1\137\1\117\1\123\1\101\1\105\1\137\1\116\1\107\1"
        u"\124\1\101\1\105\1\122\1\116\1\125\1\137\1\114\3\uffff\1\101\1"
        u"\105\1\uffff\1\114\1\111\1\120\1\122\3\uffff\1\105\1\125\1\137"
        u"\1\105\1\uffff\1\110\1\106\1\uffff\1\124\1\uffff\2\137\1\116\1"
        u"\uffff\1\120\1\137\1\105\1\137\1\uffff\1\116\1\105\1\111\2\uffff"
        u"\1\137\1\uffff\1\122\1\103\1\105\1\137\1\uffff\2\137\1\127\1\137"
        u"\1\124\1\105\1\uffff\1\125\1\137\1\122\1\137\1\uffff\3\137\1\115"
        u"\1\137\1\122\1\137\1\124\1\uffff\1\105\1\122\1\101\1\114\1\124"
        u"\1\137\1\101\1\137\1\107\1\uffff\1\104\1\105\1\106\1\137\2\uffff"
        u"\1\123\1\137\1\uffff\1\137\1\uffff\1\103\1\137\1\115\1\uffff\1"
        u"\137\1\110\1\116\3\uffff\1\111\1\uffff\1\137\1\115\1\120\1\uffff"
        u"\1\122\4\uffff\1\137\1\uffff\1\137\1\uffff\2\137\1\122\1\116\1"
        u"\105\1\111\1\uffff\1\124\1\uffff\1\110\1\125\1\123\1\106\1\uffff"
        u"\1\137\2\uffff\1\124\1\uffff\1\105\1\uffff\2\137\1\123\1\uffff"
        u"\1\101\1\137\1\101\4\uffff\1\101\1\137\1\114\1\117\1\105\1\137"
        u"\1\103\1\137\1\uffff\1\uffff\2\137\2\uffff\1\105\1\137\1\uffff"
        u"\2\131\1\uffff\1\137\1\116\1\137\1\uffff\1\105\3\uffff\1\137\1"
        u"\uffff\2\137\1\uffff\1\137\1\uffff\1\137\5\uffff"
        )

    DFA15_accept = DFA.unpack(
        u"\27\uffff\1\121\1\uffff\1\123\4\uffff\1\133\1\134\1\137\2\uffff"
        u"\1\142\1\143\1\144\1\145\1\146\1\147\1\150\1\151\1\153\1\157\1"
        u"\160\1\162\67\uffff\1\114\1\152\1\116\1\115\1\120\1\117\1\122\1"
        u"\135\1\124\2\uffff\1\125\1\130\1\136\1\126\1\155\1\154\3\uffff"
        u"\1\131\1\132\1\140\1\161\1\141\1\156\5\uffff\1\24\1\62\17\uffff"
        u"\1\105\7\uffff\1\41\23\uffff\1\27\2\uffff\1\30\6\uffff\1\104\7"
        u"\uffff\1\103\3\uffff\1\127\2\uffff\1\131\3\uffff\1\50\20\uffff"
        u"\1\107\33\uffff\1\26\1\45\1\40\2\uffff\1\57\4\uffff\1\106\1\42"
        u"\1\110\4\uffff\1\61\2\uffff\1\1\1\uffff\1\23\3\uffff\1\11\4\uffff"
        u"\1\46\3\uffff\1\5\1\51\1\uffff\1\100\4\uffff\1\102\6\uffff\1\13"
        u"\4\uffff\1\17\10\uffff\1\67\11\uffff\1\112\4\uffff\1\32\1\71\2"
        u"\uffff\1\101\1\uffff\1\12\3\uffff\1\76\3\uffff\1\52\1\113\1\10"
        u"\1\uffff\1\33\3\uffff\1\20\1\uffff\1\70\1\21\1\31\1\22\1\uffff"
        u"\1\65\1\uffff\1\74\6\uffff\1\37\1\uffff\1\60\4\uffff\1\2\1\uffff"
        u"\1\14\1\4\1\uffff\1\53\1\uffff\1\6\3\uffff\1\72\3\uffff\1\63\1"
        u"\73\1\75\1\77\11\uffff\1\3\2\uffff\1\7\1\44\2\uffff\1\16\2\uffff"
        u"\1\47\3\uffff\1\64\1\uffff\1\111\1\15\1\54\1\uffff\1\34\2\uffff"
        u"\1\35\1\uffff\1\43\1\uffff\1\25\1\55\1\56\1\36\1\66"
        )

    DFA15_special = DFA.unpack(
        u"\35\uffff\1\0\132\uffff\1\3\120\uffff\1\2\u00c9\uffff\1\1\40\uffff"
        )

            
    DFA15_transition = [
        DFA.unpack(u"\2\40\1\uffff\2\40\22\uffff\1\40\1\27\1\uffff\1\52\1"
        u"\33\1\54\1\uffff\1\35\1\44\1\45\1\37\1\55\1\53\1\41\1\34\1\42\12"
        u"\32\1\30\1\43\1\25\1\24\1\26\1\56\1\uffff\1\14\1\15\1\10\1\4\1"
        u"\23\1\6\1\17\1\31\1\2\1\11\1\31\1\5\1\22\1\20\1\7\1\16\1\31\1\3"
        u"\1\13\1\21\1\12\1\1\4\31\1\50\1\uffff\1\51\2\uffff\1\36\32\uffff"
        u"\1\46\1\uffff\1\47"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\62\6\uffff\1\60\1\61\4\uffff\1\63"),
        DFA.unpack(u"\1\65\3\uffff\1\64\3\uffff\1\67\5\uffff\1\66"),
        DFA.unpack(u"\1\73\3\uffff\1\70\3\uffff\1\71\5\uffff\1\72"),
        DFA.unpack(u"\1\76\3\uffff\1\75\5\uffff\1\74\4\uffff\1\77"),
        DFA.unpack(u"\1\104\7\uffff\1\100\2\uffff\1\102\2\uffff\1\101\5"
        u"\uffff\1\103"),
        DFA.unpack(u"\1\110\3\uffff\1\105\1\uffff\1\106\1\107"),
        DFA.unpack(u"\1\115\6\uffff\1\114\6\uffff\1\112\2\uffff\1\113\2"
        u"\uffff\1\111"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117\4\uffff\1\120"),
        DFA.unpack(u"\1\124\6\uffff\1\123\7\uffff\1\121\3\uffff\1\122"),
        DFA.unpack(u"\1\125\1\uffff\1\127\4\uffff\1\126"),
        DFA.unpack(u"\1\132\15\uffff\1\131\11\uffff\1\130"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\135\14\uffff\1\134\1\uffff\1\136"),
        DFA.unpack(u"\1\140\11\uffff\1\137"),
        DFA.unpack(u"\1\142\11\uffff\1\143\2\uffff\1\141"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\157\1\uffff\12\32\13\uffff\1\160\1\162\5\uffff\1"
        u"\161"),
        DFA.unpack(u"\12\164"),
        DFA.unpack(u"\1\165\1\uffff\12\167"),
        DFA.unpack(u"\12\170\1\173\2\170\1\173\31\170\1\172\64\170\1\171"
        u"\uffa3\170"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0083\1\uffff\1\u0084\3\uffff\1\u0082"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b\7\uffff\1\u008c\4\uffff\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091\14\uffff\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0094"),
        DFA.unpack(u"\13\31\6\uffff\4\31\1\u0095\25\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u0099\15\uffff\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\13\31\6\uffff\3\31\1\u009d\26\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ad\12\uffff\1\u00ac\2\uffff\1\u00ab"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\13\31\6\uffff\2\31\1\u00b1\27\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\13\31\6\uffff\23\31\1\u00b4\6\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\13\31\6\uffff\4\31\1\u00bb\25\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\1\u00c2\3\uffff\1\u00c3"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00c5"),
        DFA.unpack(u"\1\u00c6\1\uffff\1\u00c6\2\uffff\12\u00c7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\167\13\uffff\1\160\1\162"),
        DFA.unpack(u"\12\170\1\173\2\170\1\173\31\170\1\172\64\170\1\171"
        u"\uffa3\170"),
        DFA.unpack(u"\1\u00c9\32\uffff\1\u00c9\3\uffff\1\u00c9\7\uffff\1"
        u"\u00c9\3\uffff\1\u00c9\1\uffff\1\u00c9\1\u00ca\6\uffff\1\u00c9"
        u"\21\uffff\1\173\3\uffff\1\173"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\13\31\6\uffff\16\31\1\u00ce\13\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\1\u00d5"),
        DFA.unpack(u"\1\u00d6"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u"\1\u00d9"),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd"),
        DFA.unpack(u"\1\u00de"),
        DFA.unpack(u"\1\u00df"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\u00e2"),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u"\1\u00e7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u"\1\u00e9\12\uffff\1\u00ea"),
        DFA.unpack(u"\1\u00eb"),
        DFA.unpack(u"\1\u00ec"),
        DFA.unpack(u"\1\u00ed"),
        DFA.unpack(u"\1\u00ee"),
        DFA.unpack(u"\1\u00ef"),
        DFA.unpack(u"\1\u00f0"),
        DFA.unpack(u"\1\u00f1"),
        DFA.unpack(u"\1\u00f2"),
        DFA.unpack(u"\1\u00f3"),
        DFA.unpack(u"\1\u00f4"),
        DFA.unpack(u"\1\u00f5"),
        DFA.unpack(u"\1\u00f6"),
        DFA.unpack(u"\1\u00f7\3\uffff\1\u00f8\5\uffff\1\u00f9"),
        DFA.unpack(u"\1\u00fa"),
        DFA.unpack(u"\1\u00fb"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u00ff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0102\22\uffff\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\1\u0105"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0109"),
        DFA.unpack(u"\1\u010a"),
        DFA.unpack(u"\1\u010b"),
        DFA.unpack(u"\13\31\6\uffff\21\31\1\u010c\10\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u010e"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u00c5\13\uffff\1\160\1\162"),
        DFA.unpack(u"\12\u00c7"),
        DFA.unpack(u"\12\u00c7\14\uffff\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\170\1\173\2\170\1\173\31\170\1\172\64\170\1\171"
        u"\uffa3\170"),
        DFA.unpack(u"\12\u010f\7\uffff\6\u010f"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0111"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0113"),
        DFA.unpack(u"\1\u0114"),
        DFA.unpack(u"\1\u0115"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0117"),
        DFA.unpack(u"\1\u0118"),
        DFA.unpack(u"\1\u0119"),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u011c"),
        DFA.unpack(u"\1\u011d"),
        DFA.unpack(u"\1\u011e"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0121"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0123"),
        DFA.unpack(u"\1\u0124"),
        DFA.unpack(u"\1\u0125"),
        DFA.unpack(u"\1\u0126"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0128"),
        DFA.unpack(u"\1\u0129"),
        DFA.unpack(u"\1\u012a"),
        DFA.unpack(u"\1\u012b"),
        DFA.unpack(u"\1\u012c"),
        DFA.unpack(u"\1\u012d"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u012f"),
        DFA.unpack(u"\1\u0130"),
        DFA.unpack(u"\1\u0131"),
        DFA.unpack(u"\1\u0132"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0134"),
        DFA.unpack(u"\1\u0135"),
        DFA.unpack(u"\1\u0136"),
        DFA.unpack(u"\1\u0137"),
        DFA.unpack(u"\1\u0138"),
        DFA.unpack(u"\1\u0139"),
        DFA.unpack(u"\1\u013a"),
        DFA.unpack(u"\1\u013b"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u013d"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u013e"),
        DFA.unpack(u"\1\u013f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0140"),
        DFA.unpack(u"\1\u0141"),
        DFA.unpack(u"\1\u0142"),
        DFA.unpack(u"\1\u0143"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0144"),
        DFA.unpack(u"\1\u0145"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0147"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0148"),
        DFA.unpack(u"\12\u0149\7\uffff\6\u0149"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u014a"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u014d"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u014e"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0150"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0152"),
        DFA.unpack(u"\1\u0153"),
        DFA.unpack(u"\1\u0154"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0156"),
        DFA.unpack(u"\1\u0157"),
        DFA.unpack(u"\1\u0158"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u015c"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u015e"),
        DFA.unpack(u"\1\u015f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0160"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0162"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0167"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0169"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u016b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u016c"),
        DFA.unpack(u"\1\u016d"),
        DFA.unpack(u"\1\u016e"),
        DFA.unpack(u"\1\u016f"),
        DFA.unpack(u"\1\u0170"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0172"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0174"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0175"),
        DFA.unpack(u"\1\u0176"),
        DFA.unpack(u"\12\u0177\7\uffff\6\u0177"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0179"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u017c"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u017e"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0180"),
        DFA.unpack(u"\1\u0181"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0182"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0184"),
        DFA.unpack(u"\1\u0185"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0186"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u018b"),
        DFA.unpack(u"\1\u018c"),
        DFA.unpack(u"\1\u018d"),
        DFA.unpack(u"\1\u018e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u018f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0190"),
        DFA.unpack(u"\1\u0191"),
        DFA.unpack(u"\1\u0192"),
        DFA.unpack(u"\12\u0193\7\uffff\6\u0193"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0195"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0196"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u0199"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u019a"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u019c"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u019d"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u019f"),
        DFA.unpack(u"\1\u01a0"),
        DFA.unpack(u"\1\u01a1"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u01a3"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\12\170\1\173\2\170\1\173\31\170\1\172\64\170\1\171"
        u"\uffa3\170"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a7"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a9"),
        DFA.unpack(u"\1\u01aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\1\u01ac"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01ae"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u"\13\31\6\uffff\32\31\4\uffff\1\31"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA15_29 = input.LA(1)

                s = -1
                if ((0 <= LA15_29 <= 9) or (11 <= LA15_29 <= 12) or (14 <= LA15_29 <= 38) or (40 <= LA15_29 <= 91) or (93 <= LA15_29 <= 65535)):
                    s = 120

                elif (LA15_29 == 92):
                    s = 121

                elif (LA15_29 == 39):
                    s = 122

                elif (LA15_29 == 10 or LA15_29 == 13):
                    s = 123

                if s >= 0:
                    return s
            elif s == 1: 
                LA15_403 = input.LA(1)

                s = -1
                if (LA15_403 == 39):
                    s = 122

                elif ((0 <= LA15_403 <= 9) or (11 <= LA15_403 <= 12) or (14 <= LA15_403 <= 38) or (40 <= LA15_403 <= 91) or (93 <= LA15_403 <= 65535)):
                    s = 120

                elif (LA15_403 == 92):
                    s = 121

                elif (LA15_403 == 10 or LA15_403 == 13):
                    s = 123

                if s >= 0:
                    return s
            elif s == 2: 
                LA15_201 = input.LA(1)

                s = -1
                if (LA15_201 == 39):
                    s = 122

                elif ((0 <= LA15_201 <= 9) or (11 <= LA15_201 <= 12) or (14 <= LA15_201 <= 38) or (40 <= LA15_201 <= 91) or (93 <= LA15_201 <= 65535)):
                    s = 120

                elif (LA15_201 == 92):
                    s = 121

                elif (LA15_201 == 10 or LA15_201 == 13):
                    s = 123

                if s >= 0:
                    return s
            elif s == 3: 
                LA15_120 = input.LA(1)

                s = -1
                if (LA15_120 == 39):
                    s = 122

                elif ((0 <= LA15_120 <= 9) or (11 <= LA15_120 <= 12) or (14 <= LA15_120 <= 38) or (40 <= LA15_120 <= 91) or (93 <= LA15_120 <= 65535)):
                    s = 120

                elif (LA15_120 == 92):
                    s = 121

                elif (LA15_120 == 10 or LA15_120 == 13):
                    s = 123

                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 15, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(QueryLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
