# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 QueryParser.g 2012-09-15 21:46:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *

         
package org.apache.pig.parser;

import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.pig.parser.PigMacro;



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPR_IN_PAREN=147
STAR=104
BAG_TYPE_CAST=150
LETTER=86
TUPLE_TYPE=144
FUNC_EVAL=127
NOT=37
TOBAG=159
DOUBLENUMBER=99
EOF=-1
CACHE=59
NESTED_CMD=138
STDOUT=64
STR_OP_NE=75
STATEMENT=124
COL_RANGE=129
TUPLE=51
IMPORT=5
DCOLON=89
FULL=69
CAST_EXPR=128
USING=28
MACRO_BODY=154
RIGHT_BRACKET=115
DOUBLE=46
STR_OP_EQ=70
VOID=4
GENERATE=38
TUPLE_TYPE_CAST=149
JOIN_ITEM=148
STREAM=54
INTO=22
MAP_VAL=132
STR_OP_LTE=74
STORE=56
OTHERWISE=24
QUOTEDSTRING=101
ASC=40
POUND=116
TOTUPLE=161
PERIOD=92
ROLLUP=15
NULL=156
BOOL=162
STDIN=63
LOAD=8
BAG_TYPE=145
INT=43
SEMI_COLON=109
BYTEARRAY=49
NUM_OP_GTE=83
NESTED_PROJ=139
REALIAS=163
GROUP=34
WS=106
SPECIALCHAR=87
CUBE=14
FUNC=125
LEFT_CURLY=112
FLOATINGPOINT=93
SL_COMMENT=107
OR=36
CHARARRAY=48
FILTER=9
FLOATNUMBER=100
LEFT_PAREN=110
QUERY=123
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
BAG_VAL=133
FLOAT=45
MACRO_DEF=153
STR_OP_MATCHES=76
NESTED_CMD_ASSI=137
AND=35
ID=88
DEFINE=7
CROSS=19
SPLIT_BRANCH=140
IF=23
ML_COMMENT=108
AS=26
RIGHT_PAREN=111
RANK=12
SAMPLE=66
TUPLE_VAL=131
BOOLEAN=42
TOMAP=160
COMMA=118
PARTITION=33
IS=53
IDENTIFIER=157
LEFT=67
EQUAL=117
ALL=25
DENSE=13
PLUS=98
DIGIT=85
IDENTIFIER_L=90
NUM_OP_GT=82
STDERROR=62
RETURNS=6
PARAMS=151
INTEGER=91
NUM_OP_NE=84
OUTER=30
BY=27
PERCENT=121
DOUBLE_PERIOD=119
DATETIME=47
MAP_TYPE=143
RIGHT=68
LONGINTEGER=94
FIELD_DEF_WITHOUT_IDENTIFIER=136
MINUS=97
DOLLARVAR=96
TRUE=77
STR_OP_LT=72
JOIN=18
UNION=20
COLON=105
FOREACH_PLAN_SIMPLE=141
ANY=158
FUNC_REF=126
BAG=50
FIELD_DEF=135
FLATTEN=39
EXECCOMMAND=103
NEG=146
MAP=52
THROUGH=55
NUM_OP_LT=80
MACRO_INLINE=155
MAPREDUCE=57
SHIP=58
RETURN_VAL=152
DESC=41
DIV=120
BIN_EXPR=130
LONG=44
FOREACH_PLAN_COMPLEX=142
NUM_OP_EQ=79
KEY_VAL_PAIR=134

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "VOID", "IMPORT", "RETURNS", "DEFINE", "LOAD", "FILTER", "FOREACH", 
    "ORDER", "RANK", "DENSE", "CUBE", "ROLLUP", "DISTINCT", "COGROUP", "JOIN", 
    "CROSS", "UNION", "SPLIT", "INTO", "IF", "OTHERWISE", "ALL", "AS", "BY", 
    "USING", "INNER", "OUTER", "ONSCHEMA", "PARALLEL", "PARTITION", "GROUP", 
    "AND", "OR", "NOT", "GENERATE", "FLATTEN", "ASC", "DESC", "BOOLEAN", 
    "INT", "LONG", "FLOAT", "DOUBLE", "DATETIME", "CHARARRAY", "BYTEARRAY", 
    "BAG", "TUPLE", "MAP", "IS", "STREAM", "THROUGH", "STORE", "MAPREDUCE", 
    "SHIP", "CACHE", "INPUT", "OUTPUT", "STDERROR", "STDIN", "STDOUT", "LIMIT", 
    "SAMPLE", "LEFT", "RIGHT", "FULL", "STR_OP_EQ", "STR_OP_GT", "STR_OP_LT", 
    "STR_OP_GTE", "STR_OP_LTE", "STR_OP_NE", "STR_OP_MATCHES", "TRUE", "FALSE", 
    "NUM_OP_EQ", "NUM_OP_LT", "NUM_OP_LTE", "NUM_OP_GT", "NUM_OP_GTE", "NUM_OP_NE", 
    "DIGIT", "LETTER", "SPECIALCHAR", "ID", "DCOLON", "IDENTIFIER_L", "INTEGER", 
    "PERIOD", "FLOATINGPOINT", "LONGINTEGER", "DOLLAR", "DOLLARVAR", "MINUS", 
    "PLUS", "DOUBLENUMBER", "FLOATNUMBER", "QUOTEDSTRING", "MULTILINE_QUOTEDSTRING", 
    "EXECCOMMAND", "STAR", "COLON", "WS", "SL_COMMENT", "ML_COMMENT", "SEMI_COLON", 
    "LEFT_PAREN", "RIGHT_PAREN", "LEFT_CURLY", "RIGHT_CURLY", "LEFT_BRACKET", 
    "RIGHT_BRACKET", "POUND", "EQUAL", "COMMA", "DOUBLE_PERIOD", "DIV", 
    "PERCENT", "QMARK", "QUERY", "STATEMENT", "FUNC", "FUNC_REF", "FUNC_EVAL", 
    "CAST_EXPR", "COL_RANGE", "BIN_EXPR", "TUPLE_VAL", "MAP_VAL", "BAG_VAL", 
    "KEY_VAL_PAIR", "FIELD_DEF", "FIELD_DEF_WITHOUT_IDENTIFIER", "NESTED_CMD_ASSI", 
    "NESTED_CMD", "NESTED_PROJ", "SPLIT_BRANCH", "FOREACH_PLAN_SIMPLE", 
    "FOREACH_PLAN_COMPLEX", "MAP_TYPE", "TUPLE_TYPE", "BAG_TYPE", "NEG", 
    "EXPR_IN_PAREN", "JOIN_ITEM", "TUPLE_TYPE_CAST", "BAG_TYPE_CAST", "PARAMS", 
    "RETURN_VAL", "MACRO_DEF", "MACRO_BODY", "MACRO_INLINE", "NULL", "IDENTIFIER", 
    "ANY", "TOBAG", "TOMAP", "TOTUPLE", "BOOL", "REALIAS"
]




class QueryParser(Parser):
    grammarFileName = "QueryParser.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(QueryParser, self).__init__(input, state, *args, **kwargs)

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

        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
            )

        self.dfa51 = self.DFA51(
            self, 51,
            eot = self.DFA51_eot,
            eof = self.DFA51_eof,
            min = self.DFA51_min,
            max = self.DFA51_max,
            accept = self.DFA51_accept,
            special = self.DFA51_special,
            transition = self.DFA51_transition
            )

        self.dfa61 = self.DFA61(
            self, 61,
            eot = self.DFA61_eot,
            eof = self.DFA61_eof,
            min = self.DFA61_min,
            max = self.DFA61_max,
            accept = self.DFA61_accept,
            special = self.DFA61_special,
            transition = self.DFA61_transition
            )

        self.dfa70 = self.DFA70(
            self, 70,
            eot = self.DFA70_eot,
            eof = self.DFA70_eof,
            min = self.DFA70_min,
            max = self.DFA70_max,
            accept = self.DFA70_accept,
            special = self.DFA70_special,
            transition = self.DFA70_transition
            )

        self.dfa63 = self.DFA63(
            self, 63,
            eot = self.DFA63_eot,
            eof = self.DFA63_eof,
            min = self.DFA63_min,
            max = self.DFA63_max,
            accept = self.DFA63_accept,
            special = self.DFA63_special,
            transition = self.DFA63_transition
            )

        self.dfa65 = self.DFA65(
            self, 65,
            eot = self.DFA65_eot,
            eof = self.DFA65_eof,
            min = self.DFA65_min,
            max = self.DFA65_max,
            accept = self.DFA65_accept,
            special = self.DFA65_special,
            transition = self.DFA65_transition
            )

        self.dfa68 = self.DFA68(
            self, 68,
            eot = self.DFA68_eot,
            eof = self.DFA68_eof,
            min = self.DFA68_min,
            max = self.DFA68_max,
            accept = self.DFA68_accept,
            special = self.DFA68_special,
            transition = self.DFA68_transition
            )

        self.dfa74 = self.DFA74(
            self, 74,
            eot = self.DFA74_eot,
            eof = self.DFA74_eof,
            min = self.DFA74_min,
            max = self.DFA74_max,
            accept = self.DFA74_accept,
            special = self.DFA74_special,
            transition = self.DFA74_transition
            )

        self.dfa81 = self.DFA81(
            self, 81,
            eot = self.DFA81_eot,
            eof = self.DFA81_eof,
            min = self.DFA81_min,
            max = self.DFA81_max,
            accept = self.DFA81_accept,
            special = self.DFA81_special,
            transition = self.DFA81_transition
            )

        self.dfa86 = self.DFA86(
            self, 86,
            eot = self.DFA86_eot,
            eof = self.DFA86_eof,
            min = self.DFA86_min,
            max = self.DFA86_max,
            accept = self.DFA86_accept,
            special = self.DFA86_special,
            transition = self.DFA86_transition
            )

        self.dfa87 = self.DFA87(
            self, 87,
            eot = self.DFA87_eot,
            eof = self.DFA87_eof,
            min = self.DFA87_min,
            max = self.DFA87_max,
            accept = self.DFA87_accept,
            special = self.DFA87_special,
            transition = self.DFA87_transition
            )

        self.dfa89 = self.DFA89(
            self, 89,
            eot = self.DFA89_eot,
            eof = self.DFA89_eof,
            min = self.DFA89_min,
            max = self.DFA89_max,
            accept = self.DFA89_accept,
            special = self.DFA89_special,
            transition = self.DFA89_transition
            )

        self.dfa126 = self.DFA126(
            self, 126,
            eot = self.DFA126_eot,
            eof = self.DFA126_eof,
            min = self.DFA126_min,
            max = self.DFA126_max,
            accept = self.DFA126_accept,
            special = self.DFA126_special,
            transition = self.DFA126_transition
            )

        self.dfa135 = self.DFA135(
            self, 135,
            eot = self.DFA135_eot,
            eof = self.DFA135_eof,
            min = self.DFA135_min,
            max = self.DFA135_max,
            accept = self.DFA135_accept,
            special = self.DFA135_special,
            transition = self.DFA135_transition
            )

        self.dfa161 = self.DFA161(
            self, 161,
            eot = self.DFA161_eot,
            eof = self.DFA161_eof,
            min = self.DFA161_min,
            max = self.DFA161_max,
            accept = self.DFA161_accept,
            special = self.DFA161_special,
            transition = self.DFA161_transition
            )

        self.dfa176 = self.DFA176(
            self, 176,
            eot = self.DFA176_eot,
            eof = self.DFA176_eof,
            min = self.DFA176_min,
            max = self.DFA176_max,
            accept = self.DFA176_accept,
            special = self.DFA176_special,
            transition = self.DFA176_transition
            )

        self.dfa179 = self.DFA179(
            self, 179,
            eot = self.DFA179_eot,
            eof = self.DFA179_eof,
            min = self.DFA179_min,
            max = self.DFA179_max,
            accept = self.DFA179_accept,
            special = self.DFA179_special,
            transition = self.DFA179_transition
            )






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

              
    private static Log log = LogFactory.getLog( QueryParser.class );

    private Set<String> memory = new HashSet<String>();

    @Override
    protected Object recoverFromMismatchedToken(IntStream input, int ttype, BitSet follow) 
    throws RecognitionException {
        throw new MismatchedTokenException( ttype, input );
    }

    @Override
    public Object recoverFromMismatchedSet(IntStream input, RecognitionException e, BitSet follow)
    throws RecognitionException {
        throw e;
    }

    @Override
    public String getErrorMessage(RecognitionException e, String[] tokenNames ) {
        if( !log.isDebugEnabled() ) {
            if( e instanceof NoViableAltException ) {
                return "Syntax error, unexpected symbol at or near " + getTokenErrorDisplay( e.token );
            } else {
                return super.getErrorMessage( e, tokenNames );
            }
        }
        
        List stack =  getRuleInvocationStack( e, this.getClass().getName() );
        String msg = null;
        if( e instanceof NoViableAltException ) {
            NoViableAltException nvae = (NoViableAltException)e;
            msg = " no viable alt; token = " + e.token + " (decision=" + nvae.decisionNumber + " state " + nvae.stateNumber + ")" +
                " decision=<<" + nvae.grammarDecisionDescription + ">>";
        } else {
            msg =  super.getErrorMessage( e, tokenNames );
        }
        return stack + " " + msg;
    }

    @Override
    public String getTokenErrorDisplay(Token t) {
        return "'" + t.getText() + "'";
    }

    @Override
    public String getErrorHeader(RecognitionException ex) {
    	return QueryParserUtils.generateErrorHeader( ex, this.getSourceName() );
    }



    class query_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.query_return, self).__init__()

            self.tree = None




    # $ANTLR start "query"
    # QueryParser.g:149:1: query : ( statement )* EOF -> ^( QUERY ( statement )* ) ;
    def query(self, ):

        retval = self.query_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        statement1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # QueryParser.g:149:7: ( ( statement )* EOF -> ^( QUERY ( statement )* ) )
                # QueryParser.g:149:9: ( statement )* EOF
                pass 
                # QueryParser.g:149:9: ( statement )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IMPORT or (DEFINE <= LA1_0 <= RANK) or LA1_0 == CUBE or (DISTINCT <= LA1_0 <= SPLIT) or LA1_0 == GROUP or LA1_0 == STREAM or (STORE <= LA1_0 <= MAPREDUCE) or (LIMIT <= LA1_0 <= SAMPLE) or LA1_0 == IDENTIFIER_L or (SEMI_COLON <= LA1_0 <= LEFT_PAREN)) :
                        alt1 = 1


                    if alt1 == 1:
                        # QueryParser.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_query372)
                        statement1 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement1.tree)


                    else:
                        break #loop1
                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_query375) 
                if self._state.backtracking == 0:
                    stream_EOF.add(EOF2)

                # AST Rewrite
                # elements: statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 150:6: -> ^( QUERY ( statement )* )
                    # QueryParser.g:150:9: ^( QUERY ( statement )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(QUERY, "QUERY"), root_1)

                    # QueryParser.g:150:18: ( statement )*
                    while stream_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_statement.nextTree())


                    stream_statement.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "query"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # QueryParser.g:153:1: statement : ( SEMI_COLON | general_statement | foreach_statement | split_statement | inline_statement | import_statement | realias_statement );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON3 = None
        general_statement4 = None

        foreach_statement5 = None

        split_statement6 = None

        inline_statement7 = None

        import_statement8 = None

        realias_statement9 = None


        SEMI_COLON3_tree = None

        try:
            try:
                # QueryParser.g:153:11: ( SEMI_COLON | general_statement | foreach_statement | split_statement | inline_statement | import_statement | realias_statement )
                alt2 = 7
                alt2 = self.dfa2.predict(self.input)
                if alt2 == 1:
                    # QueryParser.g:153:13: SEMI_COLON
                    pass 
                    root_0 = self._adaptor.nil()

                    SEMI_COLON3=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_statement400)


                elif alt2 == 2:
                    # QueryParser.g:154:13: general_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_general_statement_in_statement415)
                    general_statement4 = self.general_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, general_statement4.tree)


                elif alt2 == 3:
                    # QueryParser.g:155:13: foreach_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_foreach_statement_in_statement429)
                    foreach_statement5 = self.foreach_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, foreach_statement5.tree)


                elif alt2 == 4:
                    # QueryParser.g:156:13: split_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_split_statement_in_statement443)
                    split_statement6 = self.split_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, split_statement6.tree)


                elif alt2 == 5:
                    # QueryParser.g:157:13: inline_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_inline_statement_in_statement459)
                    inline_statement7 = self.inline_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, inline_statement7.tree)


                elif alt2 == 6:
                    # QueryParser.g:158:13: import_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_import_statement_in_statement481)
                    import_statement8 = self.import_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, import_statement8.tree)


                elif alt2 == 7:
                    # QueryParser.g:159:13: realias_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_realias_statement_in_statement495)
                    realias_statement9 = self.realias_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, realias_statement9.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "statement"

    class import_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.import_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "import_statement"
    # QueryParser.g:162:1: import_statement : import_clause SEMI_COLON ;
    def import_statement(self, ):

        retval = self.import_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON11 = None
        import_clause10 = None


        SEMI_COLON11_tree = None

        try:
            try:
                # QueryParser.g:162:18: ( import_clause SEMI_COLON )
                # QueryParser.g:162:20: import_clause SEMI_COLON
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_import_clause_in_import_statement504)
                import_clause10 = self.import_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, import_clause10.tree)
                SEMI_COLON11=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_import_statement506)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "import_statement"

    class inline_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.inline_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "inline_statement"
    # QueryParser.g:165:1: inline_statement : inline_clause SEMI_COLON ;
    def inline_statement(self, ):

        retval = self.inline_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON13 = None
        inline_clause12 = None


        SEMI_COLON13_tree = None

        try:
            try:
                # QueryParser.g:165:18: ( inline_clause SEMI_COLON )
                # QueryParser.g:165:20: inline_clause SEMI_COLON
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_inline_clause_in_inline_statement516)
                inline_clause12 = self.inline_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, inline_clause12.tree)
                SEMI_COLON13=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_inline_statement518)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "inline_statement"

    class split_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.split_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "split_statement"
    # QueryParser.g:168:1: split_statement : split_clause SEMI_COLON ;
    def split_statement(self, ):

        retval = self.split_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON15 = None
        split_clause14 = None


        SEMI_COLON15_tree = None

        try:
            try:
                # QueryParser.g:168:17: ( split_clause SEMI_COLON )
                # QueryParser.g:168:19: split_clause SEMI_COLON
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_split_clause_in_split_statement528)
                split_clause14 = self.split_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, split_clause14.tree)
                SEMI_COLON15=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_split_statement530)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "split_statement"

    class general_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.general_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "general_statement"
    # QueryParser.g:171:1: general_statement : ( alias EQUAL )? ( op_clause ( parallel_clause )? | LEFT_PAREN op_clause ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON -> ^( STATEMENT ( alias )? op_clause ( parallel_clause )? ) ;
    def general_statement(self, ):

        retval = self.general_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL17 = None
        LEFT_PAREN20 = None
        RIGHT_PAREN23 = None
        SEMI_COLON24 = None
        alias16 = None

        op_clause18 = None

        parallel_clause19 = None

        op_clause21 = None

        parallel_clause22 = None


        EQUAL17_tree = None
        LEFT_PAREN20_tree = None
        RIGHT_PAREN23_tree = None
        SEMI_COLON24_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_SEMI_COLON = RewriteRuleTokenStream(self._adaptor, "token SEMI_COLON")
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_parallel_clause = RewriteRuleSubtreeStream(self._adaptor, "rule parallel_clause")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_op_clause = RewriteRuleSubtreeStream(self._adaptor, "rule op_clause")
        try:
            try:
                # QueryParser.g:171:19: ( ( alias EQUAL )? ( op_clause ( parallel_clause )? | LEFT_PAREN op_clause ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON -> ^( STATEMENT ( alias )? op_clause ( parallel_clause )? ) )
                # QueryParser.g:171:21: ( alias EQUAL )? ( op_clause ( parallel_clause )? | LEFT_PAREN op_clause ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON
                pass 
                # QueryParser.g:171:21: ( alias EQUAL )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER_L) :
                    alt3 = 1
                if alt3 == 1:
                    # QueryParser.g:171:23: alias EQUAL
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_general_statement542)
                    alias16 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias16.tree)
                    EQUAL17=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_general_statement544) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL17)



                # QueryParser.g:171:38: ( op_clause ( parallel_clause )? | LEFT_PAREN op_clause ( parallel_clause )? RIGHT_PAREN )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((DEFINE <= LA6_0 <= FILTER) or (ORDER <= LA6_0 <= RANK) or LA6_0 == CUBE or (DISTINCT <= LA6_0 <= UNION) or LA6_0 == GROUP or LA6_0 == STREAM or (STORE <= LA6_0 <= MAPREDUCE) or (LIMIT <= LA6_0 <= SAMPLE)) :
                    alt6 = 1
                elif (LA6_0 == LEFT_PAREN) :
                    alt6 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # QueryParser.g:171:39: op_clause ( parallel_clause )?
                    pass 
                    self._state.following.append(self.FOLLOW_op_clause_in_general_statement550)
                    op_clause18 = self.op_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_op_clause.add(op_clause18.tree)
                    # QueryParser.g:171:49: ( parallel_clause )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == PARALLEL) :
                        alt4 = 1
                    if alt4 == 1:
                        # QueryParser.g:0:0: parallel_clause
                        pass 
                        self._state.following.append(self.FOLLOW_parallel_clause_in_general_statement552)
                        parallel_clause19 = self.parallel_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parallel_clause.add(parallel_clause19.tree)





                elif alt6 == 2:
                    # QueryParser.g:171:68: LEFT_PAREN op_clause ( parallel_clause )? RIGHT_PAREN
                    pass 
                    LEFT_PAREN20=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_general_statement557) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN20)
                    self._state.following.append(self.FOLLOW_op_clause_in_general_statement559)
                    op_clause21 = self.op_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_op_clause.add(op_clause21.tree)
                    # QueryParser.g:171:89: ( parallel_clause )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == PARALLEL) :
                        alt5 = 1
                    if alt5 == 1:
                        # QueryParser.g:0:0: parallel_clause
                        pass 
                        self._state.following.append(self.FOLLOW_parallel_clause_in_general_statement561)
                        parallel_clause22 = self.parallel_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parallel_clause.add(parallel_clause22.tree)



                    RIGHT_PAREN23=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_general_statement564) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN23)



                SEMI_COLON24=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_general_statement567) 
                if self._state.backtracking == 0:
                    stream_SEMI_COLON.add(SEMI_COLON24)

                # AST Rewrite
                # elements: parallel_clause, op_clause, alias
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 172:18: -> ^( STATEMENT ( alias )? op_clause ( parallel_clause )? )
                    # QueryParser.g:172:21: ^( STATEMENT ( alias )? op_clause ( parallel_clause )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENT, "STATEMENT"), root_1)

                    # QueryParser.g:172:34: ( alias )?
                    if stream_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_alias.nextTree())


                    stream_alias.reset();
                    self._adaptor.addChild(root_1, stream_op_clause.nextTree())
                    # QueryParser.g:172:51: ( parallel_clause )?
                    if stream_parallel_clause.hasNext():
                        self._adaptor.addChild(root_1, stream_parallel_clause.nextTree())


                    stream_parallel_clause.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "general_statement"

    class realias_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.realias_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "realias_statement"
    # QueryParser.g:175:1: realias_statement : realias_clause SEMI_COLON ;
    def realias_statement(self, ):

        retval = self.realias_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON26 = None
        realias_clause25 = None


        SEMI_COLON26_tree = None

        try:
            try:
                # QueryParser.g:175:19: ( realias_clause SEMI_COLON )
                # QueryParser.g:175:21: realias_clause SEMI_COLON
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_realias_clause_in_realias_statement610)
                realias_clause25 = self.realias_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, realias_clause25.tree)
                SEMI_COLON26=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_realias_statement612)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "realias_statement"

    class realias_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.realias_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "realias_clause"
    # QueryParser.g:178:1: realias_clause : alias EQUAL identifier -> ^( REALIAS alias identifier ) ;
    def realias_clause(self, ):

        retval = self.realias_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL28 = None
        alias27 = None

        identifier29 = None


        EQUAL28_tree = None
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # QueryParser.g:178:16: ( alias EQUAL identifier -> ^( REALIAS alias identifier ) )
                # QueryParser.g:178:18: alias EQUAL identifier
                pass 
                self._state.following.append(self.FOLLOW_alias_in_realias_clause622)
                alias27 = self.alias()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_alias.add(alias27.tree)
                EQUAL28=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_realias_clause624) 
                if self._state.backtracking == 0:
                    stream_EQUAL.add(EQUAL28)
                self._state.following.append(self.FOLLOW_identifier_in_realias_clause626)
                identifier29 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_identifier.add(identifier29.tree)

                # AST Rewrite
                # elements: alias, identifier
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 179:5: -> ^( REALIAS alias identifier )
                    # QueryParser.g:179:8: ^( REALIAS alias identifier )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(REALIAS, "REALIAS"), root_1)

                    self._adaptor.addChild(root_1, stream_alias.nextTree())
                    self._adaptor.addChild(root_1, stream_identifier.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "realias_clause"

    class parallel_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.parallel_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "parallel_clause"
    # QueryParser.g:182:1: parallel_clause : PARALLEL INTEGER ;
    def parallel_clause(self, ):

        retval = self.parallel_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARALLEL30 = None
        INTEGER31 = None

        PARALLEL30_tree = None
        INTEGER31_tree = None

        try:
            try:
                # QueryParser.g:182:17: ( PARALLEL INTEGER )
                # QueryParser.g:182:19: PARALLEL INTEGER
                pass 
                root_0 = self._adaptor.nil()

                PARALLEL30=self.match(self.input, PARALLEL, self.FOLLOW_PARALLEL_in_parallel_clause650)
                if self._state.backtracking == 0:

                    PARALLEL30_tree = self._adaptor.createWithPayload(PARALLEL30)
                    root_0 = self._adaptor.becomeRoot(PARALLEL30_tree, root_0)

                INTEGER31=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_parallel_clause653)
                if self._state.backtracking == 0:

                    INTEGER31_tree = self._adaptor.createWithPayload(INTEGER31)
                    self._adaptor.addChild(root_0, INTEGER31_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "parallel_clause"

    class foreach_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_statement"
    # QueryParser.g:189:1: foreach_statement : ( ( ( alias EQUAL )? FOREACH rel LEFT_CURLY )=> foreach_complex_statement | foreach_simple_statement );
    def foreach_statement(self, ):

        retval = self.foreach_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        foreach_complex_statement32 = None

        foreach_simple_statement33 = None



        try:
            try:
                # QueryParser.g:189:19: ( ( ( alias EQUAL )? FOREACH rel LEFT_CURLY )=> foreach_complex_statement | foreach_simple_statement )
                alt7 = 2
                LA7 = self.input.LA(1)
                if LA7 == IDENTIFIER_L:
                    LA7_1 = self.input.LA(2)

                    if (((self.synpred13_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))) :
                        alt7 = 1
                    elif ((!input.LT(1).getText().equalsIgnoreCase("NULL"))) :
                        alt7 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae

                elif LA7 == FOREACH:
                    LA7_2 = self.input.LA(2)

                    if (self.synpred13_QueryParser()) :
                        alt7 = 1
                    elif (True) :
                        alt7 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 7, 2, self.input)

                        raise nvae

                elif LA7 == LEFT_PAREN:
                    alt7 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae

                if alt7 == 1:
                    # QueryParser.g:189:21: ( ( alias EQUAL )? FOREACH rel LEFT_CURLY )=> foreach_complex_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_foreach_complex_statement_in_foreach_statement688)
                    foreach_complex_statement32 = self.foreach_complex_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, foreach_complex_statement32.tree)


                elif alt7 == 2:
                    # QueryParser.g:190:21: foreach_simple_statement
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_foreach_simple_statement_in_foreach_statement710)
                    foreach_simple_statement33 = self.foreach_simple_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, foreach_simple_statement33.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_statement"

    class foreach_complex_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_complex_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_complex_statement"
    # QueryParser.g:193:1: foreach_complex_statement : ( alias EQUAL )? foreach_clause_complex ( SEMI_COLON )? -> ^( STATEMENT ( alias )? foreach_clause_complex ) ;
    def foreach_complex_statement(self, ):

        retval = self.foreach_complex_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL35 = None
        SEMI_COLON37 = None
        alias34 = None

        foreach_clause_complex36 = None


        EQUAL35_tree = None
        SEMI_COLON37_tree = None
        stream_SEMI_COLON = RewriteRuleTokenStream(self._adaptor, "token SEMI_COLON")
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_foreach_clause_complex = RewriteRuleSubtreeStream(self._adaptor, "rule foreach_clause_complex")
        try:
            try:
                # QueryParser.g:193:27: ( ( alias EQUAL )? foreach_clause_complex ( SEMI_COLON )? -> ^( STATEMENT ( alias )? foreach_clause_complex ) )
                # QueryParser.g:193:29: ( alias EQUAL )? foreach_clause_complex ( SEMI_COLON )?
                pass 
                # QueryParser.g:193:29: ( alias EQUAL )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == IDENTIFIER_L) :
                    alt8 = 1
                if alt8 == 1:
                    # QueryParser.g:193:31: alias EQUAL
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_foreach_complex_statement721)
                    alias34 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias34.tree)
                    EQUAL35=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_foreach_complex_statement723) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL35)



                self._state.following.append(self.FOLLOW_foreach_clause_complex_in_foreach_complex_statement728)
                foreach_clause_complex36 = self.foreach_clause_complex()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_foreach_clause_complex.add(foreach_clause_complex36.tree)
                # QueryParser.g:193:69: ( SEMI_COLON )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == SEMI_COLON) :
                    LA9_1 = self.input.LA(2)

                    if (self.synpred15_QueryParser()) :
                        alt9 = 1
                if alt9 == 1:
                    # QueryParser.g:0:0: SEMI_COLON
                    pass 
                    SEMI_COLON37=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_foreach_complex_statement730) 
                    if self._state.backtracking == 0:
                        stream_SEMI_COLON.add(SEMI_COLON37)




                # AST Rewrite
                # elements: alias, foreach_clause_complex
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 194:26: -> ^( STATEMENT ( alias )? foreach_clause_complex )
                    # QueryParser.g:194:29: ^( STATEMENT ( alias )? foreach_clause_complex )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENT, "STATEMENT"), root_1)

                    # QueryParser.g:194:42: ( alias )?
                    if stream_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_alias.nextTree())


                    stream_alias.reset();
                    self._adaptor.addChild(root_1, stream_foreach_clause_complex.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_complex_statement"

    class foreach_simple_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_simple_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_simple_statement"
    # QueryParser.g:197:1: foreach_simple_statement : ( alias EQUAL )? ( foreach_clause_simple ( parallel_clause )? | LEFT_PAREN foreach_clause_simple ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON -> ^( STATEMENT ( alias )? foreach_clause_simple ( parallel_clause )? ) ;
    def foreach_simple_statement(self, ):

        retval = self.foreach_simple_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL39 = None
        LEFT_PAREN42 = None
        RIGHT_PAREN45 = None
        SEMI_COLON46 = None
        alias38 = None

        foreach_clause_simple40 = None

        parallel_clause41 = None

        foreach_clause_simple43 = None

        parallel_clause44 = None


        EQUAL39_tree = None
        LEFT_PAREN42_tree = None
        RIGHT_PAREN45_tree = None
        SEMI_COLON46_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_SEMI_COLON = RewriteRuleTokenStream(self._adaptor, "token SEMI_COLON")
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_parallel_clause = RewriteRuleSubtreeStream(self._adaptor, "rule parallel_clause")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_foreach_clause_simple = RewriteRuleSubtreeStream(self._adaptor, "rule foreach_clause_simple")
        try:
            try:
                # QueryParser.g:197:26: ( ( alias EQUAL )? ( foreach_clause_simple ( parallel_clause )? | LEFT_PAREN foreach_clause_simple ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON -> ^( STATEMENT ( alias )? foreach_clause_simple ( parallel_clause )? ) )
                # QueryParser.g:197:28: ( alias EQUAL )? ( foreach_clause_simple ( parallel_clause )? | LEFT_PAREN foreach_clause_simple ( parallel_clause )? RIGHT_PAREN ) SEMI_COLON
                pass 
                # QueryParser.g:197:28: ( alias EQUAL )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == IDENTIFIER_L) :
                    alt10 = 1
                if alt10 == 1:
                    # QueryParser.g:197:30: alias EQUAL
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_foreach_simple_statement780)
                    alias38 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias38.tree)
                    EQUAL39=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_foreach_simple_statement782) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL39)



                # QueryParser.g:197:45: ( foreach_clause_simple ( parallel_clause )? | LEFT_PAREN foreach_clause_simple ( parallel_clause )? RIGHT_PAREN )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == FOREACH) :
                    alt13 = 1
                elif (LA13_0 == LEFT_PAREN) :
                    alt13 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # QueryParser.g:197:46: foreach_clause_simple ( parallel_clause )?
                    pass 
                    self._state.following.append(self.FOLLOW_foreach_clause_simple_in_foreach_simple_statement788)
                    foreach_clause_simple40 = self.foreach_clause_simple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_foreach_clause_simple.add(foreach_clause_simple40.tree)
                    # QueryParser.g:197:68: ( parallel_clause )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == PARALLEL) :
                        alt11 = 1
                    if alt11 == 1:
                        # QueryParser.g:0:0: parallel_clause
                        pass 
                        self._state.following.append(self.FOLLOW_parallel_clause_in_foreach_simple_statement790)
                        parallel_clause41 = self.parallel_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parallel_clause.add(parallel_clause41.tree)





                elif alt13 == 2:
                    # QueryParser.g:198:51: LEFT_PAREN foreach_clause_simple ( parallel_clause )? RIGHT_PAREN
                    pass 
                    LEFT_PAREN42=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_foreach_simple_statement844) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN42)
                    self._state.following.append(self.FOLLOW_foreach_clause_simple_in_foreach_simple_statement846)
                    foreach_clause_simple43 = self.foreach_clause_simple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_foreach_clause_simple.add(foreach_clause_simple43.tree)
                    # QueryParser.g:198:84: ( parallel_clause )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == PARALLEL) :
                        alt12 = 1
                    if alt12 == 1:
                        # QueryParser.g:0:0: parallel_clause
                        pass 
                        self._state.following.append(self.FOLLOW_parallel_clause_in_foreach_simple_statement848)
                        parallel_clause44 = self.parallel_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parallel_clause.add(parallel_clause44.tree)



                    RIGHT_PAREN45=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_foreach_simple_statement851) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN45)



                SEMI_COLON46=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_foreach_simple_statement854) 
                if self._state.backtracking == 0:
                    stream_SEMI_COLON.add(SEMI_COLON46)

                # AST Rewrite
                # elements: alias, parallel_clause, foreach_clause_simple
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 199:25: -> ^( STATEMENT ( alias )? foreach_clause_simple ( parallel_clause )? )
                    # QueryParser.g:199:28: ^( STATEMENT ( alias )? foreach_clause_simple ( parallel_clause )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(STATEMENT, "STATEMENT"), root_1)

                    # QueryParser.g:199:41: ( alias )?
                    if stream_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_alias.nextTree())


                    stream_alias.reset();
                    self._adaptor.addChild(root_1, stream_foreach_clause_simple.nextTree())
                    # QueryParser.g:199:70: ( parallel_clause )?
                    if stream_parallel_clause.hasNext():
                        self._adaptor.addChild(root_1, stream_parallel_clause.nextTree())


                    stream_parallel_clause.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_simple_statement"

    class alias_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.alias_return, self).__init__()

            self.tree = None




    # $ANTLR start "alias"
    # QueryParser.g:202:1: alias : identifier ;
    def alias(self, ):

        retval = self.alias_return()
        retval.start = self.input.LT(1)

        root_0 = None

        identifier47 = None



        try:
            try:
                # QueryParser.g:202:7: ( identifier )
                # QueryParser.g:202:9: identifier
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_identifier_in_alias903)
                identifier47 = self.identifier()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, identifier47.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "alias"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # QueryParser.g:205:1: parameter : ( identifier | INTEGER | DOUBLENUMBER | QUOTEDSTRING | DOLLARVAR );
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INTEGER49 = None
        DOUBLENUMBER50 = None
        QUOTEDSTRING51 = None
        DOLLARVAR52 = None
        identifier48 = None


        INTEGER49_tree = None
        DOUBLENUMBER50_tree = None
        QUOTEDSTRING51_tree = None
        DOLLARVAR52_tree = None

        try:
            try:
                # QueryParser.g:206:5: ( identifier | INTEGER | DOUBLENUMBER | QUOTEDSTRING | DOLLARVAR )
                alt14 = 5
                LA14 = self.input.LA(1)
                if LA14 == IDENTIFIER_L:
                    alt14 = 1
                elif LA14 == INTEGER:
                    alt14 = 2
                elif LA14 == DOUBLENUMBER:
                    alt14 = 3
                elif LA14 == QUOTEDSTRING:
                    alt14 = 4
                elif LA14 == DOLLARVAR:
                    alt14 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # QueryParser.g:206:7: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_parameter917)
                    identifier48 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier48.tree)


                elif alt14 == 2:
                    # QueryParser.g:207:7: INTEGER
                    pass 
                    root_0 = self._adaptor.nil()

                    INTEGER49=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_parameter926)
                    if self._state.backtracking == 0:

                        INTEGER49_tree = self._adaptor.createWithPayload(INTEGER49)
                        self._adaptor.addChild(root_0, INTEGER49_tree)



                elif alt14 == 3:
                    # QueryParser.g:208:7: DOUBLENUMBER
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLENUMBER50=self.match(self.input, DOUBLENUMBER, self.FOLLOW_DOUBLENUMBER_in_parameter935)
                    if self._state.backtracking == 0:

                        DOUBLENUMBER50_tree = self._adaptor.createWithPayload(DOUBLENUMBER50)
                        self._adaptor.addChild(root_0, DOUBLENUMBER50_tree)



                elif alt14 == 4:
                    # QueryParser.g:209:7: QUOTEDSTRING
                    pass 
                    root_0 = self._adaptor.nil()

                    QUOTEDSTRING51=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_parameter943)
                    if self._state.backtracking == 0:

                        QUOTEDSTRING51_tree = self._adaptor.createWithPayload(QUOTEDSTRING51)
                        self._adaptor.addChild(root_0, QUOTEDSTRING51_tree)



                elif alt14 == 5:
                    # QueryParser.g:210:7: DOLLARVAR
                    pass 
                    root_0 = self._adaptor.nil()

                    DOLLARVAR52=self.match(self.input, DOLLARVAR, self.FOLLOW_DOLLARVAR_in_parameter951)
                    if self._state.backtracking == 0:

                        DOLLARVAR52_tree = self._adaptor.createWithPayload(DOLLARVAR52)
                        self._adaptor.addChild(root_0, DOLLARVAR52_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "parameter"

    class content_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.content_return, self).__init__()

            self.tree = None




    # $ANTLR start "content"
    # QueryParser.g:213:1: content : LEFT_CURLY ( content | ~ ( LEFT_CURLY | RIGHT_CURLY ) )* RIGHT_CURLY ;
    def content(self, ):

        retval = self.content_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_CURLY53 = None
        set55 = None
        RIGHT_CURLY56 = None
        content54 = None


        LEFT_CURLY53_tree = None
        set55_tree = None
        RIGHT_CURLY56_tree = None

        try:
            try:
                # QueryParser.g:213:9: ( LEFT_CURLY ( content | ~ ( LEFT_CURLY | RIGHT_CURLY ) )* RIGHT_CURLY )
                # QueryParser.g:213:11: LEFT_CURLY ( content | ~ ( LEFT_CURLY | RIGHT_CURLY ) )* RIGHT_CURLY
                pass 
                root_0 = self._adaptor.nil()

                LEFT_CURLY53=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_content960)
                if self._state.backtracking == 0:

                    LEFT_CURLY53_tree = self._adaptor.createWithPayload(LEFT_CURLY53)
                    self._adaptor.addChild(root_0, LEFT_CURLY53_tree)

                # QueryParser.g:213:22: ( content | ~ ( LEFT_CURLY | RIGHT_CURLY ) )*
                while True: #loop15
                    alt15 = 3
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == LEFT_CURLY) :
                        alt15 = 1
                    elif ((VOID <= LA15_0 <= RIGHT_PAREN) or (LEFT_BRACKET <= LA15_0 <= REALIAS)) :
                        alt15 = 2


                    if alt15 == 1:
                        # QueryParser.g:213:24: content
                        pass 
                        self._state.following.append(self.FOLLOW_content_in_content964)
                        content54 = self.content()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, content54.tree)


                    elif alt15 == 2:
                        # QueryParser.g:213:34: ~ ( LEFT_CURLY | RIGHT_CURLY )
                        pass 
                        set55 = self.input.LT(1)
                        if (VOID <= self.input.LA(1) <= RIGHT_PAREN) or (LEFT_BRACKET <= self.input.LA(1) <= REALIAS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set55))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop15
                RIGHT_CURLY56=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_content980)
                if self._state.backtracking == 0:

                    RIGHT_CURLY56_tree = self._adaptor.createWithPayload(RIGHT_CURLY56)
                    self._adaptor.addChild(root_0, RIGHT_CURLY56_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "content"

    class op_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.op_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "op_clause"
    # QueryParser.g:216:1: op_clause : ( define_clause | load_clause | group_clause | cube_clause | store_clause | filter_clause | distinct_clause | limit_clause | sample_clause | order_clause | rank_clause | cross_clause | join_clause | union_clause | stream_clause | mr_clause );
    def op_clause(self, ):

        retval = self.op_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        define_clause57 = None

        load_clause58 = None

        group_clause59 = None

        cube_clause60 = None

        store_clause61 = None

        filter_clause62 = None

        distinct_clause63 = None

        limit_clause64 = None

        sample_clause65 = None

        order_clause66 = None

        rank_clause67 = None

        cross_clause68 = None

        join_clause69 = None

        union_clause70 = None

        stream_clause71 = None

        mr_clause72 = None



        try:
            try:
                # QueryParser.g:216:11: ( define_clause | load_clause | group_clause | cube_clause | store_clause | filter_clause | distinct_clause | limit_clause | sample_clause | order_clause | rank_clause | cross_clause | join_clause | union_clause | stream_clause | mr_clause )
                alt16 = 16
                LA16 = self.input.LA(1)
                if LA16 == DEFINE:
                    alt16 = 1
                elif LA16 == LOAD:
                    alt16 = 2
                elif LA16 == COGROUP or LA16 == GROUP:
                    alt16 = 3
                elif LA16 == CUBE:
                    alt16 = 4
                elif LA16 == STORE:
                    alt16 = 5
                elif LA16 == FILTER:
                    alt16 = 6
                elif LA16 == DISTINCT:
                    alt16 = 7
                elif LA16 == LIMIT:
                    alt16 = 8
                elif LA16 == SAMPLE:
                    alt16 = 9
                elif LA16 == ORDER:
                    alt16 = 10
                elif LA16 == RANK:
                    alt16 = 11
                elif LA16 == CROSS:
                    alt16 = 12
                elif LA16 == JOIN:
                    alt16 = 13
                elif LA16 == UNION:
                    alt16 = 14
                elif LA16 == STREAM:
                    alt16 = 15
                elif LA16 == MAPREDUCE:
                    alt16 = 16
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # QueryParser.g:216:13: define_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_define_clause_in_op_clause989)
                    define_clause57 = self.define_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, define_clause57.tree)


                elif alt16 == 2:
                    # QueryParser.g:217:13: load_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_load_clause_in_op_clause1004)
                    load_clause58 = self.load_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, load_clause58.tree)


                elif alt16 == 3:
                    # QueryParser.g:218:13: group_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_group_clause_in_op_clause1018)
                    group_clause59 = self.group_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, group_clause59.tree)


                elif alt16 == 4:
                    # QueryParser.g:219:13: cube_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cube_clause_in_op_clause1032)
                    cube_clause60 = self.cube_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cube_clause60.tree)


                elif alt16 == 5:
                    # QueryParser.g:220:13: store_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_store_clause_in_op_clause1046)
                    store_clause61 = self.store_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, store_clause61.tree)


                elif alt16 == 6:
                    # QueryParser.g:221:13: filter_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_filter_clause_in_op_clause1060)
                    filter_clause62 = self.filter_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, filter_clause62.tree)


                elif alt16 == 7:
                    # QueryParser.g:222:13: distinct_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_distinct_clause_in_op_clause1074)
                    distinct_clause63 = self.distinct_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, distinct_clause63.tree)


                elif alt16 == 8:
                    # QueryParser.g:223:13: limit_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_limit_clause_in_op_clause1088)
                    limit_clause64 = self.limit_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, limit_clause64.tree)


                elif alt16 == 9:
                    # QueryParser.g:224:13: sample_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_sample_clause_in_op_clause1102)
                    sample_clause65 = self.sample_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, sample_clause65.tree)


                elif alt16 == 10:
                    # QueryParser.g:225:13: order_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_order_clause_in_op_clause1116)
                    order_clause66 = self.order_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, order_clause66.tree)


                elif alt16 == 11:
                    # QueryParser.g:226:13: rank_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rank_clause_in_op_clause1130)
                    rank_clause67 = self.rank_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rank_clause67.tree)


                elif alt16 == 12:
                    # QueryParser.g:227:13: cross_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_cross_clause_in_op_clause1144)
                    cross_clause68 = self.cross_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cross_clause68.tree)


                elif alt16 == 13:
                    # QueryParser.g:228:13: join_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_join_clause_in_op_clause1158)
                    join_clause69 = self.join_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_clause69.tree)


                elif alt16 == 14:
                    # QueryParser.g:229:13: union_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_union_clause_in_op_clause1172)
                    union_clause70 = self.union_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, union_clause70.tree)


                elif alt16 == 15:
                    # QueryParser.g:230:13: stream_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_stream_clause_in_op_clause1186)
                    stream_clause71 = self.stream_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, stream_clause71.tree)


                elif alt16 == 16:
                    # QueryParser.g:231:13: mr_clause
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_mr_clause_in_op_clause1200)
                    mr_clause72 = self.mr_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, mr_clause72.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "op_clause"

    class macro_param_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.macro_param_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "macro_param_clause"
    # QueryParser.g:234:1: macro_param_clause : LEFT_PAREN ( alias ( COMMA alias )* )? RIGHT_PAREN -> ^( PARAMS ( alias )* ) ;
    def macro_param_clause(self, ):

        retval = self.macro_param_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN73 = None
        COMMA75 = None
        RIGHT_PAREN77 = None
        alias74 = None

        alias76 = None


        LEFT_PAREN73_tree = None
        COMMA75_tree = None
        RIGHT_PAREN77_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        try:
            try:
                # QueryParser.g:234:20: ( LEFT_PAREN ( alias ( COMMA alias )* )? RIGHT_PAREN -> ^( PARAMS ( alias )* ) )
                # QueryParser.g:234:22: LEFT_PAREN ( alias ( COMMA alias )* )? RIGHT_PAREN
                pass 
                LEFT_PAREN73=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_macro_param_clause1209) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN73)
                # QueryParser.g:234:33: ( alias ( COMMA alias )* )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == IDENTIFIER_L) :
                    alt18 = 1
                if alt18 == 1:
                    # QueryParser.g:234:35: alias ( COMMA alias )*
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_macro_param_clause1213)
                    alias74 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias74.tree)
                    # QueryParser.g:234:41: ( COMMA alias )*
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == COMMA) :
                            alt17 = 1


                        if alt17 == 1:
                            # QueryParser.g:234:42: COMMA alias
                            pass 
                            COMMA75=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_macro_param_clause1216) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA75)
                            self._state.following.append(self.FOLLOW_alias_in_macro_param_clause1218)
                            alias76 = self.alias()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_alias.add(alias76.tree)


                        else:
                            break #loop17



                RIGHT_PAREN77=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_macro_param_clause1225) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN77)

                # AST Rewrite
                # elements: alias
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 235:5: -> ^( PARAMS ( alias )* )
                    # QueryParser.g:235:8: ^( PARAMS ( alias )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMS, "PARAMS"), root_1)

                    # QueryParser.g:235:17: ( alias )*
                    while stream_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_alias.nextTree())


                    stream_alias.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "macro_param_clause"

    class macro_return_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.macro_return_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "macro_return_clause"
    # QueryParser.g:238:1: macro_return_clause : RETURNS ( ( alias ( COMMA alias )* ) | VOID ) -> ^( RETURN_VAL ( alias )* ) ;
    def macro_return_clause(self, ):

        retval = self.macro_return_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RETURNS78 = None
        COMMA80 = None
        VOID82 = None
        alias79 = None

        alias81 = None


        RETURNS78_tree = None
        COMMA80_tree = None
        VOID82_tree = None
        stream_VOID = RewriteRuleTokenStream(self._adaptor, "token VOID")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_RETURNS = RewriteRuleTokenStream(self._adaptor, "token RETURNS")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        try:
            try:
                # QueryParser.g:239:5: ( RETURNS ( ( alias ( COMMA alias )* ) | VOID ) -> ^( RETURN_VAL ( alias )* ) )
                # QueryParser.g:239:7: RETURNS ( ( alias ( COMMA alias )* ) | VOID )
                pass 
                RETURNS78=self.match(self.input, RETURNS, self.FOLLOW_RETURNS_in_macro_return_clause1252) 
                if self._state.backtracking == 0:
                    stream_RETURNS.add(RETURNS78)
                # QueryParser.g:239:15: ( ( alias ( COMMA alias )* ) | VOID )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == IDENTIFIER_L) :
                    alt20 = 1
                elif (LA20_0 == VOID) :
                    alt20 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # QueryParser.g:239:16: ( alias ( COMMA alias )* )
                    pass 
                    # QueryParser.g:239:16: ( alias ( COMMA alias )* )
                    # QueryParser.g:239:17: alias ( COMMA alias )*
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_macro_return_clause1256)
                    alias79 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias79.tree)
                    # QueryParser.g:239:23: ( COMMA alias )*
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == COMMA) :
                            alt19 = 1


                        if alt19 == 1:
                            # QueryParser.g:239:24: COMMA alias
                            pass 
                            COMMA80=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_macro_return_clause1259) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA80)
                            self._state.following.append(self.FOLLOW_alias_in_macro_return_clause1261)
                            alias81 = self.alias()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_alias.add(alias81.tree)


                        else:
                            break #loop19





                elif alt20 == 2:
                    # QueryParser.g:239:41: VOID
                    pass 
                    VOID82=self.match(self.input, VOID, self.FOLLOW_VOID_in_macro_return_clause1268) 
                    if self._state.backtracking == 0:
                        stream_VOID.add(VOID82)




                # AST Rewrite
                # elements: alias
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 240:9: -> ^( RETURN_VAL ( alias )* )
                    # QueryParser.g:240:12: ^( RETURN_VAL ( alias )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURN_VAL, "RETURN_VAL"), root_1)

                    # QueryParser.g:240:25: ( alias )*
                    while stream_alias.hasNext():
                        self._adaptor.addChild(root_1, stream_alias.nextTree())


                    stream_alias.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "macro_return_clause"

    class macro_body_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.macro_body_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "macro_body_clause"
    # QueryParser.g:243:1: macro_body_clause : content -> ^( MACRO_BODY ) ;
    def macro_body_clause(self, ):

        retval = self.macro_body_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        content83 = None


        stream_content = RewriteRuleSubtreeStream(self._adaptor, "rule content")
        try:
            try:
                # QueryParser.g:243:19: ( content -> ^( MACRO_BODY ) )
                # QueryParser.g:243:21: content
                pass 
                self._state.following.append(self.FOLLOW_content_in_macro_body_clause1295)
                content83 = self.content()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_content.add(content83.tree)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 244:5: -> ^( MACRO_BODY )
                    # QueryParser.g:244:8: ^( MACRO_BODY )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MACRO_BODY, "MACRO_BODY"), root_1)

                    self._adaptor.addChild(root_1, new PigParserNode(new CommonToken(1, ((content83 is not None) and [self.input.toString(content83.start,content83.stop)] or [None])[0]), this.getSourceName(), content83.start) )

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "macro_body_clause"

    class macro_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.macro_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "macro_clause"
    # QueryParser.g:247:1: macro_clause : macro_param_clause macro_return_clause macro_body_clause -> ^( MACRO_DEF macro_param_clause macro_return_clause macro_body_clause ) ;
    def macro_clause(self, ):

        retval = self.macro_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        macro_param_clause84 = None

        macro_return_clause85 = None

        macro_body_clause86 = None


        stream_macro_body_clause = RewriteRuleSubtreeStream(self._adaptor, "rule macro_body_clause")
        stream_macro_param_clause = RewriteRuleSubtreeStream(self._adaptor, "rule macro_param_clause")
        stream_macro_return_clause = RewriteRuleSubtreeStream(self._adaptor, "rule macro_return_clause")
        try:
            try:
                # QueryParser.g:247:14: ( macro_param_clause macro_return_clause macro_body_clause -> ^( MACRO_DEF macro_param_clause macro_return_clause macro_body_clause ) )
                # QueryParser.g:247:16: macro_param_clause macro_return_clause macro_body_clause
                pass 
                self._state.following.append(self.FOLLOW_macro_param_clause_in_macro_clause1317)
                macro_param_clause84 = self.macro_param_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_macro_param_clause.add(macro_param_clause84.tree)
                self._state.following.append(self.FOLLOW_macro_return_clause_in_macro_clause1319)
                macro_return_clause85 = self.macro_return_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_macro_return_clause.add(macro_return_clause85.tree)
                self._state.following.append(self.FOLLOW_macro_body_clause_in_macro_clause1321)
                macro_body_clause86 = self.macro_body_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_macro_body_clause.add(macro_body_clause86.tree)

                # AST Rewrite
                # elements: macro_body_clause, macro_return_clause, macro_param_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 248:5: -> ^( MACRO_DEF macro_param_clause macro_return_clause macro_body_clause )
                    # QueryParser.g:248:8: ^( MACRO_DEF macro_param_clause macro_return_clause macro_body_clause )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MACRO_DEF, "MACRO_DEF"), root_1)

                    self._adaptor.addChild(root_1, stream_macro_param_clause.nextTree())
                    self._adaptor.addChild(root_1, stream_macro_return_clause.nextTree())
                    self._adaptor.addChild(root_1, stream_macro_body_clause.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "macro_clause"

    class inline_return_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.inline_return_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "inline_return_clause"
    # QueryParser.g:251:1: inline_return_clause : ( alias EQUAL -> ^( RETURN_VAL alias ) | alias ( COMMA alias )+ EQUAL -> ^( RETURN_VAL ( alias )+ ) | -> ^( RETURN_VAL ) );
    def inline_return_clause(self, ):

        retval = self.inline_return_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL88 = None
        COMMA90 = None
        EQUAL92 = None
        alias87 = None

        alias89 = None

        alias91 = None


        EQUAL88_tree = None
        COMMA90_tree = None
        EQUAL92_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        try:
            try:
                # QueryParser.g:252:5: ( alias EQUAL -> ^( RETURN_VAL alias ) | alias ( COMMA alias )+ EQUAL -> ^( RETURN_VAL ( alias )+ ) | -> ^( RETURN_VAL ) )
                alt22 = 3
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IDENTIFIER_L) :
                    LA22 = self.input.LA(2)
                    if LA22 == LEFT_PAREN:
                        alt22 = 3
                    elif LA22 == EQUAL:
                        alt22 = 1
                    elif LA22 == COMMA:
                        alt22 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # QueryParser.g:252:7: alias EQUAL
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_inline_return_clause1351)
                    alias87 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias87.tree)
                    EQUAL88=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_inline_return_clause1353) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL88)

                    # AST Rewrite
                    # elements: alias
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 252:19: -> ^( RETURN_VAL alias )
                        # QueryParser.g:252:22: ^( RETURN_VAL alias )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURN_VAL, "RETURN_VAL"), root_1)

                        self._adaptor.addChild(root_1, stream_alias.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 2:
                    # QueryParser.g:253:4: alias ( COMMA alias )+ EQUAL
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_inline_return_clause1366)
                    alias89 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_alias.add(alias89.tree)
                    # QueryParser.g:253:10: ( COMMA alias )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == COMMA) :
                            alt21 = 1


                        if alt21 == 1:
                            # QueryParser.g:253:11: COMMA alias
                            pass 
                            COMMA90=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_inline_return_clause1369) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA90)
                            self._state.following.append(self.FOLLOW_alias_in_inline_return_clause1371)
                            alias91 = self.alias()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_alias.add(alias91.tree)


                        else:
                            if cnt21 >= 1:
                                break #loop21

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1
                    EQUAL92=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_inline_return_clause1375) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL92)

                    # AST Rewrite
                    # elements: alias
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 253:31: -> ^( RETURN_VAL ( alias )+ )
                        # QueryParser.g:253:34: ^( RETURN_VAL ( alias )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURN_VAL, "RETURN_VAL"), root_1)

                        # QueryParser.g:253:47: ( alias )+
                        if not (stream_alias.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_alias.hasNext():
                            self._adaptor.addChild(root_1, stream_alias.nextTree())


                        stream_alias.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt22 == 3:
                    # QueryParser.g:254:4: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 254:4: -> ^( RETURN_VAL )
                        # QueryParser.g:254:7: ^( RETURN_VAL )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(RETURN_VAL, "RETURN_VAL"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "inline_return_clause"

    class inline_param_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.inline_param_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "inline_param_clause"
    # QueryParser.g:257:1: inline_param_clause : LEFT_PAREN ( parameter ( COMMA parameter )* )? RIGHT_PAREN -> ^( PARAMS ( parameter )* ) ;
    def inline_param_clause(self, ):

        retval = self.inline_param_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN93 = None
        COMMA95 = None
        RIGHT_PAREN97 = None
        parameter94 = None

        parameter96 = None


        LEFT_PAREN93_tree = None
        COMMA95_tree = None
        RIGHT_PAREN97_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # QueryParser.g:257:21: ( LEFT_PAREN ( parameter ( COMMA parameter )* )? RIGHT_PAREN -> ^( PARAMS ( parameter )* ) )
                # QueryParser.g:257:23: LEFT_PAREN ( parameter ( COMMA parameter )* )? RIGHT_PAREN
                pass 
                LEFT_PAREN93=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_inline_param_clause1404) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN93)
                # QueryParser.g:257:34: ( parameter ( COMMA parameter )* )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((IDENTIFIER_L <= LA24_0 <= INTEGER) or LA24_0 == DOLLARVAR or LA24_0 == DOUBLENUMBER or LA24_0 == QUOTEDSTRING) :
                    alt24 = 1
                if alt24 == 1:
                    # QueryParser.g:257:36: parameter ( COMMA parameter )*
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_in_inline_param_clause1408)
                    parameter94 = self.parameter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameter.add(parameter94.tree)
                    # QueryParser.g:257:46: ( COMMA parameter )*
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == COMMA) :
                            alt23 = 1


                        if alt23 == 1:
                            # QueryParser.g:257:47: COMMA parameter
                            pass 
                            COMMA95=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_inline_param_clause1411) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA95)
                            self._state.following.append(self.FOLLOW_parameter_in_inline_param_clause1413)
                            parameter96 = self.parameter()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_parameter.add(parameter96.tree)


                        else:
                            break #loop23



                RIGHT_PAREN97=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_inline_param_clause1420) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN97)

                # AST Rewrite
                # elements: parameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 258:5: -> ^( PARAMS ( parameter )* )
                    # QueryParser.g:258:8: ^( PARAMS ( parameter )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(PARAMS, "PARAMS"), root_1)

                    # QueryParser.g:258:17: ( parameter )*
                    while stream_parameter.hasNext():
                        self._adaptor.addChild(root_1, stream_parameter.nextTree())


                    stream_parameter.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "inline_param_clause"

    class inline_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.inline_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "inline_clause"
    # QueryParser.g:261:1: inline_clause : inline_return_clause alias inline_param_clause -> ^( MACRO_INLINE alias inline_return_clause inline_param_clause ) ;
    def inline_clause(self, ):

        retval = self.inline_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        inline_return_clause98 = None

        alias99 = None

        inline_param_clause100 = None


        stream_inline_return_clause = RewriteRuleSubtreeStream(self._adaptor, "rule inline_return_clause")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_inline_param_clause = RewriteRuleSubtreeStream(self._adaptor, "rule inline_param_clause")
        try:
            try:
                # QueryParser.g:261:15: ( inline_return_clause alias inline_param_clause -> ^( MACRO_INLINE alias inline_return_clause inline_param_clause ) )
                # QueryParser.g:261:17: inline_return_clause alias inline_param_clause
                pass 
                self._state.following.append(self.FOLLOW_inline_return_clause_in_inline_clause1442)
                inline_return_clause98 = self.inline_return_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_inline_return_clause.add(inline_return_clause98.tree)
                self._state.following.append(self.FOLLOW_alias_in_inline_clause1444)
                alias99 = self.alias()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_alias.add(alias99.tree)
                self._state.following.append(self.FOLLOW_inline_param_clause_in_inline_clause1446)
                inline_param_clause100 = self.inline_param_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_inline_param_clause.add(inline_param_clause100.tree)

                # AST Rewrite
                # elements: alias, inline_return_clause, inline_param_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 262:5: -> ^( MACRO_INLINE alias inline_return_clause inline_param_clause )
                    # QueryParser.g:262:8: ^( MACRO_INLINE alias inline_return_clause inline_param_clause )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MACRO_INLINE, "MACRO_INLINE"), root_1)

                    self._adaptor.addChild(root_1, stream_alias.nextTree())
                    self._adaptor.addChild(root_1, stream_inline_return_clause.nextTree())
                    self._adaptor.addChild(root_1, stream_inline_param_clause.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "inline_clause"

    class import_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.import_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "import_clause"
    # QueryParser.g:265:1: import_clause : IMPORT QUOTEDSTRING ;
    def import_clause(self, ):

        retval = self.import_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT101 = None
        QUOTEDSTRING102 = None

        IMPORT101_tree = None
        QUOTEDSTRING102_tree = None

        try:
            try:
                # QueryParser.g:265:15: ( IMPORT QUOTEDSTRING )
                # QueryParser.g:265:17: IMPORT QUOTEDSTRING
                pass 
                root_0 = self._adaptor.nil()

                IMPORT101=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_import_clause1471)
                if self._state.backtracking == 0:

                    IMPORT101_tree = self._adaptor.createWithPayload(IMPORT101)
                    root_0 = self._adaptor.becomeRoot(IMPORT101_tree, root_0)

                QUOTEDSTRING102=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_import_clause1474)
                if self._state.backtracking == 0:

                    QUOTEDSTRING102_tree = self._adaptor.createWithPayload(QUOTEDSTRING102)
                    self._adaptor.addChild(root_0, QUOTEDSTRING102_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "import_clause"

    class define_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.define_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "define_clause"
    # QueryParser.g:268:1: define_clause : DEFINE alias ( cmd | func_clause | macro_clause ) ;
    def define_clause(self, ):

        retval = self.define_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DEFINE103 = None
        alias104 = None

        cmd105 = None

        func_clause106 = None

        macro_clause107 = None


        DEFINE103_tree = None

        try:
            try:
                # QueryParser.g:268:15: ( DEFINE alias ( cmd | func_clause | macro_clause ) )
                # QueryParser.g:268:17: DEFINE alias ( cmd | func_clause | macro_clause )
                pass 
                root_0 = self._adaptor.nil()

                DEFINE103=self.match(self.input, DEFINE, self.FOLLOW_DEFINE_in_define_clause1483)
                if self._state.backtracking == 0:

                    DEFINE103_tree = self._adaptor.createWithPayload(DEFINE103)
                    root_0 = self._adaptor.becomeRoot(DEFINE103_tree, root_0)

                self._state.following.append(self.FOLLOW_alias_in_define_clause1486)
                alias104 = self.alias()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, alias104.tree)
                # QueryParser.g:268:31: ( cmd | func_clause | macro_clause )
                alt25 = 3
                LA25 = self.input.LA(1)
                if LA25 == EXECCOMMAND:
                    alt25 = 1
                elif LA25 == IMPORT or LA25 == RETURNS or LA25 == DEFINE or LA25 == LOAD or LA25 == FILTER or LA25 == FOREACH or LA25 == ORDER or LA25 == CUBE or LA25 == ROLLUP or LA25 == DISTINCT or LA25 == COGROUP or LA25 == JOIN or LA25 == CROSS or LA25 == UNION or LA25 == SPLIT or LA25 == INTO or LA25 == IF or LA25 == ALL or LA25 == AS or LA25 == BY or LA25 == USING or LA25 == INNER or LA25 == OUTER or LA25 == PARALLEL or LA25 == PARTITION or LA25 == GROUP or LA25 == AND or LA25 == OR or LA25 == NOT or LA25 == GENERATE or LA25 == FLATTEN or LA25 == ASC or LA25 == DESC or LA25 == INT or LA25 == LONG or LA25 == FLOAT or LA25 == DOUBLE or LA25 == DATETIME or LA25 == CHARARRAY or LA25 == BYTEARRAY or LA25 == BAG or LA25 == TUPLE or LA25 == MAP or LA25 == IS or LA25 == STREAM or LA25 == THROUGH or LA25 == STORE or LA25 == MAPREDUCE or LA25 == SHIP or LA25 == CACHE or LA25 == INPUT or LA25 == OUTPUT or LA25 == STDERROR or LA25 == STDIN or LA25 == STDOUT or LA25 == LIMIT or LA25 == SAMPLE or LA25 == LEFT or LA25 == RIGHT or LA25 == FULL or LA25 == STR_OP_EQ or LA25 == STR_OP_GT or LA25 == STR_OP_LT or LA25 == STR_OP_GTE or LA25 == STR_OP_LTE or LA25 == STR_OP_NE or LA25 == STR_OP_MATCHES or LA25 == TRUE or LA25 == FALSE or LA25 == IDENTIFIER_L or LA25 == BOOL or LA25 == REALIAS:
                    alt25 = 2
                elif LA25 == LEFT_PAREN:
                    alt25 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # QueryParser.g:268:33: cmd
                    pass 
                    self._state.following.append(self.FOLLOW_cmd_in_define_clause1490)
                    cmd105 = self.cmd()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cmd105.tree)


                elif alt25 == 2:
                    # QueryParser.g:268:39: func_clause
                    pass 
                    self._state.following.append(self.FOLLOW_func_clause_in_define_clause1494)
                    func_clause106 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause106.tree)


                elif alt25 == 3:
                    # QueryParser.g:268:53: macro_clause
                    pass 
                    self._state.following.append(self.FOLLOW_macro_clause_in_define_clause1498)
                    macro_clause107 = self.macro_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, macro_clause107.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "define_clause"

    class cmd_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cmd_return, self).__init__()

            self.tree = None




    # $ANTLR start "cmd"
    # QueryParser.g:271:1: cmd : EXECCOMMAND ( ship_clause | cache_clause | input_clause | output_clause | error_clause )* ;
    def cmd(self, ):

        retval = self.cmd_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EXECCOMMAND108 = None
        ship_clause109 = None

        cache_clause110 = None

        input_clause111 = None

        output_clause112 = None

        error_clause113 = None


        EXECCOMMAND108_tree = None

        try:
            try:
                # QueryParser.g:271:5: ( EXECCOMMAND ( ship_clause | cache_clause | input_clause | output_clause | error_clause )* )
                # QueryParser.g:271:7: EXECCOMMAND ( ship_clause | cache_clause | input_clause | output_clause | error_clause )*
                pass 
                root_0 = self._adaptor.nil()

                EXECCOMMAND108=self.match(self.input, EXECCOMMAND, self.FOLLOW_EXECCOMMAND_in_cmd1508)
                if self._state.backtracking == 0:

                    EXECCOMMAND108_tree = self._adaptor.createWithPayload(EXECCOMMAND108)
                    root_0 = self._adaptor.becomeRoot(EXECCOMMAND108_tree, root_0)

                # QueryParser.g:271:20: ( ship_clause | cache_clause | input_clause | output_clause | error_clause )*
                while True: #loop26
                    alt26 = 6
                    LA26 = self.input.LA(1)
                    if LA26 == SHIP:
                        alt26 = 1
                    elif LA26 == CACHE:
                        alt26 = 2
                    elif LA26 == INPUT:
                        alt26 = 3
                    elif LA26 == OUTPUT:
                        alt26 = 4
                    elif LA26 == STDERROR:
                        alt26 = 5

                    if alt26 == 1:
                        # QueryParser.g:271:22: ship_clause
                        pass 
                        self._state.following.append(self.FOLLOW_ship_clause_in_cmd1513)
                        ship_clause109 = self.ship_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, ship_clause109.tree)


                    elif alt26 == 2:
                        # QueryParser.g:271:36: cache_clause
                        pass 
                        self._state.following.append(self.FOLLOW_cache_clause_in_cmd1517)
                        cache_clause110 = self.cache_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, cache_clause110.tree)


                    elif alt26 == 3:
                        # QueryParser.g:271:51: input_clause
                        pass 
                        self._state.following.append(self.FOLLOW_input_clause_in_cmd1521)
                        input_clause111 = self.input_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, input_clause111.tree)


                    elif alt26 == 4:
                        # QueryParser.g:271:66: output_clause
                        pass 
                        self._state.following.append(self.FOLLOW_output_clause_in_cmd1525)
                        output_clause112 = self.output_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, output_clause112.tree)


                    elif alt26 == 5:
                        # QueryParser.g:271:82: error_clause
                        pass 
                        self._state.following.append(self.FOLLOW_error_clause_in_cmd1529)
                        error_clause113 = self.error_clause()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, error_clause113.tree)


                    else:
                        break #loop26



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cmd"

    class ship_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.ship_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "ship_clause"
    # QueryParser.g:274:1: ship_clause : SHIP LEFT_PAREN ( path_list )? RIGHT_PAREN ;
    def ship_clause(self, ):

        retval = self.ship_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SHIP114 = None
        LEFT_PAREN115 = None
        RIGHT_PAREN117 = None
        path_list116 = None


        SHIP114_tree = None
        LEFT_PAREN115_tree = None
        RIGHT_PAREN117_tree = None

        try:
            try:
                # QueryParser.g:274:13: ( SHIP LEFT_PAREN ( path_list )? RIGHT_PAREN )
                # QueryParser.g:274:15: SHIP LEFT_PAREN ( path_list )? RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                SHIP114=self.match(self.input, SHIP, self.FOLLOW_SHIP_in_ship_clause1541)
                if self._state.backtracking == 0:

                    SHIP114_tree = self._adaptor.createWithPayload(SHIP114)
                    root_0 = self._adaptor.becomeRoot(SHIP114_tree, root_0)

                LEFT_PAREN115=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_ship_clause1544)
                # QueryParser.g:274:33: ( path_list )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == QUOTEDSTRING) :
                    alt27 = 1
                if alt27 == 1:
                    # QueryParser.g:0:0: path_list
                    pass 
                    self._state.following.append(self.FOLLOW_path_list_in_ship_clause1547)
                    path_list116 = self.path_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, path_list116.tree)



                RIGHT_PAREN117=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_ship_clause1550)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "ship_clause"

    class path_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.path_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "path_list"
    # QueryParser.g:277:1: path_list : QUOTEDSTRING ( COMMA QUOTEDSTRING )* -> ( QUOTEDSTRING )+ ;
    def path_list(self, ):

        retval = self.path_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING118 = None
        COMMA119 = None
        QUOTEDSTRING120 = None

        QUOTEDSTRING118_tree = None
        COMMA119_tree = None
        QUOTEDSTRING120_tree = None
        stream_QUOTEDSTRING = RewriteRuleTokenStream(self._adaptor, "token QUOTEDSTRING")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")

        try:
            try:
                # QueryParser.g:277:11: ( QUOTEDSTRING ( COMMA QUOTEDSTRING )* -> ( QUOTEDSTRING )+ )
                # QueryParser.g:277:13: QUOTEDSTRING ( COMMA QUOTEDSTRING )*
                pass 
                QUOTEDSTRING118=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_path_list1560) 
                if self._state.backtracking == 0:
                    stream_QUOTEDSTRING.add(QUOTEDSTRING118)
                # QueryParser.g:277:26: ( COMMA QUOTEDSTRING )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == COMMA) :
                        alt28 = 1


                    if alt28 == 1:
                        # QueryParser.g:277:28: COMMA QUOTEDSTRING
                        pass 
                        COMMA119=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_path_list1564) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA119)
                        QUOTEDSTRING120=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_path_list1566) 
                        if self._state.backtracking == 0:
                            stream_QUOTEDSTRING.add(QUOTEDSTRING120)


                    else:
                        break #loop28

                # AST Rewrite
                # elements: QUOTEDSTRING
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 278:10: -> ( QUOTEDSTRING )+
                    # QueryParser.g:278:13: ( QUOTEDSTRING )+
                    if not (stream_QUOTEDSTRING.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_QUOTEDSTRING.hasNext():
                        self._adaptor.addChild(root_0, stream_QUOTEDSTRING.nextNode())


                    stream_QUOTEDSTRING.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "path_list"

    class cache_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cache_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "cache_clause"
    # QueryParser.g:281:1: cache_clause : CACHE LEFT_PAREN path_list RIGHT_PAREN ;
    def cache_clause(self, ):

        retval = self.cache_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CACHE121 = None
        LEFT_PAREN122 = None
        RIGHT_PAREN124 = None
        path_list123 = None


        CACHE121_tree = None
        LEFT_PAREN122_tree = None
        RIGHT_PAREN124_tree = None

        try:
            try:
                # QueryParser.g:281:14: ( CACHE LEFT_PAREN path_list RIGHT_PAREN )
                # QueryParser.g:281:16: CACHE LEFT_PAREN path_list RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                CACHE121=self.match(self.input, CACHE, self.FOLLOW_CACHE_in_cache_clause1593)
                if self._state.backtracking == 0:

                    CACHE121_tree = self._adaptor.createWithPayload(CACHE121)
                    root_0 = self._adaptor.becomeRoot(CACHE121_tree, root_0)

                LEFT_PAREN122=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_cache_clause1596)
                self._state.following.append(self.FOLLOW_path_list_in_cache_clause1599)
                path_list123 = self.path_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, path_list123.tree)
                RIGHT_PAREN124=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_cache_clause1601)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cache_clause"

    class input_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.input_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "input_clause"
    # QueryParser.g:284:1: input_clause : INPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN ;
    def input_clause(self, ):

        retval = self.input_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        INPUT125 = None
        LEFT_PAREN126 = None
        RIGHT_PAREN128 = None
        stream_cmd_list127 = None


        INPUT125_tree = None
        LEFT_PAREN126_tree = None
        RIGHT_PAREN128_tree = None

        try:
            try:
                # QueryParser.g:284:14: ( INPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN )
                # QueryParser.g:284:16: INPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                INPUT125=self.match(self.input, INPUT, self.FOLLOW_INPUT_in_input_clause1611)
                if self._state.backtracking == 0:

                    INPUT125_tree = self._adaptor.createWithPayload(INPUT125)
                    root_0 = self._adaptor.becomeRoot(INPUT125_tree, root_0)

                LEFT_PAREN126=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_input_clause1614)
                self._state.following.append(self.FOLLOW_stream_cmd_list_in_input_clause1617)
                stream_cmd_list127 = self.stream_cmd_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, stream_cmd_list127.tree)
                RIGHT_PAREN128=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_input_clause1619)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "input_clause"

    class stream_cmd_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.stream_cmd_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "stream_cmd_list"
    # QueryParser.g:287:1: stream_cmd_list : stream_cmd ( COMMA stream_cmd )* -> ( stream_cmd )+ ;
    def stream_cmd_list(self, ):

        retval = self.stream_cmd_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA130 = None
        stream_cmd129 = None

        stream_cmd131 = None


        COMMA130_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_stream_cmd = RewriteRuleSubtreeStream(self._adaptor, "rule stream_cmd")
        try:
            try:
                # QueryParser.g:287:17: ( stream_cmd ( COMMA stream_cmd )* -> ( stream_cmd )+ )
                # QueryParser.g:287:19: stream_cmd ( COMMA stream_cmd )*
                pass 
                self._state.following.append(self.FOLLOW_stream_cmd_in_stream_cmd_list1629)
                stream_cmd129 = self.stream_cmd()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_stream_cmd.add(stream_cmd129.tree)
                # QueryParser.g:287:30: ( COMMA stream_cmd )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == COMMA) :
                        alt29 = 1


                    if alt29 == 1:
                        # QueryParser.g:287:32: COMMA stream_cmd
                        pass 
                        COMMA130=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_stream_cmd_list1633) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA130)
                        self._state.following.append(self.FOLLOW_stream_cmd_in_stream_cmd_list1635)
                        stream_cmd131 = self.stream_cmd()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_stream_cmd.add(stream_cmd131.tree)


                    else:
                        break #loop29

                # AST Rewrite
                # elements: stream_cmd
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 288:16: -> ( stream_cmd )+
                    # QueryParser.g:288:19: ( stream_cmd )+
                    if not (stream_stream_cmd.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_stream_cmd.hasNext():
                        self._adaptor.addChild(root_0, stream_stream_cmd.nextTree())


                    stream_stream_cmd.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "stream_cmd_list"

    class stream_cmd_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.stream_cmd_return, self).__init__()

            self.tree = None




    # $ANTLR start "stream_cmd"
    # QueryParser.g:291:1: stream_cmd : ( STDIN | STDOUT | QUOTEDSTRING ) ( USING ( func_clause ) )? ;
    def stream_cmd(self, ):

        retval = self.stream_cmd_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set132 = None
        USING133 = None
        func_clause134 = None


        set132_tree = None
        USING133_tree = None

        try:
            try:
                # QueryParser.g:291:12: ( ( STDIN | STDOUT | QUOTEDSTRING ) ( USING ( func_clause ) )? )
                # QueryParser.g:291:14: ( STDIN | STDOUT | QUOTEDSTRING ) ( USING ( func_clause ) )?
                pass 
                root_0 = self._adaptor.nil()

                set132 = self.input.LT(1)
                set132 = self.input.LT(1)
                if (STDIN <= self.input.LA(1) <= STDOUT) or self.input.LA(1) == QUOTEDSTRING:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set132), root_0)
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                # QueryParser.g:291:49: ( USING ( func_clause ) )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == USING) :
                    alt30 = 1
                if alt30 == 1:
                    # QueryParser.g:291:51: USING ( func_clause )
                    pass 
                    USING133=self.match(self.input, USING, self.FOLLOW_USING_in_stream_cmd1684)
                    # QueryParser.g:291:58: ( func_clause )
                    # QueryParser.g:291:60: func_clause
                    pass 
                    self._state.following.append(self.FOLLOW_func_clause_in_stream_cmd1689)
                    func_clause134 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause134.tree)









                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "stream_cmd"

    class output_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.output_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "output_clause"
    # QueryParser.g:294:1: output_clause : OUTPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN ;
    def output_clause(self, ):

        retval = self.output_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OUTPUT135 = None
        LEFT_PAREN136 = None
        RIGHT_PAREN138 = None
        stream_cmd_list137 = None


        OUTPUT135_tree = None
        LEFT_PAREN136_tree = None
        RIGHT_PAREN138_tree = None

        try:
            try:
                # QueryParser.g:294:15: ( OUTPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN )
                # QueryParser.g:294:17: OUTPUT LEFT_PAREN stream_cmd_list RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                OUTPUT135=self.match(self.input, OUTPUT, self.FOLLOW_OUTPUT_in_output_clause1703)
                if self._state.backtracking == 0:

                    OUTPUT135_tree = self._adaptor.createWithPayload(OUTPUT135)
                    root_0 = self._adaptor.becomeRoot(OUTPUT135_tree, root_0)

                LEFT_PAREN136=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_output_clause1706)
                self._state.following.append(self.FOLLOW_stream_cmd_list_in_output_clause1709)
                stream_cmd_list137 = self.stream_cmd_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, stream_cmd_list137.tree)
                RIGHT_PAREN138=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_output_clause1711)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "output_clause"

    class error_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.error_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "error_clause"
    # QueryParser.g:297:1: error_clause : STDERROR LEFT_PAREN ( QUOTEDSTRING ( LIMIT INTEGER )? )? RIGHT_PAREN ;
    def error_clause(self, ):

        retval = self.error_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STDERROR139 = None
        LEFT_PAREN140 = None
        QUOTEDSTRING141 = None
        LIMIT142 = None
        INTEGER143 = None
        RIGHT_PAREN144 = None

        STDERROR139_tree = None
        LEFT_PAREN140_tree = None
        QUOTEDSTRING141_tree = None
        LIMIT142_tree = None
        INTEGER143_tree = None
        RIGHT_PAREN144_tree = None

        try:
            try:
                # QueryParser.g:297:14: ( STDERROR LEFT_PAREN ( QUOTEDSTRING ( LIMIT INTEGER )? )? RIGHT_PAREN )
                # QueryParser.g:297:16: STDERROR LEFT_PAREN ( QUOTEDSTRING ( LIMIT INTEGER )? )? RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                STDERROR139=self.match(self.input, STDERROR, self.FOLLOW_STDERROR_in_error_clause1721)
                if self._state.backtracking == 0:

                    STDERROR139_tree = self._adaptor.createWithPayload(STDERROR139)
                    root_0 = self._adaptor.becomeRoot(STDERROR139_tree, root_0)

                LEFT_PAREN140=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_error_clause1724)
                # QueryParser.g:297:38: ( QUOTEDSTRING ( LIMIT INTEGER )? )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == QUOTEDSTRING) :
                    alt32 = 1
                if alt32 == 1:
                    # QueryParser.g:297:40: QUOTEDSTRING ( LIMIT INTEGER )?
                    pass 
                    QUOTEDSTRING141=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_error_clause1729)
                    if self._state.backtracking == 0:

                        QUOTEDSTRING141_tree = self._adaptor.createWithPayload(QUOTEDSTRING141)
                        self._adaptor.addChild(root_0, QUOTEDSTRING141_tree)

                    # QueryParser.g:297:53: ( LIMIT INTEGER )?
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == LIMIT) :
                        alt31 = 1
                    if alt31 == 1:
                        # QueryParser.g:297:55: LIMIT INTEGER
                        pass 
                        LIMIT142=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_error_clause1733)
                        INTEGER143=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_error_clause1736)
                        if self._state.backtracking == 0:

                            INTEGER143_tree = self._adaptor.createWithPayload(INTEGER143)
                            self._adaptor.addChild(root_0, INTEGER143_tree)







                RIGHT_PAREN144=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_error_clause1744)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "error_clause"

    class load_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.load_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "load_clause"
    # QueryParser.g:300:1: load_clause : LOAD filename ( USING func_clause )? ( as_clause )? ;
    def load_clause(self, ):

        retval = self.load_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LOAD145 = None
        USING147 = None
        filename146 = None

        func_clause148 = None

        as_clause149 = None


        LOAD145_tree = None
        USING147_tree = None

        try:
            try:
                # QueryParser.g:300:13: ( LOAD filename ( USING func_clause )? ( as_clause )? )
                # QueryParser.g:300:15: LOAD filename ( USING func_clause )? ( as_clause )?
                pass 
                root_0 = self._adaptor.nil()

                LOAD145=self.match(self.input, LOAD, self.FOLLOW_LOAD_in_load_clause1754)
                if self._state.backtracking == 0:

                    LOAD145_tree = self._adaptor.createWithPayload(LOAD145)
                    root_0 = self._adaptor.becomeRoot(LOAD145_tree, root_0)

                self._state.following.append(self.FOLLOW_filename_in_load_clause1757)
                filename146 = self.filename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, filename146.tree)
                # QueryParser.g:300:30: ( USING func_clause )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == USING) :
                    alt33 = 1
                if alt33 == 1:
                    # QueryParser.g:300:32: USING func_clause
                    pass 
                    USING147=self.match(self.input, USING, self.FOLLOW_USING_in_load_clause1761)
                    self._state.following.append(self.FOLLOW_func_clause_in_load_clause1764)
                    func_clause148 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause148.tree)



                # QueryParser.g:300:54: ( as_clause )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == AS) :
                    alt34 = 1
                if alt34 == 1:
                    # QueryParser.g:0:0: as_clause
                    pass 
                    self._state.following.append(self.FOLLOW_as_clause_in_load_clause1769)
                    as_clause149 = self.as_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, as_clause149.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "load_clause"

    class filename_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.filename_return, self).__init__()

            self.tree = None




    # $ANTLR start "filename"
    # QueryParser.g:303:1: filename : QUOTEDSTRING ;
    def filename(self, ):

        retval = self.filename_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING150 = None

        QUOTEDSTRING150_tree = None

        try:
            try:
                # QueryParser.g:303:10: ( QUOTEDSTRING )
                # QueryParser.g:303:12: QUOTEDSTRING
                pass 
                root_0 = self._adaptor.nil()

                QUOTEDSTRING150=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_filename1779)
                if self._state.backtracking == 0:

                    QUOTEDSTRING150_tree = self._adaptor.createWithPayload(QUOTEDSTRING150)
                    self._adaptor.addChild(root_0, QUOTEDSTRING150_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "filename"

    class as_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.as_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "as_clause"
    # QueryParser.g:306:1: as_clause : AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) ;
    def as_clause(self, ):

        retval = self.as_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS151 = None
        LEFT_PAREN152 = None
        RIGHT_PAREN154 = None
        field_def_list153 = None

        field_def155 = None


        AS151_tree = None
        LEFT_PAREN152_tree = None
        RIGHT_PAREN154_tree = None

        try:
            try:
                # QueryParser.g:306:10: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )
                # QueryParser.g:306:12: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                pass 
                root_0 = self._adaptor.nil()

                AS151=self.match(self.input, AS, self.FOLLOW_AS_in_as_clause1787)
                if self._state.backtracking == 0:

                    AS151_tree = self._adaptor.createWithPayload(AS151)
                    root_0 = self._adaptor.becomeRoot(AS151_tree, root_0)

                # QueryParser.g:306:16: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                alt35 = 2
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # QueryParser.g:306:18: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                    pass 
                    # QueryParser.g:306:18: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                    # QueryParser.g:306:20: LEFT_PAREN field_def_list RIGHT_PAREN
                    pass 
                    LEFT_PAREN152=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_as_clause1794)
                    self._state.following.append(self.FOLLOW_field_def_list_in_as_clause1797)
                    field_def_list153 = self.field_def_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, field_def_list153.tree)
                    RIGHT_PAREN154=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_as_clause1799)





                elif alt35 == 2:
                    # QueryParser.g:306:64: field_def
                    pass 
                    self._state.following.append(self.FOLLOW_field_def_in_as_clause1806)
                    field_def155 = self.field_def()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, field_def155.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "as_clause"

    class field_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.field_def_return, self).__init__()

            self.tree = None




    # $ANTLR start "field_def"
    # QueryParser.g:309:1: field_def : ( identifier ( COLON type )? -> ^( FIELD_DEF identifier ( type )? ) | type -> ^( FIELD_DEF_WITHOUT_IDENTIFIER type ) );
    def field_def(self, ):

        retval = self.field_def_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COLON157 = None
        identifier156 = None

        type158 = None

        type159 = None


        COLON157_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # QueryParser.g:309:11: ( identifier ( COLON type )? -> ^( FIELD_DEF identifier ( type )? ) | type -> ^( FIELD_DEF_WITHOUT_IDENTIFIER type ) )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == IDENTIFIER_L) :
                    alt37 = 1
                elif ((BOOLEAN <= LA37_0 <= MAP) or LA37_0 == LEFT_PAREN or LA37_0 == LEFT_CURLY or LA37_0 == LEFT_BRACKET) :
                    alt37 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae

                if alt37 == 1:
                    # QueryParser.g:309:13: identifier ( COLON type )?
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_field_def1817)
                    identifier156 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier156.tree)
                    # QueryParser.g:309:24: ( COLON type )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == COLON) :
                        alt36 = 1
                    if alt36 == 1:
                        # QueryParser.g:309:26: COLON type
                        pass 
                        COLON157=self.match(self.input, COLON, self.FOLLOW_COLON_in_field_def1821) 
                        if self._state.backtracking == 0:
                            stream_COLON.add(COLON157)
                        self._state.following.append(self.FOLLOW_type_in_field_def1823)
                        type158 = self.type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_type.add(type158.tree)




                    # AST Rewrite
                    # elements: identifier, type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 310:10: -> ^( FIELD_DEF identifier ( type )? )
                        # QueryParser.g:310:13: ^( FIELD_DEF identifier ( type )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FIELD_DEF, "FIELD_DEF"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        # QueryParser.g:310:37: ( type )?
                        if stream_type.hasNext():
                            self._adaptor.addChild(root_1, stream_type.nextTree())


                        stream_type.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt37 == 2:
                    # QueryParser.g:311:13: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_field_def1862)
                    type159 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type159.tree)

                    # AST Rewrite
                    # elements: type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 312:10: -> ^( FIELD_DEF_WITHOUT_IDENTIFIER type )
                        # QueryParser.g:312:13: ^( FIELD_DEF_WITHOUT_IDENTIFIER type )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FIELD_DEF_WITHOUT_IDENTIFIER, "FIELD_DEF_WITHOUT_IDENTIFIER"), root_1)

                        self._adaptor.addChild(root_1, stream_type.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "field_def"

    class field_def_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.field_def_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "field_def_list"
    # QueryParser.g:315:1: field_def_list : field_def ( COMMA field_def )* -> ( field_def )+ ;
    def field_def_list(self, ):

        retval = self.field_def_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA161 = None
        field_def160 = None

        field_def162 = None


        COMMA161_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_field_def = RewriteRuleSubtreeStream(self._adaptor, "rule field_def")
        try:
            try:
                # QueryParser.g:315:16: ( field_def ( COMMA field_def )* -> ( field_def )+ )
                # QueryParser.g:315:18: field_def ( COMMA field_def )*
                pass 
                self._state.following.append(self.FOLLOW_field_def_in_field_def_list1890)
                field_def160 = self.field_def()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_field_def.add(field_def160.tree)
                # QueryParser.g:315:28: ( COMMA field_def )*
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == COMMA) :
                        alt38 = 1


                    if alt38 == 1:
                        # QueryParser.g:315:30: COMMA field_def
                        pass 
                        COMMA161=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_field_def_list1894) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA161)
                        self._state.following.append(self.FOLLOW_field_def_in_field_def_list1896)
                        field_def162 = self.field_def()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_field_def.add(field_def162.tree)


                    else:
                        break #loop38

                # AST Rewrite
                # elements: field_def
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 316:15: -> ( field_def )+
                    # QueryParser.g:316:18: ( field_def )+
                    if not (stream_field_def.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_field_def.hasNext():
                        self._adaptor.addChild(root_0, stream_field_def.nextTree())


                    stream_field_def.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "field_def_list"

    class type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.type_return, self).__init__()

            self.tree = None




    # $ANTLR start "type"
    # QueryParser.g:319:1: type : ( simple_type | tuple_type | bag_type | map_type );
    def type(self, ):

        retval = self.type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simple_type163 = None

        tuple_type164 = None

        bag_type165 = None

        map_type166 = None



        try:
            try:
                # QueryParser.g:319:6: ( simple_type | tuple_type | bag_type | map_type )
                alt39 = 4
                LA39 = self.input.LA(1)
                if LA39 == BOOLEAN or LA39 == INT or LA39 == LONG or LA39 == FLOAT or LA39 == DOUBLE or LA39 == DATETIME or LA39 == CHARARRAY or LA39 == BYTEARRAY:
                    alt39 = 1
                elif LA39 == TUPLE or LA39 == LEFT_PAREN:
                    alt39 = 2
                elif LA39 == BAG or LA39 == LEFT_CURLY:
                    alt39 = 3
                elif LA39 == MAP or LA39 == LEFT_BRACKET:
                    alt39 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae

                if alt39 == 1:
                    # QueryParser.g:319:8: simple_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_type_in_type1927)
                    simple_type163 = self.simple_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_type163.tree)


                elif alt39 == 2:
                    # QueryParser.g:319:22: tuple_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_tuple_type_in_type1931)
                    tuple_type164 = self.tuple_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple_type164.tree)


                elif alt39 == 3:
                    # QueryParser.g:319:35: bag_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_bag_type_in_type1935)
                    bag_type165 = self.bag_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bag_type165.tree)


                elif alt39 == 4:
                    # QueryParser.g:319:46: map_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_map_type_in_type1939)
                    map_type166 = self.map_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, map_type166.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "type"

    class simple_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.simple_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "simple_type"
    # QueryParser.g:322:1: simple_type : ( BOOLEAN | INT | LONG | FLOAT | DOUBLE | DATETIME | CHARARRAY | BYTEARRAY );
    def simple_type(self, ):

        retval = self.simple_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set167 = None

        set167_tree = None

        try:
            try:
                # QueryParser.g:322:13: ( BOOLEAN | INT | LONG | FLOAT | DOUBLE | DATETIME | CHARARRAY | BYTEARRAY )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set167 = self.input.LT(1)
                if (BOOLEAN <= self.input.LA(1) <= BYTEARRAY):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set167))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "simple_type"

    class tuple_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.tuple_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "tuple_type"
    # QueryParser.g:325:1: tuple_type : ( TUPLE )? LEFT_PAREN ( field_def_list )? RIGHT_PAREN -> ^( TUPLE_TYPE ( field_def_list )? ) ;
    def tuple_type(self, ):

        retval = self.tuple_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TUPLE168 = None
        LEFT_PAREN169 = None
        RIGHT_PAREN171 = None
        field_def_list170 = None


        TUPLE168_tree = None
        LEFT_PAREN169_tree = None
        RIGHT_PAREN171_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_TUPLE = RewriteRuleTokenStream(self._adaptor, "token TUPLE")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_field_def_list = RewriteRuleSubtreeStream(self._adaptor, "rule field_def_list")
        try:
            try:
                # QueryParser.g:325:12: ( ( TUPLE )? LEFT_PAREN ( field_def_list )? RIGHT_PAREN -> ^( TUPLE_TYPE ( field_def_list )? ) )
                # QueryParser.g:325:14: ( TUPLE )? LEFT_PAREN ( field_def_list )? RIGHT_PAREN
                pass 
                # QueryParser.g:325:14: ( TUPLE )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == TUPLE) :
                    alt40 = 1
                if alt40 == 1:
                    # QueryParser.g:0:0: TUPLE
                    pass 
                    TUPLE168=self.match(self.input, TUPLE, self.FOLLOW_TUPLE_in_tuple_type1985) 
                    if self._state.backtracking == 0:
                        stream_TUPLE.add(TUPLE168)



                LEFT_PAREN169=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_tuple_type1988) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN169)
                # QueryParser.g:325:32: ( field_def_list )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((BOOLEAN <= LA41_0 <= MAP) or LA41_0 == IDENTIFIER_L or LA41_0 == LEFT_PAREN or LA41_0 == LEFT_CURLY or LA41_0 == LEFT_BRACKET) :
                    alt41 = 1
                if alt41 == 1:
                    # QueryParser.g:0:0: field_def_list
                    pass 
                    self._state.following.append(self.FOLLOW_field_def_list_in_tuple_type1990)
                    field_def_list170 = self.field_def_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_field_def_list.add(field_def_list170.tree)



                RIGHT_PAREN171=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_tuple_type1993) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN171)

                # AST Rewrite
                # elements: field_def_list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 326:11: -> ^( TUPLE_TYPE ( field_def_list )? )
                    # QueryParser.g:326:14: ^( TUPLE_TYPE ( field_def_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TUPLE_TYPE, "TUPLE_TYPE"), root_1)

                    # QueryParser.g:326:28: ( field_def_list )?
                    if stream_field_def_list.hasNext():
                        self._adaptor.addChild(root_1, stream_field_def_list.nextTree())


                    stream_field_def_list.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "tuple_type"

    class bag_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.bag_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "bag_type"
    # QueryParser.g:329:1: bag_type : ( ( BAG )? LEFT_CURLY ( null_keyword COLON ( tuple_type )? ) RIGHT_CURLY -> ^( BAG_TYPE ( tuple_type )? ) | ( BAG )? LEFT_CURLY ( ( identifier COLON )? tuple_type )? RIGHT_CURLY -> ^( BAG_TYPE ( identifier )? ( tuple_type )? ) );
    def bag_type(self, ):

        retval = self.bag_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BAG172 = None
        LEFT_CURLY173 = None
        COLON175 = None
        RIGHT_CURLY177 = None
        BAG178 = None
        LEFT_CURLY179 = None
        COLON181 = None
        RIGHT_CURLY183 = None
        null_keyword174 = None

        tuple_type176 = None

        identifier180 = None

        tuple_type182 = None


        BAG172_tree = None
        LEFT_CURLY173_tree = None
        COLON175_tree = None
        RIGHT_CURLY177_tree = None
        BAG178_tree = None
        LEFT_CURLY179_tree = None
        COLON181_tree = None
        RIGHT_CURLY183_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_BAG = RewriteRuleTokenStream(self._adaptor, "token BAG")
        stream_RIGHT_CURLY = RewriteRuleTokenStream(self._adaptor, "token RIGHT_CURLY")
        stream_LEFT_CURLY = RewriteRuleTokenStream(self._adaptor, "token LEFT_CURLY")
        stream_tuple_type = RewriteRuleSubtreeStream(self._adaptor, "rule tuple_type")
        stream_null_keyword = RewriteRuleSubtreeStream(self._adaptor, "rule null_keyword")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # QueryParser.g:329:10: ( ( BAG )? LEFT_CURLY ( null_keyword COLON ( tuple_type )? ) RIGHT_CURLY -> ^( BAG_TYPE ( tuple_type )? ) | ( BAG )? LEFT_CURLY ( ( identifier COLON )? tuple_type )? RIGHT_CURLY -> ^( BAG_TYPE ( identifier )? ( tuple_type )? ) )
                alt47 = 2
                LA47_0 = self.input.LA(1)

                if (LA47_0 == BAG) :
                    LA47_1 = self.input.LA(2)

                    if (self.synpred86_QueryParser()) :
                        alt47 = 1
                    elif (True) :
                        alt47 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 47, 1, self.input)

                        raise nvae

                elif (LA47_0 == LEFT_CURLY) :
                    LA47_2 = self.input.LA(2)

                    if (self.synpred86_QueryParser()) :
                        alt47 = 1
                    elif (True) :
                        alt47 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 47, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae

                if alt47 == 1:
                    # QueryParser.g:329:12: ( BAG )? LEFT_CURLY ( null_keyword COLON ( tuple_type )? ) RIGHT_CURLY
                    pass 
                    # QueryParser.g:329:12: ( BAG )?
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == BAG) :
                        alt42 = 1
                    if alt42 == 1:
                        # QueryParser.g:0:0: BAG
                        pass 
                        BAG172=self.match(self.input, BAG, self.FOLLOW_BAG_in_bag_type2023) 
                        if self._state.backtracking == 0:
                            stream_BAG.add(BAG172)



                    LEFT_CURLY173=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_bag_type2026) 
                    if self._state.backtracking == 0:
                        stream_LEFT_CURLY.add(LEFT_CURLY173)
                    # QueryParser.g:329:28: ( null_keyword COLON ( tuple_type )? )
                    # QueryParser.g:329:30: null_keyword COLON ( tuple_type )?
                    pass 
                    self._state.following.append(self.FOLLOW_null_keyword_in_bag_type2030)
                    null_keyword174 = self.null_keyword()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_null_keyword.add(null_keyword174.tree)
                    COLON175=self.match(self.input, COLON, self.FOLLOW_COLON_in_bag_type2032) 
                    if self._state.backtracking == 0:
                        stream_COLON.add(COLON175)
                    # QueryParser.g:329:49: ( tuple_type )?
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == TUPLE or LA43_0 == LEFT_PAREN) :
                        alt43 = 1
                    if alt43 == 1:
                        # QueryParser.g:0:0: tuple_type
                        pass 
                        self._state.following.append(self.FOLLOW_tuple_type_in_bag_type2034)
                        tuple_type176 = self.tuple_type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_tuple_type.add(tuple_type176.tree)






                    RIGHT_CURLY177=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_bag_type2039) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_CURLY.add(RIGHT_CURLY177)

                    # AST Rewrite
                    # elements: tuple_type
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 330:9: -> ^( BAG_TYPE ( tuple_type )? )
                        # QueryParser.g:330:12: ^( BAG_TYPE ( tuple_type )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BAG_TYPE, "BAG_TYPE"), root_1)

                        # QueryParser.g:330:24: ( tuple_type )?
                        if stream_tuple_type.hasNext():
                            self._adaptor.addChild(root_1, stream_tuple_type.nextTree())


                        stream_tuple_type.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt47 == 2:
                    # QueryParser.g:331:12: ( BAG )? LEFT_CURLY ( ( identifier COLON )? tuple_type )? RIGHT_CURLY
                    pass 
                    # QueryParser.g:331:12: ( BAG )?
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == BAG) :
                        alt44 = 1
                    if alt44 == 1:
                        # QueryParser.g:0:0: BAG
                        pass 
                        BAG178=self.match(self.input, BAG, self.FOLLOW_BAG_in_bag_type2071) 
                        if self._state.backtracking == 0:
                            stream_BAG.add(BAG178)



                    LEFT_CURLY179=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_bag_type2074) 
                    if self._state.backtracking == 0:
                        stream_LEFT_CURLY.add(LEFT_CURLY179)
                    # QueryParser.g:331:28: ( ( identifier COLON )? tuple_type )?
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == TUPLE or LA46_0 == IDENTIFIER_L or LA46_0 == LEFT_PAREN) :
                        alt46 = 1
                    if alt46 == 1:
                        # QueryParser.g:331:30: ( identifier COLON )? tuple_type
                        pass 
                        # QueryParser.g:331:30: ( identifier COLON )?
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == IDENTIFIER_L) :
                            alt45 = 1
                        if alt45 == 1:
                            # QueryParser.g:331:32: identifier COLON
                            pass 
                            self._state.following.append(self.FOLLOW_identifier_in_bag_type2080)
                            identifier180 = self.identifier()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_identifier.add(identifier180.tree)
                            COLON181=self.match(self.input, COLON, self.FOLLOW_COLON_in_bag_type2082) 
                            if self._state.backtracking == 0:
                                stream_COLON.add(COLON181)



                        self._state.following.append(self.FOLLOW_tuple_type_in_bag_type2087)
                        tuple_type182 = self.tuple_type()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_tuple_type.add(tuple_type182.tree)



                    RIGHT_CURLY183=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_bag_type2092) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_CURLY.add(RIGHT_CURLY183)

                    # AST Rewrite
                    # elements: tuple_type, identifier
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 332:9: -> ^( BAG_TYPE ( identifier )? ( tuple_type )? )
                        # QueryParser.g:332:12: ^( BAG_TYPE ( identifier )? ( tuple_type )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BAG_TYPE, "BAG_TYPE"), root_1)

                        # QueryParser.g:332:24: ( identifier )?
                        if stream_identifier.hasNext():
                            self._adaptor.addChild(root_1, stream_identifier.nextTree())


                        stream_identifier.reset();
                        # QueryParser.g:332:36: ( tuple_type )?
                        if stream_tuple_type.hasNext():
                            self._adaptor.addChild(root_1, stream_tuple_type.nextTree())


                        stream_tuple_type.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "bag_type"

    class map_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.map_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "map_type"
    # QueryParser.g:335:1: map_type : ( MAP )? LEFT_BRACKET ( type )? RIGHT_BRACKET -> ^( MAP_TYPE ( type )? ) ;
    def map_type(self, ):

        retval = self.map_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MAP184 = None
        LEFT_BRACKET185 = None
        RIGHT_BRACKET187 = None
        type186 = None


        MAP184_tree = None
        LEFT_BRACKET185_tree = None
        RIGHT_BRACKET187_tree = None
        stream_LEFT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token LEFT_BRACKET")
        stream_MAP = RewriteRuleTokenStream(self._adaptor, "token MAP")
        stream_RIGHT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token RIGHT_BRACKET")
        stream_type = RewriteRuleSubtreeStream(self._adaptor, "rule type")
        try:
            try:
                # QueryParser.g:335:10: ( ( MAP )? LEFT_BRACKET ( type )? RIGHT_BRACKET -> ^( MAP_TYPE ( type )? ) )
                # QueryParser.g:335:12: ( MAP )? LEFT_BRACKET ( type )? RIGHT_BRACKET
                pass 
                # QueryParser.g:335:12: ( MAP )?
                alt48 = 2
                LA48_0 = self.input.LA(1)

                if (LA48_0 == MAP) :
                    alt48 = 1
                if alt48 == 1:
                    # QueryParser.g:0:0: MAP
                    pass 
                    MAP184=self.match(self.input, MAP, self.FOLLOW_MAP_in_map_type2123) 
                    if self._state.backtracking == 0:
                        stream_MAP.add(MAP184)



                LEFT_BRACKET185=self.match(self.input, LEFT_BRACKET, self.FOLLOW_LEFT_BRACKET_in_map_type2126) 
                if self._state.backtracking == 0:
                    stream_LEFT_BRACKET.add(LEFT_BRACKET185)
                # QueryParser.g:335:30: ( type )?
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if ((BOOLEAN <= LA49_0 <= MAP) or LA49_0 == LEFT_PAREN or LA49_0 == LEFT_CURLY or LA49_0 == LEFT_BRACKET) :
                    alt49 = 1
                if alt49 == 1:
                    # QueryParser.g:0:0: type
                    pass 
                    self._state.following.append(self.FOLLOW_type_in_map_type2128)
                    type186 = self.type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type.add(type186.tree)



                RIGHT_BRACKET187=self.match(self.input, RIGHT_BRACKET, self.FOLLOW_RIGHT_BRACKET_in_map_type2131) 
                if self._state.backtracking == 0:
                    stream_RIGHT_BRACKET.add(RIGHT_BRACKET187)

                # AST Rewrite
                # elements: type
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 336:9: -> ^( MAP_TYPE ( type )? )
                    # QueryParser.g:336:12: ^( MAP_TYPE ( type )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAP_TYPE, "MAP_TYPE"), root_1)

                    # QueryParser.g:336:24: ( type )?
                    if stream_type.hasNext():
                        self._adaptor.addChild(root_1, stream_type.nextTree())


                    stream_type.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "map_type"

    class func_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.func_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "func_clause"
    # QueryParser.g:339:1: func_clause : ( func_name -> ^( FUNC_REF func_name ) | func_name LEFT_PAREN ( func_args )? RIGHT_PAREN -> ^( FUNC func_name ( func_args )? ) );
    def func_clause(self, ):

        retval = self.func_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN190 = None
        RIGHT_PAREN192 = None
        func_name188 = None

        func_name189 = None

        func_args191 = None


        LEFT_PAREN190_tree = None
        RIGHT_PAREN192_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_func_args = RewriteRuleSubtreeStream(self._adaptor, "rule func_args")
        stream_func_name = RewriteRuleSubtreeStream(self._adaptor, "rule func_name")
        try:
            try:
                # QueryParser.g:339:13: ( func_name -> ^( FUNC_REF func_name ) | func_name LEFT_PAREN ( func_args )? RIGHT_PAREN -> ^( FUNC func_name ( func_args )? ) )
                alt51 = 2
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # QueryParser.g:339:15: func_name
                    pass 
                    self._state.following.append(self.FOLLOW_func_name_in_func_clause2159)
                    func_name188 = self.func_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_func_name.add(func_name188.tree)

                    # AST Rewrite
                    # elements: func_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 340:12: -> ^( FUNC_REF func_name )
                        # QueryParser.g:340:15: ^( FUNC_REF func_name )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_REF, "FUNC_REF"), root_1)

                        self._adaptor.addChild(root_1, stream_func_name.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt51 == 2:
                    # QueryParser.g:341:15: func_name LEFT_PAREN ( func_args )? RIGHT_PAREN
                    pass 
                    self._state.following.append(self.FOLLOW_func_name_in_func_clause2196)
                    func_name189 = self.func_name()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_func_name.add(func_name189.tree)
                    LEFT_PAREN190=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_func_clause2198) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN190)
                    # QueryParser.g:341:36: ( func_args )?
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if ((QUOTEDSTRING <= LA50_0 <= MULTILINE_QUOTEDSTRING)) :
                        alt50 = 1
                    if alt50 == 1:
                        # QueryParser.g:0:0: func_args
                        pass 
                        self._state.following.append(self.FOLLOW_func_args_in_func_clause2200)
                        func_args191 = self.func_args()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_func_args.add(func_args191.tree)



                    RIGHT_PAREN192=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_func_clause2203) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN192)

                    # AST Rewrite
                    # elements: func_args, func_name
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 342:12: -> ^( FUNC func_name ( func_args )? )
                        # QueryParser.g:342:15: ^( FUNC func_name ( func_args )? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC, "FUNC"), root_1)

                        self._adaptor.addChild(root_1, stream_func_name.nextTree())
                        # QueryParser.g:342:33: ( func_args )?
                        if stream_func_args.hasNext():
                            self._adaptor.addChild(root_1, stream_func_args.nextTree())


                        stream_func_args.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "func_clause"

    class func_name_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.func_name_return, self).__init__()

            self.tree = None




    # $ANTLR start "func_name"
    # QueryParser.g:345:1: func_name : eid ( ( PERIOD | DOLLAR ) eid )* ;
    def func_name(self, ):

        retval = self.func_name_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set194 = None
        eid193 = None

        eid195 = None


        set194_tree = None

        try:
            try:
                # QueryParser.g:345:11: ( eid ( ( PERIOD | DOLLAR ) eid )* )
                # QueryParser.g:345:13: eid ( ( PERIOD | DOLLAR ) eid )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_eid_in_func_name2236)
                eid193 = self.eid()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, eid193.tree)
                # QueryParser.g:345:17: ( ( PERIOD | DOLLAR ) eid )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == PERIOD or LA52_0 == DOLLAR) :
                        alt52 = 1


                    if alt52 == 1:
                        # QueryParser.g:345:19: ( PERIOD | DOLLAR ) eid
                        pass 
                        set194 = self.input.LT(1)
                        if self.input.LA(1) == PERIOD or self.input.LA(1) == DOLLAR:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set194))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_eid_in_func_name2250)
                        eid195 = self.eid()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, eid195.tree)


                    else:
                        break #loop52



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "func_name"

    class func_args_string_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.func_args_string_return, self).__init__()

            self.tree = None




    # $ANTLR start "func_args_string"
    # QueryParser.g:348:1: func_args_string : ( QUOTEDSTRING | MULTILINE_QUOTEDSTRING );
    def func_args_string(self, ):

        retval = self.func_args_string_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set196 = None

        set196_tree = None

        try:
            try:
                # QueryParser.g:348:18: ( QUOTEDSTRING | MULTILINE_QUOTEDSTRING )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set196 = self.input.LT(1)
                if (QUOTEDSTRING <= self.input.LA(1) <= MULTILINE_QUOTEDSTRING):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set196))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "func_args_string"

    class func_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.func_args_return, self).__init__()

            self.tree = None




    # $ANTLR start "func_args"
    # QueryParser.g:351:1: func_args : func_args_string ( COMMA func_args_string )* -> ( func_args_string )+ ;
    def func_args(self, ):

        retval = self.func_args_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA198 = None
        func_args_string197 = None

        func_args_string199 = None


        COMMA198_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_func_args_string = RewriteRuleSubtreeStream(self._adaptor, "rule func_args_string")
        try:
            try:
                # QueryParser.g:351:11: ( func_args_string ( COMMA func_args_string )* -> ( func_args_string )+ )
                # QueryParser.g:351:13: func_args_string ( COMMA func_args_string )*
                pass 
                self._state.following.append(self.FOLLOW_func_args_string_in_func_args2275)
                func_args_string197 = self.func_args_string()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_func_args_string.add(func_args_string197.tree)
                # QueryParser.g:351:30: ( COMMA func_args_string )*
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == COMMA) :
                        alt53 = 1


                    if alt53 == 1:
                        # QueryParser.g:351:32: COMMA func_args_string
                        pass 
                        COMMA198=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_func_args2279) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA198)
                        self._state.following.append(self.FOLLOW_func_args_string_in_func_args2281)
                        func_args_string199 = self.func_args_string()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_func_args_string.add(func_args_string199.tree)


                    else:
                        break #loop53

                # AST Rewrite
                # elements: func_args_string
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 352:10: -> ( func_args_string )+
                    # QueryParser.g:352:13: ( func_args_string )+
                    if not (stream_func_args_string.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_func_args_string.hasNext():
                        self._adaptor.addChild(root_0, stream_func_args_string.nextTree())


                    stream_func_args_string.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "func_args"

    class group_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.group_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "group_clause"
    # QueryParser.g:355:1: group_clause : ( GROUP | COGROUP ) group_item_list ( USING group_type )? ( partition_clause )? ;
    def group_clause(self, ):

        retval = self.group_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set200 = None
        USING202 = None
        group_item_list201 = None

        group_type203 = None

        partition_clause204 = None


        set200_tree = None
        USING202_tree = None

        try:
            try:
                # QueryParser.g:355:14: ( ( GROUP | COGROUP ) group_item_list ( USING group_type )? ( partition_clause )? )
                # QueryParser.g:355:16: ( GROUP | COGROUP ) group_item_list ( USING group_type )? ( partition_clause )?
                pass 
                root_0 = self._adaptor.nil()

                set200 = self.input.LT(1)
                set200 = self.input.LT(1)
                if self.input.LA(1) == COGROUP or self.input.LA(1) == GROUP:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set200), root_0)
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_group_item_list_in_group_clause2318)
                group_item_list201 = self.group_item_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, group_item_list201.tree)
                # QueryParser.g:355:53: ( USING group_type )?
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == USING) :
                    alt54 = 1
                if alt54 == 1:
                    # QueryParser.g:355:55: USING group_type
                    pass 
                    USING202=self.match(self.input, USING, self.FOLLOW_USING_in_group_clause2322)
                    self._state.following.append(self.FOLLOW_group_type_in_group_clause2325)
                    group_type203 = self.group_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, group_type203.tree)



                # QueryParser.g:355:76: ( partition_clause )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == PARTITION) :
                    alt55 = 1
                if alt55 == 1:
                    # QueryParser.g:0:0: partition_clause
                    pass 
                    self._state.following.append(self.FOLLOW_partition_clause_in_group_clause2330)
                    partition_clause204 = self.partition_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, partition_clause204.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "group_clause"

    class group_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.group_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "group_type"
    # QueryParser.g:358:1: group_type : QUOTEDSTRING ;
    def group_type(self, ):

        retval = self.group_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING205 = None

        QUOTEDSTRING205_tree = None

        try:
            try:
                # QueryParser.g:358:12: ( QUOTEDSTRING )
                # QueryParser.g:358:14: QUOTEDSTRING
                pass 
                root_0 = self._adaptor.nil()

                QUOTEDSTRING205=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_group_type2340)
                if self._state.backtracking == 0:

                    QUOTEDSTRING205_tree = self._adaptor.createWithPayload(QUOTEDSTRING205)
                    self._adaptor.addChild(root_0, QUOTEDSTRING205_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "group_type"

    class group_item_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.group_item_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "group_item_list"
    # QueryParser.g:361:1: group_item_list : group_item ( COMMA group_item )* -> ( group_item )+ ;
    def group_item_list(self, ):

        retval = self.group_item_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA207 = None
        group_item206 = None

        group_item208 = None


        COMMA207_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_group_item = RewriteRuleSubtreeStream(self._adaptor, "rule group_item")
        try:
            try:
                # QueryParser.g:361:17: ( group_item ( COMMA group_item )* -> ( group_item )+ )
                # QueryParser.g:361:19: group_item ( COMMA group_item )*
                pass 
                self._state.following.append(self.FOLLOW_group_item_in_group_item_list2349)
                group_item206 = self.group_item()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_group_item.add(group_item206.tree)
                # QueryParser.g:361:30: ( COMMA group_item )*
                while True: #loop56
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == COMMA) :
                        alt56 = 1


                    if alt56 == 1:
                        # QueryParser.g:361:32: COMMA group_item
                        pass 
                        COMMA207=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_group_item_list2353) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA207)
                        self._state.following.append(self.FOLLOW_group_item_in_group_item_list2355)
                        group_item208 = self.group_item()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_group_item.add(group_item208.tree)


                    else:
                        break #loop56

                # AST Rewrite
                # elements: group_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 362:16: -> ( group_item )+
                    # QueryParser.g:362:19: ( group_item )+
                    if not (stream_group_item.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_group_item.hasNext():
                        self._adaptor.addChild(root_0, stream_group_item.nextTree())


                    stream_group_item.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "group_item_list"

    class group_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.group_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "group_item"
    # QueryParser.g:365:1: group_item : rel ( join_group_by_clause | ALL | ANY ) ( INNER | OUTER )? ;
    def group_item(self, ):

        retval = self.group_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ALL211 = None
        ANY212 = None
        set213 = None
        rel209 = None

        join_group_by_clause210 = None


        ALL211_tree = None
        ANY212_tree = None
        set213_tree = None

        try:
            try:
                # QueryParser.g:365:12: ( rel ( join_group_by_clause | ALL | ANY ) ( INNER | OUTER )? )
                # QueryParser.g:365:14: rel ( join_group_by_clause | ALL | ANY ) ( INNER | OUTER )?
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_rel_in_group_item2387)
                rel209 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel209.tree)
                # QueryParser.g:365:18: ( join_group_by_clause | ALL | ANY )
                alt57 = 3
                LA57 = self.input.LA(1)
                if LA57 == BY:
                    alt57 = 1
                elif LA57 == ALL:
                    alt57 = 2
                elif LA57 == ANY:
                    alt57 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # QueryParser.g:365:20: join_group_by_clause
                    pass 
                    self._state.following.append(self.FOLLOW_join_group_by_clause_in_group_item2391)
                    join_group_by_clause210 = self.join_group_by_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_group_by_clause210.tree)


                elif alt57 == 2:
                    # QueryParser.g:365:43: ALL
                    pass 
                    ALL211=self.match(self.input, ALL, self.FOLLOW_ALL_in_group_item2395)
                    if self._state.backtracking == 0:

                        ALL211_tree = self._adaptor.createWithPayload(ALL211)
                        self._adaptor.addChild(root_0, ALL211_tree)



                elif alt57 == 3:
                    # QueryParser.g:365:49: ANY
                    pass 
                    ANY212=self.match(self.input, ANY, self.FOLLOW_ANY_in_group_item2399)
                    if self._state.backtracking == 0:

                        ANY212_tree = self._adaptor.createWithPayload(ANY212)
                        self._adaptor.addChild(root_0, ANY212_tree)




                # QueryParser.g:365:55: ( INNER | OUTER )?
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if ((INNER <= LA58_0 <= OUTER)) :
                    alt58 = 1
                if alt58 == 1:
                    # QueryParser.g:
                    pass 
                    set213 = self.input.LT(1)
                    if (INNER <= self.input.LA(1) <= OUTER):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set213))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse








                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "group_item"

    class rel_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel"
    # QueryParser.g:368:1: rel : ( alias | LEFT_PAREN ( foreach_clause_complex | ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? ) ) RIGHT_PAREN );
    def rel(self, ):

        retval = self.rel_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN215 = None
        RIGHT_PAREN220 = None
        alias214 = None

        foreach_clause_complex216 = None

        op_clause217 = None

        foreach_clause_simple218 = None

        parallel_clause219 = None


        LEFT_PAREN215_tree = None
        RIGHT_PAREN220_tree = None

        try:
            try:
                # QueryParser.g:368:5: ( alias | LEFT_PAREN ( foreach_clause_complex | ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? ) ) RIGHT_PAREN )
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == IDENTIFIER_L) :
                    alt62 = 1
                elif (LA62_0 == LEFT_PAREN) :
                    alt62 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 62, 0, self.input)

                    raise nvae

                if alt62 == 1:
                    # QueryParser.g:368:7: alias
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_alias_in_rel2421)
                    alias214 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, alias214.tree)


                elif alt62 == 2:
                    # QueryParser.g:369:7: LEFT_PAREN ( foreach_clause_complex | ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? ) ) RIGHT_PAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LEFT_PAREN215=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_rel2430)
                    # QueryParser.g:369:19: ( foreach_clause_complex | ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? ) )
                    alt61 = 2
                    alt61 = self.dfa61.predict(self.input)
                    if alt61 == 1:
                        # QueryParser.g:369:21: foreach_clause_complex
                        pass 
                        self._state.following.append(self.FOLLOW_foreach_clause_complex_in_rel2435)
                        foreach_clause_complex216 = self.foreach_clause_complex()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, foreach_clause_complex216.tree)


                    elif alt61 == 2:
                        # QueryParser.g:369:46: ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? )
                        pass 
                        # QueryParser.g:369:46: ( ( op_clause | foreach_clause_simple ) ( parallel_clause )? )
                        # QueryParser.g:369:48: ( op_clause | foreach_clause_simple ) ( parallel_clause )?
                        pass 
                        # QueryParser.g:369:48: ( op_clause | foreach_clause_simple )
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if ((DEFINE <= LA59_0 <= FILTER) or (ORDER <= LA59_0 <= RANK) or LA59_0 == CUBE or (DISTINCT <= LA59_0 <= UNION) or LA59_0 == GROUP or LA59_0 == STREAM or (STORE <= LA59_0 <= MAPREDUCE) or (LIMIT <= LA59_0 <= SAMPLE)) :
                            alt59 = 1
                        elif (LA59_0 == FOREACH) :
                            alt59 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            nvae = NoViableAltException("", 59, 0, self.input)

                            raise nvae

                        if alt59 == 1:
                            # QueryParser.g:369:50: op_clause
                            pass 
                            self._state.following.append(self.FOLLOW_op_clause_in_rel2443)
                            op_clause217 = self.op_clause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, op_clause217.tree)


                        elif alt59 == 2:
                            # QueryParser.g:369:62: foreach_clause_simple
                            pass 
                            self._state.following.append(self.FOLLOW_foreach_clause_simple_in_rel2447)
                            foreach_clause_simple218 = self.foreach_clause_simple()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, foreach_clause_simple218.tree)



                        # QueryParser.g:369:86: ( parallel_clause )?
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if (LA60_0 == PARALLEL) :
                            alt60 = 1
                        if alt60 == 1:
                            # QueryParser.g:0:0: parallel_clause
                            pass 
                            self._state.following.append(self.FOLLOW_parallel_clause_in_rel2451)
                            parallel_clause219 = self.parallel_clause()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, parallel_clause219.tree)









                    RIGHT_PAREN220=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_rel2458)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel"

    class flatten_generated_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.flatten_generated_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "flatten_generated_item"
    # QueryParser.g:372:1: flatten_generated_item : ( flatten_clause ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? | col_range ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? | expr ( AS field_def )? | STAR ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? );
    def flatten_generated_item(self, ):

        retval = self.flatten_generated_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AS222 = None
        LEFT_PAREN223 = None
        RIGHT_PAREN225 = None
        AS228 = None
        LEFT_PAREN229 = None
        RIGHT_PAREN231 = None
        AS234 = None
        STAR236 = None
        AS237 = None
        LEFT_PAREN238 = None
        RIGHT_PAREN240 = None
        flatten_clause221 = None

        field_def_list224 = None

        field_def226 = None

        col_range227 = None

        field_def_list230 = None

        field_def232 = None

        expr233 = None

        field_def235 = None

        field_def_list239 = None

        field_def241 = None


        AS222_tree = None
        LEFT_PAREN223_tree = None
        RIGHT_PAREN225_tree = None
        AS228_tree = None
        LEFT_PAREN229_tree = None
        RIGHT_PAREN231_tree = None
        AS234_tree = None
        STAR236_tree = None
        AS237_tree = None
        LEFT_PAREN238_tree = None
        RIGHT_PAREN240_tree = None

        try:
            try:
                # QueryParser.g:372:24: ( flatten_clause ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? | col_range ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? | expr ( AS field_def )? | STAR ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? )
                alt70 = 4
                alt70 = self.dfa70.predict(self.input)
                if alt70 == 1:
                    # QueryParser.g:372:26: flatten_clause ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_flatten_clause_in_flatten_generated_item2468)
                    flatten_clause221 = self.flatten_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, flatten_clause221.tree)
                    # QueryParser.g:372:41: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    alt64 = 2
                    LA64_0 = self.input.LA(1)

                    if (LA64_0 == AS) :
                        alt64 = 1
                    if alt64 == 1:
                        # QueryParser.g:372:43: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        pass 
                        AS222=self.match(self.input, AS, self.FOLLOW_AS_in_flatten_generated_item2472)
                        # QueryParser.g:372:47: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        alt63 = 2
                        alt63 = self.dfa63.predict(self.input)
                        if alt63 == 1:
                            # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            pass 
                            # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            # QueryParser.g:372:51: LEFT_PAREN field_def_list RIGHT_PAREN
                            pass 
                            LEFT_PAREN223=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_flatten_generated_item2479)
                            self._state.following.append(self.FOLLOW_field_def_list_in_flatten_generated_item2482)
                            field_def_list224 = self.field_def_list()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def_list224.tree)
                            RIGHT_PAREN225=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_flatten_generated_item2484)





                        elif alt63 == 2:
                            # QueryParser.g:372:95: field_def
                            pass 
                            self._state.following.append(self.FOLLOW_field_def_in_flatten_generated_item2491)
                            field_def226 = self.field_def()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def226.tree)








                elif alt70 == 2:
                    # QueryParser.g:373:26: col_range ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_flatten_generated_item2523)
                    col_range227 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range227.tree)
                    # QueryParser.g:373:36: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    alt66 = 2
                    LA66_0 = self.input.LA(1)

                    if (LA66_0 == AS) :
                        alt66 = 1
                    if alt66 == 1:
                        # QueryParser.g:373:38: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        pass 
                        AS228=self.match(self.input, AS, self.FOLLOW_AS_in_flatten_generated_item2527)
                        # QueryParser.g:373:42: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        alt65 = 2
                        alt65 = self.dfa65.predict(self.input)
                        if alt65 == 1:
                            # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            pass 
                            # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            # QueryParser.g:373:46: LEFT_PAREN field_def_list RIGHT_PAREN
                            pass 
                            LEFT_PAREN229=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_flatten_generated_item2534)
                            self._state.following.append(self.FOLLOW_field_def_list_in_flatten_generated_item2537)
                            field_def_list230 = self.field_def_list()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def_list230.tree)
                            RIGHT_PAREN231=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_flatten_generated_item2539)





                        elif alt65 == 2:
                            # QueryParser.g:373:90: field_def
                            pass 
                            self._state.following.append(self.FOLLOW_field_def_in_flatten_generated_item2546)
                            field_def232 = self.field_def()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def232.tree)








                elif alt70 == 3:
                    # QueryParser.g:374:26: expr ( AS field_def )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_flatten_generated_item2578)
                    expr233 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr233.tree)
                    # QueryParser.g:374:31: ( AS field_def )?
                    alt67 = 2
                    LA67_0 = self.input.LA(1)

                    if (LA67_0 == AS) :
                        alt67 = 1
                    if alt67 == 1:
                        # QueryParser.g:374:33: AS field_def
                        pass 
                        AS234=self.match(self.input, AS, self.FOLLOW_AS_in_flatten_generated_item2582)
                        self._state.following.append(self.FOLLOW_field_def_in_flatten_generated_item2585)
                        field_def235 = self.field_def()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, field_def235.tree)





                elif alt70 == 4:
                    # QueryParser.g:375:26: STAR ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR236=self.match(self.input, STAR, self.FOLLOW_STAR_in_flatten_generated_item2615)
                    if self._state.backtracking == 0:

                        STAR236_tree = self._adaptor.createWithPayload(STAR236)
                        self._adaptor.addChild(root_0, STAR236_tree)

                    # QueryParser.g:375:31: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
                    alt69 = 2
                    LA69_0 = self.input.LA(1)

                    if (LA69_0 == AS) :
                        alt69 = 1
                    if alt69 == 1:
                        # QueryParser.g:375:33: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        pass 
                        AS237=self.match(self.input, AS, self.FOLLOW_AS_in_flatten_generated_item2619)
                        # QueryParser.g:375:37: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
                        alt68 = 2
                        alt68 = self.dfa68.predict(self.input)
                        if alt68 == 1:
                            # QueryParser.g:375:39: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            pass 
                            # QueryParser.g:375:39: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                            # QueryParser.g:375:41: LEFT_PAREN field_def_list RIGHT_PAREN
                            pass 
                            LEFT_PAREN238=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_flatten_generated_item2626)
                            self._state.following.append(self.FOLLOW_field_def_list_in_flatten_generated_item2629)
                            field_def_list239 = self.field_def_list()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def_list239.tree)
                            RIGHT_PAREN240=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_flatten_generated_item2631)





                        elif alt68 == 2:
                            # QueryParser.g:375:85: field_def
                            pass 
                            self._state.following.append(self.FOLLOW_field_def_in_flatten_generated_item2638)
                            field_def241 = self.field_def()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, field_def241.tree)








                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "flatten_generated_item"

    class flatten_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.flatten_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "flatten_clause"
    # QueryParser.g:378:1: flatten_clause : FLATTEN LEFT_PAREN expr RIGHT_PAREN ;
    def flatten_clause(self, ):

        retval = self.flatten_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FLATTEN242 = None
        LEFT_PAREN243 = None
        RIGHT_PAREN245 = None
        expr244 = None


        FLATTEN242_tree = None
        LEFT_PAREN243_tree = None
        RIGHT_PAREN245_tree = None

        try:
            try:
                # QueryParser.g:378:16: ( FLATTEN LEFT_PAREN expr RIGHT_PAREN )
                # QueryParser.g:378:18: FLATTEN LEFT_PAREN expr RIGHT_PAREN
                pass 
                root_0 = self._adaptor.nil()

                FLATTEN242=self.match(self.input, FLATTEN, self.FOLLOW_FLATTEN_in_flatten_clause2653)
                if self._state.backtracking == 0:

                    FLATTEN242_tree = self._adaptor.createWithPayload(FLATTEN242)
                    root_0 = self._adaptor.becomeRoot(FLATTEN242_tree, root_0)

                LEFT_PAREN243=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_flatten_clause2656)
                self._state.following.append(self.FOLLOW_expr_in_flatten_clause2659)
                expr244 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr244.tree)
                RIGHT_PAREN245=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_flatten_clause2661)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "flatten_clause"

    class store_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.store_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "store_clause"
    # QueryParser.g:381:1: store_clause : STORE rel INTO filename ( USING func_clause )? ;
    def store_clause(self, ):

        retval = self.store_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STORE246 = None
        INTO248 = None
        USING250 = None
        rel247 = None

        filename249 = None

        func_clause251 = None


        STORE246_tree = None
        INTO248_tree = None
        USING250_tree = None

        try:
            try:
                # QueryParser.g:381:14: ( STORE rel INTO filename ( USING func_clause )? )
                # QueryParser.g:381:16: STORE rel INTO filename ( USING func_clause )?
                pass 
                root_0 = self._adaptor.nil()

                STORE246=self.match(self.input, STORE, self.FOLLOW_STORE_in_store_clause2671)
                if self._state.backtracking == 0:

                    STORE246_tree = self._adaptor.createWithPayload(STORE246)
                    root_0 = self._adaptor.becomeRoot(STORE246_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_store_clause2674)
                rel247 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel247.tree)
                INTO248=self.match(self.input, INTO, self.FOLLOW_INTO_in_store_clause2676)
                self._state.following.append(self.FOLLOW_filename_in_store_clause2679)
                filename249 = self.filename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, filename249.tree)
                # QueryParser.g:381:42: ( USING func_clause )?
                alt71 = 2
                LA71_0 = self.input.LA(1)

                if (LA71_0 == USING) :
                    alt71 = 1
                if alt71 == 1:
                    # QueryParser.g:381:44: USING func_clause
                    pass 
                    USING250=self.match(self.input, USING, self.FOLLOW_USING_in_store_clause2683)
                    self._state.following.append(self.FOLLOW_func_clause_in_store_clause2686)
                    func_clause251 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause251.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "store_clause"

    class filter_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.filter_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "filter_clause"
    # QueryParser.g:384:1: filter_clause : FILTER rel BY cond ;
    def filter_clause(self, ):

        retval = self.filter_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FILTER252 = None
        BY254 = None
        rel253 = None

        cond255 = None


        FILTER252_tree = None
        BY254_tree = None

        try:
            try:
                # QueryParser.g:384:15: ( FILTER rel BY cond )
                # QueryParser.g:384:17: FILTER rel BY cond
                pass 
                root_0 = self._adaptor.nil()

                FILTER252=self.match(self.input, FILTER, self.FOLLOW_FILTER_in_filter_clause2698)
                if self._state.backtracking == 0:

                    FILTER252_tree = self._adaptor.createWithPayload(FILTER252)
                    root_0 = self._adaptor.becomeRoot(FILTER252_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_filter_clause2701)
                rel253 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel253.tree)
                BY254=self.match(self.input, BY, self.FOLLOW_BY_in_filter_clause2703)
                self._state.following.append(self.FOLLOW_cond_in_filter_clause2706)
                cond255 = self.cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cond255.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "filter_clause"

    class cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "cond"
    # QueryParser.g:387:1: cond : or_cond ;
    def cond(self, ):

        retval = self.cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        or_cond256 = None



        try:
            try:
                # QueryParser.g:387:6: ( or_cond )
                # QueryParser.g:387:8: or_cond
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_or_cond_in_cond2715)
                or_cond256 = self.or_cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_cond256.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cond"

    class or_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.or_cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "or_cond"
    # QueryParser.g:390:1: or_cond : and_cond ( OR and_cond )* ;
    def or_cond(self, ):

        retval = self.or_cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR258 = None
        and_cond257 = None

        and_cond259 = None


        OR258_tree = None

        try:
            try:
                # QueryParser.g:390:9: ( and_cond ( OR and_cond )* )
                # QueryParser.g:390:11: and_cond ( OR and_cond )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_cond_in_or_cond2724)
                and_cond257 = self.and_cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_cond257.tree)
                # QueryParser.g:390:21: ( OR and_cond )*
                while True: #loop72
                    alt72 = 2
                    LA72_0 = self.input.LA(1)

                    if (LA72_0 == OR) :
                        alt72 = 1


                    if alt72 == 1:
                        # QueryParser.g:390:23: OR and_cond
                        pass 
                        OR258=self.match(self.input, OR, self.FOLLOW_OR_in_or_cond2729)
                        if self._state.backtracking == 0:

                            OR258_tree = self._adaptor.createWithPayload(OR258)
                            root_0 = self._adaptor.becomeRoot(OR258_tree, root_0)

                        self._state.following.append(self.FOLLOW_and_cond_in_or_cond2732)
                        and_cond259 = self.and_cond()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, and_cond259.tree)


                    else:
                        break #loop72



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "or_cond"

    class and_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.and_cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_cond"
    # QueryParser.g:393:1: and_cond : unary_cond ( AND unary_cond )* ;
    def and_cond(self, ):

        retval = self.and_cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND261 = None
        unary_cond260 = None

        unary_cond262 = None


        AND261_tree = None

        try:
            try:
                # QueryParser.g:393:10: ( unary_cond ( AND unary_cond )* )
                # QueryParser.g:393:12: unary_cond ( AND unary_cond )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_unary_cond_in_and_cond2744)
                unary_cond260 = self.unary_cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unary_cond260.tree)
                # QueryParser.g:393:23: ( AND unary_cond )*
                while True: #loop73
                    alt73 = 2
                    LA73_0 = self.input.LA(1)

                    if (LA73_0 == AND) :
                        alt73 = 1


                    if alt73 == 1:
                        # QueryParser.g:393:25: AND unary_cond
                        pass 
                        AND261=self.match(self.input, AND, self.FOLLOW_AND_in_and_cond2748)
                        if self._state.backtracking == 0:

                            AND261_tree = self._adaptor.createWithPayload(AND261)
                            root_0 = self._adaptor.becomeRoot(AND261_tree, root_0)

                        self._state.following.append(self.FOLLOW_unary_cond_in_and_cond2751)
                        unary_cond262 = self.unary_cond()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, unary_cond262.tree)


                    else:
                        break #loop73



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "and_cond"

    class unary_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.unary_cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "unary_cond"
    # QueryParser.g:396:1: unary_cond : ( LEFT_PAREN cond RIGHT_PAREN | not_cond | expr rel_op expr | func_eval | null_check_cond );
    def unary_cond(self, ):

        retval = self.unary_cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN263 = None
        RIGHT_PAREN265 = None
        cond264 = None

        not_cond266 = None

        expr267 = None

        rel_op268 = None

        expr269 = None

        func_eval270 = None

        null_check_cond271 = None


        LEFT_PAREN263_tree = None
        RIGHT_PAREN265_tree = None

        try:
            try:
                # QueryParser.g:396:12: ( LEFT_PAREN cond RIGHT_PAREN | not_cond | expr rel_op expr | func_eval | null_check_cond )
                alt74 = 5
                alt74 = self.dfa74.predict(self.input)
                if alt74 == 1:
                    # QueryParser.g:396:14: LEFT_PAREN cond RIGHT_PAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LEFT_PAREN263=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_unary_cond2763)
                    self._state.following.append(self.FOLLOW_cond_in_unary_cond2766)
                    cond264 = self.cond()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, cond264.tree)
                    RIGHT_PAREN265=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_unary_cond2768)


                elif alt74 == 2:
                    # QueryParser.g:397:14: not_cond
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_not_cond_in_unary_cond2784)
                    not_cond266 = self.not_cond()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, not_cond266.tree)


                elif alt74 == 3:
                    # QueryParser.g:398:14: expr rel_op expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_unary_cond2799)
                    expr267 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr267.tree)
                    self._state.following.append(self.FOLLOW_rel_op_in_unary_cond2801)
                    rel_op268 = self.rel_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(rel_op268.tree, root_0)
                    self._state.following.append(self.FOLLOW_expr_in_unary_cond2804)
                    expr269 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr269.tree)


                elif alt74 == 4:
                    # QueryParser.g:399:14: func_eval
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_func_eval_in_unary_cond2819)
                    func_eval270 = self.func_eval()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_eval270.tree)


                elif alt74 == 5:
                    # QueryParser.g:400:14: null_check_cond
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_null_check_cond_in_unary_cond2834)
                    null_check_cond271 = self.null_check_cond()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, null_check_cond271.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "unary_cond"

    class not_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.not_cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "not_cond"
    # QueryParser.g:403:1: not_cond : NOT unary_cond ;
    def not_cond(self, ):

        retval = self.not_cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        NOT272 = None
        unary_cond273 = None


        NOT272_tree = None

        try:
            try:
                # QueryParser.g:403:10: ( NOT unary_cond )
                # QueryParser.g:403:12: NOT unary_cond
                pass 
                root_0 = self._adaptor.nil()

                NOT272=self.match(self.input, NOT, self.FOLLOW_NOT_in_not_cond2843)
                if self._state.backtracking == 0:

                    NOT272_tree = self._adaptor.createWithPayload(NOT272)
                    root_0 = self._adaptor.becomeRoot(NOT272_tree, root_0)

                self._state.following.append(self.FOLLOW_unary_cond_in_not_cond2846)
                unary_cond273 = self.unary_cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, unary_cond273.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "not_cond"

    class func_eval_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.func_eval_return, self).__init__()

            self.tree = None




    # $ANTLR start "func_eval"
    # QueryParser.g:406:1: func_eval : func_name LEFT_PAREN ( real_arg_list )? RIGHT_PAREN -> ^( FUNC_EVAL func_name ( real_arg_list )? ) ;
    def func_eval(self, ):

        retval = self.func_eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN275 = None
        RIGHT_PAREN277 = None
        func_name274 = None

        real_arg_list276 = None


        LEFT_PAREN275_tree = None
        RIGHT_PAREN277_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_real_arg_list = RewriteRuleSubtreeStream(self._adaptor, "rule real_arg_list")
        stream_func_name = RewriteRuleSubtreeStream(self._adaptor, "rule func_name")
        try:
            try:
                # QueryParser.g:406:11: ( func_name LEFT_PAREN ( real_arg_list )? RIGHT_PAREN -> ^( FUNC_EVAL func_name ( real_arg_list )? ) )
                # QueryParser.g:406:13: func_name LEFT_PAREN ( real_arg_list )? RIGHT_PAREN
                pass 
                self._state.following.append(self.FOLLOW_func_name_in_func_eval2855)
                func_name274 = self.func_name()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_func_name.add(func_name274.tree)
                LEFT_PAREN275=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_func_eval2857) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN275)
                # QueryParser.g:406:34: ( real_arg_list )?
                alt75 = 2
                LA75_0 = self.input.LA(1)

                if ((IMPORT <= LA75_0 <= ORDER) or (CUBE <= LA75_0 <= IF) or (ALL <= LA75_0 <= OUTER) or (PARALLEL <= LA75_0 <= DESC) or (INT <= LA75_0 <= FALSE) or (IDENTIFIER_L <= LA75_0 <= INTEGER) or LA75_0 == LONGINTEGER or (DOLLARVAR <= LA75_0 <= MINUS) or (DOUBLENUMBER <= LA75_0 <= QUOTEDSTRING) or LA75_0 == STAR or LA75_0 == LEFT_PAREN or LA75_0 == LEFT_CURLY or LA75_0 == LEFT_BRACKET or LA75_0 == DOUBLE_PERIOD or (BOOL <= LA75_0 <= REALIAS)) :
                    alt75 = 1
                if alt75 == 1:
                    # QueryParser.g:0:0: real_arg_list
                    pass 
                    self._state.following.append(self.FOLLOW_real_arg_list_in_func_eval2859)
                    real_arg_list276 = self.real_arg_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_real_arg_list.add(real_arg_list276.tree)



                RIGHT_PAREN277=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_func_eval2862) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN277)

                # AST Rewrite
                # elements: func_name, real_arg_list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 407:11: -> ^( FUNC_EVAL func_name ( real_arg_list )? )
                    # QueryParser.g:407:14: ^( FUNC_EVAL func_name ( real_arg_list )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_EVAL, "FUNC_EVAL"), root_1)

                    self._adaptor.addChild(root_1, stream_func_name.nextTree())
                    # QueryParser.g:407:37: ( real_arg_list )?
                    if stream_real_arg_list.hasNext():
                        self._adaptor.addChild(root_1, stream_real_arg_list.nextTree())


                    stream_real_arg_list.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "func_eval"

    class real_arg_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.real_arg_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "real_arg_list"
    # QueryParser.g:410:1: real_arg_list : real_arg ( COMMA real_arg )* -> ( real_arg )+ ;
    def real_arg_list(self, ):

        retval = self.real_arg_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA279 = None
        real_arg278 = None

        real_arg280 = None


        COMMA279_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_real_arg = RewriteRuleSubtreeStream(self._adaptor, "rule real_arg")
        try:
            try:
                # QueryParser.g:410:15: ( real_arg ( COMMA real_arg )* -> ( real_arg )+ )
                # QueryParser.g:410:17: real_arg ( COMMA real_arg )*
                pass 
                self._state.following.append(self.FOLLOW_real_arg_in_real_arg_list2894)
                real_arg278 = self.real_arg()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_real_arg.add(real_arg278.tree)
                # QueryParser.g:410:26: ( COMMA real_arg )*
                while True: #loop76
                    alt76 = 2
                    LA76_0 = self.input.LA(1)

                    if (LA76_0 == COMMA) :
                        alt76 = 1


                    if alt76 == 1:
                        # QueryParser.g:410:28: COMMA real_arg
                        pass 
                        COMMA279=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_real_arg_list2898) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA279)
                        self._state.following.append(self.FOLLOW_real_arg_in_real_arg_list2900)
                        real_arg280 = self.real_arg()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_real_arg.add(real_arg280.tree)


                    else:
                        break #loop76

                # AST Rewrite
                # elements: real_arg
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 411:14: -> ( real_arg )+
                    # QueryParser.g:411:17: ( real_arg )+
                    if not (stream_real_arg.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_real_arg.hasNext():
                        self._adaptor.addChild(root_0, stream_real_arg.nextTree())


                    stream_real_arg.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "real_arg_list"

    class real_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.real_arg_return, self).__init__()

            self.tree = None




    # $ANTLR start "real_arg"
    # QueryParser.g:414:1: real_arg : ( expr | STAR | col_range );
    def real_arg(self, ):

        retval = self.real_arg_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STAR282 = None
        expr281 = None

        col_range283 = None


        STAR282_tree = None

        try:
            try:
                # QueryParser.g:414:10: ( expr | STAR | col_range )
                alt77 = 3
                LA77 = self.input.LA(1)
                if LA77 == IMPORT or LA77 == RETURNS or LA77 == DEFINE or LA77 == LOAD or LA77 == FILTER or LA77 == FOREACH or LA77 == ORDER or LA77 == ROLLUP or LA77 == DISTINCT or LA77 == COGROUP or LA77 == JOIN or LA77 == CROSS or LA77 == UNION or LA77 == SPLIT or LA77 == INTO or LA77 == IF or LA77 == ALL or LA77 == AS or LA77 == BY or LA77 == USING or LA77 == INNER or LA77 == OUTER or LA77 == PARALLEL or LA77 == PARTITION or LA77 == AND or LA77 == OR or LA77 == NOT or LA77 == GENERATE or LA77 == FLATTEN or LA77 == ASC or LA77 == DESC or LA77 == INT or LA77 == LONG or LA77 == FLOAT or LA77 == DOUBLE or LA77 == DATETIME or LA77 == CHARARRAY or LA77 == BYTEARRAY or LA77 == BAG or LA77 == TUPLE or LA77 == MAP or LA77 == IS or LA77 == STREAM or LA77 == THROUGH or LA77 == STORE or LA77 == MAPREDUCE or LA77 == SHIP or LA77 == CACHE or LA77 == INPUT or LA77 == OUTPUT or LA77 == STDERROR or LA77 == STDIN or LA77 == STDOUT or LA77 == LIMIT or LA77 == SAMPLE or LA77 == LEFT or LA77 == RIGHT or LA77 == FULL or LA77 == STR_OP_EQ or LA77 == STR_OP_GT or LA77 == STR_OP_LT or LA77 == STR_OP_GTE or LA77 == STR_OP_LTE or LA77 == STR_OP_NE or LA77 == STR_OP_MATCHES or LA77 == TRUE or LA77 == FALSE or LA77 == INTEGER or LA77 == LONGINTEGER or LA77 == MINUS or LA77 == DOUBLENUMBER or LA77 == FLOATNUMBER or LA77 == QUOTEDSTRING or LA77 == LEFT_PAREN or LA77 == LEFT_CURLY or LA77 == LEFT_BRACKET or LA77 == BOOL or LA77 == REALIAS:
                    alt77 = 1
                elif LA77 == IDENTIFIER_L:
                    LA77_2 = self.input.LA(2)

                    if (LA77_2 == EOF or LA77_2 == PERIOD or LA77_2 == DOLLAR or (MINUS <= LA77_2 <= PLUS) or LA77_2 == STAR or (LEFT_PAREN <= LA77_2 <= RIGHT_PAREN) or LA77_2 == RIGHT_CURLY or (RIGHT_BRACKET <= LA77_2 <= POUND) or LA77_2 == COMMA or (DIV <= LA77_2 <= PERCENT)) :
                        alt77 = 1
                    elif (LA77_2 == DOUBLE_PERIOD) :
                        alt77 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 77, 2, self.input)

                        raise nvae

                elif LA77 == CUBE:
                    LA77_3 = self.input.LA(2)

                    if (LA77_3 == EOF or LA77_3 == PERIOD or LA77_3 == DOLLAR or (MINUS <= LA77_3 <= PLUS) or LA77_3 == STAR or (LEFT_PAREN <= LA77_3 <= RIGHT_PAREN) or LA77_3 == RIGHT_CURLY or (RIGHT_BRACKET <= LA77_3 <= POUND) or LA77_3 == COMMA or (DIV <= LA77_3 <= PERCENT)) :
                        alt77 = 1
                    elif (LA77_3 == DOUBLE_PERIOD) :
                        alt77 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 77, 3, self.input)

                        raise nvae

                elif LA77 == GROUP:
                    LA77_4 = self.input.LA(2)

                    if (LA77_4 == EOF or LA77_4 == PERIOD or LA77_4 == DOLLAR or (MINUS <= LA77_4 <= PLUS) or LA77_4 == STAR or (LEFT_PAREN <= LA77_4 <= RIGHT_PAREN) or LA77_4 == RIGHT_CURLY or (RIGHT_BRACKET <= LA77_4 <= POUND) or LA77_4 == COMMA or (DIV <= LA77_4 <= PERCENT)) :
                        alt77 = 1
                    elif (LA77_4 == DOUBLE_PERIOD) :
                        alt77 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 77, 4, self.input)

                        raise nvae

                elif LA77 == DOLLARVAR:
                    LA77_5 = self.input.LA(2)

                    if (LA77_5 == EOF or LA77_5 == PERIOD or (MINUS <= LA77_5 <= PLUS) or LA77_5 == STAR or LA77_5 == RIGHT_PAREN or LA77_5 == RIGHT_CURLY or (RIGHT_BRACKET <= LA77_5 <= POUND) or LA77_5 == COMMA or (DIV <= LA77_5 <= PERCENT)) :
                        alt77 = 1
                    elif (LA77_5 == DOUBLE_PERIOD) :
                        alt77 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 77, 5, self.input)

                        raise nvae

                elif LA77 == STAR:
                    alt77 = 2
                elif LA77 == DOUBLE_PERIOD:
                    alt77 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 77, 0, self.input)

                    raise nvae

                if alt77 == 1:
                    # QueryParser.g:414:12: expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_real_arg2930)
                    expr281 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr281.tree)


                elif alt77 == 2:
                    # QueryParser.g:414:19: STAR
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR282=self.match(self.input, STAR, self.FOLLOW_STAR_in_real_arg2934)
                    if self._state.backtracking == 0:

                        STAR282_tree = self._adaptor.createWithPayload(STAR282)
                        self._adaptor.addChild(root_0, STAR282_tree)



                elif alt77 == 3:
                    # QueryParser.g:414:26: col_range
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_real_arg2938)
                    col_range283 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range283.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "real_arg"

    class null_check_cond_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.null_check_cond_return, self).__init__()

            self.tree = None




    # $ANTLR start "null_check_cond"
    # QueryParser.g:417:1: null_check_cond : expr IS ( NOT )? null_keyword ;
    def null_check_cond(self, ):

        retval = self.null_check_cond_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IS285 = None
        NOT286 = None
        expr284 = None

        null_keyword287 = None


        IS285_tree = None
        NOT286_tree = None

        try:
            try:
                # QueryParser.g:417:17: ( expr IS ( NOT )? null_keyword )
                # QueryParser.g:417:19: expr IS ( NOT )? null_keyword
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_expr_in_null_check_cond2947)
                expr284 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, expr284.tree)
                IS285=self.match(self.input, IS, self.FOLLOW_IS_in_null_check_cond2949)
                # QueryParser.g:417:28: ( NOT )?
                alt78 = 2
                LA78_0 = self.input.LA(1)

                if (LA78_0 == NOT) :
                    alt78 = 1
                if alt78 == 1:
                    # QueryParser.g:0:0: NOT
                    pass 
                    NOT286=self.match(self.input, NOT, self.FOLLOW_NOT_in_null_check_cond2952)
                    if self._state.backtracking == 0:

                        NOT286_tree = self._adaptor.createWithPayload(NOT286)
                        self._adaptor.addChild(root_0, NOT286_tree)




                self._state.following.append(self.FOLLOW_null_keyword_in_null_check_cond2955)
                null_keyword287 = self.null_keyword()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    root_0 = self._adaptor.becomeRoot(null_keyword287.tree, root_0)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "null_check_cond"

    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr"
    # QueryParser.g:420:1: expr : add_expr ;
    def expr(self, ):

        retval = self.expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        add_expr288 = None



        try:
            try:
                # QueryParser.g:420:6: ( add_expr )
                # QueryParser.g:420:8: add_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_add_expr_in_expr2965)
                add_expr288 = self.add_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, add_expr288.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "expr"

    class add_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.add_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "add_expr"
    # QueryParser.g:423:1: add_expr : multi_expr ( ( PLUS | MINUS ) multi_expr )* ;
    def add_expr(self, ):

        retval = self.add_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set290 = None
        multi_expr289 = None

        multi_expr291 = None


        set290_tree = None

        try:
            try:
                # QueryParser.g:423:10: ( multi_expr ( ( PLUS | MINUS ) multi_expr )* )
                # QueryParser.g:423:12: multi_expr ( ( PLUS | MINUS ) multi_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_multi_expr_in_add_expr2974)
                multi_expr289 = self.multi_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, multi_expr289.tree)
                # QueryParser.g:423:23: ( ( PLUS | MINUS ) multi_expr )*
                while True: #loop79
                    alt79 = 2
                    LA79_0 = self.input.LA(1)

                    if ((MINUS <= LA79_0 <= PLUS)) :
                        alt79 = 1


                    if alt79 == 1:
                        # QueryParser.g:423:25: ( PLUS | MINUS ) multi_expr
                        pass 
                        set290 = self.input.LT(1)
                        set290 = self.input.LT(1)
                        if (MINUS <= self.input.LA(1) <= PLUS):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set290), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_multi_expr_in_add_expr2989)
                        multi_expr291 = self.multi_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, multi_expr291.tree)


                    else:
                        break #loop79



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "add_expr"

    class multi_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.multi_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "multi_expr"
    # QueryParser.g:426:1: multi_expr : cast_expr ( ( STAR | DIV | PERCENT ) cast_expr )* ;
    def multi_expr(self, ):

        retval = self.multi_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set293 = None
        cast_expr292 = None

        cast_expr294 = None


        set293_tree = None

        try:
            try:
                # QueryParser.g:426:12: ( cast_expr ( ( STAR | DIV | PERCENT ) cast_expr )* )
                # QueryParser.g:426:14: cast_expr ( ( STAR | DIV | PERCENT ) cast_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_cast_expr_in_multi_expr3001)
                cast_expr292 = self.cast_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cast_expr292.tree)
                # QueryParser.g:426:24: ( ( STAR | DIV | PERCENT ) cast_expr )*
                while True: #loop80
                    alt80 = 2
                    LA80_0 = self.input.LA(1)

                    if (LA80_0 == STAR or (DIV <= LA80_0 <= PERCENT)) :
                        alt80 = 1


                    if alt80 == 1:
                        # QueryParser.g:426:26: ( STAR | DIV | PERCENT ) cast_expr
                        pass 
                        set293 = self.input.LT(1)
                        set293 = self.input.LT(1)
                        if self.input.LA(1) == STAR or (DIV <= self.input.LA(1) <= PERCENT):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set293), root_0)
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse


                        self._state.following.append(self.FOLLOW_cast_expr_in_multi_expr3020)
                        cast_expr294 = self.cast_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, cast_expr294.tree)


                    else:
                        break #loop80



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "multi_expr"

    class cast_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cast_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "cast_expr"
    # QueryParser.g:429:1: cast_expr : ( LEFT_PAREN type_cast RIGHT_PAREN unary_expr -> ^( CAST_EXPR type_cast unary_expr ) | unary_expr );
    def cast_expr(self, ):

        retval = self.cast_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN295 = None
        RIGHT_PAREN297 = None
        type_cast296 = None

        unary_expr298 = None

        unary_expr299 = None


        LEFT_PAREN295_tree = None
        RIGHT_PAREN297_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_unary_expr = RewriteRuleSubtreeStream(self._adaptor, "rule unary_expr")
        stream_type_cast = RewriteRuleSubtreeStream(self._adaptor, "rule type_cast")
        try:
            try:
                # QueryParser.g:429:11: ( LEFT_PAREN type_cast RIGHT_PAREN unary_expr -> ^( CAST_EXPR type_cast unary_expr ) | unary_expr )
                alt81 = 2
                alt81 = self.dfa81.predict(self.input)
                if alt81 == 1:
                    # QueryParser.g:429:13: LEFT_PAREN type_cast RIGHT_PAREN unary_expr
                    pass 
                    LEFT_PAREN295=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_cast_expr3032) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN295)
                    self._state.following.append(self.FOLLOW_type_cast_in_cast_expr3034)
                    type_cast296 = self.type_cast()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type_cast.add(type_cast296.tree)
                    RIGHT_PAREN297=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_cast_expr3036) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN297)
                    self._state.following.append(self.FOLLOW_unary_expr_in_cast_expr3038)
                    unary_expr298 = self.unary_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_unary_expr.add(unary_expr298.tree)

                    # AST Rewrite
                    # elements: type_cast, unary_expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 430:10: -> ^( CAST_EXPR type_cast unary_expr )
                        # QueryParser.g:430:13: ^( CAST_EXPR type_cast unary_expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(CAST_EXPR, "CAST_EXPR"), root_1)

                        self._adaptor.addChild(root_1, stream_type_cast.nextTree())
                        self._adaptor.addChild(root_1, stream_unary_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt81 == 2:
                    # QueryParser.g:431:13: unary_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_unary_expr_in_cast_expr3073)
                    unary_expr299 = self.unary_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, unary_expr299.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cast_expr"

    class type_cast_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.type_cast_return, self).__init__()

            self.tree = None




    # $ANTLR start "type_cast"
    # QueryParser.g:434:1: type_cast : ( simple_type | map_type | tuple_type_cast | bag_type_cast );
    def type_cast(self, ):

        retval = self.type_cast_return()
        retval.start = self.input.LT(1)

        root_0 = None

        simple_type300 = None

        map_type301 = None

        tuple_type_cast302 = None

        bag_type_cast303 = None



        try:
            try:
                # QueryParser.g:434:11: ( simple_type | map_type | tuple_type_cast | bag_type_cast )
                alt82 = 4
                LA82 = self.input.LA(1)
                if LA82 == BOOLEAN or LA82 == INT or LA82 == LONG or LA82 == FLOAT or LA82 == DOUBLE or LA82 == DATETIME or LA82 == CHARARRAY or LA82 == BYTEARRAY:
                    alt82 = 1
                elif LA82 == MAP or LA82 == LEFT_BRACKET:
                    alt82 = 2
                elif LA82 == TUPLE:
                    alt82 = 3
                elif LA82 == BAG:
                    alt82 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 82, 0, self.input)

                    raise nvae

                if alt82 == 1:
                    # QueryParser.g:434:13: simple_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_simple_type_in_type_cast3082)
                    simple_type300 = self.simple_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simple_type300.tree)


                elif alt82 == 2:
                    # QueryParser.g:434:27: map_type
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_map_type_in_type_cast3086)
                    map_type301 = self.map_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, map_type301.tree)


                elif alt82 == 3:
                    # QueryParser.g:434:38: tuple_type_cast
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_tuple_type_cast_in_type_cast3090)
                    tuple_type_cast302 = self.tuple_type_cast()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple_type_cast302.tree)


                elif alt82 == 4:
                    # QueryParser.g:434:56: bag_type_cast
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_bag_type_cast_in_type_cast3094)
                    bag_type_cast303 = self.bag_type_cast()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bag_type_cast303.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "type_cast"

    class tuple_type_cast_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.tuple_type_cast_return, self).__init__()

            self.tree = None




    # $ANTLR start "tuple_type_cast"
    # QueryParser.g:437:1: tuple_type_cast : TUPLE LEFT_PAREN ( type_cast ( COMMA type_cast )* )? RIGHT_PAREN -> ^( TUPLE_TYPE_CAST ( type_cast )* ) ;
    def tuple_type_cast(self, ):

        retval = self.tuple_type_cast_return()
        retval.start = self.input.LT(1)

        root_0 = None

        TUPLE304 = None
        LEFT_PAREN305 = None
        COMMA307 = None
        RIGHT_PAREN309 = None
        type_cast306 = None

        type_cast308 = None


        TUPLE304_tree = None
        LEFT_PAREN305_tree = None
        COMMA307_tree = None
        RIGHT_PAREN309_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_TUPLE = RewriteRuleTokenStream(self._adaptor, "token TUPLE")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_type_cast = RewriteRuleSubtreeStream(self._adaptor, "rule type_cast")
        try:
            try:
                # QueryParser.g:437:17: ( TUPLE LEFT_PAREN ( type_cast ( COMMA type_cast )* )? RIGHT_PAREN -> ^( TUPLE_TYPE_CAST ( type_cast )* ) )
                # QueryParser.g:437:19: TUPLE LEFT_PAREN ( type_cast ( COMMA type_cast )* )? RIGHT_PAREN
                pass 
                TUPLE304=self.match(self.input, TUPLE, self.FOLLOW_TUPLE_in_tuple_type_cast3103) 
                if self._state.backtracking == 0:
                    stream_TUPLE.add(TUPLE304)
                LEFT_PAREN305=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_tuple_type_cast3105) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN305)
                # QueryParser.g:437:36: ( type_cast ( COMMA type_cast )* )?
                alt84 = 2
                LA84_0 = self.input.LA(1)

                if ((BOOLEAN <= LA84_0 <= MAP) or LA84_0 == LEFT_BRACKET) :
                    alt84 = 1
                if alt84 == 1:
                    # QueryParser.g:437:38: type_cast ( COMMA type_cast )*
                    pass 
                    self._state.following.append(self.FOLLOW_type_cast_in_tuple_type_cast3109)
                    type_cast306 = self.type_cast()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_type_cast.add(type_cast306.tree)
                    # QueryParser.g:437:48: ( COMMA type_cast )*
                    while True: #loop83
                        alt83 = 2
                        LA83_0 = self.input.LA(1)

                        if (LA83_0 == COMMA) :
                            alt83 = 1


                        if alt83 == 1:
                            # QueryParser.g:437:50: COMMA type_cast
                            pass 
                            COMMA307=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple_type_cast3113) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA307)
                            self._state.following.append(self.FOLLOW_type_cast_in_tuple_type_cast3115)
                            type_cast308 = self.type_cast()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_type_cast.add(type_cast308.tree)


                        else:
                            break #loop83



                RIGHT_PAREN309=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_tuple_type_cast3123) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN309)

                # AST Rewrite
                # elements: type_cast
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 438:16: -> ^( TUPLE_TYPE_CAST ( type_cast )* )
                    # QueryParser.g:438:19: ^( TUPLE_TYPE_CAST ( type_cast )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TUPLE_TYPE_CAST, "TUPLE_TYPE_CAST"), root_1)

                    # QueryParser.g:438:38: ( type_cast )*
                    while stream_type_cast.hasNext():
                        self._adaptor.addChild(root_1, stream_type_cast.nextTree())


                    stream_type_cast.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "tuple_type_cast"

    class bag_type_cast_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.bag_type_cast_return, self).__init__()

            self.tree = None




    # $ANTLR start "bag_type_cast"
    # QueryParser.g:441:1: bag_type_cast : BAG LEFT_CURLY ( tuple_type_cast )? RIGHT_CURLY -> ^( BAG_TYPE_CAST ( tuple_type_cast )? ) ;
    def bag_type_cast(self, ):

        retval = self.bag_type_cast_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BAG310 = None
        LEFT_CURLY311 = None
        RIGHT_CURLY313 = None
        tuple_type_cast312 = None


        BAG310_tree = None
        LEFT_CURLY311_tree = None
        RIGHT_CURLY313_tree = None
        stream_BAG = RewriteRuleTokenStream(self._adaptor, "token BAG")
        stream_RIGHT_CURLY = RewriteRuleTokenStream(self._adaptor, "token RIGHT_CURLY")
        stream_LEFT_CURLY = RewriteRuleTokenStream(self._adaptor, "token LEFT_CURLY")
        stream_tuple_type_cast = RewriteRuleSubtreeStream(self._adaptor, "rule tuple_type_cast")
        try:
            try:
                # QueryParser.g:441:15: ( BAG LEFT_CURLY ( tuple_type_cast )? RIGHT_CURLY -> ^( BAG_TYPE_CAST ( tuple_type_cast )? ) )
                # QueryParser.g:441:17: BAG LEFT_CURLY ( tuple_type_cast )? RIGHT_CURLY
                pass 
                BAG310=self.match(self.input, BAG, self.FOLLOW_BAG_in_bag_type_cast3158) 
                if self._state.backtracking == 0:
                    stream_BAG.add(BAG310)
                LEFT_CURLY311=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_bag_type_cast3160) 
                if self._state.backtracking == 0:
                    stream_LEFT_CURLY.add(LEFT_CURLY311)
                # QueryParser.g:441:32: ( tuple_type_cast )?
                alt85 = 2
                LA85_0 = self.input.LA(1)

                if (LA85_0 == TUPLE) :
                    alt85 = 1
                if alt85 == 1:
                    # QueryParser.g:0:0: tuple_type_cast
                    pass 
                    self._state.following.append(self.FOLLOW_tuple_type_cast_in_bag_type_cast3162)
                    tuple_type_cast312 = self.tuple_type_cast()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_tuple_type_cast.add(tuple_type_cast312.tree)



                RIGHT_CURLY313=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_bag_type_cast3165) 
                if self._state.backtracking == 0:
                    stream_RIGHT_CURLY.add(RIGHT_CURLY313)

                # AST Rewrite
                # elements: tuple_type_cast
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 442:14: -> ^( BAG_TYPE_CAST ( tuple_type_cast )? )
                    # QueryParser.g:442:17: ^( BAG_TYPE_CAST ( tuple_type_cast )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BAG_TYPE_CAST, "BAG_TYPE_CAST"), root_1)

                    # QueryParser.g:442:34: ( tuple_type_cast )?
                    if stream_tuple_type_cast.hasNext():
                        self._adaptor.addChild(root_1, stream_tuple_type_cast.nextTree())


                    stream_tuple_type_cast.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "bag_type_cast"

    class unary_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.unary_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "unary_expr"
    # QueryParser.g:445:1: unary_expr : ( expr_eval | LEFT_PAREN expr RIGHT_PAREN -> ^( EXPR_IN_PAREN expr ) | neg_expr );
    def unary_expr(self, ):

        retval = self.unary_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN315 = None
        RIGHT_PAREN317 = None
        expr_eval314 = None

        expr316 = None

        neg_expr318 = None


        LEFT_PAREN315_tree = None
        RIGHT_PAREN317_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # QueryParser.g:445:12: ( expr_eval | LEFT_PAREN expr RIGHT_PAREN -> ^( EXPR_IN_PAREN expr ) | neg_expr )
                alt86 = 3
                alt86 = self.dfa86.predict(self.input)
                if alt86 == 1:
                    # QueryParser.g:445:14: expr_eval
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_eval_in_unary_expr3198)
                    expr_eval314 = self.expr_eval()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr_eval314.tree)


                elif alt86 == 2:
                    # QueryParser.g:446:14: LEFT_PAREN expr RIGHT_PAREN
                    pass 
                    LEFT_PAREN315=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_unary_expr3214) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN315)
                    self._state.following.append(self.FOLLOW_expr_in_unary_expr3216)
                    expr316 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr316.tree)
                    RIGHT_PAREN317=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_unary_expr3218) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN317)

                    # AST Rewrite
                    # elements: expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 447:11: -> ^( EXPR_IN_PAREN expr )
                        # QueryParser.g:447:14: ^( EXPR_IN_PAREN expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(EXPR_IN_PAREN, "EXPR_IN_PAREN"), root_1)

                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt86 == 3:
                    # QueryParser.g:448:14: neg_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_neg_expr_in_unary_expr3253)
                    neg_expr318 = self.neg_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, neg_expr318.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "unary_expr"

    class expr_eval_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.expr_eval_return, self).__init__()

            self.tree = None




    # $ANTLR start "expr_eval"
    # QueryParser.g:451:1: expr_eval : ( const_expr | var_expr );
    def expr_eval(self, ):

        retval = self.expr_eval_return()
        retval.start = self.input.LT(1)

        root_0 = None

        const_expr319 = None

        var_expr320 = None



        try:
            try:
                # QueryParser.g:451:11: ( const_expr | var_expr )
                alt87 = 2
                alt87 = self.dfa87.predict(self.input)
                if alt87 == 1:
                    # QueryParser.g:451:13: const_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_const_expr_in_expr_eval3262)
                    const_expr319 = self.const_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, const_expr319.tree)


                elif alt87 == 2:
                    # QueryParser.g:451:26: var_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_var_expr_in_expr_eval3266)
                    var_expr320 = self.var_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, var_expr320.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "expr_eval"

    class var_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.var_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "var_expr"
    # QueryParser.g:454:1: var_expr : projectable_expr ( dot_proj | pound_proj )* ;
    def var_expr(self, ):

        retval = self.var_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        projectable_expr321 = None

        dot_proj322 = None

        pound_proj323 = None



        try:
            try:
                # QueryParser.g:454:10: ( projectable_expr ( dot_proj | pound_proj )* )
                # QueryParser.g:454:12: projectable_expr ( dot_proj | pound_proj )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_projectable_expr_in_var_expr3275)
                projectable_expr321 = self.projectable_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, projectable_expr321.tree)
                # QueryParser.g:454:29: ( dot_proj | pound_proj )*
                while True: #loop88
                    alt88 = 3
                    LA88_0 = self.input.LA(1)

                    if (LA88_0 == PERIOD) :
                        alt88 = 1
                    elif (LA88_0 == POUND) :
                        alt88 = 2


                    if alt88 == 1:
                        # QueryParser.g:454:31: dot_proj
                        pass 
                        self._state.following.append(self.FOLLOW_dot_proj_in_var_expr3279)
                        dot_proj322 = self.dot_proj()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, dot_proj322.tree)


                    elif alt88 == 2:
                        # QueryParser.g:454:42: pound_proj
                        pass 
                        self._state.following.append(self.FOLLOW_pound_proj_in_var_expr3283)
                        pound_proj323 = self.pound_proj()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, pound_proj323.tree)


                    else:
                        break #loop88



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "var_expr"

    class projectable_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.projectable_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "projectable_expr"
    # QueryParser.g:457:1: projectable_expr : ( func_eval | col_ref | bin_expr | type_conversion );
    def projectable_expr(self, ):

        retval = self.projectable_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        func_eval324 = None

        col_ref325 = None

        bin_expr326 = None

        type_conversion327 = None



        try:
            try:
                # QueryParser.g:457:17: ( func_eval | col_ref | bin_expr | type_conversion )
                alt89 = 4
                alt89 = self.dfa89.predict(self.input)
                if alt89 == 1:
                    # QueryParser.g:457:19: func_eval
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_func_eval_in_projectable_expr3294)
                    func_eval324 = self.func_eval()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_eval324.tree)


                elif alt89 == 2:
                    # QueryParser.g:457:31: col_ref
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_ref_in_projectable_expr3298)
                    col_ref325 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_ref325.tree)


                elif alt89 == 3:
                    # QueryParser.g:457:41: bin_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_bin_expr_in_projectable_expr3302)
                    bin_expr326 = self.bin_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bin_expr326.tree)


                elif alt89 == 4:
                    # QueryParser.g:457:52: type_conversion
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_type_conversion_in_projectable_expr3306)
                    type_conversion327 = self.type_conversion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, type_conversion327.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "projectable_expr"

    class type_conversion_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.type_conversion_return, self).__init__()

            self.tree = None




    # $ANTLR start "type_conversion"
    # QueryParser.g:460:1: type_conversion : ( LEFT_CURLY real_arg_list RIGHT_CURLY -> ^( FUNC_EVAL TOBAG real_arg_list ) | LEFT_BRACKET real_arg_list RIGHT_BRACKET -> ^( FUNC_EVAL TOMAP real_arg_list ) | LEFT_PAREN real_arg ( COMMA real_arg )+ RIGHT_PAREN -> ^( FUNC_EVAL TOTUPLE ( real_arg )+ ) );
    def type_conversion(self, ):

        retval = self.type_conversion_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_CURLY328 = None
        RIGHT_CURLY330 = None
        LEFT_BRACKET331 = None
        RIGHT_BRACKET333 = None
        LEFT_PAREN334 = None
        COMMA336 = None
        RIGHT_PAREN338 = None
        real_arg_list329 = None

        real_arg_list332 = None

        real_arg335 = None

        real_arg337 = None


        LEFT_CURLY328_tree = None
        RIGHT_CURLY330_tree = None
        LEFT_BRACKET331_tree = None
        RIGHT_BRACKET333_tree = None
        LEFT_PAREN334_tree = None
        COMMA336_tree = None
        RIGHT_PAREN338_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_RIGHT_CURLY = RewriteRuleTokenStream(self._adaptor, "token RIGHT_CURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LEFT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token LEFT_BRACKET")
        stream_LEFT_CURLY = RewriteRuleTokenStream(self._adaptor, "token LEFT_CURLY")
        stream_RIGHT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token RIGHT_BRACKET")
        stream_real_arg_list = RewriteRuleSubtreeStream(self._adaptor, "rule real_arg_list")
        stream_real_arg = RewriteRuleSubtreeStream(self._adaptor, "rule real_arg")
        try:
            try:
                # QueryParser.g:460:17: ( LEFT_CURLY real_arg_list RIGHT_CURLY -> ^( FUNC_EVAL TOBAG real_arg_list ) | LEFT_BRACKET real_arg_list RIGHT_BRACKET -> ^( FUNC_EVAL TOMAP real_arg_list ) | LEFT_PAREN real_arg ( COMMA real_arg )+ RIGHT_PAREN -> ^( FUNC_EVAL TOTUPLE ( real_arg )+ ) )
                alt91 = 3
                LA91 = self.input.LA(1)
                if LA91 == LEFT_CURLY:
                    alt91 = 1
                elif LA91 == LEFT_BRACKET:
                    alt91 = 2
                elif LA91 == LEFT_PAREN:
                    alt91 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 91, 0, self.input)

                    raise nvae

                if alt91 == 1:
                    # QueryParser.g:460:19: LEFT_CURLY real_arg_list RIGHT_CURLY
                    pass 
                    LEFT_CURLY328=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_type_conversion3315) 
                    if self._state.backtracking == 0:
                        stream_LEFT_CURLY.add(LEFT_CURLY328)
                    self._state.following.append(self.FOLLOW_real_arg_list_in_type_conversion3317)
                    real_arg_list329 = self.real_arg_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_real_arg_list.add(real_arg_list329.tree)
                    RIGHT_CURLY330=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_type_conversion3319) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_CURLY.add(RIGHT_CURLY330)

                    # AST Rewrite
                    # elements: real_arg_list
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 461:16: -> ^( FUNC_EVAL TOBAG real_arg_list )
                        # QueryParser.g:461:19: ^( FUNC_EVAL TOBAG real_arg_list )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_EVAL, "FUNC_EVAL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(TOBAG, "TOBAG"))
                        self._adaptor.addChild(root_1, stream_real_arg_list.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt91 == 2:
                    # QueryParser.g:462:18: LEFT_BRACKET real_arg_list RIGHT_BRACKET
                    pass 
                    LEFT_BRACKET331=self.match(self.input, LEFT_BRACKET, self.FOLLOW_LEFT_BRACKET_in_type_conversion3366) 
                    if self._state.backtracking == 0:
                        stream_LEFT_BRACKET.add(LEFT_BRACKET331)
                    self._state.following.append(self.FOLLOW_real_arg_list_in_type_conversion3368)
                    real_arg_list332 = self.real_arg_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_real_arg_list.add(real_arg_list332.tree)
                    RIGHT_BRACKET333=self.match(self.input, RIGHT_BRACKET, self.FOLLOW_RIGHT_BRACKET_in_type_conversion3370) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_BRACKET.add(RIGHT_BRACKET333)

                    # AST Rewrite
                    # elements: real_arg_list
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 463:16: -> ^( FUNC_EVAL TOMAP real_arg_list )
                        # QueryParser.g:463:19: ^( FUNC_EVAL TOMAP real_arg_list )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_EVAL, "FUNC_EVAL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(TOMAP, "TOMAP"))
                        self._adaptor.addChild(root_1, stream_real_arg_list.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt91 == 3:
                    # QueryParser.g:464:18: LEFT_PAREN real_arg ( COMMA real_arg )+ RIGHT_PAREN
                    pass 
                    LEFT_PAREN334=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_type_conversion3417) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN334)
                    self._state.following.append(self.FOLLOW_real_arg_in_type_conversion3419)
                    real_arg335 = self.real_arg()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_real_arg.add(real_arg335.tree)
                    # QueryParser.g:464:38: ( COMMA real_arg )+
                    cnt90 = 0
                    while True: #loop90
                        alt90 = 2
                        LA90_0 = self.input.LA(1)

                        if (LA90_0 == COMMA) :
                            alt90 = 1


                        if alt90 == 1:
                            # QueryParser.g:464:40: COMMA real_arg
                            pass 
                            COMMA336=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_type_conversion3423) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA336)
                            self._state.following.append(self.FOLLOW_real_arg_in_type_conversion3425)
                            real_arg337 = self.real_arg()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_real_arg.add(real_arg337.tree)


                        else:
                            if cnt90 >= 1:
                                break #loop90

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(90, self.input)
                            raise eee

                        cnt90 += 1
                    RIGHT_PAREN338=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_type_conversion3430) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN338)

                    # AST Rewrite
                    # elements: real_arg
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 465:16: -> ^( FUNC_EVAL TOTUPLE ( real_arg )+ )
                        # QueryParser.g:465:19: ^( FUNC_EVAL TOTUPLE ( real_arg )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FUNC_EVAL, "FUNC_EVAL"), root_1)

                        self._adaptor.addChild(root_1, self._adaptor.createFromType(TOTUPLE, "TOTUPLE"))
                        # QueryParser.g:465:40: ( real_arg )+
                        if not (stream_real_arg.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_real_arg.hasNext():
                            self._adaptor.addChild(root_1, stream_real_arg.nextTree())


                        stream_real_arg.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "type_conversion"

    class dot_proj_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.dot_proj_return, self).__init__()

            self.tree = None




    # $ANTLR start "dot_proj"
    # QueryParser.g:468:1: dot_proj : PERIOD ( col_alias_or_index | ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN ) ) -> ^( PERIOD ( col_alias_or_index )+ ) ;
    def dot_proj(self, ):

        retval = self.dot_proj_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PERIOD339 = None
        LEFT_PAREN341 = None
        COMMA343 = None
        RIGHT_PAREN345 = None
        col_alias_or_index340 = None

        col_alias_or_index342 = None

        col_alias_or_index344 = None


        PERIOD339_tree = None
        LEFT_PAREN341_tree = None
        COMMA343_tree = None
        RIGHT_PAREN345_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_PERIOD = RewriteRuleTokenStream(self._adaptor, "token PERIOD")
        stream_col_alias_or_index = RewriteRuleSubtreeStream(self._adaptor, "rule col_alias_or_index")
        try:
            try:
                # QueryParser.g:468:10: ( PERIOD ( col_alias_or_index | ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN ) ) -> ^( PERIOD ( col_alias_or_index )+ ) )
                # QueryParser.g:468:12: PERIOD ( col_alias_or_index | ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN ) )
                pass 
                PERIOD339=self.match(self.input, PERIOD, self.FOLLOW_PERIOD_in_dot_proj3468) 
                if self._state.backtracking == 0:
                    stream_PERIOD.add(PERIOD339)
                # QueryParser.g:468:19: ( col_alias_or_index | ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN ) )
                alt93 = 2
                LA93_0 = self.input.LA(1)

                if (LA93_0 == CUBE or LA93_0 == GROUP or LA93_0 == IDENTIFIER_L or LA93_0 == DOLLARVAR) :
                    alt93 = 1
                elif (LA93_0 == LEFT_PAREN) :
                    alt93 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 93, 0, self.input)

                    raise nvae

                if alt93 == 1:
                    # QueryParser.g:468:21: col_alias_or_index
                    pass 
                    self._state.following.append(self.FOLLOW_col_alias_or_index_in_dot_proj3472)
                    col_alias_or_index340 = self.col_alias_or_index()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_alias_or_index.add(col_alias_or_index340.tree)


                elif alt93 == 2:
                    # QueryParser.g:469:21: ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN )
                    pass 
                    # QueryParser.g:469:21: ( LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN )
                    # QueryParser.g:469:23: LEFT_PAREN col_alias_or_index ( COMMA col_alias_or_index )* RIGHT_PAREN
                    pass 
                    LEFT_PAREN341=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_dot_proj3497) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN341)
                    self._state.following.append(self.FOLLOW_col_alias_or_index_in_dot_proj3499)
                    col_alias_or_index342 = self.col_alias_or_index()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_alias_or_index.add(col_alias_or_index342.tree)
                    # QueryParser.g:469:53: ( COMMA col_alias_or_index )*
                    while True: #loop92
                        alt92 = 2
                        LA92_0 = self.input.LA(1)

                        if (LA92_0 == COMMA) :
                            alt92 = 1


                        if alt92 == 1:
                            # QueryParser.g:469:55: COMMA col_alias_or_index
                            pass 
                            COMMA343=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dot_proj3503) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA343)
                            self._state.following.append(self.FOLLOW_col_alias_or_index_in_dot_proj3505)
                            col_alias_or_index344 = self.col_alias_or_index()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_col_alias_or_index.add(col_alias_or_index344.tree)


                        else:
                            break #loop92
                    RIGHT_PAREN345=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_dot_proj3510) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN345)







                # AST Rewrite
                # elements: col_alias_or_index, PERIOD
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 470:9: -> ^( PERIOD ( col_alias_or_index )+ )
                    # QueryParser.g:470:12: ^( PERIOD ( col_alias_or_index )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_PERIOD.nextNode(), root_1)

                    # QueryParser.g:470:22: ( col_alias_or_index )+
                    if not (stream_col_alias_or_index.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_col_alias_or_index.hasNext():
                        self._adaptor.addChild(root_1, stream_col_alias_or_index.nextTree())


                    stream_col_alias_or_index.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "dot_proj"

    class col_alias_or_index_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_alias_or_index_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_alias_or_index"
    # QueryParser.g:473:1: col_alias_or_index : ( col_alias | col_index );
    def col_alias_or_index(self, ):

        retval = self.col_alias_or_index_return()
        retval.start = self.input.LT(1)

        root_0 = None

        col_alias346 = None

        col_index347 = None



        try:
            try:
                # QueryParser.g:473:20: ( col_alias | col_index )
                alt94 = 2
                LA94_0 = self.input.LA(1)

                if (LA94_0 == CUBE or LA94_0 == GROUP or LA94_0 == IDENTIFIER_L) :
                    alt94 = 1
                elif (LA94_0 == DOLLARVAR) :
                    alt94 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 94, 0, self.input)

                    raise nvae

                if alt94 == 1:
                    # QueryParser.g:473:22: col_alias
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_alias_in_col_alias_or_index3542)
                    col_alias346 = self.col_alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_alias346.tree)


                elif alt94 == 2:
                    # QueryParser.g:473:34: col_index
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_index_in_col_alias_or_index3546)
                    col_index347 = self.col_index()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_index347.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_alias_or_index"

    class col_alias_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_alias_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_alias"
    # QueryParser.g:476:1: col_alias : ( GROUP | CUBE | identifier );
    def col_alias(self, ):

        retval = self.col_alias_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP348 = None
        CUBE349 = None
        identifier350 = None


        GROUP348_tree = None
        CUBE349_tree = None

        try:
            try:
                # QueryParser.g:476:11: ( GROUP | CUBE | identifier )
                alt95 = 3
                LA95 = self.input.LA(1)
                if LA95 == GROUP:
                    alt95 = 1
                elif LA95 == CUBE:
                    alt95 = 2
                elif LA95 == IDENTIFIER_L:
                    alt95 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 95, 0, self.input)

                    raise nvae

                if alt95 == 1:
                    # QueryParser.g:476:13: GROUP
                    pass 
                    root_0 = self._adaptor.nil()

                    GROUP348=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_col_alias3555)
                    if self._state.backtracking == 0:

                        GROUP348_tree = self._adaptor.createWithPayload(GROUP348)
                        self._adaptor.addChild(root_0, GROUP348_tree)



                elif alt95 == 2:
                    # QueryParser.g:476:21: CUBE
                    pass 
                    root_0 = self._adaptor.nil()

                    CUBE349=self.match(self.input, CUBE, self.FOLLOW_CUBE_in_col_alias3559)
                    if self._state.backtracking == 0:

                        CUBE349_tree = self._adaptor.createWithPayload(CUBE349)
                        self._adaptor.addChild(root_0, CUBE349_tree)



                elif alt95 == 3:
                    # QueryParser.g:476:28: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_col_alias3563)
                    identifier350 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier350.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_alias"

    class col_index_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_index_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_index"
    # QueryParser.g:479:1: col_index : DOLLARVAR ;
    def col_index(self, ):

        retval = self.col_index_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOLLARVAR351 = None

        DOLLARVAR351_tree = None

        try:
            try:
                # QueryParser.g:479:11: ( DOLLARVAR )
                # QueryParser.g:479:13: DOLLARVAR
                pass 
                root_0 = self._adaptor.nil()

                DOLLARVAR351=self.match(self.input, DOLLARVAR, self.FOLLOW_DOLLARVAR_in_col_index3572)
                if self._state.backtracking == 0:

                    DOLLARVAR351_tree = self._adaptor.createWithPayload(DOLLARVAR351)
                    self._adaptor.addChild(root_0, DOLLARVAR351_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_index"

    class col_range_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_range_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_range"
    # QueryParser.g:482:1: col_range : (c1= col_ref DOUBLE_PERIOD (c2= col_ref )? -> ^( COL_RANGE $c1 DOUBLE_PERIOD ( $c2)? ) | DOUBLE_PERIOD col_ref -> ^( COL_RANGE DOUBLE_PERIOD col_ref ) );
    def col_range(self, ):

        retval = self.col_range_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOUBLE_PERIOD352 = None
        DOUBLE_PERIOD353 = None
        c1 = None

        c2 = None

        col_ref354 = None


        DOUBLE_PERIOD352_tree = None
        DOUBLE_PERIOD353_tree = None
        stream_DOUBLE_PERIOD = RewriteRuleTokenStream(self._adaptor, "token DOUBLE_PERIOD")
        stream_col_ref = RewriteRuleSubtreeStream(self._adaptor, "rule col_ref")
        try:
            try:
                # QueryParser.g:482:11: (c1= col_ref DOUBLE_PERIOD (c2= col_ref )? -> ^( COL_RANGE $c1 DOUBLE_PERIOD ( $c2)? ) | DOUBLE_PERIOD col_ref -> ^( COL_RANGE DOUBLE_PERIOD col_ref ) )
                alt97 = 2
                LA97_0 = self.input.LA(1)

                if (LA97_0 == CUBE or LA97_0 == GROUP or LA97_0 == IDENTIFIER_L or LA97_0 == DOLLARVAR) :
                    alt97 = 1
                elif (LA97_0 == DOUBLE_PERIOD) :
                    alt97 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 97, 0, self.input)

                    raise nvae

                if alt97 == 1:
                    # QueryParser.g:482:13: c1= col_ref DOUBLE_PERIOD (c2= col_ref )?
                    pass 
                    self._state.following.append(self.FOLLOW_col_ref_in_col_range3585)
                    c1 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_ref.add(c1.tree)
                    DOUBLE_PERIOD352=self.match(self.input, DOUBLE_PERIOD, self.FOLLOW_DOUBLE_PERIOD_in_col_range3587) 
                    if self._state.backtracking == 0:
                        stream_DOUBLE_PERIOD.add(DOUBLE_PERIOD352)
                    # QueryParser.g:482:43: (c2= col_ref )?
                    alt96 = 2
                    LA96_0 = self.input.LA(1)

                    if (LA96_0 == CUBE or LA96_0 == GROUP or LA96_0 == IDENTIFIER_L or LA96_0 == DOLLARVAR) :
                        alt96 = 1
                    if alt96 == 1:
                        # QueryParser.g:0:0: c2= col_ref
                        pass 
                        self._state.following.append(self.FOLLOW_col_ref_in_col_range3593)
                        c2 = self.col_ref()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_col_ref.add(c2.tree)




                    # AST Rewrite
                    # elements: c1, DOUBLE_PERIOD, c2
                    # token labels: 
                    # rule labels: retval, c1, c2
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        if c1 is not None:
                            stream_c1 = RewriteRuleSubtreeStream(self._adaptor, "rule c1", c1.tree)
                        else:
                            stream_c1 = RewriteRuleSubtreeStream(self._adaptor, "token c1", None)


                        if c2 is not None:
                            stream_c2 = RewriteRuleSubtreeStream(self._adaptor, "rule c2", c2.tree)
                        else:
                            stream_c2 = RewriteRuleSubtreeStream(self._adaptor, "token c2", None)


                        root_0 = self._adaptor.nil()
                        # 483:11: -> ^( COL_RANGE $c1 DOUBLE_PERIOD ( $c2)? )
                        # QueryParser.g:483:14: ^( COL_RANGE $c1 DOUBLE_PERIOD ( $c2)? )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(COL_RANGE, "COL_RANGE"), root_1)

                        self._adaptor.addChild(root_1, stream_c1.nextTree())
                        self._adaptor.addChild(root_1, stream_DOUBLE_PERIOD.nextNode())
                        # QueryParser.g:483:44: ( $c2)?
                        if stream_c2.hasNext():
                            self._adaptor.addChild(root_1, stream_c2.nextTree())


                        stream_c2.reset();

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt97 == 2:
                    # QueryParser.g:484:14: DOUBLE_PERIOD col_ref
                    pass 
                    DOUBLE_PERIOD353=self.match(self.input, DOUBLE_PERIOD, self.FOLLOW_DOUBLE_PERIOD_in_col_range3634) 
                    if self._state.backtracking == 0:
                        stream_DOUBLE_PERIOD.add(DOUBLE_PERIOD353)
                    self._state.following.append(self.FOLLOW_col_ref_in_col_range3636)
                    col_ref354 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_ref.add(col_ref354.tree)

                    # AST Rewrite
                    # elements: col_ref, DOUBLE_PERIOD
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 485:11: -> ^( COL_RANGE DOUBLE_PERIOD col_ref )
                        # QueryParser.g:485:14: ^( COL_RANGE DOUBLE_PERIOD col_ref )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(COL_RANGE, "COL_RANGE"), root_1)

                        self._adaptor.addChild(root_1, stream_DOUBLE_PERIOD.nextNode())
                        self._adaptor.addChild(root_1, stream_col_ref.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_range"

    class pound_proj_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.pound_proj_return, self).__init__()

            self.tree = None




    # $ANTLR start "pound_proj"
    # QueryParser.g:489:1: pound_proj : POUND ( QUOTEDSTRING | null_keyword ) ;
    def pound_proj(self, ):

        retval = self.pound_proj_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POUND355 = None
        QUOTEDSTRING356 = None
        null_keyword357 = None


        POUND355_tree = None
        QUOTEDSTRING356_tree = None

        try:
            try:
                # QueryParser.g:489:12: ( POUND ( QUOTEDSTRING | null_keyword ) )
                # QueryParser.g:489:14: POUND ( QUOTEDSTRING | null_keyword )
                pass 
                root_0 = self._adaptor.nil()

                POUND355=self.match(self.input, POUND, self.FOLLOW_POUND_in_pound_proj3667)
                if self._state.backtracking == 0:

                    POUND355_tree = self._adaptor.createWithPayload(POUND355)
                    root_0 = self._adaptor.becomeRoot(POUND355_tree, root_0)

                # QueryParser.g:489:21: ( QUOTEDSTRING | null_keyword )
                alt98 = 2
                LA98_0 = self.input.LA(1)

                if (LA98_0 == QUOTEDSTRING) :
                    alt98 = 1
                elif (LA98_0 == IDENTIFIER_L) :
                    alt98 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 98, 0, self.input)

                    raise nvae

                if alt98 == 1:
                    # QueryParser.g:489:23: QUOTEDSTRING
                    pass 
                    QUOTEDSTRING356=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_pound_proj3672)
                    if self._state.backtracking == 0:

                        QUOTEDSTRING356_tree = self._adaptor.createWithPayload(QUOTEDSTRING356)
                        self._adaptor.addChild(root_0, QUOTEDSTRING356_tree)



                elif alt98 == 2:
                    # QueryParser.g:489:38: null_keyword
                    pass 
                    self._state.following.append(self.FOLLOW_null_keyword_in_pound_proj3676)
                    null_keyword357 = self.null_keyword()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, null_keyword357.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "pound_proj"

    class bin_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.bin_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "bin_expr"
    # QueryParser.g:492:1: bin_expr : LEFT_PAREN cond QMARK exp1= expr COLON exp2= expr RIGHT_PAREN -> ^( BIN_EXPR cond $exp1 $exp2) ;
    def bin_expr(self, ):

        retval = self.bin_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN358 = None
        QMARK360 = None
        COLON361 = None
        RIGHT_PAREN362 = None
        exp1 = None

        exp2 = None

        cond359 = None


        LEFT_PAREN358_tree = None
        QMARK360_tree = None
        COLON361_tree = None
        RIGHT_PAREN362_tree = None
        stream_COLON = RewriteRuleTokenStream(self._adaptor, "token COLON")
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_QMARK = RewriteRuleTokenStream(self._adaptor, "token QMARK")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_cond = RewriteRuleSubtreeStream(self._adaptor, "rule cond")
        try:
            try:
                # QueryParser.g:492:10: ( LEFT_PAREN cond QMARK exp1= expr COLON exp2= expr RIGHT_PAREN -> ^( BIN_EXPR cond $exp1 $exp2) )
                # QueryParser.g:492:12: LEFT_PAREN cond QMARK exp1= expr COLON exp2= expr RIGHT_PAREN
                pass 
                LEFT_PAREN358=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_bin_expr3687) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN358)
                self._state.following.append(self.FOLLOW_cond_in_bin_expr3689)
                cond359 = self.cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_cond.add(cond359.tree)
                QMARK360=self.match(self.input, QMARK, self.FOLLOW_QMARK_in_bin_expr3691) 
                if self._state.backtracking == 0:
                    stream_QMARK.add(QMARK360)
                self._state.following.append(self.FOLLOW_expr_in_bin_expr3697)
                exp1 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(exp1.tree)
                COLON361=self.match(self.input, COLON, self.FOLLOW_COLON_in_bin_expr3699) 
                if self._state.backtracking == 0:
                    stream_COLON.add(COLON361)
                self._state.following.append(self.FOLLOW_expr_in_bin_expr3705)
                exp2 = self.expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_expr.add(exp2.tree)
                RIGHT_PAREN362=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_bin_expr3707) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN362)

                # AST Rewrite
                # elements: cond, exp2, exp1
                # token labels: 
                # rule labels: retval, exp2, exp1
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    if exp2 is not None:
                        stream_exp2 = RewriteRuleSubtreeStream(self._adaptor, "rule exp2", exp2.tree)
                    else:
                        stream_exp2 = RewriteRuleSubtreeStream(self._adaptor, "token exp2", None)


                    if exp1 is not None:
                        stream_exp1 = RewriteRuleSubtreeStream(self._adaptor, "rule exp1", exp1.tree)
                    else:
                        stream_exp1 = RewriteRuleSubtreeStream(self._adaptor, "token exp1", None)


                    root_0 = self._adaptor.nil()
                    # 493:9: -> ^( BIN_EXPR cond $exp1 $exp2)
                    # QueryParser.g:493:12: ^( BIN_EXPR cond $exp1 $exp2)
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BIN_EXPR, "BIN_EXPR"), root_1)

                    self._adaptor.addChild(root_1, stream_cond.nextTree())
                    self._adaptor.addChild(root_1, stream_exp1.nextTree())
                    self._adaptor.addChild(root_1, stream_exp2.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "bin_expr"

    class neg_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.neg_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "neg_expr"
    # QueryParser.g:496:1: neg_expr : MINUS cast_expr -> ^( NEG cast_expr ) ;
    def neg_expr(self, ):

        retval = self.neg_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MINUS363 = None
        cast_expr364 = None


        MINUS363_tree = None
        stream_MINUS = RewriteRuleTokenStream(self._adaptor, "token MINUS")
        stream_cast_expr = RewriteRuleSubtreeStream(self._adaptor, "rule cast_expr")
        try:
            try:
                # QueryParser.g:496:10: ( MINUS cast_expr -> ^( NEG cast_expr ) )
                # QueryParser.g:496:12: MINUS cast_expr
                pass 
                MINUS363=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_neg_expr3740) 
                if self._state.backtracking == 0:
                    stream_MINUS.add(MINUS363)
                self._state.following.append(self.FOLLOW_cast_expr_in_neg_expr3742)
                cast_expr364 = self.cast_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_cast_expr.add(cast_expr364.tree)

                # AST Rewrite
                # elements: cast_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 497:9: -> ^( NEG cast_expr )
                    # QueryParser.g:497:12: ^( NEG cast_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NEG, "NEG"), root_1)

                    self._adaptor.addChild(root_1, stream_cast_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "neg_expr"

    class limit_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.limit_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "limit_clause"
    # QueryParser.g:500:1: limit_clause : LIMIT rel ( ( INTEGER SEMI_COLON )=> INTEGER | ( LONGINTEGER SEMI_COLON )=> LONGINTEGER | expr ) ;
    def limit_clause(self, ):

        retval = self.limit_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIMIT365 = None
        INTEGER367 = None
        LONGINTEGER368 = None
        rel366 = None

        expr369 = None


        LIMIT365_tree = None
        INTEGER367_tree = None
        LONGINTEGER368_tree = None

        try:
            try:
                # QueryParser.g:500:14: ( LIMIT rel ( ( INTEGER SEMI_COLON )=> INTEGER | ( LONGINTEGER SEMI_COLON )=> LONGINTEGER | expr ) )
                # QueryParser.g:500:16: LIMIT rel ( ( INTEGER SEMI_COLON )=> INTEGER | ( LONGINTEGER SEMI_COLON )=> LONGINTEGER | expr )
                pass 
                root_0 = self._adaptor.nil()

                LIMIT365=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_limit_clause3769)
                if self._state.backtracking == 0:

                    LIMIT365_tree = self._adaptor.createWithPayload(LIMIT365)
                    root_0 = self._adaptor.becomeRoot(LIMIT365_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_limit_clause3772)
                rel366 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel366.tree)
                # QueryParser.g:500:27: ( ( INTEGER SEMI_COLON )=> INTEGER | ( LONGINTEGER SEMI_COLON )=> LONGINTEGER | expr )
                alt99 = 3
                LA99 = self.input.LA(1)
                if LA99 == INTEGER:
                    LA99_1 = self.input.LA(2)

                    if (self.synpred163_QueryParser()) :
                        alt99 = 1
                    elif (True) :
                        alt99 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 99, 1, self.input)

                        raise nvae

                elif LA99 == LONGINTEGER:
                    LA99_2 = self.input.LA(2)

                    if (self.synpred164_QueryParser()) :
                        alt99 = 2
                    elif (True) :
                        alt99 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 99, 2, self.input)

                        raise nvae

                elif LA99 == IMPORT or LA99 == RETURNS or LA99 == DEFINE or LA99 == LOAD or LA99 == FILTER or LA99 == FOREACH or LA99 == ORDER or LA99 == CUBE or LA99 == ROLLUP or LA99 == DISTINCT or LA99 == COGROUP or LA99 == JOIN or LA99 == CROSS or LA99 == UNION or LA99 == SPLIT or LA99 == INTO or LA99 == IF or LA99 == ALL or LA99 == AS or LA99 == BY or LA99 == USING or LA99 == INNER or LA99 == OUTER or LA99 == PARALLEL or LA99 == PARTITION or LA99 == GROUP or LA99 == AND or LA99 == OR or LA99 == NOT or LA99 == GENERATE or LA99 == FLATTEN or LA99 == ASC or LA99 == DESC or LA99 == INT or LA99 == LONG or LA99 == FLOAT or LA99 == DOUBLE or LA99 == DATETIME or LA99 == CHARARRAY or LA99 == BYTEARRAY or LA99 == BAG or LA99 == TUPLE or LA99 == MAP or LA99 == IS or LA99 == STREAM or LA99 == THROUGH or LA99 == STORE or LA99 == MAPREDUCE or LA99 == SHIP or LA99 == CACHE or LA99 == INPUT or LA99 == OUTPUT or LA99 == STDERROR or LA99 == STDIN or LA99 == STDOUT or LA99 == LIMIT or LA99 == SAMPLE or LA99 == LEFT or LA99 == RIGHT or LA99 == FULL or LA99 == STR_OP_EQ or LA99 == STR_OP_GT or LA99 == STR_OP_LT or LA99 == STR_OP_GTE or LA99 == STR_OP_LTE or LA99 == STR_OP_NE or LA99 == STR_OP_MATCHES or LA99 == TRUE or LA99 == FALSE or LA99 == IDENTIFIER_L or LA99 == DOLLARVAR or LA99 == MINUS or LA99 == DOUBLENUMBER or LA99 == FLOATNUMBER or LA99 == QUOTEDSTRING or LA99 == LEFT_PAREN or LA99 == LEFT_CURLY or LA99 == LEFT_BRACKET or LA99 == BOOL or LA99 == REALIAS:
                    alt99 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 99, 0, self.input)

                    raise nvae

                if alt99 == 1:
                    # QueryParser.g:500:29: ( INTEGER SEMI_COLON )=> INTEGER
                    pass 
                    INTEGER367=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_limit_clause3784)
                    if self._state.backtracking == 0:

                        INTEGER367_tree = self._adaptor.createWithPayload(INTEGER367)
                        self._adaptor.addChild(root_0, INTEGER367_tree)



                elif alt99 == 2:
                    # QueryParser.g:500:63: ( LONGINTEGER SEMI_COLON )=> LONGINTEGER
                    pass 
                    LONGINTEGER368=self.match(self.input, LONGINTEGER, self.FOLLOW_LONGINTEGER_in_limit_clause3796)
                    if self._state.backtracking == 0:

                        LONGINTEGER368_tree = self._adaptor.createWithPayload(LONGINTEGER368)
                        self._adaptor.addChild(root_0, LONGINTEGER368_tree)



                elif alt99 == 3:
                    # QueryParser.g:500:105: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_limit_clause3800)
                    expr369 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr369.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "limit_clause"

    class sample_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.sample_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "sample_clause"
    # QueryParser.g:503:1: sample_clause : SAMPLE rel ( ( DOUBLENUMBER SEMI_COLON )=> DOUBLENUMBER | expr ) ;
    def sample_clause(self, ):

        retval = self.sample_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SAMPLE370 = None
        DOUBLENUMBER372 = None
        rel371 = None

        expr373 = None


        SAMPLE370_tree = None
        DOUBLENUMBER372_tree = None

        try:
            try:
                # QueryParser.g:503:15: ( SAMPLE rel ( ( DOUBLENUMBER SEMI_COLON )=> DOUBLENUMBER | expr ) )
                # QueryParser.g:503:17: SAMPLE rel ( ( DOUBLENUMBER SEMI_COLON )=> DOUBLENUMBER | expr )
                pass 
                root_0 = self._adaptor.nil()

                SAMPLE370=self.match(self.input, SAMPLE, self.FOLLOW_SAMPLE_in_sample_clause3811)
                if self._state.backtracking == 0:

                    SAMPLE370_tree = self._adaptor.createWithPayload(SAMPLE370)
                    root_0 = self._adaptor.becomeRoot(SAMPLE370_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_sample_clause3814)
                rel371 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel371.tree)
                # QueryParser.g:503:29: ( ( DOUBLENUMBER SEMI_COLON )=> DOUBLENUMBER | expr )
                alt100 = 2
                LA100_0 = self.input.LA(1)

                if (LA100_0 == DOUBLENUMBER) :
                    LA100_1 = self.input.LA(2)

                    if (self.synpred165_QueryParser()) :
                        alt100 = 1
                    elif (True) :
                        alt100 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 100, 1, self.input)

                        raise nvae

                elif ((IMPORT <= LA100_0 <= ORDER) or (CUBE <= LA100_0 <= IF) or (ALL <= LA100_0 <= OUTER) or (PARALLEL <= LA100_0 <= DESC) or (INT <= LA100_0 <= FALSE) or (IDENTIFIER_L <= LA100_0 <= INTEGER) or LA100_0 == LONGINTEGER or (DOLLARVAR <= LA100_0 <= MINUS) or (FLOATNUMBER <= LA100_0 <= QUOTEDSTRING) or LA100_0 == LEFT_PAREN or LA100_0 == LEFT_CURLY or LA100_0 == LEFT_BRACKET or (BOOL <= LA100_0 <= REALIAS)) :
                    alt100 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 100, 0, self.input)

                    raise nvae

                if alt100 == 1:
                    # QueryParser.g:503:31: ( DOUBLENUMBER SEMI_COLON )=> DOUBLENUMBER
                    pass 
                    DOUBLENUMBER372=self.match(self.input, DOUBLENUMBER, self.FOLLOW_DOUBLENUMBER_in_sample_clause3826)
                    if self._state.backtracking == 0:

                        DOUBLENUMBER372_tree = self._adaptor.createWithPayload(DOUBLENUMBER372)
                        self._adaptor.addChild(root_0, DOUBLENUMBER372_tree)



                elif alt100 == 2:
                    # QueryParser.g:503:75: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_sample_clause3830)
                    expr373 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr373.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "sample_clause"

    class rank_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rank_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "rank_clause"
    # QueryParser.g:506:1: rank_clause : RANK rel ( rank_by_statement )? ;
    def rank_clause(self, ):

        retval = self.rank_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        RANK374 = None
        rel375 = None

        rank_by_statement376 = None


        RANK374_tree = None

        try:
            try:
                # QueryParser.g:506:13: ( RANK rel ( rank_by_statement )? )
                # QueryParser.g:506:15: RANK rel ( rank_by_statement )?
                pass 
                root_0 = self._adaptor.nil()

                RANK374=self.match(self.input, RANK, self.FOLLOW_RANK_in_rank_clause3841)
                if self._state.backtracking == 0:

                    RANK374_tree = self._adaptor.createWithPayload(RANK374)
                    root_0 = self._adaptor.becomeRoot(RANK374_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_rank_clause3844)
                rel375 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel375.tree)
                # QueryParser.g:506:25: ( rank_by_statement )?
                alt101 = 2
                LA101_0 = self.input.LA(1)

                if (LA101_0 == BY) :
                    alt101 = 1
                if alt101 == 1:
                    # QueryParser.g:506:27: rank_by_statement
                    pass 
                    self._state.following.append(self.FOLLOW_rank_by_statement_in_rank_clause3848)
                    rank_by_statement376 = self.rank_by_statement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rank_by_statement376.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rank_clause"

    class rank_by_statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rank_by_statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "rank_by_statement"
    # QueryParser.g:509:1: rank_by_statement : BY rank_by_clause ( DENSE )? ;
    def rank_by_statement(self, ):

        retval = self.rank_by_statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BY377 = None
        DENSE379 = None
        rank_by_clause378 = None


        BY377_tree = None
        DENSE379_tree = None

        try:
            try:
                # QueryParser.g:509:19: ( BY rank_by_clause ( DENSE )? )
                # QueryParser.g:509:21: BY rank_by_clause ( DENSE )?
                pass 
                root_0 = self._adaptor.nil()

                BY377=self.match(self.input, BY, self.FOLLOW_BY_in_rank_by_statement3860)
                if self._state.backtracking == 0:

                    BY377_tree = self._adaptor.createWithPayload(BY377)
                    root_0 = self._adaptor.becomeRoot(BY377_tree, root_0)

                self._state.following.append(self.FOLLOW_rank_by_clause_in_rank_by_statement3863)
                rank_by_clause378 = self.rank_by_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rank_by_clause378.tree)
                # QueryParser.g:509:40: ( DENSE )?
                alt102 = 2
                LA102_0 = self.input.LA(1)

                if (LA102_0 == DENSE) :
                    alt102 = 1
                if alt102 == 1:
                    # QueryParser.g:509:42: DENSE
                    pass 
                    DENSE379=self.match(self.input, DENSE, self.FOLLOW_DENSE_in_rank_by_statement3867)
                    if self._state.backtracking == 0:

                        DENSE379_tree = self._adaptor.createWithPayload(DENSE379)
                        self._adaptor.addChild(root_0, DENSE379_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rank_by_statement"

    class rank_by_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rank_by_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "rank_by_clause"
    # QueryParser.g:512:1: rank_by_clause : ( STAR ( ASC | DESC )? | rank_list );
    def rank_by_clause(self, ):

        retval = self.rank_by_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STAR380 = None
        set381 = None
        rank_list382 = None


        STAR380_tree = None
        set381_tree = None

        try:
            try:
                # QueryParser.g:512:16: ( STAR ( ASC | DESC )? | rank_list )
                alt104 = 2
                LA104_0 = self.input.LA(1)

                if (LA104_0 == STAR) :
                    alt104 = 1
                elif (LA104_0 == CUBE or LA104_0 == GROUP or LA104_0 == IDENTIFIER_L or LA104_0 == DOLLARVAR or LA104_0 == DOUBLE_PERIOD) :
                    alt104 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 104, 0, self.input)

                    raise nvae

                if alt104 == 1:
                    # QueryParser.g:512:18: STAR ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR380=self.match(self.input, STAR, self.FOLLOW_STAR_in_rank_by_clause3879)
                    if self._state.backtracking == 0:

                        STAR380_tree = self._adaptor.createWithPayload(STAR380)
                        self._adaptor.addChild(root_0, STAR380_tree)

                    # QueryParser.g:512:23: ( ASC | DESC )?
                    alt103 = 2
                    LA103_0 = self.input.LA(1)

                    if ((ASC <= LA103_0 <= DESC)) :
                        alt103 = 1
                    if alt103 == 1:
                        # QueryParser.g:
                        pass 
                        set381 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set381))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                elif alt104 == 2:
                    # QueryParser.g:513:9: rank_list
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rank_list_in_rank_by_clause3900)
                    rank_list382 = self.rank_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rank_list382.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rank_by_clause"

    class rank_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rank_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "rank_list"
    # QueryParser.g:516:1: rank_list : rank_col ( COMMA rank_col )* -> ( rank_col )+ ;
    def rank_list(self, ):

        retval = self.rank_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA384 = None
        rank_col383 = None

        rank_col385 = None


        COMMA384_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_rank_col = RewriteRuleSubtreeStream(self._adaptor, "rule rank_col")
        try:
            try:
                # QueryParser.g:516:11: ( rank_col ( COMMA rank_col )* -> ( rank_col )+ )
                # QueryParser.g:516:13: rank_col ( COMMA rank_col )*
                pass 
                self._state.following.append(self.FOLLOW_rank_col_in_rank_list3909)
                rank_col383 = self.rank_col()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rank_col.add(rank_col383.tree)
                # QueryParser.g:516:22: ( COMMA rank_col )*
                while True: #loop105
                    alt105 = 2
                    LA105_0 = self.input.LA(1)

                    if (LA105_0 == COMMA) :
                        alt105 = 1


                    if alt105 == 1:
                        # QueryParser.g:516:24: COMMA rank_col
                        pass 
                        COMMA384=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rank_list3913) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA384)
                        self._state.following.append(self.FOLLOW_rank_col_in_rank_list3915)
                        rank_col385 = self.rank_col()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rank_col.add(rank_col385.tree)


                    else:
                        break #loop105

                # AST Rewrite
                # elements: rank_col
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 517:10: -> ( rank_col )+
                    # QueryParser.g:517:13: ( rank_col )+
                    if not (stream_rank_col.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rank_col.hasNext():
                        self._adaptor.addChild(root_0, stream_rank_col.nextTree())


                    stream_rank_col.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rank_list"

    class rank_col_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rank_col_return, self).__init__()

            self.tree = None




    # $ANTLR start "rank_col"
    # QueryParser.g:520:1: rank_col : ( col_range ( ASC | DESC )? | col_ref ( ASC | DESC )? );
    def rank_col(self, ):

        retval = self.rank_col_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set387 = None
        set389 = None
        col_range386 = None

        col_ref388 = None


        set387_tree = None
        set389_tree = None

        try:
            try:
                # QueryParser.g:520:10: ( col_range ( ASC | DESC )? | col_ref ( ASC | DESC )? )
                alt108 = 2
                LA108 = self.input.LA(1)
                if LA108 == GROUP:
                    LA108_1 = self.input.LA(2)

                    if (LA108_1 == DOUBLE_PERIOD) :
                        alt108 = 1
                    elif (LA108_1 == EOF or LA108_1 == DENSE or LA108_1 == PARALLEL or (ASC <= LA108_1 <= DESC) or LA108_1 == SEMI_COLON or LA108_1 == RIGHT_PAREN or LA108_1 == COMMA) :
                        alt108 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 108, 1, self.input)

                        raise nvae

                elif LA108 == CUBE:
                    LA108_2 = self.input.LA(2)

                    if (LA108_2 == EOF or LA108_2 == DENSE or LA108_2 == PARALLEL or (ASC <= LA108_2 <= DESC) or LA108_2 == SEMI_COLON or LA108_2 == RIGHT_PAREN or LA108_2 == COMMA) :
                        alt108 = 2
                    elif (LA108_2 == DOUBLE_PERIOD) :
                        alt108 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 108, 2, self.input)

                        raise nvae

                elif LA108 == IDENTIFIER_L:
                    LA108_3 = self.input.LA(2)

                    if (LA108_3 == DOUBLE_PERIOD) :
                        alt108 = 1
                    elif (LA108_3 == EOF or LA108_3 == DENSE or LA108_3 == PARALLEL or (ASC <= LA108_3 <= DESC) or LA108_3 == SEMI_COLON or LA108_3 == RIGHT_PAREN or LA108_3 == COMMA) :
                        alt108 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 108, 3, self.input)

                        raise nvae

                elif LA108 == DOLLARVAR:
                    LA108_4 = self.input.LA(2)

                    if (LA108_4 == DOUBLE_PERIOD) :
                        alt108 = 1
                    elif (LA108_4 == EOF or LA108_4 == DENSE or LA108_4 == PARALLEL or (ASC <= LA108_4 <= DESC) or LA108_4 == SEMI_COLON or LA108_4 == RIGHT_PAREN or LA108_4 == COMMA) :
                        alt108 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 108, 4, self.input)

                        raise nvae

                elif LA108 == DOUBLE_PERIOD:
                    alt108 = 1
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 108, 0, self.input)

                    raise nvae

                if alt108 == 1:
                    # QueryParser.g:520:12: col_range ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_rank_col3941)
                    col_range386 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range386.tree)
                    # QueryParser.g:520:22: ( ASC | DESC )?
                    alt106 = 2
                    LA106_0 = self.input.LA(1)

                    if ((ASC <= LA106_0 <= DESC)) :
                        alt106 = 1
                    if alt106 == 1:
                        # QueryParser.g:
                        pass 
                        set387 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set387))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                elif alt108 == 2:
                    # QueryParser.g:521:12: col_ref ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_ref_in_rank_col3965)
                    col_ref388 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_ref388.tree)
                    # QueryParser.g:521:20: ( ASC | DESC )?
                    alt107 = 2
                    LA107_0 = self.input.LA(1)

                    if ((ASC <= LA107_0 <= DESC)) :
                        alt107 = 1
                    if alt107 == 1:
                        # QueryParser.g:
                        pass 
                        set389 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set389))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rank_col"

    class order_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.order_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "order_clause"
    # QueryParser.g:524:1: order_clause : ORDER rel BY order_by_clause ( USING func_clause )? ;
    def order_clause(self, ):

        retval = self.order_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER390 = None
        BY392 = None
        USING394 = None
        rel391 = None

        order_by_clause393 = None

        func_clause395 = None


        ORDER390_tree = None
        BY392_tree = None
        USING394_tree = None

        try:
            try:
                # QueryParser.g:524:14: ( ORDER rel BY order_by_clause ( USING func_clause )? )
                # QueryParser.g:524:16: ORDER rel BY order_by_clause ( USING func_clause )?
                pass 
                root_0 = self._adaptor.nil()

                ORDER390=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_order_clause3985)
                if self._state.backtracking == 0:

                    ORDER390_tree = self._adaptor.createWithPayload(ORDER390)
                    root_0 = self._adaptor.becomeRoot(ORDER390_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_order_clause3988)
                rel391 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel391.tree)
                BY392=self.match(self.input, BY, self.FOLLOW_BY_in_order_clause3990)
                self._state.following.append(self.FOLLOW_order_by_clause_in_order_clause3993)
                order_by_clause393 = self.order_by_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, order_by_clause393.tree)
                # QueryParser.g:524:47: ( USING func_clause )?
                alt109 = 2
                LA109_0 = self.input.LA(1)

                if (LA109_0 == USING) :
                    alt109 = 1
                if alt109 == 1:
                    # QueryParser.g:524:49: USING func_clause
                    pass 
                    USING394=self.match(self.input, USING, self.FOLLOW_USING_in_order_clause3997)
                    self._state.following.append(self.FOLLOW_func_clause_in_order_clause4000)
                    func_clause395 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause395.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "order_clause"

    class order_by_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.order_by_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "order_by_clause"
    # QueryParser.g:527:1: order_by_clause : ( STAR ( ASC | DESC )? | order_col_list );
    def order_by_clause(self, ):

        retval = self.order_by_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STAR396 = None
        set397 = None
        order_col_list398 = None


        STAR396_tree = None
        set397_tree = None

        try:
            try:
                # QueryParser.g:527:17: ( STAR ( ASC | DESC )? | order_col_list )
                alt111 = 2
                LA111_0 = self.input.LA(1)

                if (LA111_0 == STAR) :
                    alt111 = 1
                elif (LA111_0 == CUBE or LA111_0 == GROUP or LA111_0 == IDENTIFIER_L or LA111_0 == DOLLARVAR or LA111_0 == LEFT_PAREN or LA111_0 == DOUBLE_PERIOD) :
                    alt111 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 111, 0, self.input)

                    raise nvae

                if alt111 == 1:
                    # QueryParser.g:527:19: STAR ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR396=self.match(self.input, STAR, self.FOLLOW_STAR_in_order_by_clause4012)
                    if self._state.backtracking == 0:

                        STAR396_tree = self._adaptor.createWithPayload(STAR396)
                        self._adaptor.addChild(root_0, STAR396_tree)

                    # QueryParser.g:527:24: ( ASC | DESC )?
                    alt110 = 2
                    LA110_0 = self.input.LA(1)

                    if ((ASC <= LA110_0 <= DESC)) :
                        alt110 = 1
                    if alt110 == 1:
                        # QueryParser.g:
                        pass 
                        set397 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set397))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                elif alt111 == 2:
                    # QueryParser.g:528:19: order_col_list
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_order_col_list_in_order_by_clause4043)
                    order_col_list398 = self.order_col_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, order_col_list398.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "order_by_clause"

    class order_col_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.order_col_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "order_col_list"
    # QueryParser.g:531:1: order_col_list : order_col ( COMMA order_col )* -> ( order_col )+ ;
    def order_col_list(self, ):

        retval = self.order_col_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA400 = None
        order_col399 = None

        order_col401 = None


        COMMA400_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_order_col = RewriteRuleSubtreeStream(self._adaptor, "rule order_col")
        try:
            try:
                # QueryParser.g:531:16: ( order_col ( COMMA order_col )* -> ( order_col )+ )
                # QueryParser.g:531:18: order_col ( COMMA order_col )*
                pass 
                self._state.following.append(self.FOLLOW_order_col_in_order_col_list4052)
                order_col399 = self.order_col()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_order_col.add(order_col399.tree)
                # QueryParser.g:531:28: ( COMMA order_col )*
                while True: #loop112
                    alt112 = 2
                    LA112_0 = self.input.LA(1)

                    if (LA112_0 == COMMA) :
                        alt112 = 1


                    if alt112 == 1:
                        # QueryParser.g:531:30: COMMA order_col
                        pass 
                        COMMA400=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_order_col_list4056) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA400)
                        self._state.following.append(self.FOLLOW_order_col_in_order_col_list4058)
                        order_col401 = self.order_col()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_order_col.add(order_col401.tree)


                    else:
                        break #loop112

                # AST Rewrite
                # elements: order_col
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 532:15: -> ( order_col )+
                    # QueryParser.g:532:18: ( order_col )+
                    if not (stream_order_col.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_order_col.hasNext():
                        self._adaptor.addChild(root_0, stream_order_col.nextTree())


                    stream_order_col.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "order_col_list"

    class order_col_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.order_col_return, self).__init__()

            self.tree = None




    # $ANTLR start "order_col"
    # QueryParser.g:535:1: order_col : ( col_range ( ASC | DESC )? | col_ref ( ASC | DESC )? | LEFT_PAREN col_ref ( ASC | DESC )? RIGHT_PAREN );
    def order_col(self, ):

        retval = self.order_col_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set403 = None
        set405 = None
        LEFT_PAREN406 = None
        set408 = None
        RIGHT_PAREN409 = None
        col_range402 = None

        col_ref404 = None

        col_ref407 = None


        set403_tree = None
        set405_tree = None
        LEFT_PAREN406_tree = None
        set408_tree = None
        RIGHT_PAREN409_tree = None

        try:
            try:
                # QueryParser.g:535:11: ( col_range ( ASC | DESC )? | col_ref ( ASC | DESC )? | LEFT_PAREN col_ref ( ASC | DESC )? RIGHT_PAREN )
                alt116 = 3
                LA116 = self.input.LA(1)
                if LA116 == GROUP:
                    LA116_1 = self.input.LA(2)

                    if (LA116_1 == DOUBLE_PERIOD) :
                        alt116 = 1
                    elif (LA116_1 == EOF or LA116_1 == USING or LA116_1 == PARALLEL or (ASC <= LA116_1 <= DESC) or LA116_1 == SEMI_COLON or LA116_1 == RIGHT_PAREN or LA116_1 == COMMA) :
                        alt116 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 116, 1, self.input)

                        raise nvae

                elif LA116 == CUBE:
                    LA116_2 = self.input.LA(2)

                    if (LA116_2 == EOF or LA116_2 == USING or LA116_2 == PARALLEL or (ASC <= LA116_2 <= DESC) or LA116_2 == SEMI_COLON or LA116_2 == RIGHT_PAREN or LA116_2 == COMMA) :
                        alt116 = 2
                    elif (LA116_2 == DOUBLE_PERIOD) :
                        alt116 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 116, 2, self.input)

                        raise nvae

                elif LA116 == IDENTIFIER_L:
                    LA116_3 = self.input.LA(2)

                    if (LA116_3 == EOF or LA116_3 == USING or LA116_3 == PARALLEL or (ASC <= LA116_3 <= DESC) or LA116_3 == SEMI_COLON or LA116_3 == RIGHT_PAREN or LA116_3 == COMMA) :
                        alt116 = 2
                    elif (LA116_3 == DOUBLE_PERIOD) :
                        alt116 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 116, 3, self.input)

                        raise nvae

                elif LA116 == DOLLARVAR:
                    LA116_4 = self.input.LA(2)

                    if (LA116_4 == DOUBLE_PERIOD) :
                        alt116 = 1
                    elif (LA116_4 == EOF or LA116_4 == USING or LA116_4 == PARALLEL or (ASC <= LA116_4 <= DESC) or LA116_4 == SEMI_COLON or LA116_4 == RIGHT_PAREN or LA116_4 == COMMA) :
                        alt116 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 116, 4, self.input)

                        raise nvae

                elif LA116 == DOUBLE_PERIOD:
                    alt116 = 1
                elif LA116 == LEFT_PAREN:
                    alt116 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 116, 0, self.input)

                    raise nvae

                if alt116 == 1:
                    # QueryParser.g:535:13: col_range ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_order_col4089)
                    col_range402 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range402.tree)
                    # QueryParser.g:535:23: ( ASC | DESC )?
                    alt113 = 2
                    LA113_0 = self.input.LA(1)

                    if ((ASC <= LA113_0 <= DESC)) :
                        alt113 = 1
                    if alt113 == 1:
                        # QueryParser.g:
                        pass 
                        set403 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set403))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                elif alt116 == 2:
                    # QueryParser.g:536:13: col_ref ( ASC | DESC )?
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_ref_in_order_col4112)
                    col_ref404 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_ref404.tree)
                    # QueryParser.g:536:21: ( ASC | DESC )?
                    alt114 = 2
                    LA114_0 = self.input.LA(1)

                    if ((ASC <= LA114_0 <= DESC)) :
                        alt114 = 1
                    if alt114 == 1:
                        # QueryParser.g:
                        pass 
                        set405 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set405))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse







                elif alt116 == 3:
                    # QueryParser.g:537:13: LEFT_PAREN col_ref ( ASC | DESC )? RIGHT_PAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LEFT_PAREN406=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_order_col4139)
                    self._state.following.append(self.FOLLOW_col_ref_in_order_col4142)
                    col_ref407 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_ref407.tree)
                    # QueryParser.g:537:33: ( ASC | DESC )?
                    alt115 = 2
                    LA115_0 = self.input.LA(1)

                    if ((ASC <= LA115_0 <= DESC)) :
                        alt115 = 1
                    if alt115 == 1:
                        # QueryParser.g:
                        pass 
                        set408 = self.input.LT(1)
                        if (ASC <= self.input.LA(1) <= DESC):
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set408))
                            self._state.errorRecovery = False

                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            mse = MismatchedSetException(None, self.input)
                            raise mse





                    RIGHT_PAREN409=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_order_col4155)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "order_col"

    class distinct_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.distinct_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "distinct_clause"
    # QueryParser.g:540:1: distinct_clause : DISTINCT rel ( partition_clause )? ;
    def distinct_clause(self, ):

        retval = self.distinct_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DISTINCT410 = None
        rel411 = None

        partition_clause412 = None


        DISTINCT410_tree = None

        try:
            try:
                # QueryParser.g:540:17: ( DISTINCT rel ( partition_clause )? )
                # QueryParser.g:540:19: DISTINCT rel ( partition_clause )?
                pass 
                root_0 = self._adaptor.nil()

                DISTINCT410=self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_distinct_clause4165)
                if self._state.backtracking == 0:

                    DISTINCT410_tree = self._adaptor.createWithPayload(DISTINCT410)
                    root_0 = self._adaptor.becomeRoot(DISTINCT410_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_distinct_clause4168)
                rel411 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel411.tree)
                # QueryParser.g:540:33: ( partition_clause )?
                alt117 = 2
                LA117_0 = self.input.LA(1)

                if (LA117_0 == PARTITION) :
                    alt117 = 1
                if alt117 == 1:
                    # QueryParser.g:0:0: partition_clause
                    pass 
                    self._state.following.append(self.FOLLOW_partition_clause_in_distinct_clause4170)
                    partition_clause412 = self.partition_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, partition_clause412.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "distinct_clause"

    class partition_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.partition_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "partition_clause"
    # QueryParser.g:543:1: partition_clause : PARTITION BY func_name ;
    def partition_clause(self, ):

        retval = self.partition_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PARTITION413 = None
        BY414 = None
        func_name415 = None


        PARTITION413_tree = None
        BY414_tree = None

        try:
            try:
                # QueryParser.g:543:18: ( PARTITION BY func_name )
                # QueryParser.g:543:20: PARTITION BY func_name
                pass 
                root_0 = self._adaptor.nil()

                PARTITION413=self.match(self.input, PARTITION, self.FOLLOW_PARTITION_in_partition_clause4180)
                if self._state.backtracking == 0:

                    PARTITION413_tree = self._adaptor.createWithPayload(PARTITION413)
                    root_0 = self._adaptor.becomeRoot(PARTITION413_tree, root_0)

                BY414=self.match(self.input, BY, self.FOLLOW_BY_in_partition_clause4183)
                self._state.following.append(self.FOLLOW_func_name_in_partition_clause4186)
                func_name415 = self.func_name()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, func_name415.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "partition_clause"

    class cross_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cross_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "cross_clause"
    # QueryParser.g:546:1: cross_clause : CROSS rel_list ( partition_clause )? ;
    def cross_clause(self, ):

        retval = self.cross_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CROSS416 = None
        rel_list417 = None

        partition_clause418 = None


        CROSS416_tree = None

        try:
            try:
                # QueryParser.g:546:14: ( CROSS rel_list ( partition_clause )? )
                # QueryParser.g:546:16: CROSS rel_list ( partition_clause )?
                pass 
                root_0 = self._adaptor.nil()

                CROSS416=self.match(self.input, CROSS, self.FOLLOW_CROSS_in_cross_clause4195)
                if self._state.backtracking == 0:

                    CROSS416_tree = self._adaptor.createWithPayload(CROSS416)
                    root_0 = self._adaptor.becomeRoot(CROSS416_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_list_in_cross_clause4198)
                rel_list417 = self.rel_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel_list417.tree)
                # QueryParser.g:546:32: ( partition_clause )?
                alt118 = 2
                LA118_0 = self.input.LA(1)

                if (LA118_0 == PARTITION) :
                    alt118 = 1
                if alt118 == 1:
                    # QueryParser.g:0:0: partition_clause
                    pass 
                    self._state.following.append(self.FOLLOW_partition_clause_in_cross_clause4200)
                    partition_clause418 = self.partition_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, partition_clause418.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cross_clause"

    class rel_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_list"
    # QueryParser.g:549:1: rel_list : rel ( COMMA rel )* -> ( rel )+ ;
    def rel_list(self, ):

        retval = self.rel_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA420 = None
        rel419 = None

        rel421 = None


        COMMA420_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_rel = RewriteRuleSubtreeStream(self._adaptor, "rule rel")
        try:
            try:
                # QueryParser.g:549:10: ( rel ( COMMA rel )* -> ( rel )+ )
                # QueryParser.g:549:12: rel ( COMMA rel )*
                pass 
                self._state.following.append(self.FOLLOW_rel_in_rel_list4210)
                rel419 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rel.add(rel419.tree)
                # QueryParser.g:549:16: ( COMMA rel )*
                while True: #loop119
                    alt119 = 2
                    LA119_0 = self.input.LA(1)

                    if (LA119_0 == COMMA) :
                        alt119 = 1


                    if alt119 == 1:
                        # QueryParser.g:549:18: COMMA rel
                        pass 
                        COMMA420=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_rel_list4214) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA420)
                        self._state.following.append(self.FOLLOW_rel_in_rel_list4216)
                        rel421 = self.rel()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rel.add(rel421.tree)


                    else:
                        break #loop119

                # AST Rewrite
                # elements: rel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 550:9: -> ( rel )+
                    # QueryParser.g:550:12: ( rel )+
                    if not (stream_rel.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rel.hasNext():
                        self._adaptor.addChild(root_0, stream_rel.nextTree())


                    stream_rel.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_list"

    class join_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_clause"
    # QueryParser.g:553:1: join_clause : JOIN join_sub_clause ( USING join_type )? ( partition_clause )? ;
    def join_clause(self, ):

        retval = self.join_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        JOIN422 = None
        USING424 = None
        join_sub_clause423 = None

        join_type425 = None

        partition_clause426 = None


        JOIN422_tree = None
        USING424_tree = None

        try:
            try:
                # QueryParser.g:553:13: ( JOIN join_sub_clause ( USING join_type )? ( partition_clause )? )
                # QueryParser.g:553:15: JOIN join_sub_clause ( USING join_type )? ( partition_clause )?
                pass 
                root_0 = self._adaptor.nil()

                JOIN422=self.match(self.input, JOIN, self.FOLLOW_JOIN_in_join_clause4241)
                if self._state.backtracking == 0:

                    JOIN422_tree = self._adaptor.createWithPayload(JOIN422)
                    root_0 = self._adaptor.becomeRoot(JOIN422_tree, root_0)

                self._state.following.append(self.FOLLOW_join_sub_clause_in_join_clause4244)
                join_sub_clause423 = self.join_sub_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, join_sub_clause423.tree)
                # QueryParser.g:553:37: ( USING join_type )?
                alt120 = 2
                LA120_0 = self.input.LA(1)

                if (LA120_0 == USING) :
                    alt120 = 1
                if alt120 == 1:
                    # QueryParser.g:553:39: USING join_type
                    pass 
                    USING424=self.match(self.input, USING, self.FOLLOW_USING_in_join_clause4248)
                    self._state.following.append(self.FOLLOW_join_type_in_join_clause4251)
                    join_type425 = self.join_type()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_type425.tree)



                # QueryParser.g:553:59: ( partition_clause )?
                alt121 = 2
                LA121_0 = self.input.LA(1)

                if (LA121_0 == PARTITION) :
                    alt121 = 1
                if alt121 == 1:
                    # QueryParser.g:0:0: partition_clause
                    pass 
                    self._state.following.append(self.FOLLOW_partition_clause_in_join_clause4256)
                    partition_clause426 = self.partition_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, partition_clause426.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_clause"

    class join_type_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_type_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_type"
    # QueryParser.g:556:1: join_type : QUOTEDSTRING ;
    def join_type(self, ):

        retval = self.join_type_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING427 = None

        QUOTEDSTRING427_tree = None

        try:
            try:
                # QueryParser.g:556:11: ( QUOTEDSTRING )
                # QueryParser.g:556:13: QUOTEDSTRING
                pass 
                root_0 = self._adaptor.nil()

                QUOTEDSTRING427=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_join_type4266)
                if self._state.backtracking == 0:

                    QUOTEDSTRING427_tree = self._adaptor.createWithPayload(QUOTEDSTRING427)
                    self._adaptor.addChild(root_0, QUOTEDSTRING427_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_type"

    class join_sub_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_sub_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_sub_clause"
    # QueryParser.g:559:1: join_sub_clause : ( join_item ( LEFT | RIGHT | FULL ) ( OUTER )? COMMA join_item | join_item_list );
    def join_sub_clause(self, ):

        retval = self.join_sub_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set429 = None
        OUTER430 = None
        COMMA431 = None
        join_item428 = None

        join_item432 = None

        join_item_list433 = None


        set429_tree = None
        OUTER430_tree = None
        COMMA431_tree = None

        try:
            try:
                # QueryParser.g:559:17: ( join_item ( LEFT | RIGHT | FULL ) ( OUTER )? COMMA join_item | join_item_list )
                alt123 = 2
                LA123_0 = self.input.LA(1)

                if (LA123_0 == IDENTIFIER_L) :
                    LA123_1 = self.input.LA(2)

                    if (((self.synpred198_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))) :
                        alt123 = 1
                    elif ((!input.LT(1).getText().equalsIgnoreCase("NULL"))) :
                        alt123 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 123, 1, self.input)

                        raise nvae

                elif (LA123_0 == LEFT_PAREN) :
                    LA123_2 = self.input.LA(2)

                    if (self.synpred198_QueryParser()) :
                        alt123 = 1
                    elif (True) :
                        alt123 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 123, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 123, 0, self.input)

                    raise nvae

                if alt123 == 1:
                    # QueryParser.g:559:19: join_item ( LEFT | RIGHT | FULL ) ( OUTER )? COMMA join_item
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_join_item_in_join_sub_clause4275)
                    join_item428 = self.join_item()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_item428.tree)
                    set429 = self.input.LT(1)
                    if (LEFT <= self.input.LA(1) <= FULL):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set429))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse


                    # QueryParser.g:559:53: ( OUTER )?
                    alt122 = 2
                    LA122_0 = self.input.LA(1)

                    if (LA122_0 == OUTER) :
                        alt122 = 1
                    if alt122 == 1:
                        # QueryParser.g:0:0: OUTER
                        pass 
                        OUTER430=self.match(self.input, OUTER, self.FOLLOW_OUTER_in_join_sub_clause4291)
                        if self._state.backtracking == 0:

                            OUTER430_tree = self._adaptor.createWithPayload(OUTER430)
                            self._adaptor.addChild(root_0, OUTER430_tree)




                    COMMA431=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_join_sub_clause4294)
                    self._state.following.append(self.FOLLOW_join_item_in_join_sub_clause4297)
                    join_item432 = self.join_item()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_item432.tree)


                elif alt123 == 2:
                    # QueryParser.g:560:19: join_item_list
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_join_item_list_in_join_sub_clause4317)
                    join_item_list433 = self.join_item_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_item_list433.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_sub_clause"

    class join_item_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_item_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_item_list"
    # QueryParser.g:563:1: join_item_list : join_item ( COMMA join_item )+ ;
    def join_item_list(self, ):

        retval = self.join_item_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA435 = None
        join_item434 = None

        join_item436 = None


        COMMA435_tree = None

        try:
            try:
                # QueryParser.g:563:16: ( join_item ( COMMA join_item )+ )
                # QueryParser.g:563:18: join_item ( COMMA join_item )+
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_join_item_in_join_item_list4326)
                join_item434 = self.join_item()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, join_item434.tree)
                # QueryParser.g:563:28: ( COMMA join_item )+
                cnt124 = 0
                while True: #loop124
                    alt124 = 2
                    LA124_0 = self.input.LA(1)

                    if (LA124_0 == COMMA) :
                        alt124 = 1


                    if alt124 == 1:
                        # QueryParser.g:563:30: COMMA join_item
                        pass 
                        COMMA435=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_join_item_list4330)
                        self._state.following.append(self.FOLLOW_join_item_in_join_item_list4333)
                        join_item436 = self.join_item()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, join_item436.tree)


                    else:
                        if cnt124 >= 1:
                            break #loop124

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(124, self.input)
                        raise eee

                    cnt124 += 1



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_item_list"

    class join_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_item"
    # QueryParser.g:566:1: join_item : rel join_group_by_clause -> ^( JOIN_ITEM rel join_group_by_clause ) ;
    def join_item(self, ):

        retval = self.join_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        rel437 = None

        join_group_by_clause438 = None


        stream_rel = RewriteRuleSubtreeStream(self._adaptor, "rule rel")
        stream_join_group_by_clause = RewriteRuleSubtreeStream(self._adaptor, "rule join_group_by_clause")
        try:
            try:
                # QueryParser.g:566:11: ( rel join_group_by_clause -> ^( JOIN_ITEM rel join_group_by_clause ) )
                # QueryParser.g:566:13: rel join_group_by_clause
                pass 
                self._state.following.append(self.FOLLOW_rel_in_join_item4345)
                rel437 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rel.add(rel437.tree)
                self._state.following.append(self.FOLLOW_join_group_by_clause_in_join_item4347)
                join_group_by_clause438 = self.join_group_by_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_join_group_by_clause.add(join_group_by_clause438.tree)

                # AST Rewrite
                # elements: rel, join_group_by_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 567:10: -> ^( JOIN_ITEM rel join_group_by_clause )
                    # QueryParser.g:567:13: ^( JOIN_ITEM rel join_group_by_clause )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(JOIN_ITEM, "JOIN_ITEM"), root_1)

                    self._adaptor.addChild(root_1, stream_rel.nextTree())
                    self._adaptor.addChild(root_1, stream_join_group_by_clause.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_item"

    class join_group_by_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_group_by_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_group_by_clause"
    # QueryParser.g:570:1: join_group_by_clause : BY join_group_by_expr_list ;
    def join_group_by_clause(self, ):

        retval = self.join_group_by_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BY439 = None
        join_group_by_expr_list440 = None


        BY439_tree = None

        try:
            try:
                # QueryParser.g:570:22: ( BY join_group_by_expr_list )
                # QueryParser.g:570:24: BY join_group_by_expr_list
                pass 
                root_0 = self._adaptor.nil()

                BY439=self.match(self.input, BY, self.FOLLOW_BY_in_join_group_by_clause4378)
                if self._state.backtracking == 0:

                    BY439_tree = self._adaptor.createWithPayload(BY439)
                    root_0 = self._adaptor.becomeRoot(BY439_tree, root_0)

                self._state.following.append(self.FOLLOW_join_group_by_expr_list_in_join_group_by_clause4381)
                join_group_by_expr_list440 = self.join_group_by_expr_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, join_group_by_expr_list440.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_group_by_clause"

    class join_group_by_expr_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_group_by_expr_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_group_by_expr_list"
    # QueryParser.g:573:1: join_group_by_expr_list : ( LEFT_PAREN join_group_by_expr ( COMMA join_group_by_expr )* RIGHT_PAREN -> ( join_group_by_expr )+ | join_group_by_expr );
    def join_group_by_expr_list(self, ):

        retval = self.join_group_by_expr_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN441 = None
        COMMA443 = None
        RIGHT_PAREN445 = None
        join_group_by_expr442 = None

        join_group_by_expr444 = None

        join_group_by_expr446 = None


        LEFT_PAREN441_tree = None
        COMMA443_tree = None
        RIGHT_PAREN445_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_join_group_by_expr = RewriteRuleSubtreeStream(self._adaptor, "rule join_group_by_expr")
        try:
            try:
                # QueryParser.g:573:25: ( LEFT_PAREN join_group_by_expr ( COMMA join_group_by_expr )* RIGHT_PAREN -> ( join_group_by_expr )+ | join_group_by_expr )
                alt126 = 2
                alt126 = self.dfa126.predict(self.input)
                if alt126 == 1:
                    # QueryParser.g:573:27: LEFT_PAREN join_group_by_expr ( COMMA join_group_by_expr )* RIGHT_PAREN
                    pass 
                    LEFT_PAREN441=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_join_group_by_expr_list4390) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN441)
                    self._state.following.append(self.FOLLOW_join_group_by_expr_in_join_group_by_expr_list4392)
                    join_group_by_expr442 = self.join_group_by_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_join_group_by_expr.add(join_group_by_expr442.tree)
                    # QueryParser.g:573:57: ( COMMA join_group_by_expr )*
                    while True: #loop125
                        alt125 = 2
                        LA125_0 = self.input.LA(1)

                        if (LA125_0 == COMMA) :
                            alt125 = 1


                        if alt125 == 1:
                            # QueryParser.g:573:59: COMMA join_group_by_expr
                            pass 
                            COMMA443=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_join_group_by_expr_list4396) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA443)
                            self._state.following.append(self.FOLLOW_join_group_by_expr_in_join_group_by_expr_list4398)
                            join_group_by_expr444 = self.join_group_by_expr()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_join_group_by_expr.add(join_group_by_expr444.tree)


                        else:
                            break #loop125
                    RIGHT_PAREN445=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_join_group_by_expr_list4403) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN445)

                    # AST Rewrite
                    # elements: join_group_by_expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 574:24: -> ( join_group_by_expr )+
                        # QueryParser.g:574:27: ( join_group_by_expr )+
                        if not (stream_join_group_by_expr.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_join_group_by_expr.hasNext():
                            self._adaptor.addChild(root_0, stream_join_group_by_expr.nextTree())


                        stream_join_group_by_expr.reset()



                        retval.tree = root_0


                elif alt126 == 2:
                    # QueryParser.g:575:27: join_group_by_expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_join_group_by_expr_in_join_group_by_expr_list4459)
                    join_group_by_expr446 = self.join_group_by_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, join_group_by_expr446.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_group_by_expr_list"

    class join_group_by_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.join_group_by_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "join_group_by_expr"
    # QueryParser.g:578:1: join_group_by_expr : ( col_range | expr | STAR );
    def join_group_by_expr(self, ):

        retval = self.join_group_by_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STAR449 = None
        col_range447 = None

        expr448 = None


        STAR449_tree = None

        try:
            try:
                # QueryParser.g:578:20: ( col_range | expr | STAR )
                alt127 = 3
                LA127 = self.input.LA(1)
                if LA127 == GROUP:
                    LA127_1 = self.input.LA(2)

                    if (LA127_1 == EOF or (USING <= LA127_1 <= OUTER) or (PARALLEL <= LA127_1 <= PARTITION) or (LEFT <= LA127_1 <= FULL) or LA127_1 == PERIOD or LA127_1 == DOLLAR or (MINUS <= LA127_1 <= PLUS) or LA127_1 == STAR or (SEMI_COLON <= LA127_1 <= RIGHT_PAREN) or LA127_1 == POUND or LA127_1 == COMMA or (DIV <= LA127_1 <= PERCENT)) :
                        alt127 = 2
                    elif (LA127_1 == DOUBLE_PERIOD) :
                        alt127 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 127, 1, self.input)

                        raise nvae

                elif LA127 == CUBE:
                    LA127_2 = self.input.LA(2)

                    if (LA127_2 == EOF or (USING <= LA127_2 <= OUTER) or (PARALLEL <= LA127_2 <= PARTITION) or (LEFT <= LA127_2 <= FULL) or LA127_2 == PERIOD or LA127_2 == DOLLAR or (MINUS <= LA127_2 <= PLUS) or LA127_2 == STAR or (SEMI_COLON <= LA127_2 <= RIGHT_PAREN) or LA127_2 == POUND or LA127_2 == COMMA or (DIV <= LA127_2 <= PERCENT)) :
                        alt127 = 2
                    elif (LA127_2 == DOUBLE_PERIOD) :
                        alt127 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 127, 2, self.input)

                        raise nvae

                elif LA127 == IDENTIFIER_L:
                    LA127_3 = self.input.LA(2)

                    if (LA127_3 == EOF or (USING <= LA127_3 <= OUTER) or (PARALLEL <= LA127_3 <= PARTITION) or (LEFT <= LA127_3 <= FULL) or LA127_3 == PERIOD or LA127_3 == DOLLAR or (MINUS <= LA127_3 <= PLUS) or LA127_3 == STAR or (SEMI_COLON <= LA127_3 <= RIGHT_PAREN) or LA127_3 == POUND or LA127_3 == COMMA or (DIV <= LA127_3 <= PERCENT)) :
                        alt127 = 2
                    elif (LA127_3 == DOUBLE_PERIOD) :
                        alt127 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 127, 3, self.input)

                        raise nvae

                elif LA127 == DOLLARVAR:
                    LA127_4 = self.input.LA(2)

                    if (LA127_4 == DOUBLE_PERIOD) :
                        alt127 = 1
                    elif (LA127_4 == EOF or (USING <= LA127_4 <= OUTER) or (PARALLEL <= LA127_4 <= PARTITION) or (LEFT <= LA127_4 <= FULL) or LA127_4 == PERIOD or (MINUS <= LA127_4 <= PLUS) or LA127_4 == STAR or LA127_4 == SEMI_COLON or LA127_4 == RIGHT_PAREN or LA127_4 == POUND or LA127_4 == COMMA or (DIV <= LA127_4 <= PERCENT)) :
                        alt127 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 127, 4, self.input)

                        raise nvae

                elif LA127 == DOUBLE_PERIOD:
                    alt127 = 1
                elif LA127 == IMPORT or LA127 == RETURNS or LA127 == DEFINE or LA127 == LOAD or LA127 == FILTER or LA127 == FOREACH or LA127 == ORDER or LA127 == ROLLUP or LA127 == DISTINCT or LA127 == COGROUP or LA127 == JOIN or LA127 == CROSS or LA127 == UNION or LA127 == SPLIT or LA127 == INTO or LA127 == IF or LA127 == ALL or LA127 == AS or LA127 == BY or LA127 == USING or LA127 == INNER or LA127 == OUTER or LA127 == PARALLEL or LA127 == PARTITION or LA127 == AND or LA127 == OR or LA127 == NOT or LA127 == GENERATE or LA127 == FLATTEN or LA127 == ASC or LA127 == DESC or LA127 == INT or LA127 == LONG or LA127 == FLOAT or LA127 == DOUBLE or LA127 == DATETIME or LA127 == CHARARRAY or LA127 == BYTEARRAY or LA127 == BAG or LA127 == TUPLE or LA127 == MAP or LA127 == IS or LA127 == STREAM or LA127 == THROUGH or LA127 == STORE or LA127 == MAPREDUCE or LA127 == SHIP or LA127 == CACHE or LA127 == INPUT or LA127 == OUTPUT or LA127 == STDERROR or LA127 == STDIN or LA127 == STDOUT or LA127 == LIMIT or LA127 == SAMPLE or LA127 == LEFT or LA127 == RIGHT or LA127 == FULL or LA127 == STR_OP_EQ or LA127 == STR_OP_GT or LA127 == STR_OP_LT or LA127 == STR_OP_GTE or LA127 == STR_OP_LTE or LA127 == STR_OP_NE or LA127 == STR_OP_MATCHES or LA127 == TRUE or LA127 == FALSE or LA127 == INTEGER or LA127 == LONGINTEGER or LA127 == MINUS or LA127 == DOUBLENUMBER or LA127 == FLOATNUMBER or LA127 == QUOTEDSTRING or LA127 == LEFT_PAREN or LA127 == LEFT_CURLY or LA127 == LEFT_BRACKET or LA127 == BOOL or LA127 == REALIAS:
                    alt127 = 2
                elif LA127 == STAR:
                    alt127 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 127, 0, self.input)

                    raise nvae

                if alt127 == 1:
                    # QueryParser.g:578:22: col_range
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_join_group_by_expr4468)
                    col_range447 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range447.tree)


                elif alt127 == 2:
                    # QueryParser.g:578:35: expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_join_group_by_expr4473)
                    expr448 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr448.tree)


                elif alt127 == 3:
                    # QueryParser.g:578:42: STAR
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR449=self.match(self.input, STAR, self.FOLLOW_STAR_in_join_group_by_expr4477)
                    if self._state.backtracking == 0:

                        STAR449_tree = self._adaptor.createWithPayload(STAR449)
                        self._adaptor.addChild(root_0, STAR449_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "join_group_by_expr"

    class union_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.union_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "union_clause"
    # QueryParser.g:581:1: union_clause : UNION ( ONSCHEMA )? rel_list ;
    def union_clause(self, ):

        retval = self.union_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        UNION450 = None
        ONSCHEMA451 = None
        rel_list452 = None


        UNION450_tree = None
        ONSCHEMA451_tree = None

        try:
            try:
                # QueryParser.g:581:14: ( UNION ( ONSCHEMA )? rel_list )
                # QueryParser.g:581:16: UNION ( ONSCHEMA )? rel_list
                pass 
                root_0 = self._adaptor.nil()

                UNION450=self.match(self.input, UNION, self.FOLLOW_UNION_in_union_clause4486)
                if self._state.backtracking == 0:

                    UNION450_tree = self._adaptor.createWithPayload(UNION450)
                    root_0 = self._adaptor.becomeRoot(UNION450_tree, root_0)

                # QueryParser.g:581:23: ( ONSCHEMA )?
                alt128 = 2
                LA128_0 = self.input.LA(1)

                if (LA128_0 == ONSCHEMA) :
                    alt128 = 1
                if alt128 == 1:
                    # QueryParser.g:0:0: ONSCHEMA
                    pass 
                    ONSCHEMA451=self.match(self.input, ONSCHEMA, self.FOLLOW_ONSCHEMA_in_union_clause4489)
                    if self._state.backtracking == 0:

                        ONSCHEMA451_tree = self._adaptor.createWithPayload(ONSCHEMA451)
                        self._adaptor.addChild(root_0, ONSCHEMA451_tree)




                self._state.following.append(self.FOLLOW_rel_list_in_union_clause4492)
                rel_list452 = self.rel_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel_list452.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "union_clause"

    class foreach_clause_simple_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_clause_simple_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_clause_simple"
    # QueryParser.g:584:1: foreach_clause_simple : FOREACH rel foreach_plan_simple ;
    def foreach_clause_simple(self, ):

        retval = self.foreach_clause_simple_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FOREACH453 = None
        rel454 = None

        foreach_plan_simple455 = None


        FOREACH453_tree = None

        try:
            try:
                # QueryParser.g:584:23: ( FOREACH rel foreach_plan_simple )
                # QueryParser.g:584:25: FOREACH rel foreach_plan_simple
                pass 
                root_0 = self._adaptor.nil()

                FOREACH453=self.match(self.input, FOREACH, self.FOLLOW_FOREACH_in_foreach_clause_simple4501)
                if self._state.backtracking == 0:

                    FOREACH453_tree = self._adaptor.createWithPayload(FOREACH453)
                    root_0 = self._adaptor.becomeRoot(FOREACH453_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_foreach_clause_simple4504)
                rel454 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel454.tree)
                self._state.following.append(self.FOLLOW_foreach_plan_simple_in_foreach_clause_simple4506)
                foreach_plan_simple455 = self.foreach_plan_simple()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, foreach_plan_simple455.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_clause_simple"

    class foreach_plan_simple_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_plan_simple_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_plan_simple"
    # QueryParser.g:587:1: foreach_plan_simple : generate_clause -> ^( FOREACH_PLAN_SIMPLE generate_clause ) ;
    def foreach_plan_simple(self, ):

        retval = self.foreach_plan_simple_return()
        retval.start = self.input.LT(1)

        root_0 = None

        generate_clause456 = None


        stream_generate_clause = RewriteRuleSubtreeStream(self._adaptor, "rule generate_clause")
        try:
            try:
                # QueryParser.g:587:21: ( generate_clause -> ^( FOREACH_PLAN_SIMPLE generate_clause ) )
                # QueryParser.g:587:23: generate_clause
                pass 
                self._state.following.append(self.FOLLOW_generate_clause_in_foreach_plan_simple4515)
                generate_clause456 = self.generate_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_generate_clause.add(generate_clause456.tree)

                # AST Rewrite
                # elements: generate_clause
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 588:20: -> ^( FOREACH_PLAN_SIMPLE generate_clause )
                    # QueryParser.g:588:23: ^( FOREACH_PLAN_SIMPLE generate_clause )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOREACH_PLAN_SIMPLE, "FOREACH_PLAN_SIMPLE"), root_1)

                    self._adaptor.addChild(root_1, stream_generate_clause.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_plan_simple"

    class foreach_clause_complex_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_clause_complex_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_clause_complex"
    # QueryParser.g:591:1: foreach_clause_complex : FOREACH rel foreach_plan_complex ;
    def foreach_clause_complex(self, ):

        retval = self.foreach_clause_complex_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FOREACH457 = None
        rel458 = None

        foreach_plan_complex459 = None


        FOREACH457_tree = None

        try:
            try:
                # QueryParser.g:591:24: ( FOREACH rel foreach_plan_complex )
                # QueryParser.g:591:26: FOREACH rel foreach_plan_complex
                pass 
                root_0 = self._adaptor.nil()

                FOREACH457=self.match(self.input, FOREACH, self.FOLLOW_FOREACH_in_foreach_clause_complex4553)
                if self._state.backtracking == 0:

                    FOREACH457_tree = self._adaptor.createWithPayload(FOREACH457)
                    root_0 = self._adaptor.becomeRoot(FOREACH457_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_foreach_clause_complex4556)
                rel458 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel458.tree)
                self._state.following.append(self.FOLLOW_foreach_plan_complex_in_foreach_clause_complex4558)
                foreach_plan_complex459 = self.foreach_plan_complex()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, foreach_plan_complex459.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_clause_complex"

    class foreach_plan_complex_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.foreach_plan_complex_return, self).__init__()

            self.tree = None




    # $ANTLR start "foreach_plan_complex"
    # QueryParser.g:594:1: foreach_plan_complex : nested_blk -> ^( FOREACH_PLAN_COMPLEX nested_blk ) ;
    def foreach_plan_complex(self, ):

        retval = self.foreach_plan_complex_return()
        retval.start = self.input.LT(1)

        root_0 = None

        nested_blk460 = None


        stream_nested_blk = RewriteRuleSubtreeStream(self._adaptor, "rule nested_blk")
        try:
            try:
                # QueryParser.g:594:22: ( nested_blk -> ^( FOREACH_PLAN_COMPLEX nested_blk ) )
                # QueryParser.g:594:24: nested_blk
                pass 
                self._state.following.append(self.FOLLOW_nested_blk_in_foreach_plan_complex4567)
                nested_blk460 = self.nested_blk()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_nested_blk.add(nested_blk460.tree)

                # AST Rewrite
                # elements: nested_blk
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 595:21: -> ^( FOREACH_PLAN_COMPLEX nested_blk )
                    # QueryParser.g:595:24: ^( FOREACH_PLAN_COMPLEX nested_blk )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(FOREACH_PLAN_COMPLEX, "FOREACH_PLAN_COMPLEX"), root_1)

                    self._adaptor.addChild(root_1, stream_nested_blk.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "foreach_plan_complex"

    class cube_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_clause"
    # QueryParser.g:598:1: cube_clause : CUBE cube_item ;
    def cube_clause(self, ):

        retval = self.cube_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CUBE461 = None
        cube_item462 = None


        CUBE461_tree = None

        try:
            try:
                # QueryParser.g:598:13: ( CUBE cube_item )
                # QueryParser.g:598:15: CUBE cube_item
                pass 
                root_0 = self._adaptor.nil()

                CUBE461=self.match(self.input, CUBE, self.FOLLOW_CUBE_in_cube_clause4606)
                if self._state.backtracking == 0:

                    CUBE461_tree = self._adaptor.createWithPayload(CUBE461)
                    root_0 = self._adaptor.becomeRoot(CUBE461_tree, root_0)

                self._state.following.append(self.FOLLOW_cube_item_in_cube_clause4609)
                cube_item462 = self.cube_item()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cube_item462.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_clause"

    class cube_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_item_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_item"
    # QueryParser.g:601:1: cube_item : rel ( cube_by_clause ) ;
    def cube_item(self, ):

        retval = self.cube_item_return()
        retval.start = self.input.LT(1)

        root_0 = None

        rel463 = None

        cube_by_clause464 = None



        try:
            try:
                # QueryParser.g:601:11: ( rel ( cube_by_clause ) )
                # QueryParser.g:601:13: rel ( cube_by_clause )
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_rel_in_cube_item4619)
                rel463 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel463.tree)
                # QueryParser.g:601:17: ( cube_by_clause )
                # QueryParser.g:601:19: cube_by_clause
                pass 
                self._state.following.append(self.FOLLOW_cube_by_clause_in_cube_item4623)
                cube_by_clause464 = self.cube_by_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cube_by_clause464.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_item"

    class cube_by_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_by_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_by_clause"
    # QueryParser.g:604:1: cube_by_clause : BY cube_or_rollup ;
    def cube_by_clause(self, ):

        retval = self.cube_by_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BY465 = None
        cube_or_rollup466 = None


        BY465_tree = None

        try:
            try:
                # QueryParser.g:604:16: ( BY cube_or_rollup )
                # QueryParser.g:604:18: BY cube_or_rollup
                pass 
                root_0 = self._adaptor.nil()

                BY465=self.match(self.input, BY, self.FOLLOW_BY_in_cube_by_clause4634)
                if self._state.backtracking == 0:

                    BY465_tree = self._adaptor.createWithPayload(BY465)
                    root_0 = self._adaptor.becomeRoot(BY465_tree, root_0)

                self._state.following.append(self.FOLLOW_cube_or_rollup_in_cube_by_clause4637)
                cube_or_rollup466 = self.cube_or_rollup()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cube_or_rollup466.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_by_clause"

    class cube_or_rollup_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_or_rollup_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_or_rollup"
    # QueryParser.g:607:1: cube_or_rollup : cube_rollup_list ( COMMA cube_rollup_list )* -> ( cube_rollup_list )+ ;
    def cube_or_rollup(self, ):

        retval = self.cube_or_rollup_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA468 = None
        cube_rollup_list467 = None

        cube_rollup_list469 = None


        COMMA468_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_cube_rollup_list = RewriteRuleSubtreeStream(self._adaptor, "rule cube_rollup_list")
        try:
            try:
                # QueryParser.g:607:16: ( cube_rollup_list ( COMMA cube_rollup_list )* -> ( cube_rollup_list )+ )
                # QueryParser.g:607:18: cube_rollup_list ( COMMA cube_rollup_list )*
                pass 
                self._state.following.append(self.FOLLOW_cube_rollup_list_in_cube_or_rollup4646)
                cube_rollup_list467 = self.cube_rollup_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_cube_rollup_list.add(cube_rollup_list467.tree)
                # QueryParser.g:607:35: ( COMMA cube_rollup_list )*
                while True: #loop129
                    alt129 = 2
                    LA129_0 = self.input.LA(1)

                    if (LA129_0 == COMMA) :
                        alt129 = 1


                    if alt129 == 1:
                        # QueryParser.g:607:37: COMMA cube_rollup_list
                        pass 
                        COMMA468=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_cube_or_rollup4650) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA468)
                        self._state.following.append(self.FOLLOW_cube_rollup_list_in_cube_or_rollup4652)
                        cube_rollup_list469 = self.cube_rollup_list()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_cube_rollup_list.add(cube_rollup_list469.tree)


                    else:
                        break #loop129

                # AST Rewrite
                # elements: cube_rollup_list
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 608:17: -> ( cube_rollup_list )+
                    # QueryParser.g:608:20: ( cube_rollup_list )+
                    if not (stream_cube_rollup_list.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_cube_rollup_list.hasNext():
                        self._adaptor.addChild(root_0, stream_cube_rollup_list.nextTree())


                    stream_cube_rollup_list.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_or_rollup"

    class cube_rollup_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_rollup_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_rollup_list"
    # QueryParser.g:611:1: cube_rollup_list : ( CUBE | ROLLUP ) cube_by_expr_list ;
    def cube_rollup_list(self, ):

        retval = self.cube_rollup_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set470 = None
        cube_by_expr_list471 = None


        set470_tree = None

        try:
            try:
                # QueryParser.g:611:18: ( ( CUBE | ROLLUP ) cube_by_expr_list )
                # QueryParser.g:611:20: ( CUBE | ROLLUP ) cube_by_expr_list
                pass 
                root_0 = self._adaptor.nil()

                set470 = self.input.LT(1)
                set470 = self.input.LT(1)
                if (CUBE <= self.input.LA(1) <= ROLLUP):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        root_0 = self._adaptor.becomeRoot(self._adaptor.createWithPayload(set470), root_0)
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse


                self._state.following.append(self.FOLLOW_cube_by_expr_list_in_cube_rollup_list4696)
                cube_by_expr_list471 = self.cube_by_expr_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cube_by_expr_list471.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_rollup_list"

    class cube_by_expr_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_by_expr_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_by_expr_list"
    # QueryParser.g:614:1: cube_by_expr_list : LEFT_PAREN cube_by_expr ( COMMA cube_by_expr )* RIGHT_PAREN -> ( cube_by_expr )+ ;
    def cube_by_expr_list(self, ):

        retval = self.cube_by_expr_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN472 = None
        COMMA474 = None
        RIGHT_PAREN476 = None
        cube_by_expr473 = None

        cube_by_expr475 = None


        LEFT_PAREN472_tree = None
        COMMA474_tree = None
        RIGHT_PAREN476_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_cube_by_expr = RewriteRuleSubtreeStream(self._adaptor, "rule cube_by_expr")
        try:
            try:
                # QueryParser.g:614:19: ( LEFT_PAREN cube_by_expr ( COMMA cube_by_expr )* RIGHT_PAREN -> ( cube_by_expr )+ )
                # QueryParser.g:614:21: LEFT_PAREN cube_by_expr ( COMMA cube_by_expr )* RIGHT_PAREN
                pass 
                LEFT_PAREN472=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_cube_by_expr_list4705) 
                if self._state.backtracking == 0:
                    stream_LEFT_PAREN.add(LEFT_PAREN472)
                self._state.following.append(self.FOLLOW_cube_by_expr_in_cube_by_expr_list4707)
                cube_by_expr473 = self.cube_by_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_cube_by_expr.add(cube_by_expr473.tree)
                # QueryParser.g:614:45: ( COMMA cube_by_expr )*
                while True: #loop130
                    alt130 = 2
                    LA130_0 = self.input.LA(1)

                    if (LA130_0 == COMMA) :
                        alt130 = 1


                    if alt130 == 1:
                        # QueryParser.g:614:47: COMMA cube_by_expr
                        pass 
                        COMMA474=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_cube_by_expr_list4711) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA474)
                        self._state.following.append(self.FOLLOW_cube_by_expr_in_cube_by_expr_list4713)
                        cube_by_expr475 = self.cube_by_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_cube_by_expr.add(cube_by_expr475.tree)


                    else:
                        break #loop130
                RIGHT_PAREN476=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_cube_by_expr_list4718) 
                if self._state.backtracking == 0:
                    stream_RIGHT_PAREN.add(RIGHT_PAREN476)

                # AST Rewrite
                # elements: cube_by_expr
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 615:20: -> ( cube_by_expr )+
                    # QueryParser.g:615:23: ( cube_by_expr )+
                    if not (stream_cube_by_expr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_cube_by_expr.hasNext():
                        self._adaptor.addChild(root_0, stream_cube_by_expr.nextTree())


                    stream_cube_by_expr.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_by_expr_list"

    class cube_by_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.cube_by_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "cube_by_expr"
    # QueryParser.g:618:1: cube_by_expr : ( col_range | expr | STAR );
    def cube_by_expr(self, ):

        retval = self.cube_by_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STAR479 = None
        col_range477 = None

        expr478 = None


        STAR479_tree = None

        try:
            try:
                # QueryParser.g:618:14: ( col_range | expr | STAR )
                alt131 = 3
                LA131 = self.input.LA(1)
                if LA131 == GROUP:
                    LA131_1 = self.input.LA(2)

                    if (LA131_1 == DOUBLE_PERIOD) :
                        alt131 = 1
                    elif (LA131_1 == EOF or LA131_1 == PERIOD or LA131_1 == DOLLAR or (MINUS <= LA131_1 <= PLUS) or LA131_1 == STAR or (LEFT_PAREN <= LA131_1 <= RIGHT_PAREN) or LA131_1 == POUND or LA131_1 == COMMA or (DIV <= LA131_1 <= PERCENT)) :
                        alt131 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 131, 1, self.input)

                        raise nvae

                elif LA131 == CUBE:
                    LA131_2 = self.input.LA(2)

                    if (LA131_2 == EOF or LA131_2 == PERIOD or LA131_2 == DOLLAR or (MINUS <= LA131_2 <= PLUS) or LA131_2 == STAR or (LEFT_PAREN <= LA131_2 <= RIGHT_PAREN) or LA131_2 == POUND or LA131_2 == COMMA or (DIV <= LA131_2 <= PERCENT)) :
                        alt131 = 2
                    elif (LA131_2 == DOUBLE_PERIOD) :
                        alt131 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 131, 2, self.input)

                        raise nvae

                elif LA131 == IDENTIFIER_L:
                    LA131_3 = self.input.LA(2)

                    if (LA131_3 == EOF or LA131_3 == PERIOD or LA131_3 == DOLLAR or (MINUS <= LA131_3 <= PLUS) or LA131_3 == STAR or (LEFT_PAREN <= LA131_3 <= RIGHT_PAREN) or LA131_3 == POUND or LA131_3 == COMMA or (DIV <= LA131_3 <= PERCENT)) :
                        alt131 = 2
                    elif (LA131_3 == DOUBLE_PERIOD) :
                        alt131 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 131, 3, self.input)

                        raise nvae

                elif LA131 == DOLLARVAR:
                    LA131_4 = self.input.LA(2)

                    if (LA131_4 == DOUBLE_PERIOD) :
                        alt131 = 1
                    elif (LA131_4 == EOF or LA131_4 == PERIOD or (MINUS <= LA131_4 <= PLUS) or LA131_4 == STAR or LA131_4 == RIGHT_PAREN or LA131_4 == POUND or LA131_4 == COMMA or (DIV <= LA131_4 <= PERCENT)) :
                        alt131 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 131, 4, self.input)

                        raise nvae

                elif LA131 == DOUBLE_PERIOD:
                    alt131 = 1
                elif LA131 == IMPORT or LA131 == RETURNS or LA131 == DEFINE or LA131 == LOAD or LA131 == FILTER or LA131 == FOREACH or LA131 == ORDER or LA131 == ROLLUP or LA131 == DISTINCT or LA131 == COGROUP or LA131 == JOIN or LA131 == CROSS or LA131 == UNION or LA131 == SPLIT or LA131 == INTO or LA131 == IF or LA131 == ALL or LA131 == AS or LA131 == BY or LA131 == USING or LA131 == INNER or LA131 == OUTER or LA131 == PARALLEL or LA131 == PARTITION or LA131 == AND or LA131 == OR or LA131 == NOT or LA131 == GENERATE or LA131 == FLATTEN or LA131 == ASC or LA131 == DESC or LA131 == INT or LA131 == LONG or LA131 == FLOAT or LA131 == DOUBLE or LA131 == DATETIME or LA131 == CHARARRAY or LA131 == BYTEARRAY or LA131 == BAG or LA131 == TUPLE or LA131 == MAP or LA131 == IS or LA131 == STREAM or LA131 == THROUGH or LA131 == STORE or LA131 == MAPREDUCE or LA131 == SHIP or LA131 == CACHE or LA131 == INPUT or LA131 == OUTPUT or LA131 == STDERROR or LA131 == STDIN or LA131 == STDOUT or LA131 == LIMIT or LA131 == SAMPLE or LA131 == LEFT or LA131 == RIGHT or LA131 == FULL or LA131 == STR_OP_EQ or LA131 == STR_OP_GT or LA131 == STR_OP_LT or LA131 == STR_OP_GTE or LA131 == STR_OP_LTE or LA131 == STR_OP_NE or LA131 == STR_OP_MATCHES or LA131 == TRUE or LA131 == FALSE or LA131 == INTEGER or LA131 == LONGINTEGER or LA131 == MINUS or LA131 == DOUBLENUMBER or LA131 == FLOATNUMBER or LA131 == QUOTEDSTRING or LA131 == LEFT_PAREN or LA131 == LEFT_CURLY or LA131 == LEFT_BRACKET or LA131 == BOOL or LA131 == REALIAS:
                    alt131 = 2
                elif LA131 == STAR:
                    alt131 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 131, 0, self.input)

                    raise nvae

                if alt131 == 1:
                    # QueryParser.g:618:16: col_range
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_range_in_cube_by_expr4751)
                    col_range477 = self.col_range()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_range477.tree)


                elif alt131 == 2:
                    # QueryParser.g:618:29: expr
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_expr_in_cube_by_expr4756)
                    expr478 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr478.tree)


                elif alt131 == 3:
                    # QueryParser.g:618:36: STAR
                    pass 
                    root_0 = self._adaptor.nil()

                    STAR479=self.match(self.input, STAR, self.FOLLOW_STAR_in_cube_by_expr4760)
                    if self._state.backtracking == 0:

                        STAR479_tree = self._adaptor.createWithPayload(STAR479)
                        self._adaptor.addChild(root_0, STAR479_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "cube_by_expr"

    class nested_blk_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_blk_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_blk"
    # QueryParser.g:621:1: nested_blk : LEFT_CURLY nested_command_list ( generate_clause SEMI_COLON ) RIGHT_CURLY ;
    def nested_blk(self, ):

        retval = self.nested_blk_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_CURLY480 = None
        SEMI_COLON483 = None
        RIGHT_CURLY484 = None
        nested_command_list481 = None

        generate_clause482 = None


        LEFT_CURLY480_tree = None
        SEMI_COLON483_tree = None
        RIGHT_CURLY484_tree = None

        try:
            try:
                # QueryParser.g:621:12: ( LEFT_CURLY nested_command_list ( generate_clause SEMI_COLON ) RIGHT_CURLY )
                # QueryParser.g:621:14: LEFT_CURLY nested_command_list ( generate_clause SEMI_COLON ) RIGHT_CURLY
                pass 
                root_0 = self._adaptor.nil()

                LEFT_CURLY480=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_nested_blk4769)
                self._state.following.append(self.FOLLOW_nested_command_list_in_nested_blk4772)
                nested_command_list481 = self.nested_command_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_command_list481.tree)
                # QueryParser.g:621:46: ( generate_clause SEMI_COLON )
                # QueryParser.g:621:48: generate_clause SEMI_COLON
                pass 
                self._state.following.append(self.FOLLOW_generate_clause_in_nested_blk4776)
                generate_clause482 = self.generate_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, generate_clause482.tree)
                SEMI_COLON483=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_nested_blk4778)



                RIGHT_CURLY484=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_nested_blk4783)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_blk"

    class generate_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.generate_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "generate_clause"
    # QueryParser.g:624:1: generate_clause : GENERATE flatten_generated_item ( COMMA flatten_generated_item )* -> ^( GENERATE ( flatten_generated_item )+ ) ;
    def generate_clause(self, ):

        retval = self.generate_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GENERATE485 = None
        COMMA487 = None
        flatten_generated_item486 = None

        flatten_generated_item488 = None


        GENERATE485_tree = None
        COMMA487_tree = None
        stream_GENERATE = RewriteRuleTokenStream(self._adaptor, "token GENERATE")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_flatten_generated_item = RewriteRuleSubtreeStream(self._adaptor, "rule flatten_generated_item")
        try:
            try:
                # QueryParser.g:624:17: ( GENERATE flatten_generated_item ( COMMA flatten_generated_item )* -> ^( GENERATE ( flatten_generated_item )+ ) )
                # QueryParser.g:624:19: GENERATE flatten_generated_item ( COMMA flatten_generated_item )*
                pass 
                GENERATE485=self.match(self.input, GENERATE, self.FOLLOW_GENERATE_in_generate_clause4793) 
                if self._state.backtracking == 0:
                    stream_GENERATE.add(GENERATE485)
                self._state.following.append(self.FOLLOW_flatten_generated_item_in_generate_clause4795)
                flatten_generated_item486 = self.flatten_generated_item()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_flatten_generated_item.add(flatten_generated_item486.tree)
                # QueryParser.g:624:51: ( COMMA flatten_generated_item )*
                while True: #loop132
                    alt132 = 2
                    LA132_0 = self.input.LA(1)

                    if (LA132_0 == COMMA) :
                        alt132 = 1


                    if alt132 == 1:
                        # QueryParser.g:624:53: COMMA flatten_generated_item
                        pass 
                        COMMA487=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_generate_clause4799) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA487)
                        self._state.following.append(self.FOLLOW_flatten_generated_item_in_generate_clause4801)
                        flatten_generated_item488 = self.flatten_generated_item()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_flatten_generated_item.add(flatten_generated_item488.tree)


                    else:
                        break #loop132

                # AST Rewrite
                # elements: GENERATE, flatten_generated_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 625:19: -> ^( GENERATE ( flatten_generated_item )+ )
                    # QueryParser.g:625:22: ^( GENERATE ( flatten_generated_item )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_GENERATE.nextNode(), root_1)

                    # QueryParser.g:625:34: ( flatten_generated_item )+
                    if not (stream_flatten_generated_item.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_flatten_generated_item.hasNext():
                        self._adaptor.addChild(root_1, stream_flatten_generated_item.nextTree())


                    stream_flatten_generated_item.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "generate_clause"

    class nested_command_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_command_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_command_list"
    # QueryParser.g:628:1: nested_command_list : ( ( nested_command SEMI_COLON )* -> ( nested_command )* | );
    def nested_command_list(self, ):

        retval = self.nested_command_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SEMI_COLON490 = None
        nested_command489 = None


        SEMI_COLON490_tree = None
        stream_SEMI_COLON = RewriteRuleTokenStream(self._adaptor, "token SEMI_COLON")
        stream_nested_command = RewriteRuleSubtreeStream(self._adaptor, "rule nested_command")
        try:
            try:
                # QueryParser.g:628:21: ( ( nested_command SEMI_COLON )* -> ( nested_command )* | )
                alt134 = 2
                LA134_0 = self.input.LA(1)

                if (LA134_0 == IDENTIFIER_L) :
                    alt134 = 1
                elif (LA134_0 == GENERATE) :
                    LA134_2 = self.input.LA(2)

                    if (self.synpred212_QueryParser()) :
                        alt134 = 1
                    elif (True) :
                        alt134 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 134, 2, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 134, 0, self.input)

                    raise nvae

                if alt134 == 1:
                    # QueryParser.g:628:23: ( nested_command SEMI_COLON )*
                    pass 
                    # QueryParser.g:628:23: ( nested_command SEMI_COLON )*
                    while True: #loop133
                        alt133 = 2
                        LA133_0 = self.input.LA(1)

                        if (LA133_0 == IDENTIFIER_L) :
                            alt133 = 1


                        if alt133 == 1:
                            # QueryParser.g:628:25: nested_command SEMI_COLON
                            pass 
                            self._state.following.append(self.FOLLOW_nested_command_in_nested_command_list4844)
                            nested_command489 = self.nested_command()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_nested_command.add(nested_command489.tree)
                            SEMI_COLON490=self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_nested_command_list4846) 
                            if self._state.backtracking == 0:
                                stream_SEMI_COLON.add(SEMI_COLON490)


                        else:
                            break #loop133

                    # AST Rewrite
                    # elements: nested_command
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 629:20: -> ( nested_command )*
                        # QueryParser.g:629:23: ( nested_command )*
                        while stream_nested_command.hasNext():
                            self._adaptor.addChild(root_0, stream_nested_command.nextTree())


                        stream_nested_command.reset();



                        retval.tree = root_0


                elif alt134 == 2:
                    # QueryParser.g:631:1: 
                    pass 
                    root_0 = self._adaptor.nil()


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_command_list"

    class nested_command_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_command_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_command"
    # QueryParser.g:633:1: nested_command : ( ( identifier EQUAL col_ref PERIOD col_ref_list {...}?)=> ( identifier EQUAL nested_proj ) -> ^( NESTED_CMD identifier nested_proj ) | identifier EQUAL expr -> ^( NESTED_CMD_ASSI identifier expr ) | identifier EQUAL nested_op -> ^( NESTED_CMD identifier nested_op ) );
    def nested_command(self, ):

        retval = self.nested_command_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EQUAL492 = None
        EQUAL495 = None
        EQUAL498 = None
        identifier491 = None

        nested_proj493 = None

        identifier494 = None

        expr496 = None

        identifier497 = None

        nested_op499 = None


        EQUAL492_tree = None
        EQUAL495_tree = None
        EQUAL498_tree = None
        stream_EQUAL = RewriteRuleTokenStream(self._adaptor, "token EQUAL")
        stream_nested_proj = RewriteRuleSubtreeStream(self._adaptor, "rule nested_proj")
        stream_nested_op = RewriteRuleSubtreeStream(self._adaptor, "rule nested_op")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        stream_identifier = RewriteRuleSubtreeStream(self._adaptor, "rule identifier")
        try:
            try:
                # QueryParser.g:633:16: ( ( identifier EQUAL col_ref PERIOD col_ref_list {...}?)=> ( identifier EQUAL nested_proj ) -> ^( NESTED_CMD identifier nested_proj ) | identifier EQUAL expr -> ^( NESTED_CMD_ASSI identifier expr ) | identifier EQUAL nested_op -> ^( NESTED_CMD identifier nested_op ) )
                alt135 = 3
                alt135 = self.dfa135.predict(self.input)
                if alt135 == 1:
                    # QueryParser.g:633:18: ( identifier EQUAL col_ref PERIOD col_ref_list {...}?)=> ( identifier EQUAL nested_proj )
                    pass 
                    # QueryParser.g:633:103: ( identifier EQUAL nested_proj )
                    # QueryParser.g:633:105: identifier EQUAL nested_proj
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_nested_command4924)
                    identifier491 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier491.tree)
                    EQUAL492=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_nested_command4926) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL492)
                    self._state.following.append(self.FOLLOW_nested_proj_in_nested_command4928)
                    nested_proj493 = self.nested_proj()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_nested_proj.add(nested_proj493.tree)




                    # AST Rewrite
                    # elements: identifier, nested_proj
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 634:15: -> ^( NESTED_CMD identifier nested_proj )
                        # QueryParser.g:634:18: ^( NESTED_CMD identifier nested_proj )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NESTED_CMD, "NESTED_CMD"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        self._adaptor.addChild(root_1, stream_nested_proj.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt135 == 2:
                    # QueryParser.g:635:18: identifier EQUAL expr
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_nested_command4975)
                    identifier494 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier494.tree)
                    EQUAL495=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_nested_command4977) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL495)
                    self._state.following.append(self.FOLLOW_expr_in_nested_command4979)
                    expr496 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_expr.add(expr496.tree)

                    # AST Rewrite
                    # elements: identifier, expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 636:15: -> ^( NESTED_CMD_ASSI identifier expr )
                        # QueryParser.g:636:18: ^( NESTED_CMD_ASSI identifier expr )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NESTED_CMD_ASSI, "NESTED_CMD_ASSI"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        self._adaptor.addChild(root_1, stream_expr.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt135 == 3:
                    # QueryParser.g:637:18: identifier EQUAL nested_op
                    pass 
                    self._state.following.append(self.FOLLOW_identifier_in_nested_command5024)
                    identifier497 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_identifier.add(identifier497.tree)
                    EQUAL498=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_nested_command5026) 
                    if self._state.backtracking == 0:
                        stream_EQUAL.add(EQUAL498)
                    self._state.following.append(self.FOLLOW_nested_op_in_nested_command5028)
                    nested_op499 = self.nested_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_nested_op.add(nested_op499.tree)

                    # AST Rewrite
                    # elements: identifier, nested_op
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 638:15: -> ^( NESTED_CMD identifier nested_op )
                        # QueryParser.g:638:18: ^( NESTED_CMD identifier nested_op )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NESTED_CMD, "NESTED_CMD"), root_1)

                        self._adaptor.addChild(root_1, stream_identifier.nextTree())
                        self._adaptor.addChild(root_1, stream_nested_op.nextTree())

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_command"

    class nested_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_op"
    # QueryParser.g:641:1: nested_op : ( nested_filter | nested_sort | nested_distinct | nested_limit | nested_cross | nested_foreach );
    def nested_op(self, ):

        retval = self.nested_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        nested_filter500 = None

        nested_sort501 = None

        nested_distinct502 = None

        nested_limit503 = None

        nested_cross504 = None

        nested_foreach505 = None



        try:
            try:
                # QueryParser.g:641:11: ( nested_filter | nested_sort | nested_distinct | nested_limit | nested_cross | nested_foreach )
                alt136 = 6
                LA136 = self.input.LA(1)
                if LA136 == FILTER:
                    alt136 = 1
                elif LA136 == ORDER:
                    alt136 = 2
                elif LA136 == DISTINCT:
                    alt136 = 3
                elif LA136 == LIMIT:
                    alt136 = 4
                elif LA136 == CROSS:
                    alt136 = 5
                elif LA136 == FOREACH:
                    alt136 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 136, 0, self.input)

                    raise nvae

                if alt136 == 1:
                    # QueryParser.g:641:13: nested_filter
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_filter_in_nested_op5063)
                    nested_filter500 = self.nested_filter()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_filter500.tree)


                elif alt136 == 2:
                    # QueryParser.g:642:13: nested_sort
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_sort_in_nested_op5077)
                    nested_sort501 = self.nested_sort()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_sort501.tree)


                elif alt136 == 3:
                    # QueryParser.g:643:13: nested_distinct
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_distinct_in_nested_op5091)
                    nested_distinct502 = self.nested_distinct()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_distinct502.tree)


                elif alt136 == 4:
                    # QueryParser.g:644:13: nested_limit
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_limit_in_nested_op5105)
                    nested_limit503 = self.nested_limit()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_limit503.tree)


                elif alt136 == 5:
                    # QueryParser.g:645:13: nested_cross
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_cross_in_nested_op5119)
                    nested_cross504 = self.nested_cross()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_cross504.tree)


                elif alt136 == 6:
                    # QueryParser.g:646:13: nested_foreach
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_foreach_in_nested_op5133)
                    nested_foreach505 = self.nested_foreach()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_foreach505.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_op"

    class nested_proj_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_proj_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_proj"
    # QueryParser.g:649:1: nested_proj : col_ref PERIOD col_ref_list -> ^( NESTED_PROJ col_ref col_ref_list ) ;
    def nested_proj(self, ):

        retval = self.nested_proj_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PERIOD507 = None
        col_ref506 = None

        col_ref_list508 = None


        PERIOD507_tree = None
        stream_PERIOD = RewriteRuleTokenStream(self._adaptor, "token PERIOD")
        stream_col_ref_list = RewriteRuleSubtreeStream(self._adaptor, "rule col_ref_list")
        stream_col_ref = RewriteRuleSubtreeStream(self._adaptor, "rule col_ref")
        try:
            try:
                # QueryParser.g:649:13: ( col_ref PERIOD col_ref_list -> ^( NESTED_PROJ col_ref col_ref_list ) )
                # QueryParser.g:649:15: col_ref PERIOD col_ref_list
                pass 
                self._state.following.append(self.FOLLOW_col_ref_in_nested_proj5142)
                col_ref506 = self.col_ref()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_col_ref.add(col_ref506.tree)
                PERIOD507=self.match(self.input, PERIOD, self.FOLLOW_PERIOD_in_nested_proj5144) 
                if self._state.backtracking == 0:
                    stream_PERIOD.add(PERIOD507)
                self._state.following.append(self.FOLLOW_col_ref_list_in_nested_proj5146)
                col_ref_list508 = self.col_ref_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_col_ref_list.add(col_ref_list508.tree)

                # AST Rewrite
                # elements: col_ref_list, col_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 650:12: -> ^( NESTED_PROJ col_ref col_ref_list )
                    # QueryParser.g:650:15: ^( NESTED_PROJ col_ref col_ref_list )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(NESTED_PROJ, "NESTED_PROJ"), root_1)

                    self._adaptor.addChild(root_1, stream_col_ref.nextTree())
                    self._adaptor.addChild(root_1, stream_col_ref_list.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_proj"

    class col_ref_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_ref_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_ref_list"
    # QueryParser.g:653:1: col_ref_list : ( col_ref | ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN ) ) -> ( col_ref )+ ;
    def col_ref_list(self, ):

        retval = self.col_ref_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN510 = None
        COMMA512 = None
        RIGHT_PAREN514 = None
        col_ref509 = None

        col_ref511 = None

        col_ref513 = None


        LEFT_PAREN510_tree = None
        COMMA512_tree = None
        RIGHT_PAREN514_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_col_ref = RewriteRuleSubtreeStream(self._adaptor, "rule col_ref")
        try:
            try:
                # QueryParser.g:653:14: ( ( col_ref | ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN ) ) -> ( col_ref )+ )
                # QueryParser.g:653:16: ( col_ref | ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN ) )
                pass 
                # QueryParser.g:653:16: ( col_ref | ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN ) )
                alt138 = 2
                LA138_0 = self.input.LA(1)

                if (LA138_0 == CUBE or LA138_0 == GROUP or LA138_0 == IDENTIFIER_L or LA138_0 == DOLLARVAR) :
                    alt138 = 1
                elif (LA138_0 == LEFT_PAREN) :
                    alt138 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 138, 0, self.input)

                    raise nvae

                if alt138 == 1:
                    # QueryParser.g:653:18: col_ref
                    pass 
                    self._state.following.append(self.FOLLOW_col_ref_in_col_ref_list5180)
                    col_ref509 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_ref.add(col_ref509.tree)


                elif alt138 == 2:
                    # QueryParser.g:653:28: ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN )
                    pass 
                    # QueryParser.g:653:28: ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN )
                    # QueryParser.g:653:30: LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN
                    pass 
                    LEFT_PAREN510=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_col_ref_list5186) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN510)
                    self._state.following.append(self.FOLLOW_col_ref_in_col_ref_list5188)
                    col_ref511 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_col_ref.add(col_ref511.tree)
                    # QueryParser.g:653:49: ( COMMA col_ref )*
                    while True: #loop137
                        alt137 = 2
                        LA137_0 = self.input.LA(1)

                        if (LA137_0 == COMMA) :
                            alt137 = 1


                        if alt137 == 1:
                            # QueryParser.g:653:51: COMMA col_ref
                            pass 
                            COMMA512=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_col_ref_list5192) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA512)
                            self._state.following.append(self.FOLLOW_col_ref_in_col_ref_list5194)
                            col_ref513 = self.col_ref()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_col_ref.add(col_ref513.tree)


                        else:
                            break #loop137
                    RIGHT_PAREN514=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_col_ref_list5199) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN514)







                # AST Rewrite
                # elements: col_ref
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 654:13: -> ( col_ref )+
                    # QueryParser.g:654:16: ( col_ref )+
                    if not (stream_col_ref.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_col_ref.hasNext():
                        self._adaptor.addChild(root_0, stream_col_ref.nextTree())


                    stream_col_ref.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_ref_list"

    class nested_filter_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_filter_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_filter"
    # QueryParser.g:657:1: nested_filter : FILTER nested_op_input BY cond ;
    def nested_filter(self, ):

        retval = self.nested_filter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FILTER515 = None
        BY517 = None
        nested_op_input516 = None

        cond518 = None


        FILTER515_tree = None
        BY517_tree = None

        try:
            try:
                # QueryParser.g:657:15: ( FILTER nested_op_input BY cond )
                # QueryParser.g:657:17: FILTER nested_op_input BY cond
                pass 
                root_0 = self._adaptor.nil()

                FILTER515=self.match(self.input, FILTER, self.FOLLOW_FILTER_in_nested_filter5229)
                if self._state.backtracking == 0:

                    FILTER515_tree = self._adaptor.createWithPayload(FILTER515)
                    root_0 = self._adaptor.becomeRoot(FILTER515_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_filter5232)
                nested_op_input516 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input516.tree)
                BY517=self.match(self.input, BY, self.FOLLOW_BY_in_nested_filter5234)
                self._state.following.append(self.FOLLOW_cond_in_nested_filter5237)
                cond518 = self.cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, cond518.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_filter"

    class nested_sort_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_sort_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_sort"
    # QueryParser.g:660:1: nested_sort : ORDER nested_op_input BY order_by_clause ( USING func_clause )? ;
    def nested_sort(self, ):

        retval = self.nested_sort_return()
        retval.start = self.input.LT(1)

        root_0 = None

        ORDER519 = None
        BY521 = None
        USING523 = None
        nested_op_input520 = None

        order_by_clause522 = None

        func_clause524 = None


        ORDER519_tree = None
        BY521_tree = None
        USING523_tree = None

        try:
            try:
                # QueryParser.g:660:13: ( ORDER nested_op_input BY order_by_clause ( USING func_clause )? )
                # QueryParser.g:660:15: ORDER nested_op_input BY order_by_clause ( USING func_clause )?
                pass 
                root_0 = self._adaptor.nil()

                ORDER519=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_nested_sort5246)
                if self._state.backtracking == 0:

                    ORDER519_tree = self._adaptor.createWithPayload(ORDER519)
                    root_0 = self._adaptor.becomeRoot(ORDER519_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_sort5249)
                nested_op_input520 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input520.tree)
                BY521=self.match(self.input, BY, self.FOLLOW_BY_in_nested_sort5251)
                self._state.following.append(self.FOLLOW_order_by_clause_in_nested_sort5255)
                order_by_clause522 = self.order_by_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, order_by_clause522.tree)
                # QueryParser.g:660:59: ( USING func_clause )?
                alt139 = 2
                LA139_0 = self.input.LA(1)

                if (LA139_0 == USING) :
                    alt139 = 1
                if alt139 == 1:
                    # QueryParser.g:660:61: USING func_clause
                    pass 
                    USING523=self.match(self.input, USING, self.FOLLOW_USING_in_nested_sort5259)
                    self._state.following.append(self.FOLLOW_func_clause_in_nested_sort5262)
                    func_clause524 = self.func_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, func_clause524.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_sort"

    class nested_distinct_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_distinct_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_distinct"
    # QueryParser.g:663:1: nested_distinct : DISTINCT nested_op_input ;
    def nested_distinct(self, ):

        retval = self.nested_distinct_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DISTINCT525 = None
        nested_op_input526 = None


        DISTINCT525_tree = None

        try:
            try:
                # QueryParser.g:663:17: ( DISTINCT nested_op_input )
                # QueryParser.g:663:19: DISTINCT nested_op_input
                pass 
                root_0 = self._adaptor.nil()

                DISTINCT525=self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_nested_distinct5274)
                if self._state.backtracking == 0:

                    DISTINCT525_tree = self._adaptor.createWithPayload(DISTINCT525)
                    root_0 = self._adaptor.becomeRoot(DISTINCT525_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_distinct5277)
                nested_op_input526 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input526.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_distinct"

    class nested_limit_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_limit_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_limit"
    # QueryParser.g:666:1: nested_limit : LIMIT nested_op_input ( ( INTEGER SEMI_COLON )=> INTEGER | expr ) ;
    def nested_limit(self, ):

        retval = self.nested_limit_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LIMIT527 = None
        INTEGER529 = None
        nested_op_input528 = None

        expr530 = None


        LIMIT527_tree = None
        INTEGER529_tree = None

        try:
            try:
                # QueryParser.g:666:14: ( LIMIT nested_op_input ( ( INTEGER SEMI_COLON )=> INTEGER | expr ) )
                # QueryParser.g:666:16: LIMIT nested_op_input ( ( INTEGER SEMI_COLON )=> INTEGER | expr )
                pass 
                root_0 = self._adaptor.nil()

                LIMIT527=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_nested_limit5286)
                if self._state.backtracking == 0:

                    LIMIT527_tree = self._adaptor.createWithPayload(LIMIT527)
                    root_0 = self._adaptor.becomeRoot(LIMIT527_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_limit5289)
                nested_op_input528 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input528.tree)
                # QueryParser.g:666:39: ( ( INTEGER SEMI_COLON )=> INTEGER | expr )
                alt140 = 2
                LA140_0 = self.input.LA(1)

                if (LA140_0 == INTEGER) :
                    LA140_1 = self.input.LA(2)

                    if (self.synpred223_QueryParser()) :
                        alt140 = 1
                    elif (True) :
                        alt140 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 140, 1, self.input)

                        raise nvae

                elif ((IMPORT <= LA140_0 <= ORDER) or (CUBE <= LA140_0 <= IF) or (ALL <= LA140_0 <= OUTER) or (PARALLEL <= LA140_0 <= DESC) or (INT <= LA140_0 <= FALSE) or LA140_0 == IDENTIFIER_L or LA140_0 == LONGINTEGER or (DOLLARVAR <= LA140_0 <= MINUS) or (DOUBLENUMBER <= LA140_0 <= QUOTEDSTRING) or LA140_0 == LEFT_PAREN or LA140_0 == LEFT_CURLY or LA140_0 == LEFT_BRACKET or (BOOL <= LA140_0 <= REALIAS)) :
                    alt140 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 140, 0, self.input)

                    raise nvae

                if alt140 == 1:
                    # QueryParser.g:666:41: ( INTEGER SEMI_COLON )=> INTEGER
                    pass 
                    INTEGER529=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_nested_limit5301)
                    if self._state.backtracking == 0:

                        INTEGER529_tree = self._adaptor.createWithPayload(INTEGER529)
                        self._adaptor.addChild(root_0, INTEGER529_tree)



                elif alt140 == 2:
                    # QueryParser.g:666:75: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_nested_limit5305)
                    expr530 = self.expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, expr530.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_limit"

    class nested_cross_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_cross_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_cross"
    # QueryParser.g:669:1: nested_cross : CROSS nested_op_input_list ;
    def nested_cross(self, ):

        retval = self.nested_cross_return()
        retval.start = self.input.LT(1)

        root_0 = None

        CROSS531 = None
        nested_op_input_list532 = None


        CROSS531_tree = None

        try:
            try:
                # QueryParser.g:669:14: ( CROSS nested_op_input_list )
                # QueryParser.g:669:16: CROSS nested_op_input_list
                pass 
                root_0 = self._adaptor.nil()

                CROSS531=self.match(self.input, CROSS, self.FOLLOW_CROSS_in_nested_cross5316)
                if self._state.backtracking == 0:

                    CROSS531_tree = self._adaptor.createWithPayload(CROSS531)
                    root_0 = self._adaptor.becomeRoot(CROSS531_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_list_in_nested_cross5319)
                nested_op_input_list532 = self.nested_op_input_list()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input_list532.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_cross"

    class nested_foreach_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_foreach_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_foreach"
    # QueryParser.g:672:1: nested_foreach : FOREACH nested_op_input generate_clause ;
    def nested_foreach(self, ):

        retval = self.nested_foreach_return()
        retval.start = self.input.LT(1)

        root_0 = None

        FOREACH533 = None
        nested_op_input534 = None

        generate_clause535 = None


        FOREACH533_tree = None

        try:
            try:
                # QueryParser.g:672:15: ( FOREACH nested_op_input generate_clause )
                # QueryParser.g:672:17: FOREACH nested_op_input generate_clause
                pass 
                root_0 = self._adaptor.nil()

                FOREACH533=self.match(self.input, FOREACH, self.FOLLOW_FOREACH_in_nested_foreach5327)
                if self._state.backtracking == 0:

                    FOREACH533_tree = self._adaptor.createWithPayload(FOREACH533)
                    root_0 = self._adaptor.becomeRoot(FOREACH533_tree, root_0)

                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_foreach5330)
                nested_op_input534 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, nested_op_input534.tree)
                self._state.following.append(self.FOLLOW_generate_clause_in_nested_foreach5332)
                generate_clause535 = self.generate_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, generate_clause535.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_foreach"

    class nested_op_input_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_op_input_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_op_input"
    # QueryParser.g:675:1: nested_op_input : ( col_ref | nested_proj );
    def nested_op_input(self, ):

        retval = self.nested_op_input_return()
        retval.start = self.input.LT(1)

        root_0 = None

        col_ref536 = None

        nested_proj537 = None



        try:
            try:
                # QueryParser.g:675:17: ( col_ref | nested_proj )
                alt141 = 2
                LA141 = self.input.LA(1)
                if LA141 == GROUP:
                    LA141_1 = self.input.LA(2)

                    if (LA141_1 == PERIOD) :
                        alt141 = 2
                    elif (LA141_1 == EOF or (IMPORT <= LA141_1 <= ORDER) or (CUBE <= LA141_1 <= IF) or (ALL <= LA141_1 <= OUTER) or (PARALLEL <= LA141_1 <= DESC) or (INT <= LA141_1 <= FALSE) or (IDENTIFIER_L <= LA141_1 <= INTEGER) or LA141_1 == LONGINTEGER or (DOLLARVAR <= LA141_1 <= MINUS) or (DOUBLENUMBER <= LA141_1 <= QUOTEDSTRING) or (SEMI_COLON <= LA141_1 <= LEFT_PAREN) or LA141_1 == LEFT_CURLY or LA141_1 == LEFT_BRACKET or LA141_1 == COMMA or (BOOL <= LA141_1 <= REALIAS)) :
                        alt141 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 141, 1, self.input)

                        raise nvae

                elif LA141 == CUBE:
                    LA141_2 = self.input.LA(2)

                    if (LA141_2 == EOF or (IMPORT <= LA141_2 <= ORDER) or (CUBE <= LA141_2 <= IF) or (ALL <= LA141_2 <= OUTER) or (PARALLEL <= LA141_2 <= DESC) or (INT <= LA141_2 <= FALSE) or (IDENTIFIER_L <= LA141_2 <= INTEGER) or LA141_2 == LONGINTEGER or (DOLLARVAR <= LA141_2 <= MINUS) or (DOUBLENUMBER <= LA141_2 <= QUOTEDSTRING) or (SEMI_COLON <= LA141_2 <= LEFT_PAREN) or LA141_2 == LEFT_CURLY or LA141_2 == LEFT_BRACKET or LA141_2 == COMMA or (BOOL <= LA141_2 <= REALIAS)) :
                        alt141 = 1
                    elif (LA141_2 == PERIOD) :
                        alt141 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 141, 2, self.input)

                        raise nvae

                elif LA141 == IDENTIFIER_L:
                    LA141_3 = self.input.LA(2)

                    if (LA141_3 == PERIOD) :
                        alt141 = 2
                    elif (LA141_3 == EOF or (IMPORT <= LA141_3 <= ORDER) or (CUBE <= LA141_3 <= IF) or (ALL <= LA141_3 <= OUTER) or (PARALLEL <= LA141_3 <= DESC) or (INT <= LA141_3 <= FALSE) or (IDENTIFIER_L <= LA141_3 <= INTEGER) or LA141_3 == LONGINTEGER or (DOLLARVAR <= LA141_3 <= MINUS) or (DOUBLENUMBER <= LA141_3 <= QUOTEDSTRING) or (SEMI_COLON <= LA141_3 <= LEFT_PAREN) or LA141_3 == LEFT_CURLY or LA141_3 == LEFT_BRACKET or LA141_3 == COMMA or (BOOL <= LA141_3 <= REALIAS)) :
                        alt141 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 141, 3, self.input)

                        raise nvae

                elif LA141 == DOLLARVAR:
                    LA141_4 = self.input.LA(2)

                    if (LA141_4 == PERIOD) :
                        alt141 = 2
                    elif (LA141_4 == EOF or (IMPORT <= LA141_4 <= ORDER) or (CUBE <= LA141_4 <= IF) or (ALL <= LA141_4 <= OUTER) or (PARALLEL <= LA141_4 <= DESC) or (INT <= LA141_4 <= FALSE) or (IDENTIFIER_L <= LA141_4 <= INTEGER) or LA141_4 == LONGINTEGER or (DOLLARVAR <= LA141_4 <= MINUS) or (DOUBLENUMBER <= LA141_4 <= QUOTEDSTRING) or (SEMI_COLON <= LA141_4 <= LEFT_PAREN) or LA141_4 == LEFT_CURLY or LA141_4 == LEFT_BRACKET or LA141_4 == COMMA or (BOOL <= LA141_4 <= REALIAS)) :
                        alt141 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 141, 4, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 141, 0, self.input)

                    raise nvae

                if alt141 == 1:
                    # QueryParser.g:675:19: col_ref
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_col_ref_in_nested_op_input5341)
                    col_ref536 = self.col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, col_ref536.tree)


                elif alt141 == 2:
                    # QueryParser.g:675:29: nested_proj
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_nested_proj_in_nested_op_input5345)
                    nested_proj537 = self.nested_proj()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, nested_proj537.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_op_input"

    class nested_op_input_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.nested_op_input_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "nested_op_input_list"
    # QueryParser.g:678:1: nested_op_input_list : nested_op_input ( COMMA nested_op_input )* -> ( nested_op_input )+ ;
    def nested_op_input_list(self, ):

        retval = self.nested_op_input_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA539 = None
        nested_op_input538 = None

        nested_op_input540 = None


        COMMA539_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_nested_op_input = RewriteRuleSubtreeStream(self._adaptor, "rule nested_op_input")
        try:
            try:
                # QueryParser.g:678:22: ( nested_op_input ( COMMA nested_op_input )* -> ( nested_op_input )+ )
                # QueryParser.g:678:24: nested_op_input ( COMMA nested_op_input )*
                pass 
                self._state.following.append(self.FOLLOW_nested_op_input_in_nested_op_input_list5354)
                nested_op_input538 = self.nested_op_input()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_nested_op_input.add(nested_op_input538.tree)
                # QueryParser.g:678:40: ( COMMA nested_op_input )*
                while True: #loop142
                    alt142 = 2
                    LA142_0 = self.input.LA(1)

                    if (LA142_0 == COMMA) :
                        alt142 = 1


                    if alt142 == 1:
                        # QueryParser.g:678:42: COMMA nested_op_input
                        pass 
                        COMMA539=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_nested_op_input_list5358) 
                        if self._state.backtracking == 0:
                            stream_COMMA.add(COMMA539)
                        self._state.following.append(self.FOLLOW_nested_op_input_in_nested_op_input_list5360)
                        nested_op_input540 = self.nested_op_input()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_nested_op_input.add(nested_op_input540.tree)


                    else:
                        break #loop142

                # AST Rewrite
                # elements: nested_op_input
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 679:9: -> ( nested_op_input )+
                    # QueryParser.g:679:12: ( nested_op_input )+
                    if not (stream_nested_op_input.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_nested_op_input.hasNext():
                        self._adaptor.addChild(root_0, stream_nested_op_input.nextTree())


                    stream_nested_op_input.reset()



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "nested_op_input_list"

    class stream_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.stream_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "stream_clause"
    # QueryParser.g:682:1: stream_clause : STREAM rel THROUGH ( EXECCOMMAND | alias ) ( as_clause )? ;
    def stream_clause(self, ):

        retval = self.stream_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STREAM541 = None
        THROUGH543 = None
        EXECCOMMAND544 = None
        rel542 = None

        alias545 = None

        as_clause546 = None


        STREAM541_tree = None
        THROUGH543_tree = None
        EXECCOMMAND544_tree = None

        try:
            try:
                # QueryParser.g:682:15: ( STREAM rel THROUGH ( EXECCOMMAND | alias ) ( as_clause )? )
                # QueryParser.g:682:17: STREAM rel THROUGH ( EXECCOMMAND | alias ) ( as_clause )?
                pass 
                root_0 = self._adaptor.nil()

                STREAM541=self.match(self.input, STREAM, self.FOLLOW_STREAM_in_stream_clause5385)
                if self._state.backtracking == 0:

                    STREAM541_tree = self._adaptor.createWithPayload(STREAM541)
                    root_0 = self._adaptor.becomeRoot(STREAM541_tree, root_0)

                self._state.following.append(self.FOLLOW_rel_in_stream_clause5388)
                rel542 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, rel542.tree)
                THROUGH543=self.match(self.input, THROUGH, self.FOLLOW_THROUGH_in_stream_clause5390)
                # QueryParser.g:682:38: ( EXECCOMMAND | alias )
                alt143 = 2
                LA143_0 = self.input.LA(1)

                if (LA143_0 == EXECCOMMAND) :
                    alt143 = 1
                elif (LA143_0 == IDENTIFIER_L) :
                    alt143 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 143, 0, self.input)

                    raise nvae

                if alt143 == 1:
                    # QueryParser.g:682:40: EXECCOMMAND
                    pass 
                    EXECCOMMAND544=self.match(self.input, EXECCOMMAND, self.FOLLOW_EXECCOMMAND_in_stream_clause5395)
                    if self._state.backtracking == 0:

                        EXECCOMMAND544_tree = self._adaptor.createWithPayload(EXECCOMMAND544)
                        self._adaptor.addChild(root_0, EXECCOMMAND544_tree)



                elif alt143 == 2:
                    # QueryParser.g:682:54: alias
                    pass 
                    self._state.following.append(self.FOLLOW_alias_in_stream_clause5399)
                    alias545 = self.alias()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, alias545.tree)



                # QueryParser.g:682:62: ( as_clause )?
                alt144 = 2
                LA144_0 = self.input.LA(1)

                if (LA144_0 == AS) :
                    alt144 = 1
                if alt144 == 1:
                    # QueryParser.g:0:0: as_clause
                    pass 
                    self._state.following.append(self.FOLLOW_as_clause_in_stream_clause5403)
                    as_clause546 = self.as_clause()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, as_clause546.tree)






                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "stream_clause"

    class mr_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.mr_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "mr_clause"
    # QueryParser.g:685:1: mr_clause : MAPREDUCE QUOTEDSTRING ( LEFT_PAREN path_list RIGHT_PAREN )? store_clause load_clause ( EXECCOMMAND )? ;
    def mr_clause(self, ):

        retval = self.mr_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MAPREDUCE547 = None
        QUOTEDSTRING548 = None
        LEFT_PAREN549 = None
        RIGHT_PAREN551 = None
        EXECCOMMAND554 = None
        path_list550 = None

        store_clause552 = None

        load_clause553 = None


        MAPREDUCE547_tree = None
        QUOTEDSTRING548_tree = None
        LEFT_PAREN549_tree = None
        RIGHT_PAREN551_tree = None
        EXECCOMMAND554_tree = None

        try:
            try:
                # QueryParser.g:685:11: ( MAPREDUCE QUOTEDSTRING ( LEFT_PAREN path_list RIGHT_PAREN )? store_clause load_clause ( EXECCOMMAND )? )
                # QueryParser.g:685:13: MAPREDUCE QUOTEDSTRING ( LEFT_PAREN path_list RIGHT_PAREN )? store_clause load_clause ( EXECCOMMAND )?
                pass 
                root_0 = self._adaptor.nil()

                MAPREDUCE547=self.match(self.input, MAPREDUCE, self.FOLLOW_MAPREDUCE_in_mr_clause5413)
                if self._state.backtracking == 0:

                    MAPREDUCE547_tree = self._adaptor.createWithPayload(MAPREDUCE547)
                    root_0 = self._adaptor.becomeRoot(MAPREDUCE547_tree, root_0)

                QUOTEDSTRING548=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_mr_clause5416)
                if self._state.backtracking == 0:

                    QUOTEDSTRING548_tree = self._adaptor.createWithPayload(QUOTEDSTRING548)
                    self._adaptor.addChild(root_0, QUOTEDSTRING548_tree)

                # QueryParser.g:685:37: ( LEFT_PAREN path_list RIGHT_PAREN )?
                alt145 = 2
                LA145_0 = self.input.LA(1)

                if (LA145_0 == LEFT_PAREN) :
                    alt145 = 1
                if alt145 == 1:
                    # QueryParser.g:685:39: LEFT_PAREN path_list RIGHT_PAREN
                    pass 
                    LEFT_PAREN549=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_mr_clause5420)
                    self._state.following.append(self.FOLLOW_path_list_in_mr_clause5423)
                    path_list550 = self.path_list()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, path_list550.tree)
                    RIGHT_PAREN551=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_mr_clause5425)



                self._state.following.append(self.FOLLOW_store_clause_in_mr_clause5431)
                store_clause552 = self.store_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, store_clause552.tree)
                self._state.following.append(self.FOLLOW_load_clause_in_mr_clause5433)
                load_clause553 = self.load_clause()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, load_clause553.tree)
                # QueryParser.g:685:102: ( EXECCOMMAND )?
                alt146 = 2
                LA146_0 = self.input.LA(1)

                if (LA146_0 == EXECCOMMAND) :
                    alt146 = 1
                if alt146 == 1:
                    # QueryParser.g:0:0: EXECCOMMAND
                    pass 
                    EXECCOMMAND554=self.match(self.input, EXECCOMMAND, self.FOLLOW_EXECCOMMAND_in_mr_clause5435)
                    if self._state.backtracking == 0:

                        EXECCOMMAND554_tree = self._adaptor.createWithPayload(EXECCOMMAND554)
                        self._adaptor.addChild(root_0, EXECCOMMAND554_tree)







                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "mr_clause"

    class split_clause_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.split_clause_return, self).__init__()

            self.tree = None




    # $ANTLR start "split_clause"
    # QueryParser.g:688:1: split_clause : SPLIT rel INTO split_branch ( ( COMMA split_branch )+ | ( ( COMMA split_branch )* COMMA split_otherwise ) ) -> ^( SPLIT rel ( split_branch )+ ( split_otherwise )? ) ;
    def split_clause(self, ):

        retval = self.split_clause_return()
        retval.start = self.input.LT(1)

        root_0 = None

        SPLIT555 = None
        INTO557 = None
        COMMA559 = None
        COMMA561 = None
        COMMA563 = None
        rel556 = None

        split_branch558 = None

        split_branch560 = None

        split_branch562 = None

        split_otherwise564 = None


        SPLIT555_tree = None
        INTO557_tree = None
        COMMA559_tree = None
        COMMA561_tree = None
        COMMA563_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_INTO = RewriteRuleTokenStream(self._adaptor, "token INTO")
        stream_SPLIT = RewriteRuleTokenStream(self._adaptor, "token SPLIT")
        stream_rel = RewriteRuleSubtreeStream(self._adaptor, "rule rel")
        stream_split_otherwise = RewriteRuleSubtreeStream(self._adaptor, "rule split_otherwise")
        stream_split_branch = RewriteRuleSubtreeStream(self._adaptor, "rule split_branch")
        try:
            try:
                # QueryParser.g:688:14: ( SPLIT rel INTO split_branch ( ( COMMA split_branch )+ | ( ( COMMA split_branch )* COMMA split_otherwise ) ) -> ^( SPLIT rel ( split_branch )+ ( split_otherwise )? ) )
                # QueryParser.g:688:16: SPLIT rel INTO split_branch ( ( COMMA split_branch )+ | ( ( COMMA split_branch )* COMMA split_otherwise ) )
                pass 
                SPLIT555=self.match(self.input, SPLIT, self.FOLLOW_SPLIT_in_split_clause5445) 
                if self._state.backtracking == 0:
                    stream_SPLIT.add(SPLIT555)
                self._state.following.append(self.FOLLOW_rel_in_split_clause5447)
                rel556 = self.rel()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rel.add(rel556.tree)
                INTO557=self.match(self.input, INTO, self.FOLLOW_INTO_in_split_clause5449) 
                if self._state.backtracking == 0:
                    stream_INTO.add(INTO557)
                self._state.following.append(self.FOLLOW_split_branch_in_split_clause5451)
                split_branch558 = self.split_branch()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_split_branch.add(split_branch558.tree)
                # QueryParser.g:688:44: ( ( COMMA split_branch )+ | ( ( COMMA split_branch )* COMMA split_otherwise ) )
                alt149 = 2
                LA149_0 = self.input.LA(1)

                if (LA149_0 == COMMA) :
                    LA149_1 = self.input.LA(2)

                    if (self.synpred231_QueryParser()) :
                        alt149 = 1
                    elif (True) :
                        alt149 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 149, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 149, 0, self.input)

                    raise nvae

                if alt149 == 1:
                    # QueryParser.g:688:46: ( COMMA split_branch )+
                    pass 
                    # QueryParser.g:688:46: ( COMMA split_branch )+
                    cnt147 = 0
                    while True: #loop147
                        alt147 = 2
                        LA147_0 = self.input.LA(1)

                        if (LA147_0 == COMMA) :
                            alt147 = 1


                        if alt147 == 1:
                            # QueryParser.g:688:48: COMMA split_branch
                            pass 
                            COMMA559=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_split_clause5457) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA559)
                            self._state.following.append(self.FOLLOW_split_branch_in_split_clause5459)
                            split_branch560 = self.split_branch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_split_branch.add(split_branch560.tree)


                        else:
                            if cnt147 >= 1:
                                break #loop147

                            if self._state.backtracking > 0:
                                raise BacktrackingFailed

                            eee = EarlyExitException(147, self.input)
                            raise eee

                        cnt147 += 1


                elif alt149 == 2:
                    # QueryParser.g:688:72: ( ( COMMA split_branch )* COMMA split_otherwise )
                    pass 
                    # QueryParser.g:688:72: ( ( COMMA split_branch )* COMMA split_otherwise )
                    # QueryParser.g:688:74: ( COMMA split_branch )* COMMA split_otherwise
                    pass 
                    # QueryParser.g:688:74: ( COMMA split_branch )*
                    while True: #loop148
                        alt148 = 2
                        LA148_0 = self.input.LA(1)

                        if (LA148_0 == COMMA) :
                            LA148_1 = self.input.LA(2)

                            if (LA148_1 == IDENTIFIER_L) :
                                LA148_2 = self.input.LA(3)

                                if (LA148_2 == IF) :
                                    alt148 = 1






                        if alt148 == 1:
                            # QueryParser.g:688:76: COMMA split_branch
                            pass 
                            COMMA561=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_split_clause5470) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA561)
                            self._state.following.append(self.FOLLOW_split_branch_in_split_clause5472)
                            split_branch562 = self.split_branch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_split_branch.add(split_branch562.tree)


                        else:
                            break #loop148
                    COMMA563=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_split_clause5477) 
                    if self._state.backtracking == 0:
                        stream_COMMA.add(COMMA563)
                    self._state.following.append(self.FOLLOW_split_otherwise_in_split_clause5479)
                    split_otherwise564 = self.split_otherwise()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_split_otherwise.add(split_otherwise564.tree)







                # AST Rewrite
                # elements: split_branch, SPLIT, split_otherwise, rel
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 689:13: -> ^( SPLIT rel ( split_branch )+ ( split_otherwise )? )
                    # QueryParser.g:689:16: ^( SPLIT rel ( split_branch )+ ( split_otherwise )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_SPLIT.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_rel.nextTree())
                    # QueryParser.g:689:29: ( split_branch )+
                    if not (stream_split_branch.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_split_branch.hasNext():
                        self._adaptor.addChild(root_1, stream_split_branch.nextTree())


                    stream_split_branch.reset()
                    # QueryParser.g:689:43: ( split_otherwise )?
                    if stream_split_otherwise.hasNext():
                        self._adaptor.addChild(root_1, stream_split_otherwise.nextTree())


                    stream_split_otherwise.reset();

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "split_clause"

    class split_branch_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.split_branch_return, self).__init__()

            self.tree = None




    # $ANTLR start "split_branch"
    # QueryParser.g:692:1: split_branch : alias IF cond -> ^( SPLIT_BRANCH alias cond ) ;
    def split_branch(self, ):

        retval = self.split_branch_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IF566 = None
        alias565 = None

        cond567 = None


        IF566_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        stream_cond = RewriteRuleSubtreeStream(self._adaptor, "rule cond")
        try:
            try:
                # QueryParser.g:692:14: ( alias IF cond -> ^( SPLIT_BRANCH alias cond ) )
                # QueryParser.g:692:16: alias IF cond
                pass 
                self._state.following.append(self.FOLLOW_alias_in_split_branch5519)
                alias565 = self.alias()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_alias.add(alias565.tree)
                IF566=self.match(self.input, IF, self.FOLLOW_IF_in_split_branch5521) 
                if self._state.backtracking == 0:
                    stream_IF.add(IF566)
                self._state.following.append(self.FOLLOW_cond_in_split_branch5523)
                cond567 = self.cond()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_cond.add(cond567.tree)

                # AST Rewrite
                # elements: cond, alias
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 693:13: -> ^( SPLIT_BRANCH alias cond )
                    # QueryParser.g:693:16: ^( SPLIT_BRANCH alias cond )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(SPLIT_BRANCH, "SPLIT_BRANCH"), root_1)

                    self._adaptor.addChild(root_1, stream_alias.nextTree())
                    self._adaptor.addChild(root_1, stream_cond.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "split_branch"

    class split_otherwise_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.split_otherwise_return, self).__init__()

            self.tree = None




    # $ANTLR start "split_otherwise"
    # QueryParser.g:696:1: split_otherwise : alias OTHERWISE -> ^( OTHERWISE alias ) ;
    def split_otherwise(self, ):

        retval = self.split_otherwise_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OTHERWISE569 = None
        alias568 = None


        OTHERWISE569_tree = None
        stream_OTHERWISE = RewriteRuleTokenStream(self._adaptor, "token OTHERWISE")
        stream_alias = RewriteRuleSubtreeStream(self._adaptor, "rule alias")
        try:
            try:
                # QueryParser.g:696:17: ( alias OTHERWISE -> ^( OTHERWISE alias ) )
                # QueryParser.g:696:19: alias OTHERWISE
                pass 
                self._state.following.append(self.FOLLOW_alias_in_split_otherwise5556)
                alias568 = self.alias()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_alias.add(alias568.tree)
                OTHERWISE569=self.match(self.input, OTHERWISE, self.FOLLOW_OTHERWISE_in_split_otherwise5558) 
                if self._state.backtracking == 0:
                    stream_OTHERWISE.add(OTHERWISE569)

                # AST Rewrite
                # elements: OTHERWISE, alias
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 697:13: -> ^( OTHERWISE alias )
                    # QueryParser.g:697:16: ^( OTHERWISE alias )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(stream_OTHERWISE.nextNode(), root_1)

                    self._adaptor.addChild(root_1, stream_alias.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "split_otherwise"

    class col_ref_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.col_ref_return, self).__init__()

            self.tree = None




    # $ANTLR start "col_ref"
    # QueryParser.g:700:1: col_ref : ( alias_col_ref | dollar_col_ref );
    def col_ref(self, ):

        retval = self.col_ref_return()
        retval.start = self.input.LT(1)

        root_0 = None

        alias_col_ref570 = None

        dollar_col_ref571 = None



        try:
            try:
                # QueryParser.g:700:9: ( alias_col_ref | dollar_col_ref )
                alt150 = 2
                LA150_0 = self.input.LA(1)

                if (LA150_0 == CUBE or LA150_0 == GROUP or LA150_0 == IDENTIFIER_L) :
                    alt150 = 1
                elif (LA150_0 == DOLLARVAR) :
                    alt150 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 150, 0, self.input)

                    raise nvae

                if alt150 == 1:
                    # QueryParser.g:700:11: alias_col_ref
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_alias_col_ref_in_col_ref5589)
                    alias_col_ref570 = self.alias_col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, alias_col_ref570.tree)


                elif alt150 == 2:
                    # QueryParser.g:700:27: dollar_col_ref
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_dollar_col_ref_in_col_ref5593)
                    dollar_col_ref571 = self.dollar_col_ref()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, dollar_col_ref571.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "col_ref"

    class alias_col_ref_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.alias_col_ref_return, self).__init__()

            self.tree = None




    # $ANTLR start "alias_col_ref"
    # QueryParser.g:703:1: alias_col_ref : ( GROUP | CUBE | identifier );
    def alias_col_ref(self, ):

        retval = self.alias_col_ref_return()
        retval.start = self.input.LT(1)

        root_0 = None

        GROUP572 = None
        CUBE573 = None
        identifier574 = None


        GROUP572_tree = None
        CUBE573_tree = None

        try:
            try:
                # QueryParser.g:703:15: ( GROUP | CUBE | identifier )
                alt151 = 3
                LA151 = self.input.LA(1)
                if LA151 == GROUP:
                    alt151 = 1
                elif LA151 == CUBE:
                    alt151 = 2
                elif LA151 == IDENTIFIER_L:
                    alt151 = 3
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 151, 0, self.input)

                    raise nvae

                if alt151 == 1:
                    # QueryParser.g:703:17: GROUP
                    pass 
                    root_0 = self._adaptor.nil()

                    GROUP572=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_alias_col_ref5602)
                    if self._state.backtracking == 0:

                        GROUP572_tree = self._adaptor.createWithPayload(GROUP572)
                        self._adaptor.addChild(root_0, GROUP572_tree)



                elif alt151 == 2:
                    # QueryParser.g:703:25: CUBE
                    pass 
                    root_0 = self._adaptor.nil()

                    CUBE573=self.match(self.input, CUBE, self.FOLLOW_CUBE_in_alias_col_ref5606)
                    if self._state.backtracking == 0:

                        CUBE573_tree = self._adaptor.createWithPayload(CUBE573)
                        self._adaptor.addChild(root_0, CUBE573_tree)



                elif alt151 == 3:
                    # QueryParser.g:703:32: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_alias_col_ref5610)
                    identifier574 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier574.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "alias_col_ref"

    class dollar_col_ref_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.dollar_col_ref_return, self).__init__()

            self.tree = None




    # $ANTLR start "dollar_col_ref"
    # QueryParser.g:706:1: dollar_col_ref : DOLLARVAR ;
    def dollar_col_ref(self, ):

        retval = self.dollar_col_ref_return()
        retval.start = self.input.LT(1)

        root_0 = None

        DOLLARVAR575 = None

        DOLLARVAR575_tree = None

        try:
            try:
                # QueryParser.g:706:16: ( DOLLARVAR )
                # QueryParser.g:706:18: DOLLARVAR
                pass 
                root_0 = self._adaptor.nil()

                DOLLARVAR575=self.match(self.input, DOLLARVAR, self.FOLLOW_DOLLARVAR_in_dollar_col_ref5619)
                if self._state.backtracking == 0:

                    DOLLARVAR575_tree = self._adaptor.createWithPayload(DOLLARVAR575)
                    self._adaptor.addChild(root_0, DOLLARVAR575_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "dollar_col_ref"

    class const_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.const_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "const_expr"
    # QueryParser.g:709:1: const_expr : literal ;
    def const_expr(self, ):

        retval = self.const_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        literal576 = None



        try:
            try:
                # QueryParser.g:709:12: ( literal )
                # QueryParser.g:709:14: literal
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_literal_in_const_expr5628)
                literal576 = self.literal()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, literal576.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "const_expr"

    class literal_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.literal_return, self).__init__()

            self.tree = None




    # $ANTLR start "literal"
    # QueryParser.g:712:1: literal : ( scalar | map | bag | tuple );
    def literal(self, ):

        retval = self.literal_return()
        retval.start = self.input.LT(1)

        root_0 = None

        scalar577 = None

        map578 = None

        bag579 = None

        tuple580 = None



        try:
            try:
                # QueryParser.g:712:9: ( scalar | map | bag | tuple )
                alt152 = 4
                LA152 = self.input.LA(1)
                if LA152 == TRUE or LA152 == FALSE or LA152 == IDENTIFIER_L or LA152 == INTEGER or LA152 == LONGINTEGER or LA152 == MINUS or LA152 == DOUBLENUMBER or LA152 == FLOATNUMBER or LA152 == QUOTEDSTRING:
                    alt152 = 1
                elif LA152 == LEFT_BRACKET:
                    alt152 = 2
                elif LA152 == LEFT_CURLY:
                    alt152 = 3
                elif LA152 == LEFT_PAREN:
                    alt152 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 152, 0, self.input)

                    raise nvae

                if alt152 == 1:
                    # QueryParser.g:712:11: scalar
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_scalar_in_literal5637)
                    scalar577 = self.scalar()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, scalar577.tree)


                elif alt152 == 2:
                    # QueryParser.g:712:20: map
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_map_in_literal5641)
                    map578 = self.map()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, map578.tree)


                elif alt152 == 3:
                    # QueryParser.g:712:26: bag
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_bag_in_literal5645)
                    bag579 = self.bag()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bag579.tree)


                elif alt152 == 4:
                    # QueryParser.g:712:32: tuple
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_tuple_in_literal5649)
                    tuple580 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, tuple580.tree)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "literal"

    class scalar_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.scalar_return, self).__init__()

            self.tree = None




    # $ANTLR start "scalar"
    # QueryParser.g:716:1: scalar : ( num_scalar | QUOTEDSTRING | null_keyword | TRUE | FALSE );
    def scalar(self, ):

        retval = self.scalar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING582 = None
        TRUE584 = None
        FALSE585 = None
        num_scalar581 = None

        null_keyword583 = None


        QUOTEDSTRING582_tree = None
        TRUE584_tree = None
        FALSE585_tree = None

        try:
            try:
                # QueryParser.g:716:8: ( num_scalar | QUOTEDSTRING | null_keyword | TRUE | FALSE )
                alt153 = 5
                LA153 = self.input.LA(1)
                if LA153 == INTEGER or LA153 == LONGINTEGER or LA153 == MINUS or LA153 == DOUBLENUMBER or LA153 == FLOATNUMBER:
                    alt153 = 1
                elif LA153 == QUOTEDSTRING:
                    alt153 = 2
                elif LA153 == IDENTIFIER_L:
                    alt153 = 3
                elif LA153 == TRUE:
                    alt153 = 4
                elif LA153 == FALSE:
                    alt153 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 153, 0, self.input)

                    raise nvae

                if alt153 == 1:
                    # QueryParser.g:716:10: num_scalar
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_num_scalar_in_scalar5659)
                    num_scalar581 = self.num_scalar()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, num_scalar581.tree)


                elif alt153 == 2:
                    # QueryParser.g:716:23: QUOTEDSTRING
                    pass 
                    root_0 = self._adaptor.nil()

                    QUOTEDSTRING582=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_scalar5663)
                    if self._state.backtracking == 0:

                        QUOTEDSTRING582_tree = self._adaptor.createWithPayload(QUOTEDSTRING582)
                        self._adaptor.addChild(root_0, QUOTEDSTRING582_tree)



                elif alt153 == 3:
                    # QueryParser.g:716:38: null_keyword
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_null_keyword_in_scalar5667)
                    null_keyword583 = self.null_keyword()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, null_keyword583.tree)


                elif alt153 == 4:
                    # QueryParser.g:716:53: TRUE
                    pass 
                    root_0 = self._adaptor.nil()

                    TRUE584=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_scalar5671)
                    if self._state.backtracking == 0:

                        TRUE584_tree = self._adaptor.createWithPayload(TRUE584)
                        self._adaptor.addChild(root_0, TRUE584_tree)



                elif alt153 == 5:
                    # QueryParser.g:716:60: FALSE
                    pass 
                    root_0 = self._adaptor.nil()

                    FALSE585=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_scalar5675)
                    if self._state.backtracking == 0:

                        FALSE585_tree = self._adaptor.createWithPayload(FALSE585)
                        self._adaptor.addChild(root_0, FALSE585_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "scalar"

    class num_scalar_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.num_scalar_return, self).__init__()

            self.tree = None




    # $ANTLR start "num_scalar"
    # QueryParser.g:719:1: num_scalar : ( MINUS )? ( INTEGER | LONGINTEGER | FLOATNUMBER | DOUBLENUMBER ) ;
    def num_scalar(self, ):

        retval = self.num_scalar_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MINUS586 = None
        set587 = None

        MINUS586_tree = None
        set587_tree = None

        try:
            try:
                # QueryParser.g:719:12: ( ( MINUS )? ( INTEGER | LONGINTEGER | FLOATNUMBER | DOUBLENUMBER ) )
                # QueryParser.g:719:14: ( MINUS )? ( INTEGER | LONGINTEGER | FLOATNUMBER | DOUBLENUMBER )
                pass 
                root_0 = self._adaptor.nil()

                # QueryParser.g:719:14: ( MINUS )?
                alt154 = 2
                LA154_0 = self.input.LA(1)

                if (LA154_0 == MINUS) :
                    alt154 = 1
                if alt154 == 1:
                    # QueryParser.g:0:0: MINUS
                    pass 
                    MINUS586=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_scalar5684)
                    if self._state.backtracking == 0:

                        MINUS586_tree = self._adaptor.createWithPayload(MINUS586)
                        self._adaptor.addChild(root_0, MINUS586_tree)




                set587 = self.input.LT(1)
                if self.input.LA(1) == INTEGER or self.input.LA(1) == LONGINTEGER or (DOUBLENUMBER <= self.input.LA(1) <= FLOATNUMBER):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set587))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "num_scalar"

    class map_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.map_return, self).__init__()

            self.tree = None




    # $ANTLR start "map"
    # QueryParser.g:722:1: map : ( LEFT_BRACKET keyvalue ( COMMA keyvalue )* RIGHT_BRACKET -> ^( MAP_VAL ( keyvalue )+ ) | LEFT_BRACKET RIGHT_BRACKET -> ^( MAP_VAL ) );
    def map(self, ):

        retval = self.map_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_BRACKET588 = None
        COMMA590 = None
        RIGHT_BRACKET592 = None
        LEFT_BRACKET593 = None
        RIGHT_BRACKET594 = None
        keyvalue589 = None

        keyvalue591 = None


        LEFT_BRACKET588_tree = None
        COMMA590_tree = None
        RIGHT_BRACKET592_tree = None
        LEFT_BRACKET593_tree = None
        RIGHT_BRACKET594_tree = None
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LEFT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token LEFT_BRACKET")
        stream_RIGHT_BRACKET = RewriteRuleTokenStream(self._adaptor, "token RIGHT_BRACKET")
        stream_keyvalue = RewriteRuleSubtreeStream(self._adaptor, "rule keyvalue")
        try:
            try:
                # QueryParser.g:722:5: ( LEFT_BRACKET keyvalue ( COMMA keyvalue )* RIGHT_BRACKET -> ^( MAP_VAL ( keyvalue )+ ) | LEFT_BRACKET RIGHT_BRACKET -> ^( MAP_VAL ) )
                alt156 = 2
                LA156_0 = self.input.LA(1)

                if (LA156_0 == LEFT_BRACKET) :
                    LA156_1 = self.input.LA(2)

                    if (LA156_1 == RIGHT_BRACKET) :
                        alt156 = 2
                    elif (LA156_1 == QUOTEDSTRING) :
                        alt156 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 156, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 156, 0, self.input)

                    raise nvae

                if alt156 == 1:
                    # QueryParser.g:722:7: LEFT_BRACKET keyvalue ( COMMA keyvalue )* RIGHT_BRACKET
                    pass 
                    LEFT_BRACKET588=self.match(self.input, LEFT_BRACKET, self.FOLLOW_LEFT_BRACKET_in_map5712) 
                    if self._state.backtracking == 0:
                        stream_LEFT_BRACKET.add(LEFT_BRACKET588)
                    self._state.following.append(self.FOLLOW_keyvalue_in_map5714)
                    keyvalue589 = self.keyvalue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_keyvalue.add(keyvalue589.tree)
                    # QueryParser.g:722:29: ( COMMA keyvalue )*
                    while True: #loop155
                        alt155 = 2
                        LA155_0 = self.input.LA(1)

                        if (LA155_0 == COMMA) :
                            alt155 = 1


                        if alt155 == 1:
                            # QueryParser.g:722:31: COMMA keyvalue
                            pass 
                            COMMA590=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_map5718) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA590)
                            self._state.following.append(self.FOLLOW_keyvalue_in_map5720)
                            keyvalue591 = self.keyvalue()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_keyvalue.add(keyvalue591.tree)


                        else:
                            break #loop155
                    RIGHT_BRACKET592=self.match(self.input, RIGHT_BRACKET, self.FOLLOW_RIGHT_BRACKET_in_map5725) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_BRACKET.add(RIGHT_BRACKET592)

                    # AST Rewrite
                    # elements: keyvalue
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 723:4: -> ^( MAP_VAL ( keyvalue )+ )
                        # QueryParser.g:723:7: ^( MAP_VAL ( keyvalue )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAP_VAL, "MAP_VAL"), root_1)

                        # QueryParser.g:723:18: ( keyvalue )+
                        if not (stream_keyvalue.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_keyvalue.hasNext():
                            self._adaptor.addChild(root_1, stream_keyvalue.nextTree())


                        stream_keyvalue.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt156 == 2:
                    # QueryParser.g:724:7: LEFT_BRACKET RIGHT_BRACKET
                    pass 
                    LEFT_BRACKET593=self.match(self.input, LEFT_BRACKET, self.FOLLOW_LEFT_BRACKET_in_map5747) 
                    if self._state.backtracking == 0:
                        stream_LEFT_BRACKET.add(LEFT_BRACKET593)
                    RIGHT_BRACKET594=self.match(self.input, RIGHT_BRACKET, self.FOLLOW_RIGHT_BRACKET_in_map5749) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_BRACKET.add(RIGHT_BRACKET594)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 725:4: -> ^( MAP_VAL )
                        # QueryParser.g:725:7: ^( MAP_VAL )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(MAP_VAL, "MAP_VAL"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "map"

    class keyvalue_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.keyvalue_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyvalue"
    # QueryParser.g:728:1: keyvalue : map_key POUND const_expr -> ^( KEY_VAL_PAIR map_key const_expr ) ;
    def keyvalue(self, ):

        retval = self.keyvalue_return()
        retval.start = self.input.LT(1)

        root_0 = None

        POUND596 = None
        map_key595 = None

        const_expr597 = None


        POUND596_tree = None
        stream_POUND = RewriteRuleTokenStream(self._adaptor, "token POUND")
        stream_const_expr = RewriteRuleSubtreeStream(self._adaptor, "rule const_expr")
        stream_map_key = RewriteRuleSubtreeStream(self._adaptor, "rule map_key")
        try:
            try:
                # QueryParser.g:728:10: ( map_key POUND const_expr -> ^( KEY_VAL_PAIR map_key const_expr ) )
                # QueryParser.g:728:12: map_key POUND const_expr
                pass 
                self._state.following.append(self.FOLLOW_map_key_in_keyvalue5769)
                map_key595 = self.map_key()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_map_key.add(map_key595.tree)
                POUND596=self.match(self.input, POUND, self.FOLLOW_POUND_in_keyvalue5771) 
                if self._state.backtracking == 0:
                    stream_POUND.add(POUND596)
                self._state.following.append(self.FOLLOW_const_expr_in_keyvalue5773)
                const_expr597 = self.const_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_const_expr.add(const_expr597.tree)

                # AST Rewrite
                # elements: const_expr, map_key
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 729:9: -> ^( KEY_VAL_PAIR map_key const_expr )
                    # QueryParser.g:729:12: ^( KEY_VAL_PAIR map_key const_expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(KEY_VAL_PAIR, "KEY_VAL_PAIR"), root_1)

                    self._adaptor.addChild(root_1, stream_map_key.nextTree())
                    self._adaptor.addChild(root_1, stream_const_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "keyvalue"

    class map_key_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.map_key_return, self).__init__()

            self.tree = None




    # $ANTLR start "map_key"
    # QueryParser.g:732:1: map_key : QUOTEDSTRING ;
    def map_key(self, ):

        retval = self.map_key_return()
        retval.start = self.input.LT(1)

        root_0 = None

        QUOTEDSTRING598 = None

        QUOTEDSTRING598_tree = None

        try:
            try:
                # QueryParser.g:732:9: ( QUOTEDSTRING )
                # QueryParser.g:732:11: QUOTEDSTRING
                pass 
                root_0 = self._adaptor.nil()

                QUOTEDSTRING598=self.match(self.input, QUOTEDSTRING, self.FOLLOW_QUOTEDSTRING_in_map_key5802)
                if self._state.backtracking == 0:

                    QUOTEDSTRING598_tree = self._adaptor.createWithPayload(QUOTEDSTRING598)
                    self._adaptor.addChild(root_0, QUOTEDSTRING598_tree)




                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "map_key"

    class bag_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.bag_return, self).__init__()

            self.tree = None




    # $ANTLR start "bag"
    # QueryParser.g:735:1: bag : ( LEFT_CURLY tuple ( COMMA tuple )* RIGHT_CURLY -> ^( BAG_VAL ( tuple )+ ) | LEFT_CURLY RIGHT_CURLY -> ^( BAG_VAL ) );
    def bag(self, ):

        retval = self.bag_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_CURLY599 = None
        COMMA601 = None
        RIGHT_CURLY603 = None
        LEFT_CURLY604 = None
        RIGHT_CURLY605 = None
        tuple600 = None

        tuple602 = None


        LEFT_CURLY599_tree = None
        COMMA601_tree = None
        RIGHT_CURLY603_tree = None
        LEFT_CURLY604_tree = None
        RIGHT_CURLY605_tree = None
        stream_RIGHT_CURLY = RewriteRuleTokenStream(self._adaptor, "token RIGHT_CURLY")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_LEFT_CURLY = RewriteRuleTokenStream(self._adaptor, "token LEFT_CURLY")
        stream_tuple = RewriteRuleSubtreeStream(self._adaptor, "rule tuple")
        try:
            try:
                # QueryParser.g:735:5: ( LEFT_CURLY tuple ( COMMA tuple )* RIGHT_CURLY -> ^( BAG_VAL ( tuple )+ ) | LEFT_CURLY RIGHT_CURLY -> ^( BAG_VAL ) )
                alt158 = 2
                LA158_0 = self.input.LA(1)

                if (LA158_0 == LEFT_CURLY) :
                    LA158_1 = self.input.LA(2)

                    if (LA158_1 == RIGHT_CURLY) :
                        alt158 = 2
                    elif (LA158_1 == LEFT_PAREN) :
                        alt158 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 158, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 158, 0, self.input)

                    raise nvae

                if alt158 == 1:
                    # QueryParser.g:735:7: LEFT_CURLY tuple ( COMMA tuple )* RIGHT_CURLY
                    pass 
                    LEFT_CURLY599=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_bag5811) 
                    if self._state.backtracking == 0:
                        stream_LEFT_CURLY.add(LEFT_CURLY599)
                    self._state.following.append(self.FOLLOW_tuple_in_bag5813)
                    tuple600 = self.tuple()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_tuple.add(tuple600.tree)
                    # QueryParser.g:735:24: ( COMMA tuple )*
                    while True: #loop157
                        alt157 = 2
                        LA157_0 = self.input.LA(1)

                        if (LA157_0 == COMMA) :
                            alt157 = 1


                        if alt157 == 1:
                            # QueryParser.g:735:26: COMMA tuple
                            pass 
                            COMMA601=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_bag5817) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA601)
                            self._state.following.append(self.FOLLOW_tuple_in_bag5819)
                            tuple602 = self.tuple()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_tuple.add(tuple602.tree)


                        else:
                            break #loop157
                    RIGHT_CURLY603=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_bag5824) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_CURLY.add(RIGHT_CURLY603)

                    # AST Rewrite
                    # elements: tuple
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 736:4: -> ^( BAG_VAL ( tuple )+ )
                        # QueryParser.g:736:7: ^( BAG_VAL ( tuple )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BAG_VAL, "BAG_VAL"), root_1)

                        # QueryParser.g:736:18: ( tuple )+
                        if not (stream_tuple.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_tuple.hasNext():
                            self._adaptor.addChild(root_1, stream_tuple.nextTree())


                        stream_tuple.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt158 == 2:
                    # QueryParser.g:737:7: LEFT_CURLY RIGHT_CURLY
                    pass 
                    LEFT_CURLY604=self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_bag5846) 
                    if self._state.backtracking == 0:
                        stream_LEFT_CURLY.add(LEFT_CURLY604)
                    RIGHT_CURLY605=self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_bag5848) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_CURLY.add(RIGHT_CURLY605)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 738:4: -> ^( BAG_VAL )
                        # QueryParser.g:738:7: ^( BAG_VAL )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BAG_VAL, "BAG_VAL"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "bag"

    class tuple_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.tuple_return, self).__init__()

            self.tree = None




    # $ANTLR start "tuple"
    # QueryParser.g:741:1: tuple : ( LEFT_PAREN literal ( COMMA literal )* RIGHT_PAREN -> ^( TUPLE_VAL ( literal )+ ) | LEFT_PAREN RIGHT_PAREN -> ^( TUPLE_VAL ) );
    def tuple(self, ):

        retval = self.tuple_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN606 = None
        COMMA608 = None
        RIGHT_PAREN610 = None
        LEFT_PAREN611 = None
        RIGHT_PAREN612 = None
        literal607 = None

        literal609 = None


        LEFT_PAREN606_tree = None
        COMMA608_tree = None
        RIGHT_PAREN610_tree = None
        LEFT_PAREN611_tree = None
        RIGHT_PAREN612_tree = None
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_COMMA = RewriteRuleTokenStream(self._adaptor, "token COMMA")
        stream_literal = RewriteRuleSubtreeStream(self._adaptor, "rule literal")
        try:
            try:
                # QueryParser.g:741:7: ( LEFT_PAREN literal ( COMMA literal )* RIGHT_PAREN -> ^( TUPLE_VAL ( literal )+ ) | LEFT_PAREN RIGHT_PAREN -> ^( TUPLE_VAL ) )
                alt160 = 2
                LA160_0 = self.input.LA(1)

                if (LA160_0 == LEFT_PAREN) :
                    LA160_1 = self.input.LA(2)

                    if (LA160_1 == RIGHT_PAREN) :
                        alt160 = 2
                    elif ((TRUE <= LA160_1 <= FALSE) or (IDENTIFIER_L <= LA160_1 <= INTEGER) or LA160_1 == LONGINTEGER or LA160_1 == MINUS or (DOUBLENUMBER <= LA160_1 <= QUOTEDSTRING) or LA160_1 == LEFT_PAREN or LA160_1 == LEFT_CURLY or LA160_1 == LEFT_BRACKET) :
                        alt160 = 1
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 160, 1, self.input)

                        raise nvae

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 160, 0, self.input)

                    raise nvae

                if alt160 == 1:
                    # QueryParser.g:741:9: LEFT_PAREN literal ( COMMA literal )* RIGHT_PAREN
                    pass 
                    LEFT_PAREN606=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_tuple5868) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN606)
                    self._state.following.append(self.FOLLOW_literal_in_tuple5870)
                    literal607 = self.literal()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_literal.add(literal607.tree)
                    # QueryParser.g:741:28: ( COMMA literal )*
                    while True: #loop159
                        alt159 = 2
                        LA159_0 = self.input.LA(1)

                        if (LA159_0 == COMMA) :
                            alt159 = 1


                        if alt159 == 1:
                            # QueryParser.g:741:30: COMMA literal
                            pass 
                            COMMA608=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_tuple5874) 
                            if self._state.backtracking == 0:
                                stream_COMMA.add(COMMA608)
                            self._state.following.append(self.FOLLOW_literal_in_tuple5876)
                            literal609 = self.literal()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_literal.add(literal609.tree)


                        else:
                            break #loop159
                    RIGHT_PAREN610=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_tuple5881) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN610)

                    # AST Rewrite
                    # elements: literal
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 742:6: -> ^( TUPLE_VAL ( literal )+ )
                        # QueryParser.g:742:9: ^( TUPLE_VAL ( literal )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TUPLE_VAL, "TUPLE_VAL"), root_1)

                        # QueryParser.g:742:22: ( literal )+
                        if not (stream_literal.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_literal.hasNext():
                            self._adaptor.addChild(root_1, stream_literal.nextTree())


                        stream_literal.reset()

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                elif alt160 == 2:
                    # QueryParser.g:743:9: LEFT_PAREN RIGHT_PAREN
                    pass 
                    LEFT_PAREN611=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_tuple5907) 
                    if self._state.backtracking == 0:
                        stream_LEFT_PAREN.add(LEFT_PAREN611)
                    RIGHT_PAREN612=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_tuple5909) 
                    if self._state.backtracking == 0:
                        stream_RIGHT_PAREN.add(RIGHT_PAREN612)

                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:

                        retval.tree = root_0

                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 744:6: -> ^( TUPLE_VAL )
                        # QueryParser.g:744:9: ^( TUPLE_VAL )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(TUPLE_VAL, "TUPLE_VAL"), root_1)

                        self._adaptor.addChild(root_0, root_1)



                        retval.tree = root_0


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "tuple"

    class eid_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.eid_return, self).__init__()

            self.tree = None




    # $ANTLR start "eid"
    # QueryParser.g:748:1: eid : ( rel_str_op | IMPORT | RETURNS | DEFINE | LOAD | FILTER | FOREACH | CUBE | ROLLUP | ORDER | DISTINCT | COGROUP | JOIN | CROSS | UNION | SPLIT | INTO | IF | ALL | AS | BY | USING | INNER | OUTER | PARALLEL | PARTITION | GROUP | AND | OR | NOT | GENERATE | FLATTEN | ASC | DESC | BOOL | INT | LONG | FLOAT | DOUBLE | DATETIME | CHARARRAY | BYTEARRAY | BAG | TUPLE | MAP | IS | STREAM | THROUGH | STORE | MAPREDUCE | SHIP | CACHE | INPUT | OUTPUT | STDERROR | STDIN | STDOUT | LIMIT | SAMPLE | LEFT | RIGHT | FULL | identifier | null_keyword | TRUE | FALSE | REALIAS );
    def eid(self, ):

        retval = self.eid_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IMPORT614 = None
        RETURNS615 = None
        DEFINE616 = None
        LOAD617 = None
        FILTER618 = None
        FOREACH619 = None
        CUBE620 = None
        ROLLUP621 = None
        ORDER622 = None
        DISTINCT623 = None
        COGROUP624 = None
        JOIN625 = None
        CROSS626 = None
        UNION627 = None
        SPLIT628 = None
        INTO629 = None
        IF630 = None
        ALL631 = None
        AS632 = None
        BY633 = None
        USING634 = None
        INNER635 = None
        OUTER636 = None
        PARALLEL637 = None
        PARTITION638 = None
        GROUP639 = None
        AND640 = None
        OR641 = None
        NOT642 = None
        GENERATE643 = None
        FLATTEN644 = None
        ASC645 = None
        DESC646 = None
        BOOL647 = None
        INT648 = None
        LONG649 = None
        FLOAT650 = None
        DOUBLE651 = None
        DATETIME652 = None
        CHARARRAY653 = None
        BYTEARRAY654 = None
        BAG655 = None
        TUPLE656 = None
        MAP657 = None
        IS658 = None
        STREAM659 = None
        THROUGH660 = None
        STORE661 = None
        MAPREDUCE662 = None
        SHIP663 = None
        CACHE664 = None
        INPUT665 = None
        OUTPUT666 = None
        STDERROR667 = None
        STDIN668 = None
        STDOUT669 = None
        LIMIT670 = None
        SAMPLE671 = None
        LEFT672 = None
        RIGHT673 = None
        FULL674 = None
        TRUE677 = None
        FALSE678 = None
        REALIAS679 = None
        rel_str_op613 = None

        identifier675 = None

        null_keyword676 = None


        IMPORT614_tree = None
        RETURNS615_tree = None
        DEFINE616_tree = None
        LOAD617_tree = None
        FILTER618_tree = None
        FOREACH619_tree = None
        CUBE620_tree = None
        ROLLUP621_tree = None
        ORDER622_tree = None
        DISTINCT623_tree = None
        COGROUP624_tree = None
        JOIN625_tree = None
        CROSS626_tree = None
        UNION627_tree = None
        SPLIT628_tree = None
        INTO629_tree = None
        IF630_tree = None
        ALL631_tree = None
        AS632_tree = None
        BY633_tree = None
        USING634_tree = None
        INNER635_tree = None
        OUTER636_tree = None
        PARALLEL637_tree = None
        PARTITION638_tree = None
        GROUP639_tree = None
        AND640_tree = None
        OR641_tree = None
        NOT642_tree = None
        GENERATE643_tree = None
        FLATTEN644_tree = None
        ASC645_tree = None
        DESC646_tree = None
        BOOL647_tree = None
        INT648_tree = None
        LONG649_tree = None
        FLOAT650_tree = None
        DOUBLE651_tree = None
        DATETIME652_tree = None
        CHARARRAY653_tree = None
        BYTEARRAY654_tree = None
        BAG655_tree = None
        TUPLE656_tree = None
        MAP657_tree = None
        IS658_tree = None
        STREAM659_tree = None
        THROUGH660_tree = None
        STORE661_tree = None
        MAPREDUCE662_tree = None
        SHIP663_tree = None
        CACHE664_tree = None
        INPUT665_tree = None
        OUTPUT666_tree = None
        STDERROR667_tree = None
        STDIN668_tree = None
        STDOUT669_tree = None
        LIMIT670_tree = None
        SAMPLE671_tree = None
        LEFT672_tree = None
        RIGHT673_tree = None
        FULL674_tree = None
        TRUE677_tree = None
        FALSE678_tree = None
        REALIAS679_tree = None

        try:
            try:
                # QueryParser.g:748:5: ( rel_str_op | IMPORT | RETURNS | DEFINE | LOAD | FILTER | FOREACH | CUBE | ROLLUP | ORDER | DISTINCT | COGROUP | JOIN | CROSS | UNION | SPLIT | INTO | IF | ALL | AS | BY | USING | INNER | OUTER | PARALLEL | PARTITION | GROUP | AND | OR | NOT | GENERATE | FLATTEN | ASC | DESC | BOOL | INT | LONG | FLOAT | DOUBLE | DATETIME | CHARARRAY | BYTEARRAY | BAG | TUPLE | MAP | IS | STREAM | THROUGH | STORE | MAPREDUCE | SHIP | CACHE | INPUT | OUTPUT | STDERROR | STDIN | STDOUT | LIMIT | SAMPLE | LEFT | RIGHT | FULL | identifier | null_keyword | TRUE | FALSE | REALIAS )
                alt161 = 67
                alt161 = self.dfa161.predict(self.input)
                if alt161 == 1:
                    # QueryParser.g:748:7: rel_str_op
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_str_op_in_eid5932)
                    rel_str_op613 = self.rel_str_op()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_str_op613.tree)


                elif alt161 == 2:
                    # QueryParser.g:749:7: IMPORT
                    pass 
                    root_0 = self._adaptor.nil()

                    IMPORT614=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_eid5940)
                    if self._state.backtracking == 0:

                        IMPORT614_tree = self._adaptor.createWithPayload(IMPORT614)
                        self._adaptor.addChild(root_0, IMPORT614_tree)



                elif alt161 == 3:
                    # QueryParser.g:750:7: RETURNS
                    pass 
                    root_0 = self._adaptor.nil()

                    RETURNS615=self.match(self.input, RETURNS, self.FOLLOW_RETURNS_in_eid5948)
                    if self._state.backtracking == 0:

                        RETURNS615_tree = self._adaptor.createWithPayload(RETURNS615)
                        self._adaptor.addChild(root_0, RETURNS615_tree)



                elif alt161 == 4:
                    # QueryParser.g:751:7: DEFINE
                    pass 
                    root_0 = self._adaptor.nil()

                    DEFINE616=self.match(self.input, DEFINE, self.FOLLOW_DEFINE_in_eid5956)
                    if self._state.backtracking == 0:

                        DEFINE616_tree = self._adaptor.createWithPayload(DEFINE616)
                        self._adaptor.addChild(root_0, DEFINE616_tree)



                elif alt161 == 5:
                    # QueryParser.g:752:7: LOAD
                    pass 
                    root_0 = self._adaptor.nil()

                    LOAD617=self.match(self.input, LOAD, self.FOLLOW_LOAD_in_eid5964)
                    if self._state.backtracking == 0:

                        LOAD617_tree = self._adaptor.createWithPayload(LOAD617)
                        self._adaptor.addChild(root_0, LOAD617_tree)



                elif alt161 == 6:
                    # QueryParser.g:753:7: FILTER
                    pass 
                    root_0 = self._adaptor.nil()

                    FILTER618=self.match(self.input, FILTER, self.FOLLOW_FILTER_in_eid5972)
                    if self._state.backtracking == 0:

                        FILTER618_tree = self._adaptor.createWithPayload(FILTER618)
                        self._adaptor.addChild(root_0, FILTER618_tree)



                elif alt161 == 7:
                    # QueryParser.g:754:7: FOREACH
                    pass 
                    root_0 = self._adaptor.nil()

                    FOREACH619=self.match(self.input, FOREACH, self.FOLLOW_FOREACH_in_eid5980)
                    if self._state.backtracking == 0:

                        FOREACH619_tree = self._adaptor.createWithPayload(FOREACH619)
                        self._adaptor.addChild(root_0, FOREACH619_tree)



                elif alt161 == 8:
                    # QueryParser.g:755:7: CUBE
                    pass 
                    root_0 = self._adaptor.nil()

                    CUBE620=self.match(self.input, CUBE, self.FOLLOW_CUBE_in_eid5988)
                    if self._state.backtracking == 0:

                        CUBE620_tree = self._adaptor.createWithPayload(CUBE620)
                        self._adaptor.addChild(root_0, CUBE620_tree)



                elif alt161 == 9:
                    # QueryParser.g:756:7: ROLLUP
                    pass 
                    root_0 = self._adaptor.nil()

                    ROLLUP621=self.match(self.input, ROLLUP, self.FOLLOW_ROLLUP_in_eid5996)
                    if self._state.backtracking == 0:

                        ROLLUP621_tree = self._adaptor.createWithPayload(ROLLUP621)
                        self._adaptor.addChild(root_0, ROLLUP621_tree)



                elif alt161 == 10:
                    # QueryParser.g:757:7: ORDER
                    pass 
                    root_0 = self._adaptor.nil()

                    ORDER622=self.match(self.input, ORDER, self.FOLLOW_ORDER_in_eid6004)
                    if self._state.backtracking == 0:

                        ORDER622_tree = self._adaptor.createWithPayload(ORDER622)
                        self._adaptor.addChild(root_0, ORDER622_tree)



                elif alt161 == 11:
                    # QueryParser.g:758:7: DISTINCT
                    pass 
                    root_0 = self._adaptor.nil()

                    DISTINCT623=self.match(self.input, DISTINCT, self.FOLLOW_DISTINCT_in_eid6012)
                    if self._state.backtracking == 0:

                        DISTINCT623_tree = self._adaptor.createWithPayload(DISTINCT623)
                        self._adaptor.addChild(root_0, DISTINCT623_tree)



                elif alt161 == 12:
                    # QueryParser.g:759:7: COGROUP
                    pass 
                    root_0 = self._adaptor.nil()

                    COGROUP624=self.match(self.input, COGROUP, self.FOLLOW_COGROUP_in_eid6020)
                    if self._state.backtracking == 0:

                        COGROUP624_tree = self._adaptor.createWithPayload(COGROUP624)
                        self._adaptor.addChild(root_0, COGROUP624_tree)



                elif alt161 == 13:
                    # QueryParser.g:760:7: JOIN
                    pass 
                    root_0 = self._adaptor.nil()

                    JOIN625=self.match(self.input, JOIN, self.FOLLOW_JOIN_in_eid6028)
                    if self._state.backtracking == 0:

                        JOIN625_tree = self._adaptor.createWithPayload(JOIN625)
                        self._adaptor.addChild(root_0, JOIN625_tree)



                elif alt161 == 14:
                    # QueryParser.g:761:7: CROSS
                    pass 
                    root_0 = self._adaptor.nil()

                    CROSS626=self.match(self.input, CROSS, self.FOLLOW_CROSS_in_eid6036)
                    if self._state.backtracking == 0:

                        CROSS626_tree = self._adaptor.createWithPayload(CROSS626)
                        self._adaptor.addChild(root_0, CROSS626_tree)



                elif alt161 == 15:
                    # QueryParser.g:762:7: UNION
                    pass 
                    root_0 = self._adaptor.nil()

                    UNION627=self.match(self.input, UNION, self.FOLLOW_UNION_in_eid6044)
                    if self._state.backtracking == 0:

                        UNION627_tree = self._adaptor.createWithPayload(UNION627)
                        self._adaptor.addChild(root_0, UNION627_tree)



                elif alt161 == 16:
                    # QueryParser.g:763:7: SPLIT
                    pass 
                    root_0 = self._adaptor.nil()

                    SPLIT628=self.match(self.input, SPLIT, self.FOLLOW_SPLIT_in_eid6052)
                    if self._state.backtracking == 0:

                        SPLIT628_tree = self._adaptor.createWithPayload(SPLIT628)
                        self._adaptor.addChild(root_0, SPLIT628_tree)



                elif alt161 == 17:
                    # QueryParser.g:764:7: INTO
                    pass 
                    root_0 = self._adaptor.nil()

                    INTO629=self.match(self.input, INTO, self.FOLLOW_INTO_in_eid6060)
                    if self._state.backtracking == 0:

                        INTO629_tree = self._adaptor.createWithPayload(INTO629)
                        self._adaptor.addChild(root_0, INTO629_tree)



                elif alt161 == 18:
                    # QueryParser.g:765:7: IF
                    pass 
                    root_0 = self._adaptor.nil()

                    IF630=self.match(self.input, IF, self.FOLLOW_IF_in_eid6068)
                    if self._state.backtracking == 0:

                        IF630_tree = self._adaptor.createWithPayload(IF630)
                        self._adaptor.addChild(root_0, IF630_tree)



                elif alt161 == 19:
                    # QueryParser.g:766:7: ALL
                    pass 
                    root_0 = self._adaptor.nil()

                    ALL631=self.match(self.input, ALL, self.FOLLOW_ALL_in_eid6076)
                    if self._state.backtracking == 0:

                        ALL631_tree = self._adaptor.createWithPayload(ALL631)
                        self._adaptor.addChild(root_0, ALL631_tree)



                elif alt161 == 20:
                    # QueryParser.g:767:7: AS
                    pass 
                    root_0 = self._adaptor.nil()

                    AS632=self.match(self.input, AS, self.FOLLOW_AS_in_eid6084)
                    if self._state.backtracking == 0:

                        AS632_tree = self._adaptor.createWithPayload(AS632)
                        self._adaptor.addChild(root_0, AS632_tree)



                elif alt161 == 21:
                    # QueryParser.g:768:7: BY
                    pass 
                    root_0 = self._adaptor.nil()

                    BY633=self.match(self.input, BY, self.FOLLOW_BY_in_eid6092)
                    if self._state.backtracking == 0:

                        BY633_tree = self._adaptor.createWithPayload(BY633)
                        self._adaptor.addChild(root_0, BY633_tree)



                elif alt161 == 22:
                    # QueryParser.g:769:7: USING
                    pass 
                    root_0 = self._adaptor.nil()

                    USING634=self.match(self.input, USING, self.FOLLOW_USING_in_eid6100)
                    if self._state.backtracking == 0:

                        USING634_tree = self._adaptor.createWithPayload(USING634)
                        self._adaptor.addChild(root_0, USING634_tree)



                elif alt161 == 23:
                    # QueryParser.g:770:7: INNER
                    pass 
                    root_0 = self._adaptor.nil()

                    INNER635=self.match(self.input, INNER, self.FOLLOW_INNER_in_eid6108)
                    if self._state.backtracking == 0:

                        INNER635_tree = self._adaptor.createWithPayload(INNER635)
                        self._adaptor.addChild(root_0, INNER635_tree)



                elif alt161 == 24:
                    # QueryParser.g:771:7: OUTER
                    pass 
                    root_0 = self._adaptor.nil()

                    OUTER636=self.match(self.input, OUTER, self.FOLLOW_OUTER_in_eid6116)
                    if self._state.backtracking == 0:

                        OUTER636_tree = self._adaptor.createWithPayload(OUTER636)
                        self._adaptor.addChild(root_0, OUTER636_tree)



                elif alt161 == 25:
                    # QueryParser.g:772:7: PARALLEL
                    pass 
                    root_0 = self._adaptor.nil()

                    PARALLEL637=self.match(self.input, PARALLEL, self.FOLLOW_PARALLEL_in_eid6124)
                    if self._state.backtracking == 0:

                        PARALLEL637_tree = self._adaptor.createWithPayload(PARALLEL637)
                        self._adaptor.addChild(root_0, PARALLEL637_tree)



                elif alt161 == 26:
                    # QueryParser.g:773:7: PARTITION
                    pass 
                    root_0 = self._adaptor.nil()

                    PARTITION638=self.match(self.input, PARTITION, self.FOLLOW_PARTITION_in_eid6132)
                    if self._state.backtracking == 0:

                        PARTITION638_tree = self._adaptor.createWithPayload(PARTITION638)
                        self._adaptor.addChild(root_0, PARTITION638_tree)



                elif alt161 == 27:
                    # QueryParser.g:774:7: GROUP
                    pass 
                    root_0 = self._adaptor.nil()

                    GROUP639=self.match(self.input, GROUP, self.FOLLOW_GROUP_in_eid6140)
                    if self._state.backtracking == 0:

                        GROUP639_tree = self._adaptor.createWithPayload(GROUP639)
                        self._adaptor.addChild(root_0, GROUP639_tree)



                elif alt161 == 28:
                    # QueryParser.g:775:7: AND
                    pass 
                    root_0 = self._adaptor.nil()

                    AND640=self.match(self.input, AND, self.FOLLOW_AND_in_eid6148)
                    if self._state.backtracking == 0:

                        AND640_tree = self._adaptor.createWithPayload(AND640)
                        self._adaptor.addChild(root_0, AND640_tree)



                elif alt161 == 29:
                    # QueryParser.g:776:7: OR
                    pass 
                    root_0 = self._adaptor.nil()

                    OR641=self.match(self.input, OR, self.FOLLOW_OR_in_eid6156)
                    if self._state.backtracking == 0:

                        OR641_tree = self._adaptor.createWithPayload(OR641)
                        self._adaptor.addChild(root_0, OR641_tree)



                elif alt161 == 30:
                    # QueryParser.g:777:7: NOT
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT642=self.match(self.input, NOT, self.FOLLOW_NOT_in_eid6164)
                    if self._state.backtracking == 0:

                        NOT642_tree = self._adaptor.createWithPayload(NOT642)
                        self._adaptor.addChild(root_0, NOT642_tree)



                elif alt161 == 31:
                    # QueryParser.g:778:7: GENERATE
                    pass 
                    root_0 = self._adaptor.nil()

                    GENERATE643=self.match(self.input, GENERATE, self.FOLLOW_GENERATE_in_eid6172)
                    if self._state.backtracking == 0:

                        GENERATE643_tree = self._adaptor.createWithPayload(GENERATE643)
                        self._adaptor.addChild(root_0, GENERATE643_tree)



                elif alt161 == 32:
                    # QueryParser.g:779:7: FLATTEN
                    pass 
                    root_0 = self._adaptor.nil()

                    FLATTEN644=self.match(self.input, FLATTEN, self.FOLLOW_FLATTEN_in_eid6180)
                    if self._state.backtracking == 0:

                        FLATTEN644_tree = self._adaptor.createWithPayload(FLATTEN644)
                        self._adaptor.addChild(root_0, FLATTEN644_tree)



                elif alt161 == 33:
                    # QueryParser.g:780:7: ASC
                    pass 
                    root_0 = self._adaptor.nil()

                    ASC645=self.match(self.input, ASC, self.FOLLOW_ASC_in_eid6188)
                    if self._state.backtracking == 0:

                        ASC645_tree = self._adaptor.createWithPayload(ASC645)
                        self._adaptor.addChild(root_0, ASC645_tree)



                elif alt161 == 34:
                    # QueryParser.g:781:7: DESC
                    pass 
                    root_0 = self._adaptor.nil()

                    DESC646=self.match(self.input, DESC, self.FOLLOW_DESC_in_eid6196)
                    if self._state.backtracking == 0:

                        DESC646_tree = self._adaptor.createWithPayload(DESC646)
                        self._adaptor.addChild(root_0, DESC646_tree)



                elif alt161 == 35:
                    # QueryParser.g:782:7: BOOL
                    pass 
                    root_0 = self._adaptor.nil()

                    BOOL647=self.match(self.input, BOOL, self.FOLLOW_BOOL_in_eid6204)
                    if self._state.backtracking == 0:

                        BOOL647_tree = self._adaptor.createWithPayload(BOOL647)
                        self._adaptor.addChild(root_0, BOOL647_tree)



                elif alt161 == 36:
                    # QueryParser.g:783:7: INT
                    pass 
                    root_0 = self._adaptor.nil()

                    INT648=self.match(self.input, INT, self.FOLLOW_INT_in_eid6212)
                    if self._state.backtracking == 0:

                        INT648_tree = self._adaptor.createWithPayload(INT648)
                        self._adaptor.addChild(root_0, INT648_tree)



                elif alt161 == 37:
                    # QueryParser.g:784:7: LONG
                    pass 
                    root_0 = self._adaptor.nil()

                    LONG649=self.match(self.input, LONG, self.FOLLOW_LONG_in_eid6220)
                    if self._state.backtracking == 0:

                        LONG649_tree = self._adaptor.createWithPayload(LONG649)
                        self._adaptor.addChild(root_0, LONG649_tree)



                elif alt161 == 38:
                    # QueryParser.g:785:7: FLOAT
                    pass 
                    root_0 = self._adaptor.nil()

                    FLOAT650=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_eid6228)
                    if self._state.backtracking == 0:

                        FLOAT650_tree = self._adaptor.createWithPayload(FLOAT650)
                        self._adaptor.addChild(root_0, FLOAT650_tree)



                elif alt161 == 39:
                    # QueryParser.g:786:7: DOUBLE
                    pass 
                    root_0 = self._adaptor.nil()

                    DOUBLE651=self.match(self.input, DOUBLE, self.FOLLOW_DOUBLE_in_eid6236)
                    if self._state.backtracking == 0:

                        DOUBLE651_tree = self._adaptor.createWithPayload(DOUBLE651)
                        self._adaptor.addChild(root_0, DOUBLE651_tree)



                elif alt161 == 40:
                    # QueryParser.g:787:7: DATETIME
                    pass 
                    root_0 = self._adaptor.nil()

                    DATETIME652=self.match(self.input, DATETIME, self.FOLLOW_DATETIME_in_eid6244)
                    if self._state.backtracking == 0:

                        DATETIME652_tree = self._adaptor.createWithPayload(DATETIME652)
                        self._adaptor.addChild(root_0, DATETIME652_tree)



                elif alt161 == 41:
                    # QueryParser.g:788:7: CHARARRAY
                    pass 
                    root_0 = self._adaptor.nil()

                    CHARARRAY653=self.match(self.input, CHARARRAY, self.FOLLOW_CHARARRAY_in_eid6252)
                    if self._state.backtracking == 0:

                        CHARARRAY653_tree = self._adaptor.createWithPayload(CHARARRAY653)
                        self._adaptor.addChild(root_0, CHARARRAY653_tree)



                elif alt161 == 42:
                    # QueryParser.g:789:7: BYTEARRAY
                    pass 
                    root_0 = self._adaptor.nil()

                    BYTEARRAY654=self.match(self.input, BYTEARRAY, self.FOLLOW_BYTEARRAY_in_eid6260)
                    if self._state.backtracking == 0:

                        BYTEARRAY654_tree = self._adaptor.createWithPayload(BYTEARRAY654)
                        self._adaptor.addChild(root_0, BYTEARRAY654_tree)



                elif alt161 == 43:
                    # QueryParser.g:790:7: BAG
                    pass 
                    root_0 = self._adaptor.nil()

                    BAG655=self.match(self.input, BAG, self.FOLLOW_BAG_in_eid6268)
                    if self._state.backtracking == 0:

                        BAG655_tree = self._adaptor.createWithPayload(BAG655)
                        self._adaptor.addChild(root_0, BAG655_tree)



                elif alt161 == 44:
                    # QueryParser.g:791:7: TUPLE
                    pass 
                    root_0 = self._adaptor.nil()

                    TUPLE656=self.match(self.input, TUPLE, self.FOLLOW_TUPLE_in_eid6276)
                    if self._state.backtracking == 0:

                        TUPLE656_tree = self._adaptor.createWithPayload(TUPLE656)
                        self._adaptor.addChild(root_0, TUPLE656_tree)



                elif alt161 == 45:
                    # QueryParser.g:792:7: MAP
                    pass 
                    root_0 = self._adaptor.nil()

                    MAP657=self.match(self.input, MAP, self.FOLLOW_MAP_in_eid6284)
                    if self._state.backtracking == 0:

                        MAP657_tree = self._adaptor.createWithPayload(MAP657)
                        self._adaptor.addChild(root_0, MAP657_tree)



                elif alt161 == 46:
                    # QueryParser.g:793:7: IS
                    pass 
                    root_0 = self._adaptor.nil()

                    IS658=self.match(self.input, IS, self.FOLLOW_IS_in_eid6292)
                    if self._state.backtracking == 0:

                        IS658_tree = self._adaptor.createWithPayload(IS658)
                        self._adaptor.addChild(root_0, IS658_tree)



                elif alt161 == 47:
                    # QueryParser.g:794:7: STREAM
                    pass 
                    root_0 = self._adaptor.nil()

                    STREAM659=self.match(self.input, STREAM, self.FOLLOW_STREAM_in_eid6300)
                    if self._state.backtracking == 0:

                        STREAM659_tree = self._adaptor.createWithPayload(STREAM659)
                        self._adaptor.addChild(root_0, STREAM659_tree)



                elif alt161 == 48:
                    # QueryParser.g:795:7: THROUGH
                    pass 
                    root_0 = self._adaptor.nil()

                    THROUGH660=self.match(self.input, THROUGH, self.FOLLOW_THROUGH_in_eid6308)
                    if self._state.backtracking == 0:

                        THROUGH660_tree = self._adaptor.createWithPayload(THROUGH660)
                        self._adaptor.addChild(root_0, THROUGH660_tree)



                elif alt161 == 49:
                    # QueryParser.g:796:7: STORE
                    pass 
                    root_0 = self._adaptor.nil()

                    STORE661=self.match(self.input, STORE, self.FOLLOW_STORE_in_eid6316)
                    if self._state.backtracking == 0:

                        STORE661_tree = self._adaptor.createWithPayload(STORE661)
                        self._adaptor.addChild(root_0, STORE661_tree)



                elif alt161 == 50:
                    # QueryParser.g:797:7: MAPREDUCE
                    pass 
                    root_0 = self._adaptor.nil()

                    MAPREDUCE662=self.match(self.input, MAPREDUCE, self.FOLLOW_MAPREDUCE_in_eid6324)
                    if self._state.backtracking == 0:

                        MAPREDUCE662_tree = self._adaptor.createWithPayload(MAPREDUCE662)
                        self._adaptor.addChild(root_0, MAPREDUCE662_tree)



                elif alt161 == 51:
                    # QueryParser.g:798:7: SHIP
                    pass 
                    root_0 = self._adaptor.nil()

                    SHIP663=self.match(self.input, SHIP, self.FOLLOW_SHIP_in_eid6332)
                    if self._state.backtracking == 0:

                        SHIP663_tree = self._adaptor.createWithPayload(SHIP663)
                        self._adaptor.addChild(root_0, SHIP663_tree)



                elif alt161 == 52:
                    # QueryParser.g:799:7: CACHE
                    pass 
                    root_0 = self._adaptor.nil()

                    CACHE664=self.match(self.input, CACHE, self.FOLLOW_CACHE_in_eid6340)
                    if self._state.backtracking == 0:

                        CACHE664_tree = self._adaptor.createWithPayload(CACHE664)
                        self._adaptor.addChild(root_0, CACHE664_tree)



                elif alt161 == 53:
                    # QueryParser.g:800:7: INPUT
                    pass 
                    root_0 = self._adaptor.nil()

                    INPUT665=self.match(self.input, INPUT, self.FOLLOW_INPUT_in_eid6348)
                    if self._state.backtracking == 0:

                        INPUT665_tree = self._adaptor.createWithPayload(INPUT665)
                        self._adaptor.addChild(root_0, INPUT665_tree)



                elif alt161 == 54:
                    # QueryParser.g:801:7: OUTPUT
                    pass 
                    root_0 = self._adaptor.nil()

                    OUTPUT666=self.match(self.input, OUTPUT, self.FOLLOW_OUTPUT_in_eid6356)
                    if self._state.backtracking == 0:

                        OUTPUT666_tree = self._adaptor.createWithPayload(OUTPUT666)
                        self._adaptor.addChild(root_0, OUTPUT666_tree)



                elif alt161 == 55:
                    # QueryParser.g:802:7: STDERROR
                    pass 
                    root_0 = self._adaptor.nil()

                    STDERROR667=self.match(self.input, STDERROR, self.FOLLOW_STDERROR_in_eid6364)
                    if self._state.backtracking == 0:

                        STDERROR667_tree = self._adaptor.createWithPayload(STDERROR667)
                        self._adaptor.addChild(root_0, STDERROR667_tree)



                elif alt161 == 56:
                    # QueryParser.g:803:7: STDIN
                    pass 
                    root_0 = self._adaptor.nil()

                    STDIN668=self.match(self.input, STDIN, self.FOLLOW_STDIN_in_eid6372)
                    if self._state.backtracking == 0:

                        STDIN668_tree = self._adaptor.createWithPayload(STDIN668)
                        self._adaptor.addChild(root_0, STDIN668_tree)



                elif alt161 == 57:
                    # QueryParser.g:804:7: STDOUT
                    pass 
                    root_0 = self._adaptor.nil()

                    STDOUT669=self.match(self.input, STDOUT, self.FOLLOW_STDOUT_in_eid6380)
                    if self._state.backtracking == 0:

                        STDOUT669_tree = self._adaptor.createWithPayload(STDOUT669)
                        self._adaptor.addChild(root_0, STDOUT669_tree)



                elif alt161 == 58:
                    # QueryParser.g:805:7: LIMIT
                    pass 
                    root_0 = self._adaptor.nil()

                    LIMIT670=self.match(self.input, LIMIT, self.FOLLOW_LIMIT_in_eid6388)
                    if self._state.backtracking == 0:

                        LIMIT670_tree = self._adaptor.createWithPayload(LIMIT670)
                        self._adaptor.addChild(root_0, LIMIT670_tree)



                elif alt161 == 59:
                    # QueryParser.g:806:7: SAMPLE
                    pass 
                    root_0 = self._adaptor.nil()

                    SAMPLE671=self.match(self.input, SAMPLE, self.FOLLOW_SAMPLE_in_eid6396)
                    if self._state.backtracking == 0:

                        SAMPLE671_tree = self._adaptor.createWithPayload(SAMPLE671)
                        self._adaptor.addChild(root_0, SAMPLE671_tree)



                elif alt161 == 60:
                    # QueryParser.g:807:7: LEFT
                    pass 
                    root_0 = self._adaptor.nil()

                    LEFT672=self.match(self.input, LEFT, self.FOLLOW_LEFT_in_eid6404)
                    if self._state.backtracking == 0:

                        LEFT672_tree = self._adaptor.createWithPayload(LEFT672)
                        self._adaptor.addChild(root_0, LEFT672_tree)



                elif alt161 == 61:
                    # QueryParser.g:808:7: RIGHT
                    pass 
                    root_0 = self._adaptor.nil()

                    RIGHT673=self.match(self.input, RIGHT, self.FOLLOW_RIGHT_in_eid6412)
                    if self._state.backtracking == 0:

                        RIGHT673_tree = self._adaptor.createWithPayload(RIGHT673)
                        self._adaptor.addChild(root_0, RIGHT673_tree)



                elif alt161 == 62:
                    # QueryParser.g:809:7: FULL
                    pass 
                    root_0 = self._adaptor.nil()

                    FULL674=self.match(self.input, FULL, self.FOLLOW_FULL_in_eid6420)
                    if self._state.backtracking == 0:

                        FULL674_tree = self._adaptor.createWithPayload(FULL674)
                        self._adaptor.addChild(root_0, FULL674_tree)



                elif alt161 == 63:
                    # QueryParser.g:810:7: identifier
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_identifier_in_eid6428)
                    identifier675 = self.identifier()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, identifier675.tree)


                elif alt161 == 64:
                    # QueryParser.g:811:7: null_keyword
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_null_keyword_in_eid6436)
                    null_keyword676 = self.null_keyword()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, null_keyword676.tree)


                elif alt161 == 65:
                    # QueryParser.g:812:7: TRUE
                    pass 
                    root_0 = self._adaptor.nil()

                    TRUE677=self.match(self.input, TRUE, self.FOLLOW_TRUE_in_eid6444)
                    if self._state.backtracking == 0:

                        TRUE677_tree = self._adaptor.createWithPayload(TRUE677)
                        self._adaptor.addChild(root_0, TRUE677_tree)



                elif alt161 == 66:
                    # QueryParser.g:813:7: FALSE
                    pass 
                    root_0 = self._adaptor.nil()

                    FALSE678=self.match(self.input, FALSE, self.FOLLOW_FALSE_in_eid6452)
                    if self._state.backtracking == 0:

                        FALSE678_tree = self._adaptor.createWithPayload(FALSE678)
                        self._adaptor.addChild(root_0, FALSE678_tree)



                elif alt161 == 67:
                    # QueryParser.g:814:7: REALIAS
                    pass 
                    root_0 = self._adaptor.nil()

                    REALIAS679=self.match(self.input, REALIAS, self.FOLLOW_REALIAS_in_eid6460)
                    if self._state.backtracking == 0:

                        REALIAS679_tree = self._adaptor.createWithPayload(REALIAS679)
                        self._adaptor.addChild(root_0, REALIAS679_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "eid"

    class rel_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op"
    # QueryParser.g:818:1: rel_op : ( rel_op_eq | rel_op_ne | rel_op_gt | rel_op_gte | rel_op_lt | rel_op_lte | STR_OP_MATCHES );
    def rel_op(self, ):

        retval = self.rel_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        STR_OP_MATCHES686 = None
        rel_op_eq680 = None

        rel_op_ne681 = None

        rel_op_gt682 = None

        rel_op_gte683 = None

        rel_op_lt684 = None

        rel_op_lte685 = None


        STR_OP_MATCHES686_tree = None

        try:
            try:
                # QueryParser.g:818:8: ( rel_op_eq | rel_op_ne | rel_op_gt | rel_op_gte | rel_op_lt | rel_op_lte | STR_OP_MATCHES )
                alt162 = 7
                LA162 = self.input.LA(1)
                if LA162 == STR_OP_EQ or LA162 == NUM_OP_EQ:
                    alt162 = 1
                elif LA162 == STR_OP_NE or LA162 == NUM_OP_NE:
                    alt162 = 2
                elif LA162 == STR_OP_GT or LA162 == NUM_OP_GT:
                    alt162 = 3
                elif LA162 == STR_OP_GTE or LA162 == NUM_OP_GTE:
                    alt162 = 4
                elif LA162 == STR_OP_LT or LA162 == NUM_OP_LT:
                    alt162 = 5
                elif LA162 == STR_OP_LTE or LA162 == NUM_OP_LTE:
                    alt162 = 6
                elif LA162 == STR_OP_MATCHES:
                    alt162 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 162, 0, self.input)

                    raise nvae

                if alt162 == 1:
                    # QueryParser.g:818:10: rel_op_eq
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_eq_in_rel_op6470)
                    rel_op_eq680 = self.rel_op_eq()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_eq680.tree)


                elif alt162 == 2:
                    # QueryParser.g:819:10: rel_op_ne
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_ne_in_rel_op6481)
                    rel_op_ne681 = self.rel_op_ne()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_ne681.tree)


                elif alt162 == 3:
                    # QueryParser.g:820:10: rel_op_gt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_gt_in_rel_op6492)
                    rel_op_gt682 = self.rel_op_gt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_gt682.tree)


                elif alt162 == 4:
                    # QueryParser.g:821:10: rel_op_gte
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_gte_in_rel_op6503)
                    rel_op_gte683 = self.rel_op_gte()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_gte683.tree)


                elif alt162 == 5:
                    # QueryParser.g:822:10: rel_op_lt
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_lt_in_rel_op6514)
                    rel_op_lt684 = self.rel_op_lt()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_lt684.tree)


                elif alt162 == 6:
                    # QueryParser.g:823:10: rel_op_lte
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_rel_op_lte_in_rel_op6525)
                    rel_op_lte685 = self.rel_op_lte()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, rel_op_lte685.tree)


                elif alt162 == 7:
                    # QueryParser.g:824:10: STR_OP_MATCHES
                    pass 
                    root_0 = self._adaptor.nil()

                    STR_OP_MATCHES686=self.match(self.input, STR_OP_MATCHES, self.FOLLOW_STR_OP_MATCHES_in_rel_op6536)
                    if self._state.backtracking == 0:

                        STR_OP_MATCHES686_tree = self._adaptor.createWithPayload(STR_OP_MATCHES686)
                        self._adaptor.addChild(root_0, STR_OP_MATCHES686_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op"

    class rel_op_eq_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_eq_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_eq"
    # QueryParser.g:827:1: rel_op_eq : ( STR_OP_EQ | NUM_OP_EQ );
    def rel_op_eq(self, ):

        retval = self.rel_op_eq_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set687 = None

        set687_tree = None

        try:
            try:
                # QueryParser.g:827:11: ( STR_OP_EQ | NUM_OP_EQ )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set687 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_EQ or self.input.LA(1) == NUM_OP_EQ:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set687))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_eq"

    class rel_op_ne_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_ne_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_ne"
    # QueryParser.g:830:1: rel_op_ne : ( STR_OP_NE | NUM_OP_NE );
    def rel_op_ne(self, ):

        retval = self.rel_op_ne_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set688 = None

        set688_tree = None

        try:
            try:
                # QueryParser.g:830:11: ( STR_OP_NE | NUM_OP_NE )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set688 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_NE or self.input.LA(1) == NUM_OP_NE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set688))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_ne"

    class rel_op_gt_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_gt_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_gt"
    # QueryParser.g:833:1: rel_op_gt : ( STR_OP_GT | NUM_OP_GT );
    def rel_op_gt(self, ):

        retval = self.rel_op_gt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set689 = None

        set689_tree = None

        try:
            try:
                # QueryParser.g:833:11: ( STR_OP_GT | NUM_OP_GT )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set689 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_GT or self.input.LA(1) == NUM_OP_GT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set689))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_gt"

    class rel_op_gte_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_gte_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_gte"
    # QueryParser.g:836:1: rel_op_gte : ( STR_OP_GTE | NUM_OP_GTE );
    def rel_op_gte(self, ):

        retval = self.rel_op_gte_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set690 = None

        set690_tree = None

        try:
            try:
                # QueryParser.g:836:12: ( STR_OP_GTE | NUM_OP_GTE )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set690 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_GTE or self.input.LA(1) == NUM_OP_GTE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set690))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_gte"

    class rel_op_lt_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_lt_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_lt"
    # QueryParser.g:839:1: rel_op_lt : ( STR_OP_LT | NUM_OP_LT );
    def rel_op_lt(self, ):

        retval = self.rel_op_lt_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set691 = None

        set691_tree = None

        try:
            try:
                # QueryParser.g:839:11: ( STR_OP_LT | NUM_OP_LT )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set691 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_LT or self.input.LA(1) == NUM_OP_LT:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set691))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_lt"

    class rel_op_lte_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_op_lte_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_op_lte"
    # QueryParser.g:842:1: rel_op_lte : ( STR_OP_LTE | NUM_OP_LTE );
    def rel_op_lte(self, ):

        retval = self.rel_op_lte_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set692 = None

        set692_tree = None

        try:
            try:
                # QueryParser.g:842:12: ( STR_OP_LTE | NUM_OP_LTE )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set692 = self.input.LT(1)
                if self.input.LA(1) == STR_OP_LTE or self.input.LA(1) == NUM_OP_LTE:
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set692))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_op_lte"

    class rel_str_op_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.rel_str_op_return, self).__init__()

            self.tree = None




    # $ANTLR start "rel_str_op"
    # QueryParser.g:845:1: rel_str_op : ( STR_OP_EQ | STR_OP_NE | STR_OP_GT | STR_OP_LT | STR_OP_GTE | STR_OP_LTE | STR_OP_MATCHES );
    def rel_str_op(self, ):

        retval = self.rel_str_op_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set693 = None

        set693_tree = None

        try:
            try:
                # QueryParser.g:845:12: ( STR_OP_EQ | STR_OP_NE | STR_OP_GT | STR_OP_LT | STR_OP_GTE | STR_OP_LTE | STR_OP_MATCHES )
                # QueryParser.g:
                pass 
                root_0 = self._adaptor.nil()

                set693 = self.input.LT(1)
                if (STR_OP_EQ <= self.input.LA(1) <= STR_OP_MATCHES):
                    self.input.consume()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set693))
                    self._state.errorRecovery = False

                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "rel_str_op"

    class null_keyword_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.null_keyword_return, self).__init__()

            self.tree = None




    # $ANTLR start "null_keyword"
    # QueryParser.g:854:1: null_keyword : {...}? IDENTIFIER_L -> NULL[$IDENTIFIER_L] ;
    def null_keyword(self, ):

        retval = self.null_keyword_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER_L694 = None

        IDENTIFIER_L694_tree = None
        stream_IDENTIFIER_L = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER_L")

        try:
            try:
                # QueryParser.g:854:14: ({...}? IDENTIFIER_L -> NULL[$IDENTIFIER_L] )
                # QueryParser.g:854:16: {...}? IDENTIFIER_L
                pass 
                if not ((input.LT(1).getText().equalsIgnoreCase("NULL"))):
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    raise FailedPredicateException(self.input, "null_keyword", "input.LT(1).getText().equalsIgnoreCase(\"NULL\")")

                IDENTIFIER_L694=self.match(self.input, IDENTIFIER_L, self.FOLLOW_IDENTIFIER_L_in_null_keyword6724) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER_L.add(IDENTIFIER_L694)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 855:6: -> NULL[$IDENTIFIER_L]
                    self._adaptor.addChild(root_0, self._adaptor.create(NULL, IDENTIFIER_L694))



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "null_keyword"

    class identifier_return(ParserRuleReturnScope):
        def __init__(self):
            super(QueryParser.identifier_return, self).__init__()

            self.tree = None




    # $ANTLR start "identifier"
    # QueryParser.g:858:1: identifier : {...}? IDENTIFIER_L -> IDENTIFIER[$IDENTIFIER_L] ;
    def identifier(self, ):

        retval = self.identifier_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENTIFIER_L695 = None

        IDENTIFIER_L695_tree = None
        stream_IDENTIFIER_L = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER_L")

        try:
            try:
                # QueryParser.g:858:12: ({...}? IDENTIFIER_L -> IDENTIFIER[$IDENTIFIER_L] )
                # QueryParser.g:858:14: {...}? IDENTIFIER_L
                pass 
                if not ((!input.LT(1).getText().equalsIgnoreCase("NULL"))):
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    raise FailedPredicateException(self.input, "identifier", "!input.LT(1).getText().equalsIgnoreCase(\"NULL\")")

                IDENTIFIER_L695=self.match(self.input, IDENTIFIER_L, self.FOLLOW_IDENTIFIER_L_in_identifier6745) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER_L.add(IDENTIFIER_L695)

                # AST Rewrite
                # elements: 
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 859:5: -> IDENTIFIER[$IDENTIFIER_L]
                    self._adaptor.addChild(root_0, self._adaptor.create(IDENTIFIER, IDENTIFIER_L695))



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


                        
            catch(RecognitionException re) {
                throw re;
            }
        finally:

            pass
        return retval

    # $ANTLR end "identifier"

    # $ANTLR start "synpred13_QueryParser"
    def synpred13_QueryParser_fragment(self, ):
        # QueryParser.g:189:21: ( ( alias EQUAL )? FOREACH rel LEFT_CURLY )
        # QueryParser.g:189:23: ( alias EQUAL )? FOREACH rel LEFT_CURLY
        pass 
        # QueryParser.g:189:23: ( alias EQUAL )?
        alt164 = 2
        LA164_0 = self.input.LA(1)

        if (LA164_0 == IDENTIFIER_L) :
            alt164 = 1
        if alt164 == 1:
            # QueryParser.g:189:25: alias EQUAL
            pass 
            self._state.following.append(self.FOLLOW_alias_in_synpred13_QueryParser670)
            self.alias()

            self._state.following.pop()
            self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_synpred13_QueryParser672)



        self.match(self.input, FOREACH, self.FOLLOW_FOREACH_in_synpred13_QueryParser678)
        self._state.following.append(self.FOLLOW_rel_in_synpred13_QueryParser680)
        self.rel()

        self._state.following.pop()
        self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_synpred13_QueryParser682)


    # $ANTLR end "synpred13_QueryParser"



    # $ANTLR start "synpred15_QueryParser"
    def synpred15_QueryParser_fragment(self, ):
        # QueryParser.g:193:69: ( SEMI_COLON )
        # QueryParser.g:193:69: SEMI_COLON
        pass 
        self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred15_QueryParser730)


    # $ANTLR end "synpred15_QueryParser"



    # $ANTLR start "synpred68_QueryParser"
    def synpred68_QueryParser_fragment(self, ):
        # QueryParser.g:306:18: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) )
        # QueryParser.g:306:18: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        pass 
        # QueryParser.g:306:18: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        # QueryParser.g:306:20: LEFT_PAREN field_def_list RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred68_QueryParser1794)
        self._state.following.append(self.FOLLOW_field_def_list_in_synpred68_QueryParser1797)
        self.field_def_list()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred68_QueryParser1799)





    # $ANTLR end "synpred68_QueryParser"



    # $ANTLR start "synpred86_QueryParser"
    def synpred86_QueryParser_fragment(self, ):
        # QueryParser.g:329:12: ( ( BAG )? LEFT_CURLY ( null_keyword COLON ( tuple_type )? ) RIGHT_CURLY )
        # QueryParser.g:329:12: ( BAG )? LEFT_CURLY ( null_keyword COLON ( tuple_type )? ) RIGHT_CURLY
        pass 
        # QueryParser.g:329:12: ( BAG )?
        alt172 = 2
        LA172_0 = self.input.LA(1)

        if (LA172_0 == BAG) :
            alt172 = 1
        if alt172 == 1:
            # QueryParser.g:0:0: BAG
            pass 
            self.match(self.input, BAG, self.FOLLOW_BAG_in_synpred86_QueryParser2023)



        self.match(self.input, LEFT_CURLY, self.FOLLOW_LEFT_CURLY_in_synpred86_QueryParser2026)
        # QueryParser.g:329:28: ( null_keyword COLON ( tuple_type )? )
        # QueryParser.g:329:30: null_keyword COLON ( tuple_type )?
        pass 
        self._state.following.append(self.FOLLOW_null_keyword_in_synpred86_QueryParser2030)
        self.null_keyword()

        self._state.following.pop()
        self.match(self.input, COLON, self.FOLLOW_COLON_in_synpred86_QueryParser2032)
        # QueryParser.g:329:49: ( tuple_type )?
        alt173 = 2
        LA173_0 = self.input.LA(1)

        if (LA173_0 == TUPLE or LA173_0 == LEFT_PAREN) :
            alt173 = 1
        if alt173 == 1:
            # QueryParser.g:0:0: tuple_type
            pass 
            self._state.following.append(self.FOLLOW_tuple_type_in_synpred86_QueryParser2034)
            self.tuple_type()

            self._state.following.pop()






        self.match(self.input, RIGHT_CURLY, self.FOLLOW_RIGHT_CURLY_in_synpred86_QueryParser2039)


    # $ANTLR end "synpred86_QueryParser"



    # $ANTLR start "synpred107_QueryParser"
    def synpred107_QueryParser_fragment(self, ):
        # QueryParser.g:369:21: ( foreach_clause_complex )
        # QueryParser.g:369:21: foreach_clause_complex
        pass 
        self._state.following.append(self.FOLLOW_foreach_clause_complex_in_synpred107_QueryParser2435)
        self.foreach_clause_complex()

        self._state.following.pop()


    # $ANTLR end "synpred107_QueryParser"



    # $ANTLR start "synpred110_QueryParser"
    def synpred110_QueryParser_fragment(self, ):
        # QueryParser.g:372:49: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) )
        # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        pass 
        # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        # QueryParser.g:372:51: LEFT_PAREN field_def_list RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred110_QueryParser2479)
        self._state.following.append(self.FOLLOW_field_def_list_in_synpred110_QueryParser2482)
        self.field_def_list()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred110_QueryParser2484)





    # $ANTLR end "synpred110_QueryParser"



    # $ANTLR start "synpred112_QueryParser"
    def synpred112_QueryParser_fragment(self, ):
        # QueryParser.g:372:26: ( flatten_clause ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? )
        # QueryParser.g:372:26: flatten_clause ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
        pass 
        self._state.following.append(self.FOLLOW_flatten_clause_in_synpred112_QueryParser2468)
        self.flatten_clause()

        self._state.following.pop()
        # QueryParser.g:372:41: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
        alt177 = 2
        LA177_0 = self.input.LA(1)

        if (LA177_0 == AS) :
            alt177 = 1
        if alt177 == 1:
            # QueryParser.g:372:43: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
            pass 
            self.match(self.input, AS, self.FOLLOW_AS_in_synpred112_QueryParser2472)
            # QueryParser.g:372:47: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
            alt176 = 2
            alt176 = self.dfa176.predict(self.input)
            if alt176 == 1:
                # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                pass 
                # QueryParser.g:372:49: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                # QueryParser.g:372:51: LEFT_PAREN field_def_list RIGHT_PAREN
                pass 
                self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred112_QueryParser2479)
                self._state.following.append(self.FOLLOW_field_def_list_in_synpred112_QueryParser2482)
                self.field_def_list()

                self._state.following.pop()
                self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred112_QueryParser2484)





            elif alt176 == 2:
                # QueryParser.g:372:95: field_def
                pass 
                self._state.following.append(self.FOLLOW_field_def_in_synpred112_QueryParser2491)
                self.field_def()

                self._state.following.pop()








    # $ANTLR end "synpred112_QueryParser"



    # $ANTLR start "synpred113_QueryParser"
    def synpred113_QueryParser_fragment(self, ):
        # QueryParser.g:373:44: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) )
        # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        pass 
        # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        # QueryParser.g:373:46: LEFT_PAREN field_def_list RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred113_QueryParser2534)
        self._state.following.append(self.FOLLOW_field_def_list_in_synpred113_QueryParser2537)
        self.field_def_list()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred113_QueryParser2539)





    # $ANTLR end "synpred113_QueryParser"



    # $ANTLR start "synpred115_QueryParser"
    def synpred115_QueryParser_fragment(self, ):
        # QueryParser.g:373:26: ( col_range ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )? )
        # QueryParser.g:373:26: col_range ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
        pass 
        self._state.following.append(self.FOLLOW_col_range_in_synpred115_QueryParser2523)
        self.col_range()

        self._state.following.pop()
        # QueryParser.g:373:36: ( AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def ) )?
        alt180 = 2
        LA180_0 = self.input.LA(1)

        if (LA180_0 == AS) :
            alt180 = 1
        if alt180 == 1:
            # QueryParser.g:373:38: AS ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
            pass 
            self.match(self.input, AS, self.FOLLOW_AS_in_synpred115_QueryParser2527)
            # QueryParser.g:373:42: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) | field_def )
            alt179 = 2
            alt179 = self.dfa179.predict(self.input)
            if alt179 == 1:
                # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                pass 
                # QueryParser.g:373:44: ( LEFT_PAREN field_def_list RIGHT_PAREN )
                # QueryParser.g:373:46: LEFT_PAREN field_def_list RIGHT_PAREN
                pass 
                self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred115_QueryParser2534)
                self._state.following.append(self.FOLLOW_field_def_list_in_synpred115_QueryParser2537)
                self.field_def_list()

                self._state.following.pop()
                self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred115_QueryParser2539)





            elif alt179 == 2:
                # QueryParser.g:373:90: field_def
                pass 
                self._state.following.append(self.FOLLOW_field_def_in_synpred115_QueryParser2546)
                self.field_def()

                self._state.following.pop()








    # $ANTLR end "synpred115_QueryParser"



    # $ANTLR start "synpred117_QueryParser"
    def synpred117_QueryParser_fragment(self, ):
        # QueryParser.g:374:26: ( expr ( AS field_def )? )
        # QueryParser.g:374:26: expr ( AS field_def )?
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred117_QueryParser2578)
        self.expr()

        self._state.following.pop()
        # QueryParser.g:374:31: ( AS field_def )?
        alt181 = 2
        LA181_0 = self.input.LA(1)

        if (LA181_0 == AS) :
            alt181 = 1
        if alt181 == 1:
            # QueryParser.g:374:33: AS field_def
            pass 
            self.match(self.input, AS, self.FOLLOW_AS_in_synpred117_QueryParser2582)
            self._state.following.append(self.FOLLOW_field_def_in_synpred117_QueryParser2585)
            self.field_def()

            self._state.following.pop()





    # $ANTLR end "synpred117_QueryParser"



    # $ANTLR start "synpred118_QueryParser"
    def synpred118_QueryParser_fragment(self, ):
        # QueryParser.g:375:39: ( ( LEFT_PAREN field_def_list RIGHT_PAREN ) )
        # QueryParser.g:375:39: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        pass 
        # QueryParser.g:375:39: ( LEFT_PAREN field_def_list RIGHT_PAREN )
        # QueryParser.g:375:41: LEFT_PAREN field_def_list RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred118_QueryParser2626)
        self._state.following.append(self.FOLLOW_field_def_list_in_synpred118_QueryParser2629)
        self.field_def_list()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred118_QueryParser2631)





    # $ANTLR end "synpred118_QueryParser"



    # $ANTLR start "synpred123_QueryParser"
    def synpred123_QueryParser_fragment(self, ):
        # QueryParser.g:396:14: ( LEFT_PAREN cond RIGHT_PAREN )
        # QueryParser.g:396:14: LEFT_PAREN cond RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred123_QueryParser2763)
        self._state.following.append(self.FOLLOW_cond_in_synpred123_QueryParser2766)
        self.cond()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred123_QueryParser2768)


    # $ANTLR end "synpred123_QueryParser"



    # $ANTLR start "synpred124_QueryParser"
    def synpred124_QueryParser_fragment(self, ):
        # QueryParser.g:397:14: ( not_cond )
        # QueryParser.g:397:14: not_cond
        pass 
        self._state.following.append(self.FOLLOW_not_cond_in_synpred124_QueryParser2784)
        self.not_cond()

        self._state.following.pop()


    # $ANTLR end "synpred124_QueryParser"



    # $ANTLR start "synpred125_QueryParser"
    def synpred125_QueryParser_fragment(self, ):
        # QueryParser.g:398:14: ( expr rel_op expr )
        # QueryParser.g:398:14: expr rel_op expr
        pass 
        self._state.following.append(self.FOLLOW_expr_in_synpred125_QueryParser2799)
        self.expr()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_rel_op_in_synpred125_QueryParser2801)
        self.rel_op()

        self._state.following.pop()
        self._state.following.append(self.FOLLOW_expr_in_synpred125_QueryParser2804)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred125_QueryParser"



    # $ANTLR start "synpred126_QueryParser"
    def synpred126_QueryParser_fragment(self, ):
        # QueryParser.g:399:14: ( func_eval )
        # QueryParser.g:399:14: func_eval
        pass 
        self._state.following.append(self.FOLLOW_func_eval_in_synpred126_QueryParser2819)
        self.func_eval()

        self._state.following.pop()


    # $ANTLR end "synpred126_QueryParser"



    # $ANTLR start "synpred137_QueryParser"
    def synpred137_QueryParser_fragment(self, ):
        # QueryParser.g:429:13: ( LEFT_PAREN type_cast RIGHT_PAREN unary_expr )
        # QueryParser.g:429:13: LEFT_PAREN type_cast RIGHT_PAREN unary_expr
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred137_QueryParser3032)
        self._state.following.append(self.FOLLOW_type_cast_in_synpred137_QueryParser3034)
        self.type_cast()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred137_QueryParser3036)
        self._state.following.append(self.FOLLOW_unary_expr_in_synpred137_QueryParser3038)
        self.unary_expr()

        self._state.following.pop()


    # $ANTLR end "synpred137_QueryParser"



    # $ANTLR start "synpred144_QueryParser"
    def synpred144_QueryParser_fragment(self, ):
        # QueryParser.g:445:14: ( expr_eval )
        # QueryParser.g:445:14: expr_eval
        pass 
        self._state.following.append(self.FOLLOW_expr_eval_in_synpred144_QueryParser3198)
        self.expr_eval()

        self._state.following.pop()


    # $ANTLR end "synpred144_QueryParser"



    # $ANTLR start "synpred145_QueryParser"
    def synpred145_QueryParser_fragment(self, ):
        # QueryParser.g:446:14: ( LEFT_PAREN expr RIGHT_PAREN )
        # QueryParser.g:446:14: LEFT_PAREN expr RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred145_QueryParser3214)
        self._state.following.append(self.FOLLOW_expr_in_synpred145_QueryParser3216)
        self.expr()

        self._state.following.pop()
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred145_QueryParser3218)


    # $ANTLR end "synpred145_QueryParser"



    # $ANTLR start "synpred146_QueryParser"
    def synpred146_QueryParser_fragment(self, ):
        # QueryParser.g:451:13: ( const_expr )
        # QueryParser.g:451:13: const_expr
        pass 
        self._state.following.append(self.FOLLOW_const_expr_in_synpred146_QueryParser3262)
        self.const_expr()

        self._state.following.pop()


    # $ANTLR end "synpred146_QueryParser"



    # $ANTLR start "synpred149_QueryParser"
    def synpred149_QueryParser_fragment(self, ):
        # QueryParser.g:457:19: ( func_eval )
        # QueryParser.g:457:19: func_eval
        pass 
        self._state.following.append(self.FOLLOW_func_eval_in_synpred149_QueryParser3294)
        self.func_eval()

        self._state.following.pop()


    # $ANTLR end "synpred149_QueryParser"



    # $ANTLR start "synpred150_QueryParser"
    def synpred150_QueryParser_fragment(self, ):
        # QueryParser.g:457:31: ( col_ref )
        # QueryParser.g:457:31: col_ref
        pass 
        self._state.following.append(self.FOLLOW_col_ref_in_synpred150_QueryParser3298)
        self.col_ref()

        self._state.following.pop()


    # $ANTLR end "synpred150_QueryParser"



    # $ANTLR start "synpred151_QueryParser"
    def synpred151_QueryParser_fragment(self, ):
        # QueryParser.g:457:41: ( bin_expr )
        # QueryParser.g:457:41: bin_expr
        pass 
        self._state.following.append(self.FOLLOW_bin_expr_in_synpred151_QueryParser3302)
        self.bin_expr()

        self._state.following.pop()


    # $ANTLR end "synpred151_QueryParser"



    # $ANTLR start "synpred163_QueryParser"
    def synpred163_QueryParser_fragment(self, ):
        # QueryParser.g:500:29: ( INTEGER SEMI_COLON )
        # QueryParser.g:500:30: INTEGER SEMI_COLON
        pass 
        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_synpred163_QueryParser3777)
        self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred163_QueryParser3779)


    # $ANTLR end "synpred163_QueryParser"



    # $ANTLR start "synpred164_QueryParser"
    def synpred164_QueryParser_fragment(self, ):
        # QueryParser.g:500:63: ( LONGINTEGER SEMI_COLON )
        # QueryParser.g:500:64: LONGINTEGER SEMI_COLON
        pass 
        self.match(self.input, LONGINTEGER, self.FOLLOW_LONGINTEGER_in_synpred164_QueryParser3789)
        self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred164_QueryParser3791)


    # $ANTLR end "synpred164_QueryParser"



    # $ANTLR start "synpred165_QueryParser"
    def synpred165_QueryParser_fragment(self, ):
        # QueryParser.g:503:31: ( DOUBLENUMBER SEMI_COLON )
        # QueryParser.g:503:32: DOUBLENUMBER SEMI_COLON
        pass 
        self.match(self.input, DOUBLENUMBER, self.FOLLOW_DOUBLENUMBER_in_synpred165_QueryParser3819)
        self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred165_QueryParser3821)


    # $ANTLR end "synpred165_QueryParser"



    # $ANTLR start "synpred198_QueryParser"
    def synpred198_QueryParser_fragment(self, ):
        # QueryParser.g:559:19: ( join_item ( LEFT | RIGHT | FULL ) ( OUTER )? COMMA join_item )
        # QueryParser.g:559:19: join_item ( LEFT | RIGHT | FULL ) ( OUTER )? COMMA join_item
        pass 
        self._state.following.append(self.FOLLOW_join_item_in_synpred198_QueryParser4275)
        self.join_item()

        self._state.following.pop()
        if (LEFT <= self.input.LA(1) <= FULL):
            self.input.consume()
            self._state.errorRecovery = False

        else:
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            mse = MismatchedSetException(None, self.input)
            raise mse


        # QueryParser.g:559:53: ( OUTER )?
        alt190 = 2
        LA190_0 = self.input.LA(1)

        if (LA190_0 == OUTER) :
            alt190 = 1
        if alt190 == 1:
            # QueryParser.g:0:0: OUTER
            pass 
            self.match(self.input, OUTER, self.FOLLOW_OUTER_in_synpred198_QueryParser4291)



        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred198_QueryParser4294)
        self._state.following.append(self.FOLLOW_join_item_in_synpred198_QueryParser4297)
        self.join_item()

        self._state.following.pop()


    # $ANTLR end "synpred198_QueryParser"



    # $ANTLR start "synpred201_QueryParser"
    def synpred201_QueryParser_fragment(self, ):
        # QueryParser.g:573:27: ( LEFT_PAREN join_group_by_expr ( COMMA join_group_by_expr )* RIGHT_PAREN )
        # QueryParser.g:573:27: LEFT_PAREN join_group_by_expr ( COMMA join_group_by_expr )* RIGHT_PAREN
        pass 
        self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_synpred201_QueryParser4390)
        self._state.following.append(self.FOLLOW_join_group_by_expr_in_synpred201_QueryParser4392)
        self.join_group_by_expr()

        self._state.following.pop()
        # QueryParser.g:573:57: ( COMMA join_group_by_expr )*
        while True: #loop191
            alt191 = 2
            LA191_0 = self.input.LA(1)

            if (LA191_0 == COMMA) :
                alt191 = 1


            if alt191 == 1:
                # QueryParser.g:573:59: COMMA join_group_by_expr
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred201_QueryParser4396)
                self._state.following.append(self.FOLLOW_join_group_by_expr_in_synpred201_QueryParser4398)
                self.join_group_by_expr()

                self._state.following.pop()


            else:
                break #loop191
        self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_synpred201_QueryParser4403)


    # $ANTLR end "synpred201_QueryParser"



    # $ANTLR start "synpred212_QueryParser"
    def synpred212_QueryParser_fragment(self, ):
        # QueryParser.g:628:23: ( ( nested_command SEMI_COLON )* )
        # QueryParser.g:628:23: ( nested_command SEMI_COLON )*
        pass 
        # QueryParser.g:628:23: ( nested_command SEMI_COLON )*
        while True: #loop192
            alt192 = 2
            LA192_0 = self.input.LA(1)

            if (LA192_0 == IDENTIFIER_L) :
                alt192 = 1


            if alt192 == 1:
                # QueryParser.g:628:25: nested_command SEMI_COLON
                pass 
                self._state.following.append(self.FOLLOW_nested_command_in_synpred212_QueryParser4844)
                self.nested_command()

                self._state.following.pop()
                self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred212_QueryParser4846)


            else:
                break #loop192


    # $ANTLR end "synpred212_QueryParser"



    # $ANTLR start "synpred213_QueryParser"
    def synpred213_QueryParser_fragment(self, ):
        # QueryParser.g:633:18: ( identifier EQUAL col_ref PERIOD col_ref_list {...}?)
        # QueryParser.g:633:20: identifier EQUAL col_ref PERIOD col_ref_list {...}?
        pass 
        self._state.following.append(self.FOLLOW_identifier_in_synpred213_QueryParser4906)
        self.identifier()

        self._state.following.pop()
        self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_synpred213_QueryParser4908)
        self._state.following.append(self.FOLLOW_col_ref_in_synpred213_QueryParser4910)
        self.col_ref()

        self._state.following.pop()
        self.match(self.input, PERIOD, self.FOLLOW_PERIOD_in_synpred213_QueryParser4912)
        self._state.following.append(self.FOLLOW_col_ref_list_in_synpred213_QueryParser4914)
        self.col_ref_list()

        self._state.following.pop()
        if not ((input.LA( 1 ) == SEMI_COLON )):
            if self._state.backtracking > 0:
                raise BacktrackingFailed

            raise FailedPredicateException(self.input, "synpred213_QueryParser", " input.LA( 1 ) == SEMI_COLON ")



    # $ANTLR end "synpred213_QueryParser"



    # $ANTLR start "synpred214_QueryParser"
    def synpred214_QueryParser_fragment(self, ):
        # QueryParser.g:635:18: ( identifier EQUAL expr )
        # QueryParser.g:635:18: identifier EQUAL expr
        pass 
        self._state.following.append(self.FOLLOW_identifier_in_synpred214_QueryParser4975)
        self.identifier()

        self._state.following.pop()
        self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_synpred214_QueryParser4977)
        self._state.following.append(self.FOLLOW_expr_in_synpred214_QueryParser4979)
        self.expr()

        self._state.following.pop()


    # $ANTLR end "synpred214_QueryParser"



    # $ANTLR start "synpred223_QueryParser"
    def synpred223_QueryParser_fragment(self, ):
        # QueryParser.g:666:41: ( INTEGER SEMI_COLON )
        # QueryParser.g:666:42: INTEGER SEMI_COLON
        pass 
        self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_synpred223_QueryParser5294)
        self.match(self.input, SEMI_COLON, self.FOLLOW_SEMI_COLON_in_synpred223_QueryParser5296)


    # $ANTLR end "synpred223_QueryParser"



    # $ANTLR start "synpred231_QueryParser"
    def synpred231_QueryParser_fragment(self, ):
        # QueryParser.g:688:46: ( ( COMMA split_branch )+ )
        # QueryParser.g:688:46: ( COMMA split_branch )+
        pass 
        # QueryParser.g:688:46: ( COMMA split_branch )+
        cnt193 = 0
        while True: #loop193
            alt193 = 2
            LA193_0 = self.input.LA(1)

            if (LA193_0 == COMMA) :
                alt193 = 1


            if alt193 == 1:
                # QueryParser.g:688:48: COMMA split_branch
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_synpred231_QueryParser5457)
                self._state.following.append(self.FOLLOW_split_branch_in_synpred231_QueryParser5459)
                self.split_branch()

                self._state.following.pop()


            else:
                if cnt193 >= 1:
                    break #loop193

                if self._state.backtracking > 0:
                    raise BacktrackingFailed

                eee = EarlyExitException(193, self.input)
                raise eee

            cnt193 += 1


    # $ANTLR end "synpred231_QueryParser"



    # $ANTLR start "synpred315_QueryParser"
    def synpred315_QueryParser_fragment(self, ):
        # QueryParser.g:810:7: ( identifier )
        # QueryParser.g:810:7: identifier
        pass 
        self._state.following.append(self.FOLLOW_identifier_in_synpred315_QueryParser6428)
        self.identifier()

        self._state.following.pop()


    # $ANTLR end "synpred315_QueryParser"



    # $ANTLR start "synpred316_QueryParser"
    def synpred316_QueryParser_fragment(self, ):
        # QueryParser.g:811:7: ( null_keyword )
        # QueryParser.g:811:7: null_keyword
        pass 
        self._state.following.append(self.FOLLOW_null_keyword_in_synpred316_QueryParser6436)
        self.null_keyword()

        self._state.following.pop()


    # $ANTLR end "synpred316_QueryParser"




    # Delegated rules

    def synpred316_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred316_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred145_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred145_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred149_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred149_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred231_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred231_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred137_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred137_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred86_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred86_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred112_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred112_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred151_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred151_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred214_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred214_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred68_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred68_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred146_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred146_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred107_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred107_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred118_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred118_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred110_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred110_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred125_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred125_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred144_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred144_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred13_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred13_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred123_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred123_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred124_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred124_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred223_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred223_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred15_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred15_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred150_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred150_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred165_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred165_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred126_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred126_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred201_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred201_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred315_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred315_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred113_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred113_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred213_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred213_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred115_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred115_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred164_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred164_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred117_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred117_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred163_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred163_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred212_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred212_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred198_QueryParser(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred198_QueryParser_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #2

    DFA2_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA2_min = DFA.unpack(
        u"\1\5\1\uffff\1\156\1\uffff\1\7\3\uffff\1\7\1\uffff\1\7\1\155\1"
        u"\uffff"
        )

    DFA2_max = DFA.unpack(
        u"\1\156\1\uffff\1\166\1\uffff\1\102\3\uffff\1\156\1\uffff\1\102"
        u"\1\156\1\uffff"
        )

    DFA2_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\2\1\uffff\1\3\1\4\1\6\1\uffff\1\5\2\uffff"
        u"\1\7"
        )

    DFA2_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA2_transition = [
        DFA.unpack(u"\1\7\1\uffff\3\3\1\5\2\3\1\uffff\1\3\1\uffff\5\3\1\6"
        u"\14\uffff\1\3\23\uffff\1\3\1\uffff\2\3\7\uffff\2\3\27\uffff\1\2"
        u"\22\uffff\1\1\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\11\6\uffff\1\10\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\3\1\5\2\3\1\uffff\1\3\1\uffff\5\3\15\uffff\1\3\23"
        u"\uffff\1\3\1\uffff\2\3\7\uffff\2\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\3\3\1\5\2\3\1\uffff\1\3\1\uffff\5\3\15\uffff\1\3\23"
        u"\uffff\1\3\1\uffff\2\3\7\uffff\2\3\27\uffff\1\13\23\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\3\3\1\5\2\3\1\uffff\1\3\1\uffff\5\3\15\uffff\1\3\23"
        u"\uffff\1\3\1\uffff\2\3\7\uffff\2\3"),
        DFA.unpack(u"\1\14\1\11"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #2

    class DFA2(DFA):
        pass


    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA35_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA35_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA35_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA35_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA35_1 = input.LA(1)

                 
                index35_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred68_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index35_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 35, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\u00cb\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\1\uffff\102\105\4\uffff\u0084\105"
        )

    DFA51_min = DFA.unpack(
        u"\1\5\102\10\1\5\2\uffff\1\5\u0084\10"
        )

    DFA51_max = DFA.unpack(
        u"\1\u00a3\102\166\1\u00a3\2\uffff\1\u00a3\u0084\166"
        )

    DFA51_accept = DFA.unpack(
        u"\104\uffff\1\2\1\1\u0085\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\u00cb\uffff"
        )

            
    DFA51_transition = [
        DFA.unpack(u"\1\2\1\3\1\4\1\5\1\6\1\7\1\12\2\uffff\1\10\1\11\1\13"
        u"\1\14\1\15\1\16\1\17\1\20\1\21\1\22\1\uffff\1\23\1\24\1\25\1\26"
        u"\1\27\1\30\1\uffff\1\31\1\32\1\33\1\34\1\35\1\36\1\37\1\40\1\41"
        u"\1\42\1\uffff\1\44\1\45\1\46\1\47\1\50\1\51\1\52\1\53\1\54\1\55"
        u"\1\56\1\57\1\60\1\61\1\62\1\63\1\64\1\65\1\66\1\67\1\70\1\71\1"
        u"\72\1\73\1\74\1\75\1\76\7\1\1\100\1\101\13\uffff\1\77\107\uffff"
        u"\1\43\1\102"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\110\1\111\1\112\1\113\1\114\1\115\1\120\2\uffff"
        u"\1\116\1\117\1\121\1\122\1\123\1\124\1\125\1\126\1\127\1\130\1"
        u"\uffff\1\131\1\132\1\133\1\134\1\135\1\136\1\uffff\1\137\1\140"
        u"\1\141\1\142\1\143\1\144\1\145\1\146\1\147\1\150\1\uffff\1\152"
        u"\1\153\1\154\1\155\1\156\1\157\1\160\1\161\1\162\1\163\1\164\1"
        u"\165\1\166\1\167\1\170\1\171\1\172\1\173\1\174\1\175\1\176\1\177"
        u"\1\u0080\1\u0081\1\u0082\1\u0083\1\u0084\7\107\1\u0086\1\u0087"
        u"\13\uffff\1\u0085\107\uffff\1\151\1\u0088"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008a\1\u008b\1\u008c\1\u008d\1\u008e\1\u008f\1"
        u"\u0092\2\uffff\1\u0090\1\u0091\1\u0093\1\u0094\1\u0095\1\u0096"
        u"\1\u0097\1\u0098\1\u0099\1\u009a\1\uffff\1\u009b\1\u009c\1\u009d"
        u"\1\u009e\1\u009f\1\u00a0\1\uffff\1\u00a1\1\u00a2\1\u00a3\1\u00a4"
        u"\1\u00a5\1\u00a6\1\u00a7\1\u00a8\1\u00a9\1\u00aa\1\uffff\1\u00ac"
        u"\1\u00ad\1\u00ae\1\u00af\1\u00b0\1\u00b1\1\u00b2\1\u00b3\1\u00b4"
        u"\1\u00b5\1\u00b6\1\u00b7\1\u00b8\1\u00b9\1\u00ba\1\u00bb\1\u00bc"
        u"\1\u00bd\1\u00be\1\u00bf\1\u00c0\1\u00c1\1\u00c2\1\u00c3\1\u00c4"
        u"\1\u00c5\1\u00c6\7\u0089\1\u00c8\1\u00c9\13\uffff\1\u00c7\107\uffff"
        u"\1\u00ab\1\u00ca"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\103"
        u"\2\uffff\1\103\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105"),
        DFA.unpack(u"\1\105\21\uffff\1\105\5\uffff\1\105\73\uffff\1\106"
        u"\2\uffff\1\106\7\uffff\1\105\5\uffff\1\105\1\104\1\105\6\uffff"
        u"\1\105")
    ]

    # class definition for DFA #51

    class DFA51(DFA):
        pass


    # lookup tables for DFA #61

    DFA61_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA61_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA61_min = DFA.unpack(
        u"\1\7\1\0\21\uffff"
        )

    DFA61_max = DFA.unpack(
        u"\1\102\1\0\21\uffff"
        )

    DFA61_accept = DFA.unpack(
        u"\2\uffff\1\2\17\uffff\1\1"
        )

    DFA61_special = DFA.unpack(
        u"\1\uffff\1\0\21\uffff"
        )

            
    DFA61_transition = [
        DFA.unpack(u"\3\2\1\1\2\2\1\uffff\1\2\1\uffff\5\2\15\uffff\1\2\23"
        u"\uffff\1\2\1\uffff\2\2\7\uffff\2\2"),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #61

    class DFA61(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA61_1 = input.LA(1)

                 
                index61_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred107_QueryParser()):
                    s = 18

                elif (True):
                    s = 2

                 
                input.seek(index61_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 61, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #70

    DFA70_eot = DFA.unpack(
        u"\115\uffff"
        )

    DFA70_eof = DFA.unpack(
        u"\115\uffff"
        )

    DFA70_min = DFA.unpack(
        u"\1\5\5\0\107\uffff"
        )

    DFA70_max = DFA.unpack(
        u"\1\u00a3\5\0\107\uffff"
        )

    DFA70_accept = DFA.unpack(
        u"\6\uffff\1\2\1\3\103\uffff\1\4\1\1"
        )

    DFA70_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\107\uffff"
        )

            
    DFA70_transition = [
        DFA.unpack(u"\7\7\2\uffff\1\3\11\7\1\uffff\6\7\1\uffff\2\7\1\2\4"
        u"\7\1\1\2\7\1\uffff\44\7\13\uffff\1\4\1\7\2\uffff\1\7\1\uffff\1"
        u"\5\1\7\1\uffff\3\7\2\uffff\1\113\5\uffff\1\7\1\uffff\1\7\1\uffff"
        u"\1\7\4\uffff\1\6\52\uffff\2\7"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #70

    class DFA70(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA70_1 = input.LA(1)

                 
                index70_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred112_QueryParser()):
                    s = 76

                elif (self.synpred117_QueryParser()):
                    s = 7

                 
                input.seek(index70_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA70_2 = input.LA(1)

                 
                index70_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred115_QueryParser()):
                    s = 6

                elif (self.synpred117_QueryParser()):
                    s = 7

                 
                input.seek(index70_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA70_3 = input.LA(1)

                 
                index70_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred115_QueryParser()):
                    s = 6

                elif (self.synpred117_QueryParser()):
                    s = 7

                 
                input.seek(index70_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA70_4 = input.LA(1)

                 
                index70_4 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred115_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 6

                elif ((((self.synpred117_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred117_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred117_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred117_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))))):
                    s = 7

                 
                input.seek(index70_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA70_5 = input.LA(1)

                 
                index70_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred115_QueryParser()):
                    s = 6

                elif (self.synpred117_QueryParser()):
                    s = 7

                 
                input.seek(index70_5)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 70, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #63

    DFA63_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA63_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA63_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA63_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA63_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA63_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA63_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #63

    class DFA63(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA63_1 = input.LA(1)

                 
                index63_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred110_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index63_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 63, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #65

    DFA65_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA65_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA65_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA65_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA65_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA65_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA65_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #65

    class DFA65(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA65_1 = input.LA(1)

                 
                index65_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred113_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index65_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 65, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #68

    DFA68_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA68_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA68_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA68_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA68_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA68_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA68_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #68

    class DFA68(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA68_1 = input.LA(1)

                 
                index68_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred118_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index68_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 68, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #74

    DFA74_eot = DFA.unpack(
        u"\117\uffff"
        )

    DFA74_eof = DFA.unpack(
        u"\117\uffff"
        )

    DFA74_min = DFA.unpack(
        u"\1\5\111\0\5\uffff"
        )

    DFA74_max = DFA.unpack(
        u"\1\u00a3\111\0\5\uffff"
        )

    DFA74_accept = DFA.unpack(
        u"\112\uffff\1\1\1\3\1\5\1\2\1\4"
        )

    DFA74_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\1\15\1\16\1\17\1\20\1\21\1\22\1\23\1\24\1\25\1\26\1\27\1\30"
        u"\1\31\1\32\1\33\1\34\1\35\1\36\1\37\1\40\1\41\1\42\1\43\1\44\1"
        u"\45\1\46\1\47\1\50\1\51\1\52\1\53\1\54\1\55\1\56\1\57\1\60\1\61"
        u"\1\62\1\63\1\64\1\65\1\66\1\67\1\70\1\71\1\72\1\73\1\74\1\75\1"
        u"\76\1\77\1\100\1\101\1\102\1\103\1\104\1\105\1\106\1\107\1\110"
        u"\5\uffff"
        )

            
    DFA74_transition = [
        DFA.unpack(u"\1\14\1\15\1\16\1\17\1\20\1\21\1\24\2\uffff\1\22\1\23"
        u"\1\25\1\26\1\27\1\30\1\31\1\32\1\33\1\34\1\uffff\1\35\1\36\1\37"
        u"\1\40\1\41\1\42\1\uffff\1\43\1\44\1\45\1\46\1\47\1\2\1\50\1\51"
        u"\1\52\1\53\1\uffff\1\55\1\56\1\57\1\60\1\61\1\62\1\63\1\64\1\65"
        u"\1\66\1\67\1\70\1\71\1\72\1\73\1\74\1\75\1\76\1\77\1\100\1\101"
        u"\1\102\1\103\1\104\1\105\1\106\1\107\7\13\1\7\1\10\13\uffff\1\6"
        u"\1\4\2\uffff\1\4\1\uffff\1\111\1\3\1\uffff\2\4\1\5\10\uffff\1\1"
        u"\1\uffff\1\12\1\uffff\1\11\57\uffff\1\54\1\110"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #74

    class DFA74(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA74_1 = input.LA(1)

                 
                index74_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred123_QueryParser()):
                    s = 74

                elif (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA74_2 = input.LA(1)

                 
                index74_2 = input.index()
                input.rewind()
                s = -1
                if (self.synpred124_QueryParser()):
                    s = 77

                elif (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA74_3 = input.LA(1)

                 
                index74_3 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_3)
                if s >= 0:
                    return s
            elif s == 3: 
                LA74_4 = input.LA(1)

                 
                index74_4 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_4)
                if s >= 0:
                    return s
            elif s == 4: 
                LA74_5 = input.LA(1)

                 
                index74_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_5)
                if s >= 0:
                    return s
            elif s == 5: 
                LA74_6 = input.LA(1)

                 
                index74_6 = input.index()
                input.rewind()
                s = -1
                if ((((self.synpred125_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred125_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred125_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred125_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))))):
                    s = 75

                elif ((((self.synpred126_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred126_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))))):
                    s = 78

                elif (((input.LT(1).getText().equalsIgnoreCase("NULL")) or (!input.LT(1).getText().equalsIgnoreCase("NULL")))):
                    s = 76

                 
                input.seek(index74_6)
                if s >= 0:
                    return s
            elif s == 6: 
                LA74_7 = input.LA(1)

                 
                index74_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_7)
                if s >= 0:
                    return s
            elif s == 7: 
                LA74_8 = input.LA(1)

                 
                index74_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_8)
                if s >= 0:
                    return s
            elif s == 8: 
                LA74_9 = input.LA(1)

                 
                index74_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_9)
                if s >= 0:
                    return s
            elif s == 9: 
                LA74_10 = input.LA(1)

                 
                index74_10 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_10)
                if s >= 0:
                    return s
            elif s == 10: 
                LA74_11 = input.LA(1)

                 
                index74_11 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_11)
                if s >= 0:
                    return s
            elif s == 11: 
                LA74_12 = input.LA(1)

                 
                index74_12 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_12)
                if s >= 0:
                    return s
            elif s == 12: 
                LA74_13 = input.LA(1)

                 
                index74_13 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_13)
                if s >= 0:
                    return s
            elif s == 13: 
                LA74_14 = input.LA(1)

                 
                index74_14 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_14)
                if s >= 0:
                    return s
            elif s == 14: 
                LA74_15 = input.LA(1)

                 
                index74_15 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_15)
                if s >= 0:
                    return s
            elif s == 15: 
                LA74_16 = input.LA(1)

                 
                index74_16 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_16)
                if s >= 0:
                    return s
            elif s == 16: 
                LA74_17 = input.LA(1)

                 
                index74_17 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_17)
                if s >= 0:
                    return s
            elif s == 17: 
                LA74_18 = input.LA(1)

                 
                index74_18 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_18)
                if s >= 0:
                    return s
            elif s == 18: 
                LA74_19 = input.LA(1)

                 
                index74_19 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_19)
                if s >= 0:
                    return s
            elif s == 19: 
                LA74_20 = input.LA(1)

                 
                index74_20 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_20)
                if s >= 0:
                    return s
            elif s == 20: 
                LA74_21 = input.LA(1)

                 
                index74_21 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_21)
                if s >= 0:
                    return s
            elif s == 21: 
                LA74_22 = input.LA(1)

                 
                index74_22 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_22)
                if s >= 0:
                    return s
            elif s == 22: 
                LA74_23 = input.LA(1)

                 
                index74_23 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_23)
                if s >= 0:
                    return s
            elif s == 23: 
                LA74_24 = input.LA(1)

                 
                index74_24 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_24)
                if s >= 0:
                    return s
            elif s == 24: 
                LA74_25 = input.LA(1)

                 
                index74_25 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_25)
                if s >= 0:
                    return s
            elif s == 25: 
                LA74_26 = input.LA(1)

                 
                index74_26 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_26)
                if s >= 0:
                    return s
            elif s == 26: 
                LA74_27 = input.LA(1)

                 
                index74_27 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_27)
                if s >= 0:
                    return s
            elif s == 27: 
                LA74_28 = input.LA(1)

                 
                index74_28 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_28)
                if s >= 0:
                    return s
            elif s == 28: 
                LA74_29 = input.LA(1)

                 
                index74_29 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_29)
                if s >= 0:
                    return s
            elif s == 29: 
                LA74_30 = input.LA(1)

                 
                index74_30 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_30)
                if s >= 0:
                    return s
            elif s == 30: 
                LA74_31 = input.LA(1)

                 
                index74_31 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_31)
                if s >= 0:
                    return s
            elif s == 31: 
                LA74_32 = input.LA(1)

                 
                index74_32 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_32)
                if s >= 0:
                    return s
            elif s == 32: 
                LA74_33 = input.LA(1)

                 
                index74_33 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_33)
                if s >= 0:
                    return s
            elif s == 33: 
                LA74_34 = input.LA(1)

                 
                index74_34 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_34)
                if s >= 0:
                    return s
            elif s == 34: 
                LA74_35 = input.LA(1)

                 
                index74_35 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_35)
                if s >= 0:
                    return s
            elif s == 35: 
                LA74_36 = input.LA(1)

                 
                index74_36 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_36)
                if s >= 0:
                    return s
            elif s == 36: 
                LA74_37 = input.LA(1)

                 
                index74_37 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_37)
                if s >= 0:
                    return s
            elif s == 37: 
                LA74_38 = input.LA(1)

                 
                index74_38 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_38)
                if s >= 0:
                    return s
            elif s == 38: 
                LA74_39 = input.LA(1)

                 
                index74_39 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_39)
                if s >= 0:
                    return s
            elif s == 39: 
                LA74_40 = input.LA(1)

                 
                index74_40 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_40)
                if s >= 0:
                    return s
            elif s == 40: 
                LA74_41 = input.LA(1)

                 
                index74_41 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_41)
                if s >= 0:
                    return s
            elif s == 41: 
                LA74_42 = input.LA(1)

                 
                index74_42 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_42)
                if s >= 0:
                    return s
            elif s == 42: 
                LA74_43 = input.LA(1)

                 
                index74_43 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_43)
                if s >= 0:
                    return s
            elif s == 43: 
                LA74_44 = input.LA(1)

                 
                index74_44 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_44)
                if s >= 0:
                    return s
            elif s == 44: 
                LA74_45 = input.LA(1)

                 
                index74_45 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_45)
                if s >= 0:
                    return s
            elif s == 45: 
                LA74_46 = input.LA(1)

                 
                index74_46 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_46)
                if s >= 0:
                    return s
            elif s == 46: 
                LA74_47 = input.LA(1)

                 
                index74_47 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_47)
                if s >= 0:
                    return s
            elif s == 47: 
                LA74_48 = input.LA(1)

                 
                index74_48 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_48)
                if s >= 0:
                    return s
            elif s == 48: 
                LA74_49 = input.LA(1)

                 
                index74_49 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_49)
                if s >= 0:
                    return s
            elif s == 49: 
                LA74_50 = input.LA(1)

                 
                index74_50 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_50)
                if s >= 0:
                    return s
            elif s == 50: 
                LA74_51 = input.LA(1)

                 
                index74_51 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_51)
                if s >= 0:
                    return s
            elif s == 51: 
                LA74_52 = input.LA(1)

                 
                index74_52 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_52)
                if s >= 0:
                    return s
            elif s == 52: 
                LA74_53 = input.LA(1)

                 
                index74_53 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_53)
                if s >= 0:
                    return s
            elif s == 53: 
                LA74_54 = input.LA(1)

                 
                index74_54 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_54)
                if s >= 0:
                    return s
            elif s == 54: 
                LA74_55 = input.LA(1)

                 
                index74_55 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_55)
                if s >= 0:
                    return s
            elif s == 55: 
                LA74_56 = input.LA(1)

                 
                index74_56 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_56)
                if s >= 0:
                    return s
            elif s == 56: 
                LA74_57 = input.LA(1)

                 
                index74_57 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_57)
                if s >= 0:
                    return s
            elif s == 57: 
                LA74_58 = input.LA(1)

                 
                index74_58 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_58)
                if s >= 0:
                    return s
            elif s == 58: 
                LA74_59 = input.LA(1)

                 
                index74_59 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_59)
                if s >= 0:
                    return s
            elif s == 59: 
                LA74_60 = input.LA(1)

                 
                index74_60 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_60)
                if s >= 0:
                    return s
            elif s == 60: 
                LA74_61 = input.LA(1)

                 
                index74_61 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_61)
                if s >= 0:
                    return s
            elif s == 61: 
                LA74_62 = input.LA(1)

                 
                index74_62 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_62)
                if s >= 0:
                    return s
            elif s == 62: 
                LA74_63 = input.LA(1)

                 
                index74_63 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_63)
                if s >= 0:
                    return s
            elif s == 63: 
                LA74_64 = input.LA(1)

                 
                index74_64 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_64)
                if s >= 0:
                    return s
            elif s == 64: 
                LA74_65 = input.LA(1)

                 
                index74_65 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_65)
                if s >= 0:
                    return s
            elif s == 65: 
                LA74_66 = input.LA(1)

                 
                index74_66 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_66)
                if s >= 0:
                    return s
            elif s == 66: 
                LA74_67 = input.LA(1)

                 
                index74_67 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_67)
                if s >= 0:
                    return s
            elif s == 67: 
                LA74_68 = input.LA(1)

                 
                index74_68 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_68)
                if s >= 0:
                    return s
            elif s == 68: 
                LA74_69 = input.LA(1)

                 
                index74_69 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_69)
                if s >= 0:
                    return s
            elif s == 69: 
                LA74_70 = input.LA(1)

                 
                index74_70 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_70)
                if s >= 0:
                    return s
            elif s == 70: 
                LA74_71 = input.LA(1)

                 
                index74_71 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_71)
                if s >= 0:
                    return s
            elif s == 71: 
                LA74_72 = input.LA(1)

                 
                index74_72 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (self.synpred126_QueryParser()):
                    s = 78

                elif (True):
                    s = 76

                 
                input.seek(index74_72)
                if s >= 0:
                    return s
            elif s == 72: 
                LA74_73 = input.LA(1)

                 
                index74_73 = input.index()
                input.rewind()
                s = -1
                if (self.synpred125_QueryParser()):
                    s = 75

                elif (True):
                    s = 76

                 
                input.seek(index74_73)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 74, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #81

    DFA81_eot = DFA.unpack(
        u"\113\uffff"
        )

    DFA81_eof = DFA.unpack(
        u"\113\uffff"
        )

    DFA81_min = DFA.unpack(
        u"\1\5\1\0\111\uffff"
        )

    DFA81_max = DFA.unpack(
        u"\1\u00a3\1\0\111\uffff"
        )

    DFA81_accept = DFA.unpack(
        u"\2\uffff\1\2\107\uffff\1\1"
        )

    DFA81_special = DFA.unpack(
        u"\1\uffff\1\0\111\uffff"
        )

            
    DFA81_transition = [
        DFA.unpack(u"\7\2\2\uffff\12\2\1\uffff\6\2\1\uffff\12\2\1\uffff\44"
        u"\2\13\uffff\2\2\2\uffff\1\2\1\uffff\2\2\1\uffff\3\2\10\uffff\1"
        u"\1\1\uffff\1\2\1\uffff\1\2\57\uffff\2\2"),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u"")
    ]

    # class definition for DFA #81

    class DFA81(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA81_1 = input.LA(1)

                 
                index81_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred137_QueryParser()):
                    s = 74

                elif (True):
                    s = 2

                 
                input.seek(index81_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 81, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #86

    DFA86_eot = DFA.unpack(
        u"\114\uffff"
        )

    DFA86_eof = DFA.unpack(
        u"\114\uffff"
        )

    DFA86_min = DFA.unpack(
        u"\1\5\1\0\7\uffff\1\0\102\uffff"
        )

    DFA86_max = DFA.unpack(
        u"\1\u00a3\1\0\7\uffff\1\0\102\uffff"
        )

    DFA86_accept = DFA.unpack(
        u"\2\uffff\1\1\107\uffff\1\3\1\2"
        )

    DFA86_special = DFA.unpack(
        u"\1\uffff\1\0\7\uffff\1\1\102\uffff"
        )

            
    DFA86_transition = [
        DFA.unpack(u"\7\2\2\uffff\12\2\1\uffff\6\2\1\uffff\12\2\1\uffff\44"
        u"\2\13\uffff\2\2\2\uffff\1\2\1\uffff\1\2\1\1\1\uffff\3\2\10\uffff"
        u"\1\11\1\uffff\1\2\1\uffff\1\2\57\uffff\2\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #86

    class DFA86(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA86_1 = input.LA(1)

                 
                index86_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred144_QueryParser()):
                    s = 2

                elif (True):
                    s = 74

                 
                input.seek(index86_1)
                if s >= 0:
                    return s
            elif s == 1: 
                LA86_9 = input.LA(1)

                 
                index86_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred144_QueryParser()):
                    s = 2

                elif (self.synpred145_QueryParser()):
                    s = 75

                 
                input.seek(index86_9)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 86, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #87

    DFA87_eot = DFA.unpack(
        u"\112\uffff"
        )

    DFA87_eof = DFA.unpack(
        u"\112\uffff"
        )

    DFA87_min = DFA.unpack(
        u"\1\5\3\uffff\6\0\100\uffff"
        )

    DFA87_max = DFA.unpack(
        u"\1\u00a3\3\uffff\6\0\100\uffff"
        )

    DFA87_accept = DFA.unpack(
        u"\1\uffff\1\1\10\uffff\1\2\77\uffff"
        )

    DFA87_special = DFA.unpack(
        u"\4\uffff\1\0\1\1\1\2\1\3\1\4\1\5\100\uffff"
        )

            
    DFA87_transition = [
        DFA.unpack(u"\7\12\2\uffff\12\12\1\uffff\6\12\1\uffff\12\12\1\uffff"
        u"\42\12\1\5\1\6\13\uffff\1\4\1\1\2\uffff\1\1\1\uffff\1\12\1\1\1"
        u"\uffff\3\1\10\uffff\1\11\1\uffff\1\10\1\uffff\1\7\57\uffff\2\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #87

    class DFA87(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA87_4 = input.LA(1)

                 
                index87_4 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred146_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 1

                elif (((input.LT(1).getText().equalsIgnoreCase("NULL")) or (!input.LT(1).getText().equalsIgnoreCase("NULL")))):
                    s = 10

                 
                input.seek(index87_4)
                if s >= 0:
                    return s
            elif s == 1: 
                LA87_5 = input.LA(1)

                 
                index87_5 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_QueryParser()):
                    s = 1

                elif (True):
                    s = 10

                 
                input.seek(index87_5)
                if s >= 0:
                    return s
            elif s == 2: 
                LA87_6 = input.LA(1)

                 
                index87_6 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_QueryParser()):
                    s = 1

                elif (True):
                    s = 10

                 
                input.seek(index87_6)
                if s >= 0:
                    return s
            elif s == 3: 
                LA87_7 = input.LA(1)

                 
                index87_7 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_QueryParser()):
                    s = 1

                elif (True):
                    s = 10

                 
                input.seek(index87_7)
                if s >= 0:
                    return s
            elif s == 4: 
                LA87_8 = input.LA(1)

                 
                index87_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_QueryParser()):
                    s = 1

                elif (True):
                    s = 10

                 
                input.seek(index87_8)
                if s >= 0:
                    return s
            elif s == 5: 
                LA87_9 = input.LA(1)

                 
                index87_9 = input.index()
                input.rewind()
                s = -1
                if (self.synpred146_QueryParser()):
                    s = 1

                elif (True):
                    s = 10

                 
                input.seek(index87_9)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 87, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #89

    DFA89_eot = DFA.unpack(
        u"\110\uffff"
        )

    DFA89_eof = DFA.unpack(
        u"\110\uffff"
        )

    DFA89_min = DFA.unpack(
        u"\1\5\7\uffff\1\0\22\uffff\1\0\43\uffff\1\0\4\uffff\1\0\3\uffff"
        )

    DFA89_max = DFA.unpack(
        u"\1\u00a3\7\uffff\1\0\22\uffff\1\0\43\uffff\1\0\4\uffff\1\0\3\uffff"
        )

    DFA89_accept = DFA.unpack(
        u"\1\uffff\1\1\101\uffff\1\2\1\uffff\1\4\1\uffff\1\3"
        )

    DFA89_special = DFA.unpack(
        u"\10\uffff\1\0\22\uffff\1\1\43\uffff\1\2\4\uffff\1\3\3\uffff"
        )

            
    DFA89_transition = [
        DFA.unpack(u"\7\1\2\uffff\1\10\11\1\1\uffff\6\1\1\uffff\2\1\1\33"
        u"\7\1\1\uffff\44\1\13\uffff\1\77\5\uffff\1\103\15\uffff\1\104\1"
        u"\uffff\1\105\1\uffff\1\105\57\uffff\2\1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #89

    class DFA89(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA89_8 = input.LA(1)

                 
                index89_8 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_QueryParser()):
                    s = 1

                elif (self.synpred150_QueryParser()):
                    s = 67

                 
                input.seek(index89_8)
                if s >= 0:
                    return s
            elif s == 1: 
                LA89_27 = input.LA(1)

                 
                index89_27 = input.index()
                input.rewind()
                s = -1
                if (self.synpred149_QueryParser()):
                    s = 1

                elif (self.synpred150_QueryParser()):
                    s = 67

                 
                input.seek(index89_27)
                if s >= 0:
                    return s
            elif s == 2: 
                LA89_63 = input.LA(1)

                 
                index89_63 = input.index()
                input.rewind()
                s = -1
                if ((((self.synpred149_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL")))) or ((self.synpred149_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL")))))):
                    s = 1

                elif (((self.synpred150_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 67

                 
                input.seek(index89_63)
                if s >= 0:
                    return s
            elif s == 3: 
                LA89_68 = input.LA(1)

                 
                index89_68 = input.index()
                input.rewind()
                s = -1
                if (self.synpred151_QueryParser()):
                    s = 71

                elif (True):
                    s = 69

                 
                input.seek(index89_68)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 89, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #126

    DFA126_eot = DFA.unpack(
        u"\115\uffff"
        )

    DFA126_eof = DFA.unpack(
        u"\115\uffff"
        )

    DFA126_min = DFA.unpack(
        u"\1\5\1\0\113\uffff"
        )

    DFA126_max = DFA.unpack(
        u"\1\u00a3\1\0\113\uffff"
        )

    DFA126_accept = DFA.unpack(
        u"\2\uffff\1\2\111\uffff\1\1"
        )

    DFA126_special = DFA.unpack(
        u"\1\uffff\1\0\113\uffff"
        )

            
    DFA126_transition = [
        DFA.unpack(u"\7\2\2\uffff\12\2\1\uffff\6\2\1\uffff\12\2\1\uffff\44"
        u"\2\13\uffff\2\2\2\uffff\1\2\1\uffff\2\2\1\uffff\3\2\2\uffff\1\2"
        u"\5\uffff\1\1\1\uffff\1\2\1\uffff\1\2\4\uffff\1\2\52\uffff\2\2"),
        DFA.unpack(u"\1\uffff"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #126

    class DFA126(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA126_1 = input.LA(1)

                 
                index126_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred201_QueryParser()):
                    s = 76

                elif (True):
                    s = 2

                 
                input.seek(index126_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 126, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #135

    DFA135_eot = DFA.unpack(
        u"\44\uffff"
        )

    DFA135_eof = DFA.unpack(
        u"\44\uffff"
        )

    DFA135_min = DFA.unpack(
        u"\1\132\1\165\1\5\1\uffff\1\134\2\16\1\134\3\16\1\134\1\16\1\134"
        u"\1\5\1\uffff\1\16\4\0\1\16\3\0\1\uffff\4\157\1\16\1\0\4\157"
        )

    DFA135_max = DFA.unpack(
        u"\1\132\1\165\1\u00a3\1\uffff\1\171\2\156\1\171\3\156\1\171\1\156"
        u"\1\171\1\u00a3\1\uffff\1\156\4\0\1\140\3\0\1\uffff\4\166\1\140"
        u"\1\0\4\166"
        )

    DFA135_accept = DFA.unpack(
        u"\3\uffff\1\2\13\uffff\1\3\11\uffff\1\1\12\uffff"
        )

    DFA135_special = DFA.unpack(
        u"\21\uffff\1\7\1\4\1\0\1\6\1\uffff\1\3\1\2\1\5\6\uffff\1\1\4\uffff"
        )

            
    DFA135_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\4\3\1\5\1\6\1\10\2\uffff\1\7\1\3\1\11\2\3\1\12\4\3"
        u"\1\uffff\6\3\1\uffff\2\3\1\13\7\3\1\uffff\26\3\1\14\15\3\13\uffff"
        u"\1\4\1\3\2\uffff\1\3\1\uffff\1\15\1\3\1\uffff\3\3\10\uffff\1\3"
        u"\1\uffff\1\3\1\uffff\1\3\57\uffff\2\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\16\2\uffff\1\3\1\uffff\2\3\5\uffff\1\3\4\uffff\2"
        u"\3\5\uffff\1\3\3\uffff\2\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\16\2\uffff\1\3\1\uffff\2\3\5\uffff\1\3\4\uffff\2"
        u"\3\5\uffff\1\3\3\uffff\2\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\16\2\uffff\1\3\1\uffff\2\3\5\uffff\1\3\4\uffff\2"
        u"\3\5\uffff\1\3\3\uffff\2\3"),
        DFA.unpack(u"\1\17\23\uffff\1\17\67\uffff\1\17\1\uffff\1\3\2\uffff"
        u"\1\3\1\17\15\uffff\1\3"),
        DFA.unpack(u"\1\20\4\uffff\2\3\5\uffff\1\3\4\uffff\1\3\6\uffff\1"
        u"\3\3\uffff\2\3"),
        DFA.unpack(u"\7\3\2\uffff\1\21\11\3\1\uffff\6\3\1\uffff\2\3\1\22"
        u"\7\3\1\uffff\44\3\13\uffff\1\23\5\uffff\1\24\15\uffff\1\25\63\uffff"
        u"\2\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\27\23\uffff\1\26\67\uffff\1\30\5\uffff\1\24\15\uffff"
        u"\1\25"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\33\23\uffff\1\32\67\uffff\1\34\5\uffff\1\35"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\41\23\uffff\1\40\67\uffff\1\42\5\uffff\1\43"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36"),
        DFA.unpack(u"\1\37\6\uffff\1\36")
    ]

    # class definition for DFA #135

    class DFA135(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA135_19 = input.LA(1)

                 
                index135_19 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_19)
                if s >= 0:
                    return s
            elif s == 1: 
                LA135_31 = input.LA(1)

                 
                index135_31 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_31)
                if s >= 0:
                    return s
            elif s == 2: 
                LA135_23 = input.LA(1)

                 
                index135_23 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_23)
                if s >= 0:
                    return s
            elif s == 3: 
                LA135_22 = input.LA(1)

                 
                index135_22 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_22)
                if s >= 0:
                    return s
            elif s == 4: 
                LA135_18 = input.LA(1)

                 
                index135_18 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_18)
                if s >= 0:
                    return s
            elif s == 5: 
                LA135_24 = input.LA(1)

                 
                index135_24 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_24)
                if s >= 0:
                    return s
            elif s == 6: 
                LA135_20 = input.LA(1)

                 
                index135_20 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_20)
                if s >= 0:
                    return s
            elif s == 7: 
                LA135_17 = input.LA(1)

                 
                index135_17 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred213_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 25

                elif (((self.synpred214_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 3

                 
                input.seek(index135_17)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 135, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #161

    DFA161_eot = DFA.unpack(
        u"\105\uffff"
        )

    DFA161_eof = DFA.unpack(
        u"\105\uffff"
        )

    DFA161_min = DFA.unpack(
        u"\1\5\76\uffff\1\0\5\uffff"
        )

    DFA161_max = DFA.unpack(
        u"\1\u00a3\76\uffff\1\0\5\uffff"
        )

    DFA161_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1\14\1"
        u"\15\1\16\1\17\1\20\1\21\1\22\1\23\1\24\1\25\1\26\1\27\1\30\1\31"
        u"\1\32\1\33\1\34\1\35\1\36\1\37\1\40\1\41\1\42\1\43\1\44\1\45\1"
        u"\46\1\47\1\50\1\51\1\52\1\53\1\54\1\55\1\56\1\57\1\60\1\61\1\62"
        u"\1\63\1\64\1\65\1\66\1\67\1\70\1\71\1\72\1\73\1\74\1\75\1\76\1"
        u"\uffff\1\101\1\102\1\103\1\77\1\100"
        )

    DFA161_special = DFA.unpack(
        u"\77\uffff\1\0\5\uffff"
        )

            
    DFA161_transition = [
        DFA.unpack(u"\1\2\1\3\1\4\1\5\1\6\1\7\1\12\2\uffff\1\10\1\11\1\13"
        u"\1\14\1\15\1\16\1\17\1\20\1\21\1\22\1\uffff\1\23\1\24\1\25\1\26"
        u"\1\27\1\30\1\uffff\1\31\1\32\1\33\1\34\1\35\1\36\1\37\1\40\1\41"
        u"\1\42\1\uffff\1\44\1\45\1\46\1\47\1\50\1\51\1\52\1\53\1\54\1\55"
        u"\1\56\1\57\1\60\1\61\1\62\1\63\1\64\1\65\1\66\1\67\1\70\1\71\1"
        u"\72\1\73\1\74\1\75\1\76\7\1\1\100\1\101\13\uffff\1\77\107\uffff"
        u"\1\43\1\102"),
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
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #161

    class DFA161(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA161_63 = input.LA(1)

                 
                index161_63 = input.index()
                input.rewind()
                s = -1
                if (((self.synpred315_QueryParser()) and ((!input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 67

                elif (((self.synpred316_QueryParser()) and ((input.LT(1).getText().equalsIgnoreCase("NULL"))))):
                    s = 68

                 
                input.seek(index161_63)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 161, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #176

    DFA176_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA176_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA176_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA176_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA176_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA176_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA176_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #176

    class DFA176(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA176_1 = input.LA(1)

                 
                index176_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred110_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index176_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 176, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #179

    DFA179_eot = DFA.unpack(
        u"\12\uffff"
        )

    DFA179_eof = DFA.unpack(
        u"\12\uffff"
        )

    DFA179_min = DFA.unpack(
        u"\1\52\1\0\10\uffff"
        )

    DFA179_max = DFA.unpack(
        u"\1\162\1\0\10\uffff"
        )

    DFA179_accept = DFA.unpack(
        u"\2\uffff\1\2\6\uffff\1\1"
        )

    DFA179_special = DFA.unpack(
        u"\1\uffff\1\0\10\uffff"
        )

            
    DFA179_transition = [
        DFA.unpack(u"\13\2\45\uffff\1\2\23\uffff\1\1\1\uffff\1\2\1\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #179

    class DFA179(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA179_1 = input.LA(1)

                 
                index179_1 = input.index()
                input.rewind()
                s = -1
                if (self.synpred113_QueryParser()):
                    s = 9

                elif (True):
                    s = 2

                 
                input.seek(index179_1)
                if s >= 0:
                    return s

            if self._state.backtracking >0:
                raise BacktrackingFailed
            nvae = NoViableAltException(self_.getDescription(), 179, _s, input)
            self_.error(nvae)
            raise nvae
 

    FOLLOW_statement_in_query372 = frozenset([5, 7, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 20, 21, 34, 54, 56, 57, 65, 66, 90, 109, 110])
    FOLLOW_EOF_in_query375 = frozenset([1])
    FOLLOW_SEMI_COLON_in_statement400 = frozenset([1])
    FOLLOW_general_statement_in_statement415 = frozenset([1])
    FOLLOW_foreach_statement_in_statement429 = frozenset([1])
    FOLLOW_split_statement_in_statement443 = frozenset([1])
    FOLLOW_inline_statement_in_statement459 = frozenset([1])
    FOLLOW_import_statement_in_statement481 = frozenset([1])
    FOLLOW_realias_statement_in_statement495 = frozenset([1])
    FOLLOW_import_clause_in_import_statement504 = frozenset([109])
    FOLLOW_SEMI_COLON_in_import_statement506 = frozenset([1])
    FOLLOW_inline_clause_in_inline_statement516 = frozenset([109])
    FOLLOW_SEMI_COLON_in_inline_statement518 = frozenset([1])
    FOLLOW_split_clause_in_split_statement528 = frozenset([109])
    FOLLOW_SEMI_COLON_in_split_statement530 = frozenset([1])
    FOLLOW_alias_in_general_statement542 = frozenset([117])
    FOLLOW_EQUAL_in_general_statement544 = frozenset([7, 8, 9, 11, 12, 14, 16, 17, 18, 19, 20, 34, 54, 56, 57, 65, 66, 110])
    FOLLOW_op_clause_in_general_statement550 = frozenset([32, 109])
    FOLLOW_parallel_clause_in_general_statement552 = frozenset([109])
    FOLLOW_LEFT_PAREN_in_general_statement557 = frozenset([7, 8, 9, 11, 12, 14, 16, 17, 18, 19, 20, 34, 54, 56, 57, 65, 66])
    FOLLOW_op_clause_in_general_statement559 = frozenset([32, 111])
    FOLLOW_parallel_clause_in_general_statement561 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_general_statement564 = frozenset([109])
    FOLLOW_SEMI_COLON_in_general_statement567 = frozenset([1])
    FOLLOW_realias_clause_in_realias_statement610 = frozenset([109])
    FOLLOW_SEMI_COLON_in_realias_statement612 = frozenset([1])
    FOLLOW_alias_in_realias_clause622 = frozenset([117])
    FOLLOW_EQUAL_in_realias_clause624 = frozenset([90])
    FOLLOW_identifier_in_realias_clause626 = frozenset([1])
    FOLLOW_PARALLEL_in_parallel_clause650 = frozenset([91])
    FOLLOW_INTEGER_in_parallel_clause653 = frozenset([1])
    FOLLOW_foreach_complex_statement_in_foreach_statement688 = frozenset([1])
    FOLLOW_foreach_simple_statement_in_foreach_statement710 = frozenset([1])
    FOLLOW_alias_in_foreach_complex_statement721 = frozenset([117])
    FOLLOW_EQUAL_in_foreach_complex_statement723 = frozenset([10, 90])
    FOLLOW_foreach_clause_complex_in_foreach_complex_statement728 = frozenset([1, 109])
    FOLLOW_SEMI_COLON_in_foreach_complex_statement730 = frozenset([1])
    FOLLOW_alias_in_foreach_simple_statement780 = frozenset([117])
    FOLLOW_EQUAL_in_foreach_simple_statement782 = frozenset([10, 110])
    FOLLOW_foreach_clause_simple_in_foreach_simple_statement788 = frozenset([32, 109])
    FOLLOW_parallel_clause_in_foreach_simple_statement790 = frozenset([109])
    FOLLOW_LEFT_PAREN_in_foreach_simple_statement844 = frozenset([10])
    FOLLOW_foreach_clause_simple_in_foreach_simple_statement846 = frozenset([32, 111])
    FOLLOW_parallel_clause_in_foreach_simple_statement848 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_foreach_simple_statement851 = frozenset([109])
    FOLLOW_SEMI_COLON_in_foreach_simple_statement854 = frozenset([1])
    FOLLOW_identifier_in_alias903 = frozenset([1])
    FOLLOW_identifier_in_parameter917 = frozenset([1])
    FOLLOW_INTEGER_in_parameter926 = frozenset([1])
    FOLLOW_DOUBLENUMBER_in_parameter935 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_parameter943 = frozenset([1])
    FOLLOW_DOLLARVAR_in_parameter951 = frozenset([1])
    FOLLOW_LEFT_CURLY_in_content960 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163])
    FOLLOW_content_in_content964 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163])
    FOLLOW_set_in_content968 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163])
    FOLLOW_RIGHT_CURLY_in_content980 = frozenset([1])
    FOLLOW_define_clause_in_op_clause989 = frozenset([1])
    FOLLOW_load_clause_in_op_clause1004 = frozenset([1])
    FOLLOW_group_clause_in_op_clause1018 = frozenset([1])
    FOLLOW_cube_clause_in_op_clause1032 = frozenset([1])
    FOLLOW_store_clause_in_op_clause1046 = frozenset([1])
    FOLLOW_filter_clause_in_op_clause1060 = frozenset([1])
    FOLLOW_distinct_clause_in_op_clause1074 = frozenset([1])
    FOLLOW_limit_clause_in_op_clause1088 = frozenset([1])
    FOLLOW_sample_clause_in_op_clause1102 = frozenset([1])
    FOLLOW_order_clause_in_op_clause1116 = frozenset([1])
    FOLLOW_rank_clause_in_op_clause1130 = frozenset([1])
    FOLLOW_cross_clause_in_op_clause1144 = frozenset([1])
    FOLLOW_join_clause_in_op_clause1158 = frozenset([1])
    FOLLOW_union_clause_in_op_clause1172 = frozenset([1])
    FOLLOW_stream_clause_in_op_clause1186 = frozenset([1])
    FOLLOW_mr_clause_in_op_clause1200 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_macro_param_clause1209 = frozenset([90, 111])
    FOLLOW_alias_in_macro_param_clause1213 = frozenset([111, 118])
    FOLLOW_COMMA_in_macro_param_clause1216 = frozenset([90])
    FOLLOW_alias_in_macro_param_clause1218 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_macro_param_clause1225 = frozenset([1])
    FOLLOW_RETURNS_in_macro_return_clause1252 = frozenset([4, 90])
    FOLLOW_alias_in_macro_return_clause1256 = frozenset([1, 118])
    FOLLOW_COMMA_in_macro_return_clause1259 = frozenset([90])
    FOLLOW_alias_in_macro_return_clause1261 = frozenset([1, 118])
    FOLLOW_VOID_in_macro_return_clause1268 = frozenset([1])
    FOLLOW_content_in_macro_body_clause1295 = frozenset([1])
    FOLLOW_macro_param_clause_in_macro_clause1317 = frozenset([6])
    FOLLOW_macro_return_clause_in_macro_clause1319 = frozenset([112])
    FOLLOW_macro_body_clause_in_macro_clause1321 = frozenset([1])
    FOLLOW_alias_in_inline_return_clause1351 = frozenset([117])
    FOLLOW_EQUAL_in_inline_return_clause1353 = frozenset([1])
    FOLLOW_alias_in_inline_return_clause1366 = frozenset([118])
    FOLLOW_COMMA_in_inline_return_clause1369 = frozenset([90])
    FOLLOW_alias_in_inline_return_clause1371 = frozenset([117, 118])
    FOLLOW_EQUAL_in_inline_return_clause1375 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_inline_param_clause1404 = frozenset([90, 91, 96, 99, 101, 111])
    FOLLOW_parameter_in_inline_param_clause1408 = frozenset([111, 118])
    FOLLOW_COMMA_in_inline_param_clause1411 = frozenset([90, 91, 96, 99, 101])
    FOLLOW_parameter_in_inline_param_clause1413 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_inline_param_clause1420 = frozenset([1])
    FOLLOW_inline_return_clause_in_inline_clause1442 = frozenset([90])
    FOLLOW_alias_in_inline_clause1444 = frozenset([110])
    FOLLOW_inline_param_clause_in_inline_clause1446 = frozenset([1])
    FOLLOW_IMPORT_in_import_clause1471 = frozenset([101])
    FOLLOW_QUOTEDSTRING_in_import_clause1474 = frozenset([1])
    FOLLOW_DEFINE_in_define_clause1483 = frozenset([90])
    FOLLOW_alias_in_define_clause1486 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 103, 110, 162, 163])
    FOLLOW_cmd_in_define_clause1490 = frozenset([1])
    FOLLOW_func_clause_in_define_clause1494 = frozenset([1])
    FOLLOW_macro_clause_in_define_clause1498 = frozenset([1])
    FOLLOW_EXECCOMMAND_in_cmd1508 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_ship_clause_in_cmd1513 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_cache_clause_in_cmd1517 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_input_clause_in_cmd1521 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_output_clause_in_cmd1525 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_error_clause_in_cmd1529 = frozenset([1, 58, 59, 60, 61, 62])
    FOLLOW_SHIP_in_ship_clause1541 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_ship_clause1544 = frozenset([101, 111])
    FOLLOW_path_list_in_ship_clause1547 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_ship_clause1550 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_path_list1560 = frozenset([1, 118])
    FOLLOW_COMMA_in_path_list1564 = frozenset([101])
    FOLLOW_QUOTEDSTRING_in_path_list1566 = frozenset([1, 118])
    FOLLOW_CACHE_in_cache_clause1593 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_cache_clause1596 = frozenset([101])
    FOLLOW_path_list_in_cache_clause1599 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_cache_clause1601 = frozenset([1])
    FOLLOW_INPUT_in_input_clause1611 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_input_clause1614 = frozenset([63, 64, 101])
    FOLLOW_stream_cmd_list_in_input_clause1617 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_input_clause1619 = frozenset([1])
    FOLLOW_stream_cmd_in_stream_cmd_list1629 = frozenset([1, 118])
    FOLLOW_COMMA_in_stream_cmd_list1633 = frozenset([63, 64, 101])
    FOLLOW_stream_cmd_in_stream_cmd_list1635 = frozenset([1, 118])
    FOLLOW_set_in_stream_cmd1667 = frozenset([1, 28])
    FOLLOW_USING_in_stream_cmd1684 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_clause_in_stream_cmd1689 = frozenset([1])
    FOLLOW_OUTPUT_in_output_clause1703 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_output_clause1706 = frozenset([63, 64, 101])
    FOLLOW_stream_cmd_list_in_output_clause1709 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_output_clause1711 = frozenset([1])
    FOLLOW_STDERROR_in_error_clause1721 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_error_clause1724 = frozenset([101, 111])
    FOLLOW_QUOTEDSTRING_in_error_clause1729 = frozenset([65, 111])
    FOLLOW_LIMIT_in_error_clause1733 = frozenset([91])
    FOLLOW_INTEGER_in_error_clause1736 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_error_clause1744 = frozenset([1])
    FOLLOW_LOAD_in_load_clause1754 = frozenset([101])
    FOLLOW_filename_in_load_clause1757 = frozenset([1, 26, 28])
    FOLLOW_USING_in_load_clause1761 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_clause_in_load_clause1764 = frozenset([1, 26])
    FOLLOW_as_clause_in_load_clause1769 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_filename1779 = frozenset([1])
    FOLLOW_AS_in_as_clause1787 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_as_clause1794 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_as_clause1797 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_as_clause1799 = frozenset([1])
    FOLLOW_field_def_in_as_clause1806 = frozenset([1])
    FOLLOW_identifier_in_field_def1817 = frozenset([1, 105])
    FOLLOW_COLON_in_field_def1821 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_type_in_field_def1823 = frozenset([1])
    FOLLOW_type_in_field_def1862 = frozenset([1])
    FOLLOW_field_def_in_field_def_list1890 = frozenset([1, 118])
    FOLLOW_COMMA_in_field_def_list1894 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_in_field_def_list1896 = frozenset([1, 118])
    FOLLOW_simple_type_in_type1927 = frozenset([1])
    FOLLOW_tuple_type_in_type1931 = frozenset([1])
    FOLLOW_bag_type_in_type1935 = frozenset([1])
    FOLLOW_map_type_in_type1939 = frozenset([1])
    FOLLOW_set_in_simple_type0 = frozenset([1])
    FOLLOW_TUPLE_in_tuple_type1985 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_tuple_type1988 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 111, 112, 114])
    FOLLOW_field_def_list_in_tuple_type1990 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_tuple_type1993 = frozenset([1])
    FOLLOW_BAG_in_bag_type2023 = frozenset([112])
    FOLLOW_LEFT_CURLY_in_bag_type2026 = frozenset([90])
    FOLLOW_null_keyword_in_bag_type2030 = frozenset([105])
    FOLLOW_COLON_in_bag_type2032 = frozenset([51, 110, 113])
    FOLLOW_tuple_type_in_bag_type2034 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_bag_type2039 = frozenset([1])
    FOLLOW_BAG_in_bag_type2071 = frozenset([112])
    FOLLOW_LEFT_CURLY_in_bag_type2074 = frozenset([51, 90, 110, 113])
    FOLLOW_identifier_in_bag_type2080 = frozenset([105])
    FOLLOW_COLON_in_bag_type2082 = frozenset([51, 110])
    FOLLOW_tuple_type_in_bag_type2087 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_bag_type2092 = frozenset([1])
    FOLLOW_MAP_in_map_type2123 = frozenset([114])
    FOLLOW_LEFT_BRACKET_in_map_type2126 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114, 115])
    FOLLOW_type_in_map_type2128 = frozenset([115])
    FOLLOW_RIGHT_BRACKET_in_map_type2131 = frozenset([1])
    FOLLOW_func_name_in_func_clause2159 = frozenset([1])
    FOLLOW_func_name_in_func_clause2196 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_func_clause2198 = frozenset([101, 102, 111])
    FOLLOW_func_args_in_func_clause2200 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_func_clause2203 = frozenset([1])
    FOLLOW_eid_in_func_name2236 = frozenset([1, 92, 95])
    FOLLOW_set_in_func_name2240 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_eid_in_func_name2250 = frozenset([1, 92, 95])
    FOLLOW_set_in_func_args_string0 = frozenset([1])
    FOLLOW_func_args_string_in_func_args2275 = frozenset([1, 118])
    FOLLOW_COMMA_in_func_args2279 = frozenset([101, 102])
    FOLLOW_func_args_string_in_func_args2281 = frozenset([1, 118])
    FOLLOW_set_in_group_clause2307 = frozenset([90, 110])
    FOLLOW_group_item_list_in_group_clause2318 = frozenset([1, 28, 33])
    FOLLOW_USING_in_group_clause2322 = frozenset([101])
    FOLLOW_group_type_in_group_clause2325 = frozenset([1, 33])
    FOLLOW_partition_clause_in_group_clause2330 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_group_type2340 = frozenset([1])
    FOLLOW_group_item_in_group_item_list2349 = frozenset([1, 118])
    FOLLOW_COMMA_in_group_item_list2353 = frozenset([90, 110])
    FOLLOW_group_item_in_group_item_list2355 = frozenset([1, 118])
    FOLLOW_rel_in_group_item2387 = frozenset([25, 27, 158])
    FOLLOW_join_group_by_clause_in_group_item2391 = frozenset([1, 29, 30])
    FOLLOW_ALL_in_group_item2395 = frozenset([1, 29, 30])
    FOLLOW_ANY_in_group_item2399 = frozenset([1, 29, 30])
    FOLLOW_set_in_group_item2403 = frozenset([1])
    FOLLOW_alias_in_rel2421 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_rel2430 = frozenset([7, 8, 9, 10, 11, 12, 14, 16, 17, 18, 19, 20, 34, 54, 56, 57, 65, 66, 90])
    FOLLOW_foreach_clause_complex_in_rel2435 = frozenset([111])
    FOLLOW_op_clause_in_rel2443 = frozenset([32, 111])
    FOLLOW_foreach_clause_simple_in_rel2447 = frozenset([32, 111])
    FOLLOW_parallel_clause_in_rel2451 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_rel2458 = frozenset([1])
    FOLLOW_flatten_clause_in_flatten_generated_item2468 = frozenset([1, 26])
    FOLLOW_AS_in_flatten_generated_item2472 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_flatten_generated_item2479 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_flatten_generated_item2482 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_flatten_generated_item2484 = frozenset([1])
    FOLLOW_field_def_in_flatten_generated_item2491 = frozenset([1])
    FOLLOW_col_range_in_flatten_generated_item2523 = frozenset([1, 26])
    FOLLOW_AS_in_flatten_generated_item2527 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_flatten_generated_item2534 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_flatten_generated_item2537 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_flatten_generated_item2539 = frozenset([1])
    FOLLOW_field_def_in_flatten_generated_item2546 = frozenset([1])
    FOLLOW_expr_in_flatten_generated_item2578 = frozenset([1, 26])
    FOLLOW_AS_in_flatten_generated_item2582 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_in_flatten_generated_item2585 = frozenset([1])
    FOLLOW_STAR_in_flatten_generated_item2615 = frozenset([1, 26])
    FOLLOW_AS_in_flatten_generated_item2619 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_flatten_generated_item2626 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_flatten_generated_item2629 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_flatten_generated_item2631 = frozenset([1])
    FOLLOW_field_def_in_flatten_generated_item2638 = frozenset([1])
    FOLLOW_FLATTEN_in_flatten_clause2653 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_flatten_clause2656 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_flatten_clause2659 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_flatten_clause2661 = frozenset([1])
    FOLLOW_STORE_in_store_clause2671 = frozenset([90, 110])
    FOLLOW_rel_in_store_clause2674 = frozenset([22])
    FOLLOW_INTO_in_store_clause2676 = frozenset([101])
    FOLLOW_filename_in_store_clause2679 = frozenset([1, 28])
    FOLLOW_USING_in_store_clause2683 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_clause_in_store_clause2686 = frozenset([1])
    FOLLOW_FILTER_in_filter_clause2698 = frozenset([90, 110])
    FOLLOW_rel_in_filter_clause2701 = frozenset([27])
    FOLLOW_BY_in_filter_clause2703 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_filter_clause2706 = frozenset([1])
    FOLLOW_or_cond_in_cond2715 = frozenset([1])
    FOLLOW_and_cond_in_or_cond2724 = frozenset([1, 36])
    FOLLOW_OR_in_or_cond2729 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_and_cond_in_or_cond2732 = frozenset([1, 36])
    FOLLOW_unary_cond_in_and_cond2744 = frozenset([1, 35])
    FOLLOW_AND_in_and_cond2748 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_unary_cond_in_and_cond2751 = frozenset([1, 35])
    FOLLOW_LEFT_PAREN_in_unary_cond2763 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_unary_cond2766 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_unary_cond2768 = frozenset([1])
    FOLLOW_not_cond_in_unary_cond2784 = frozenset([1])
    FOLLOW_expr_in_unary_cond2799 = frozenset([70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 83, 84])
    FOLLOW_rel_op_in_unary_cond2801 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_unary_cond2804 = frozenset([1])
    FOLLOW_func_eval_in_unary_cond2819 = frozenset([1])
    FOLLOW_null_check_cond_in_unary_cond2834 = frozenset([1])
    FOLLOW_NOT_in_not_cond2843 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_unary_cond_in_not_cond2846 = frozenset([1])
    FOLLOW_func_name_in_func_eval2855 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_func_eval2857 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 111, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_list_in_func_eval2859 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_func_eval2862 = frozenset([1])
    FOLLOW_real_arg_in_real_arg_list2894 = frozenset([1, 118])
    FOLLOW_COMMA_in_real_arg_list2898 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_in_real_arg_list2900 = frozenset([1, 118])
    FOLLOW_expr_in_real_arg2930 = frozenset([1])
    FOLLOW_STAR_in_real_arg2934 = frozenset([1])
    FOLLOW_col_range_in_real_arg2938 = frozenset([1])
    FOLLOW_expr_in_null_check_cond2947 = frozenset([53])
    FOLLOW_IS_in_null_check_cond2949 = frozenset([37, 90])
    FOLLOW_NOT_in_null_check_cond2952 = frozenset([90])
    FOLLOW_null_keyword_in_null_check_cond2955 = frozenset([1])
    FOLLOW_add_expr_in_expr2965 = frozenset([1])
    FOLLOW_multi_expr_in_add_expr2974 = frozenset([1, 97, 98])
    FOLLOW_set_in_add_expr2978 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_multi_expr_in_add_expr2989 = frozenset([1, 97, 98])
    FOLLOW_cast_expr_in_multi_expr3001 = frozenset([1, 104, 120, 121])
    FOLLOW_set_in_multi_expr3005 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cast_expr_in_multi_expr3020 = frozenset([1, 104, 120, 121])
    FOLLOW_LEFT_PAREN_in_cast_expr3032 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_type_cast_in_cast_expr3034 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_cast_expr3036 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_unary_expr_in_cast_expr3038 = frozenset([1])
    FOLLOW_unary_expr_in_cast_expr3073 = frozenset([1])
    FOLLOW_simple_type_in_type_cast3082 = frozenset([1])
    FOLLOW_map_type_in_type_cast3086 = frozenset([1])
    FOLLOW_tuple_type_cast_in_type_cast3090 = frozenset([1])
    FOLLOW_bag_type_cast_in_type_cast3094 = frozenset([1])
    FOLLOW_TUPLE_in_tuple_type_cast3103 = frozenset([110])
    FOLLOW_LEFT_PAREN_in_tuple_type_cast3105 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 111, 112, 114])
    FOLLOW_type_cast_in_tuple_type_cast3109 = frozenset([111, 118])
    FOLLOW_COMMA_in_tuple_type_cast3113 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_type_cast_in_tuple_type_cast3115 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_tuple_type_cast3123 = frozenset([1])
    FOLLOW_BAG_in_bag_type_cast3158 = frozenset([112])
    FOLLOW_LEFT_CURLY_in_bag_type_cast3160 = frozenset([51, 113])
    FOLLOW_tuple_type_cast_in_bag_type_cast3162 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_bag_type_cast3165 = frozenset([1])
    FOLLOW_expr_eval_in_unary_expr3198 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_unary_expr3214 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_unary_expr3216 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_unary_expr3218 = frozenset([1])
    FOLLOW_neg_expr_in_unary_expr3253 = frozenset([1])
    FOLLOW_const_expr_in_expr_eval3262 = frozenset([1])
    FOLLOW_var_expr_in_expr_eval3266 = frozenset([1])
    FOLLOW_projectable_expr_in_var_expr3275 = frozenset([1, 92, 116])
    FOLLOW_dot_proj_in_var_expr3279 = frozenset([1, 92, 116])
    FOLLOW_pound_proj_in_var_expr3283 = frozenset([1, 92, 116])
    FOLLOW_func_eval_in_projectable_expr3294 = frozenset([1])
    FOLLOW_col_ref_in_projectable_expr3298 = frozenset([1])
    FOLLOW_bin_expr_in_projectable_expr3302 = frozenset([1])
    FOLLOW_type_conversion_in_projectable_expr3306 = frozenset([1])
    FOLLOW_LEFT_CURLY_in_type_conversion3315 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_list_in_type_conversion3317 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_type_conversion3319 = frozenset([1])
    FOLLOW_LEFT_BRACKET_in_type_conversion3366 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_list_in_type_conversion3368 = frozenset([115])
    FOLLOW_RIGHT_BRACKET_in_type_conversion3370 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_type_conversion3417 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_in_type_conversion3419 = frozenset([118])
    FOLLOW_COMMA_in_type_conversion3423 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_real_arg_in_type_conversion3425 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_type_conversion3430 = frozenset([1])
    FOLLOW_PERIOD_in_dot_proj3468 = frozenset([14, 34, 90, 96, 110])
    FOLLOW_col_alias_or_index_in_dot_proj3472 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_dot_proj3497 = frozenset([14, 34, 90, 96])
    FOLLOW_col_alias_or_index_in_dot_proj3499 = frozenset([111, 118])
    FOLLOW_COMMA_in_dot_proj3503 = frozenset([14, 34, 90, 96])
    FOLLOW_col_alias_or_index_in_dot_proj3505 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_dot_proj3510 = frozenset([1])
    FOLLOW_col_alias_in_col_alias_or_index3542 = frozenset([1])
    FOLLOW_col_index_in_col_alias_or_index3546 = frozenset([1])
    FOLLOW_GROUP_in_col_alias3555 = frozenset([1])
    FOLLOW_CUBE_in_col_alias3559 = frozenset([1])
    FOLLOW_identifier_in_col_alias3563 = frozenset([1])
    FOLLOW_DOLLARVAR_in_col_index3572 = frozenset([1])
    FOLLOW_col_ref_in_col_range3585 = frozenset([119])
    FOLLOW_DOUBLE_PERIOD_in_col_range3587 = frozenset([1, 14, 34, 90, 96])
    FOLLOW_col_ref_in_col_range3593 = frozenset([1])
    FOLLOW_DOUBLE_PERIOD_in_col_range3634 = frozenset([14, 34, 90, 96])
    FOLLOW_col_ref_in_col_range3636 = frozenset([1])
    FOLLOW_POUND_in_pound_proj3667 = frozenset([90, 101])
    FOLLOW_QUOTEDSTRING_in_pound_proj3672 = frozenset([1])
    FOLLOW_null_keyword_in_pound_proj3676 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_bin_expr3687 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_bin_expr3689 = frozenset([122])
    FOLLOW_QMARK_in_bin_expr3691 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_bin_expr3697 = frozenset([105])
    FOLLOW_COLON_in_bin_expr3699 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_bin_expr3705 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_bin_expr3707 = frozenset([1])
    FOLLOW_MINUS_in_neg_expr3740 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cast_expr_in_neg_expr3742 = frozenset([1])
    FOLLOW_LIMIT_in_limit_clause3769 = frozenset([90, 110])
    FOLLOW_rel_in_limit_clause3772 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_INTEGER_in_limit_clause3784 = frozenset([1])
    FOLLOW_LONGINTEGER_in_limit_clause3796 = frozenset([1])
    FOLLOW_expr_in_limit_clause3800 = frozenset([1])
    FOLLOW_SAMPLE_in_sample_clause3811 = frozenset([90, 110])
    FOLLOW_rel_in_sample_clause3814 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_DOUBLENUMBER_in_sample_clause3826 = frozenset([1])
    FOLLOW_expr_in_sample_clause3830 = frozenset([1])
    FOLLOW_RANK_in_rank_clause3841 = frozenset([90, 110])
    FOLLOW_rel_in_rank_clause3844 = frozenset([1, 27])
    FOLLOW_rank_by_statement_in_rank_clause3848 = frozenset([1])
    FOLLOW_BY_in_rank_by_statement3860 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_rank_by_clause_in_rank_by_statement3863 = frozenset([1, 13])
    FOLLOW_DENSE_in_rank_by_statement3867 = frozenset([1])
    FOLLOW_STAR_in_rank_by_clause3879 = frozenset([1, 40, 41])
    FOLLOW_set_in_rank_by_clause3881 = frozenset([1])
    FOLLOW_rank_list_in_rank_by_clause3900 = frozenset([1])
    FOLLOW_rank_col_in_rank_list3909 = frozenset([1, 118])
    FOLLOW_COMMA_in_rank_list3913 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_rank_col_in_rank_list3915 = frozenset([1, 118])
    FOLLOW_col_range_in_rank_col3941 = frozenset([1, 40, 41])
    FOLLOW_set_in_rank_col3943 = frozenset([1])
    FOLLOW_col_ref_in_rank_col3965 = frozenset([1, 40, 41])
    FOLLOW_set_in_rank_col3967 = frozenset([1])
    FOLLOW_ORDER_in_order_clause3985 = frozenset([90, 110])
    FOLLOW_rel_in_order_clause3988 = frozenset([27])
    FOLLOW_BY_in_order_clause3990 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_order_by_clause_in_order_clause3993 = frozenset([1, 28])
    FOLLOW_USING_in_order_clause3997 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_clause_in_order_clause4000 = frozenset([1])
    FOLLOW_STAR_in_order_by_clause4012 = frozenset([1, 40, 41])
    FOLLOW_set_in_order_by_clause4014 = frozenset([1])
    FOLLOW_order_col_list_in_order_by_clause4043 = frozenset([1])
    FOLLOW_order_col_in_order_col_list4052 = frozenset([1, 118])
    FOLLOW_COMMA_in_order_col_list4056 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_order_col_in_order_col_list4058 = frozenset([1, 118])
    FOLLOW_col_range_in_order_col4089 = frozenset([1, 40, 41])
    FOLLOW_set_in_order_col4091 = frozenset([1])
    FOLLOW_col_ref_in_order_col4112 = frozenset([1, 40, 41])
    FOLLOW_set_in_order_col4114 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_order_col4139 = frozenset([14, 34, 90, 96])
    FOLLOW_col_ref_in_order_col4142 = frozenset([40, 41, 111])
    FOLLOW_set_in_order_col4144 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_order_col4155 = frozenset([1])
    FOLLOW_DISTINCT_in_distinct_clause4165 = frozenset([90, 110])
    FOLLOW_rel_in_distinct_clause4168 = frozenset([1, 33])
    FOLLOW_partition_clause_in_distinct_clause4170 = frozenset([1])
    FOLLOW_PARTITION_in_partition_clause4180 = frozenset([27])
    FOLLOW_BY_in_partition_clause4183 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_name_in_partition_clause4186 = frozenset([1])
    FOLLOW_CROSS_in_cross_clause4195 = frozenset([90, 110])
    FOLLOW_rel_list_in_cross_clause4198 = frozenset([1, 33])
    FOLLOW_partition_clause_in_cross_clause4200 = frozenset([1])
    FOLLOW_rel_in_rel_list4210 = frozenset([1, 118])
    FOLLOW_COMMA_in_rel_list4214 = frozenset([90, 110])
    FOLLOW_rel_in_rel_list4216 = frozenset([1, 118])
    FOLLOW_JOIN_in_join_clause4241 = frozenset([90, 110])
    FOLLOW_join_sub_clause_in_join_clause4244 = frozenset([1, 28, 33])
    FOLLOW_USING_in_join_clause4248 = frozenset([101])
    FOLLOW_join_type_in_join_clause4251 = frozenset([1, 33])
    FOLLOW_partition_clause_in_join_clause4256 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_join_type4266 = frozenset([1])
    FOLLOW_join_item_in_join_sub_clause4275 = frozenset([67, 68, 69])
    FOLLOW_set_in_join_sub_clause4277 = frozenset([30, 118])
    FOLLOW_OUTER_in_join_sub_clause4291 = frozenset([118])
    FOLLOW_COMMA_in_join_sub_clause4294 = frozenset([90, 110])
    FOLLOW_join_item_in_join_sub_clause4297 = frozenset([1])
    FOLLOW_join_item_list_in_join_sub_clause4317 = frozenset([1])
    FOLLOW_join_item_in_join_item_list4326 = frozenset([118])
    FOLLOW_COMMA_in_join_item_list4330 = frozenset([90, 110])
    FOLLOW_join_item_in_join_item_list4333 = frozenset([1, 118])
    FOLLOW_rel_in_join_item4345 = frozenset([27])
    FOLLOW_join_group_by_clause_in_join_item4347 = frozenset([1])
    FOLLOW_BY_in_join_group_by_clause4378 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_join_group_by_expr_list_in_join_group_by_clause4381 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_join_group_by_expr_list4390 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_join_group_by_expr_in_join_group_by_expr_list4392 = frozenset([111, 118])
    FOLLOW_COMMA_in_join_group_by_expr_list4396 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_join_group_by_expr_in_join_group_by_expr_list4398 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_join_group_by_expr_list4403 = frozenset([1])
    FOLLOW_join_group_by_expr_in_join_group_by_expr_list4459 = frozenset([1])
    FOLLOW_col_range_in_join_group_by_expr4468 = frozenset([1])
    FOLLOW_expr_in_join_group_by_expr4473 = frozenset([1])
    FOLLOW_STAR_in_join_group_by_expr4477 = frozenset([1])
    FOLLOW_UNION_in_union_clause4486 = frozenset([31, 90, 110])
    FOLLOW_ONSCHEMA_in_union_clause4489 = frozenset([90, 110])
    FOLLOW_rel_list_in_union_clause4492 = frozenset([1])
    FOLLOW_FOREACH_in_foreach_clause_simple4501 = frozenset([90, 110])
    FOLLOW_rel_in_foreach_clause_simple4504 = frozenset([38])
    FOLLOW_foreach_plan_simple_in_foreach_clause_simple4506 = frozenset([1])
    FOLLOW_generate_clause_in_foreach_plan_simple4515 = frozenset([1])
    FOLLOW_FOREACH_in_foreach_clause_complex4553 = frozenset([90, 110])
    FOLLOW_rel_in_foreach_clause_complex4556 = frozenset([112])
    FOLLOW_foreach_plan_complex_in_foreach_clause_complex4558 = frozenset([1])
    FOLLOW_nested_blk_in_foreach_plan_complex4567 = frozenset([1])
    FOLLOW_CUBE_in_cube_clause4606 = frozenset([90, 110])
    FOLLOW_cube_item_in_cube_clause4609 = frozenset([1])
    FOLLOW_rel_in_cube_item4619 = frozenset([27])
    FOLLOW_cube_by_clause_in_cube_item4623 = frozenset([1])
    FOLLOW_BY_in_cube_by_clause4634 = frozenset([14, 15])
    FOLLOW_cube_or_rollup_in_cube_by_clause4637 = frozenset([1])
    FOLLOW_cube_rollup_list_in_cube_or_rollup4646 = frozenset([1, 118])
    FOLLOW_COMMA_in_cube_or_rollup4650 = frozenset([14, 15])
    FOLLOW_cube_rollup_list_in_cube_or_rollup4652 = frozenset([1, 118])
    FOLLOW_set_in_cube_rollup_list4685 = frozenset([110])
    FOLLOW_cube_by_expr_list_in_cube_rollup_list4696 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_cube_by_expr_list4705 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_cube_by_expr_in_cube_by_expr_list4707 = frozenset([111, 118])
    FOLLOW_COMMA_in_cube_by_expr_list4711 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_cube_by_expr_in_cube_by_expr_list4713 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_cube_by_expr_list4718 = frozenset([1])
    FOLLOW_col_range_in_cube_by_expr4751 = frozenset([1])
    FOLLOW_expr_in_cube_by_expr4756 = frozenset([1])
    FOLLOW_STAR_in_cube_by_expr4760 = frozenset([1])
    FOLLOW_LEFT_CURLY_in_nested_blk4769 = frozenset([38, 90])
    FOLLOW_nested_command_list_in_nested_blk4772 = frozenset([38])
    FOLLOW_generate_clause_in_nested_blk4776 = frozenset([109])
    FOLLOW_SEMI_COLON_in_nested_blk4778 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_nested_blk4783 = frozenset([1])
    FOLLOW_GENERATE_in_generate_clause4793 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_flatten_generated_item_in_generate_clause4795 = frozenset([1, 118])
    FOLLOW_COMMA_in_generate_clause4799 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_flatten_generated_item_in_generate_clause4801 = frozenset([1, 118])
    FOLLOW_nested_command_in_nested_command_list4844 = frozenset([109])
    FOLLOW_SEMI_COLON_in_nested_command_list4846 = frozenset([1, 90])
    FOLLOW_identifier_in_nested_command4924 = frozenset([117])
    FOLLOW_EQUAL_in_nested_command4926 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_proj_in_nested_command4928 = frozenset([1])
    FOLLOW_identifier_in_nested_command4975 = frozenset([117])
    FOLLOW_EQUAL_in_nested_command4977 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_nested_command4979 = frozenset([1])
    FOLLOW_identifier_in_nested_command5024 = frozenset([117])
    FOLLOW_EQUAL_in_nested_command5026 = frozenset([9, 10, 11, 16, 19, 65])
    FOLLOW_nested_op_in_nested_command5028 = frozenset([1])
    FOLLOW_nested_filter_in_nested_op5063 = frozenset([1])
    FOLLOW_nested_sort_in_nested_op5077 = frozenset([1])
    FOLLOW_nested_distinct_in_nested_op5091 = frozenset([1])
    FOLLOW_nested_limit_in_nested_op5105 = frozenset([1])
    FOLLOW_nested_cross_in_nested_op5119 = frozenset([1])
    FOLLOW_nested_foreach_in_nested_op5133 = frozenset([1])
    FOLLOW_col_ref_in_nested_proj5142 = frozenset([92])
    FOLLOW_PERIOD_in_nested_proj5144 = frozenset([14, 34, 90, 96, 110])
    FOLLOW_col_ref_list_in_nested_proj5146 = frozenset([1])
    FOLLOW_col_ref_in_col_ref_list5180 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_col_ref_list5186 = frozenset([14, 34, 90, 96])
    FOLLOW_col_ref_in_col_ref_list5188 = frozenset([111, 118])
    FOLLOW_COMMA_in_col_ref_list5192 = frozenset([14, 34, 90, 96])
    FOLLOW_col_ref_in_col_ref_list5194 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_col_ref_list5199 = frozenset([1])
    FOLLOW_FILTER_in_nested_filter5229 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_filter5232 = frozenset([27])
    FOLLOW_BY_in_nested_filter5234 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_nested_filter5237 = frozenset([1])
    FOLLOW_ORDER_in_nested_sort5246 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_sort5249 = frozenset([27])
    FOLLOW_BY_in_nested_sort5251 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_order_by_clause_in_nested_sort5255 = frozenset([1, 28])
    FOLLOW_USING_in_nested_sort5259 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 162, 163])
    FOLLOW_func_clause_in_nested_sort5262 = frozenset([1])
    FOLLOW_DISTINCT_in_nested_distinct5274 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_distinct5277 = frozenset([1])
    FOLLOW_LIMIT_in_nested_limit5286 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_limit5289 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_INTEGER_in_nested_limit5301 = frozenset([1])
    FOLLOW_expr_in_nested_limit5305 = frozenset([1])
    FOLLOW_CROSS_in_nested_cross5316 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_list_in_nested_cross5319 = frozenset([1])
    FOLLOW_FOREACH_in_nested_foreach5327 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_foreach5330 = frozenset([38])
    FOLLOW_generate_clause_in_nested_foreach5332 = frozenset([1])
    FOLLOW_col_ref_in_nested_op_input5341 = frozenset([1])
    FOLLOW_nested_proj_in_nested_op_input5345 = frozenset([1])
    FOLLOW_nested_op_input_in_nested_op_input_list5354 = frozenset([1, 118])
    FOLLOW_COMMA_in_nested_op_input_list5358 = frozenset([14, 34, 90, 96])
    FOLLOW_nested_op_input_in_nested_op_input_list5360 = frozenset([1, 118])
    FOLLOW_STREAM_in_stream_clause5385 = frozenset([90, 110])
    FOLLOW_rel_in_stream_clause5388 = frozenset([55])
    FOLLOW_THROUGH_in_stream_clause5390 = frozenset([90, 103])
    FOLLOW_EXECCOMMAND_in_stream_clause5395 = frozenset([1, 26])
    FOLLOW_alias_in_stream_clause5399 = frozenset([1, 26])
    FOLLOW_as_clause_in_stream_clause5403 = frozenset([1])
    FOLLOW_MAPREDUCE_in_mr_clause5413 = frozenset([101])
    FOLLOW_QUOTEDSTRING_in_mr_clause5416 = frozenset([56, 110])
    FOLLOW_LEFT_PAREN_in_mr_clause5420 = frozenset([101])
    FOLLOW_path_list_in_mr_clause5423 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_mr_clause5425 = frozenset([56])
    FOLLOW_store_clause_in_mr_clause5431 = frozenset([8])
    FOLLOW_load_clause_in_mr_clause5433 = frozenset([1, 103])
    FOLLOW_EXECCOMMAND_in_mr_clause5435 = frozenset([1])
    FOLLOW_SPLIT_in_split_clause5445 = frozenset([90, 110])
    FOLLOW_rel_in_split_clause5447 = frozenset([22])
    FOLLOW_INTO_in_split_clause5449 = frozenset([90])
    FOLLOW_split_branch_in_split_clause5451 = frozenset([118])
    FOLLOW_COMMA_in_split_clause5457 = frozenset([90])
    FOLLOW_split_branch_in_split_clause5459 = frozenset([1, 118])
    FOLLOW_COMMA_in_split_clause5470 = frozenset([90])
    FOLLOW_split_branch_in_split_clause5472 = frozenset([118])
    FOLLOW_COMMA_in_split_clause5477 = frozenset([90])
    FOLLOW_split_otherwise_in_split_clause5479 = frozenset([1])
    FOLLOW_alias_in_split_branch5519 = frozenset([23])
    FOLLOW_IF_in_split_branch5521 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_split_branch5523 = frozenset([1])
    FOLLOW_alias_in_split_otherwise5556 = frozenset([24])
    FOLLOW_OTHERWISE_in_split_otherwise5558 = frozenset([1])
    FOLLOW_alias_col_ref_in_col_ref5589 = frozenset([1])
    FOLLOW_dollar_col_ref_in_col_ref5593 = frozenset([1])
    FOLLOW_GROUP_in_alias_col_ref5602 = frozenset([1])
    FOLLOW_CUBE_in_alias_col_ref5606 = frozenset([1])
    FOLLOW_identifier_in_alias_col_ref5610 = frozenset([1])
    FOLLOW_DOLLARVAR_in_dollar_col_ref5619 = frozenset([1])
    FOLLOW_literal_in_const_expr5628 = frozenset([1])
    FOLLOW_scalar_in_literal5637 = frozenset([1])
    FOLLOW_map_in_literal5641 = frozenset([1])
    FOLLOW_bag_in_literal5645 = frozenset([1])
    FOLLOW_tuple_in_literal5649 = frozenset([1])
    FOLLOW_num_scalar_in_scalar5659 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_scalar5663 = frozenset([1])
    FOLLOW_null_keyword_in_scalar5667 = frozenset([1])
    FOLLOW_TRUE_in_scalar5671 = frozenset([1])
    FOLLOW_FALSE_in_scalar5675 = frozenset([1])
    FOLLOW_MINUS_in_num_scalar5684 = frozenset([91, 94, 99, 100])
    FOLLOW_set_in_num_scalar5687 = frozenset([1])
    FOLLOW_LEFT_BRACKET_in_map5712 = frozenset([101])
    FOLLOW_keyvalue_in_map5714 = frozenset([115, 118])
    FOLLOW_COMMA_in_map5718 = frozenset([101])
    FOLLOW_keyvalue_in_map5720 = frozenset([115, 118])
    FOLLOW_RIGHT_BRACKET_in_map5725 = frozenset([1])
    FOLLOW_LEFT_BRACKET_in_map5747 = frozenset([115])
    FOLLOW_RIGHT_BRACKET_in_map5749 = frozenset([1])
    FOLLOW_map_key_in_keyvalue5769 = frozenset([116])
    FOLLOW_POUND_in_keyvalue5771 = frozenset([77, 78, 90, 91, 94, 97, 99, 100, 101, 110, 112, 114])
    FOLLOW_const_expr_in_keyvalue5773 = frozenset([1])
    FOLLOW_QUOTEDSTRING_in_map_key5802 = frozenset([1])
    FOLLOW_LEFT_CURLY_in_bag5811 = frozenset([77, 78, 90, 91, 94, 97, 99, 100, 101, 110, 112, 114])
    FOLLOW_tuple_in_bag5813 = frozenset([113, 118])
    FOLLOW_COMMA_in_bag5817 = frozenset([77, 78, 90, 91, 94, 97, 99, 100, 101, 110, 112, 114])
    FOLLOW_tuple_in_bag5819 = frozenset([113, 118])
    FOLLOW_RIGHT_CURLY_in_bag5824 = frozenset([1])
    FOLLOW_LEFT_CURLY_in_bag5846 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_bag5848 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_tuple5868 = frozenset([77, 78, 90, 91, 94, 97, 99, 100, 101, 110, 112, 114])
    FOLLOW_literal_in_tuple5870 = frozenset([111, 118])
    FOLLOW_COMMA_in_tuple5874 = frozenset([77, 78, 90, 91, 94, 97, 99, 100, 101, 110, 112, 114])
    FOLLOW_literal_in_tuple5876 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_tuple5881 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_tuple5907 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_tuple5909 = frozenset([1])
    FOLLOW_rel_str_op_in_eid5932 = frozenset([1])
    FOLLOW_IMPORT_in_eid5940 = frozenset([1])
    FOLLOW_RETURNS_in_eid5948 = frozenset([1])
    FOLLOW_DEFINE_in_eid5956 = frozenset([1])
    FOLLOW_LOAD_in_eid5964 = frozenset([1])
    FOLLOW_FILTER_in_eid5972 = frozenset([1])
    FOLLOW_FOREACH_in_eid5980 = frozenset([1])
    FOLLOW_CUBE_in_eid5988 = frozenset([1])
    FOLLOW_ROLLUP_in_eid5996 = frozenset([1])
    FOLLOW_ORDER_in_eid6004 = frozenset([1])
    FOLLOW_DISTINCT_in_eid6012 = frozenset([1])
    FOLLOW_COGROUP_in_eid6020 = frozenset([1])
    FOLLOW_JOIN_in_eid6028 = frozenset([1])
    FOLLOW_CROSS_in_eid6036 = frozenset([1])
    FOLLOW_UNION_in_eid6044 = frozenset([1])
    FOLLOW_SPLIT_in_eid6052 = frozenset([1])
    FOLLOW_INTO_in_eid6060 = frozenset([1])
    FOLLOW_IF_in_eid6068 = frozenset([1])
    FOLLOW_ALL_in_eid6076 = frozenset([1])
    FOLLOW_AS_in_eid6084 = frozenset([1])
    FOLLOW_BY_in_eid6092 = frozenset([1])
    FOLLOW_USING_in_eid6100 = frozenset([1])
    FOLLOW_INNER_in_eid6108 = frozenset([1])
    FOLLOW_OUTER_in_eid6116 = frozenset([1])
    FOLLOW_PARALLEL_in_eid6124 = frozenset([1])
    FOLLOW_PARTITION_in_eid6132 = frozenset([1])
    FOLLOW_GROUP_in_eid6140 = frozenset([1])
    FOLLOW_AND_in_eid6148 = frozenset([1])
    FOLLOW_OR_in_eid6156 = frozenset([1])
    FOLLOW_NOT_in_eid6164 = frozenset([1])
    FOLLOW_GENERATE_in_eid6172 = frozenset([1])
    FOLLOW_FLATTEN_in_eid6180 = frozenset([1])
    FOLLOW_ASC_in_eid6188 = frozenset([1])
    FOLLOW_DESC_in_eid6196 = frozenset([1])
    FOLLOW_BOOL_in_eid6204 = frozenset([1])
    FOLLOW_INT_in_eid6212 = frozenset([1])
    FOLLOW_LONG_in_eid6220 = frozenset([1])
    FOLLOW_FLOAT_in_eid6228 = frozenset([1])
    FOLLOW_DOUBLE_in_eid6236 = frozenset([1])
    FOLLOW_DATETIME_in_eid6244 = frozenset([1])
    FOLLOW_CHARARRAY_in_eid6252 = frozenset([1])
    FOLLOW_BYTEARRAY_in_eid6260 = frozenset([1])
    FOLLOW_BAG_in_eid6268 = frozenset([1])
    FOLLOW_TUPLE_in_eid6276 = frozenset([1])
    FOLLOW_MAP_in_eid6284 = frozenset([1])
    FOLLOW_IS_in_eid6292 = frozenset([1])
    FOLLOW_STREAM_in_eid6300 = frozenset([1])
    FOLLOW_THROUGH_in_eid6308 = frozenset([1])
    FOLLOW_STORE_in_eid6316 = frozenset([1])
    FOLLOW_MAPREDUCE_in_eid6324 = frozenset([1])
    FOLLOW_SHIP_in_eid6332 = frozenset([1])
    FOLLOW_CACHE_in_eid6340 = frozenset([1])
    FOLLOW_INPUT_in_eid6348 = frozenset([1])
    FOLLOW_OUTPUT_in_eid6356 = frozenset([1])
    FOLLOW_STDERROR_in_eid6364 = frozenset([1])
    FOLLOW_STDIN_in_eid6372 = frozenset([1])
    FOLLOW_STDOUT_in_eid6380 = frozenset([1])
    FOLLOW_LIMIT_in_eid6388 = frozenset([1])
    FOLLOW_SAMPLE_in_eid6396 = frozenset([1])
    FOLLOW_LEFT_in_eid6404 = frozenset([1])
    FOLLOW_RIGHT_in_eid6412 = frozenset([1])
    FOLLOW_FULL_in_eid6420 = frozenset([1])
    FOLLOW_identifier_in_eid6428 = frozenset([1])
    FOLLOW_null_keyword_in_eid6436 = frozenset([1])
    FOLLOW_TRUE_in_eid6444 = frozenset([1])
    FOLLOW_FALSE_in_eid6452 = frozenset([1])
    FOLLOW_REALIAS_in_eid6460 = frozenset([1])
    FOLLOW_rel_op_eq_in_rel_op6470 = frozenset([1])
    FOLLOW_rel_op_ne_in_rel_op6481 = frozenset([1])
    FOLLOW_rel_op_gt_in_rel_op6492 = frozenset([1])
    FOLLOW_rel_op_gte_in_rel_op6503 = frozenset([1])
    FOLLOW_rel_op_lt_in_rel_op6514 = frozenset([1])
    FOLLOW_rel_op_lte_in_rel_op6525 = frozenset([1])
    FOLLOW_STR_OP_MATCHES_in_rel_op6536 = frozenset([1])
    FOLLOW_set_in_rel_op_eq0 = frozenset([1])
    FOLLOW_set_in_rel_op_ne0 = frozenset([1])
    FOLLOW_set_in_rel_op_gt0 = frozenset([1])
    FOLLOW_set_in_rel_op_gte0 = frozenset([1])
    FOLLOW_set_in_rel_op_lt0 = frozenset([1])
    FOLLOW_set_in_rel_op_lte0 = frozenset([1])
    FOLLOW_set_in_rel_str_op0 = frozenset([1])
    FOLLOW_IDENTIFIER_L_in_null_keyword6724 = frozenset([1])
    FOLLOW_IDENTIFIER_L_in_identifier6745 = frozenset([1])
    FOLLOW_alias_in_synpred13_QueryParser670 = frozenset([117])
    FOLLOW_EQUAL_in_synpred13_QueryParser672 = frozenset([10])
    FOLLOW_FOREACH_in_synpred13_QueryParser678 = frozenset([90, 110])
    FOLLOW_rel_in_synpred13_QueryParser680 = frozenset([112])
    FOLLOW_LEFT_CURLY_in_synpred13_QueryParser682 = frozenset([1])
    FOLLOW_SEMI_COLON_in_synpred15_QueryParser730 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred68_QueryParser1794 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred68_QueryParser1797 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred68_QueryParser1799 = frozenset([1])
    FOLLOW_BAG_in_synpred86_QueryParser2023 = frozenset([112])
    FOLLOW_LEFT_CURLY_in_synpred86_QueryParser2026 = frozenset([90])
    FOLLOW_null_keyword_in_synpred86_QueryParser2030 = frozenset([105])
    FOLLOW_COLON_in_synpred86_QueryParser2032 = frozenset([51, 110, 113])
    FOLLOW_tuple_type_in_synpred86_QueryParser2034 = frozenset([113])
    FOLLOW_RIGHT_CURLY_in_synpred86_QueryParser2039 = frozenset([1])
    FOLLOW_foreach_clause_complex_in_synpred107_QueryParser2435 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred110_QueryParser2479 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred110_QueryParser2482 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred110_QueryParser2484 = frozenset([1])
    FOLLOW_flatten_clause_in_synpred112_QueryParser2468 = frozenset([1, 26])
    FOLLOW_AS_in_synpred112_QueryParser2472 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_synpred112_QueryParser2479 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred112_QueryParser2482 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred112_QueryParser2484 = frozenset([1])
    FOLLOW_field_def_in_synpred112_QueryParser2491 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred113_QueryParser2534 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred113_QueryParser2537 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred113_QueryParser2539 = frozenset([1])
    FOLLOW_col_range_in_synpred115_QueryParser2523 = frozenset([1, 26])
    FOLLOW_AS_in_synpred115_QueryParser2527 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_LEFT_PAREN_in_synpred115_QueryParser2534 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred115_QueryParser2537 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred115_QueryParser2539 = frozenset([1])
    FOLLOW_field_def_in_synpred115_QueryParser2546 = frozenset([1])
    FOLLOW_expr_in_synpred117_QueryParser2578 = frozenset([1, 26])
    FOLLOW_AS_in_synpred117_QueryParser2582 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_in_synpred117_QueryParser2585 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred118_QueryParser2626 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_field_def_list_in_synpred118_QueryParser2629 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred118_QueryParser2631 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred123_QueryParser2763 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_cond_in_synpred123_QueryParser2766 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred123_QueryParser2768 = frozenset([1])
    FOLLOW_not_cond_in_synpred124_QueryParser2784 = frozenset([1])
    FOLLOW_expr_in_synpred125_QueryParser2799 = frozenset([70, 71, 72, 73, 74, 75, 76, 79, 80, 81, 82, 83, 84])
    FOLLOW_rel_op_in_synpred125_QueryParser2801 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_synpred125_QueryParser2804 = frozenset([1])
    FOLLOW_func_eval_in_synpred126_QueryParser2819 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred137_QueryParser3032 = frozenset([42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 90, 110, 112, 114])
    FOLLOW_type_cast_in_synpred137_QueryParser3034 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred137_QueryParser3036 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_unary_expr_in_synpred137_QueryParser3038 = frozenset([1])
    FOLLOW_expr_eval_in_synpred144_QueryParser3198 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred145_QueryParser3214 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_synpred145_QueryParser3216 = frozenset([111])
    FOLLOW_RIGHT_PAREN_in_synpred145_QueryParser3218 = frozenset([1])
    FOLLOW_const_expr_in_synpred146_QueryParser3262 = frozenset([1])
    FOLLOW_func_eval_in_synpred149_QueryParser3294 = frozenset([1])
    FOLLOW_col_ref_in_synpred150_QueryParser3298 = frozenset([1])
    FOLLOW_bin_expr_in_synpred151_QueryParser3302 = frozenset([1])
    FOLLOW_INTEGER_in_synpred163_QueryParser3777 = frozenset([109])
    FOLLOW_SEMI_COLON_in_synpred163_QueryParser3779 = frozenset([1])
    FOLLOW_LONGINTEGER_in_synpred164_QueryParser3789 = frozenset([109])
    FOLLOW_SEMI_COLON_in_synpred164_QueryParser3791 = frozenset([1])
    FOLLOW_DOUBLENUMBER_in_synpred165_QueryParser3819 = frozenset([109])
    FOLLOW_SEMI_COLON_in_synpred165_QueryParser3821 = frozenset([1])
    FOLLOW_join_item_in_synpred198_QueryParser4275 = frozenset([67, 68, 69])
    FOLLOW_set_in_synpred198_QueryParser4277 = frozenset([30, 118])
    FOLLOW_OUTER_in_synpred198_QueryParser4291 = frozenset([118])
    FOLLOW_COMMA_in_synpred198_QueryParser4294 = frozenset([90, 110])
    FOLLOW_join_item_in_synpred198_QueryParser4297 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_synpred201_QueryParser4390 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_join_group_by_expr_in_synpred201_QueryParser4392 = frozenset([111, 118])
    FOLLOW_COMMA_in_synpred201_QueryParser4396 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 104, 110, 112, 114, 119, 162, 163])
    FOLLOW_join_group_by_expr_in_synpred201_QueryParser4398 = frozenset([111, 118])
    FOLLOW_RIGHT_PAREN_in_synpred201_QueryParser4403 = frozenset([1])
    FOLLOW_nested_command_in_synpred212_QueryParser4844 = frozenset([109])
    FOLLOW_SEMI_COLON_in_synpred212_QueryParser4846 = frozenset([1, 90])
    FOLLOW_identifier_in_synpred213_QueryParser4906 = frozenset([117])
    FOLLOW_EQUAL_in_synpred213_QueryParser4908 = frozenset([14, 34, 90, 96])
    FOLLOW_col_ref_in_synpred213_QueryParser4910 = frozenset([92])
    FOLLOW_PERIOD_in_synpred213_QueryParser4912 = frozenset([14, 34, 90, 96, 110])
    FOLLOW_col_ref_list_in_synpred213_QueryParser4914 = frozenset([1])
    FOLLOW_identifier_in_synpred214_QueryParser4975 = frozenset([117])
    FOLLOW_EQUAL_in_synpred214_QueryParser4977 = frozenset([5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 90, 91, 94, 96, 97, 99, 100, 101, 110, 112, 114, 162, 163])
    FOLLOW_expr_in_synpred214_QueryParser4979 = frozenset([1])
    FOLLOW_INTEGER_in_synpred223_QueryParser5294 = frozenset([109])
    FOLLOW_SEMI_COLON_in_synpred223_QueryParser5296 = frozenset([1])
    FOLLOW_COMMA_in_synpred231_QueryParser5457 = frozenset([90])
    FOLLOW_split_branch_in_synpred231_QueryParser5459 = frozenset([1, 118])
    FOLLOW_identifier_in_synpred315_QueryParser6428 = frozenset([1])
    FOLLOW_null_keyword_in_synpred316_QueryParser6436 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("QueryParserLexer", QueryParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
