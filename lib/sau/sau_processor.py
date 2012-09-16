from antlr3 import ANTLRStringStream
from antlr3 import CommonTokenStream
from antlr3 import tree
from QueryParser import QueryParser
from QueryLexer import QueryLexer

class SauProcessor(object):
    def execute(self, line):
        s = line.encode('utf8')

        stream = ANTLRStringStream(s)
        lexer = QueryLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = QueryParser(tokens)
        q = parser.query()
        
        print "aaaaa   %s" % q
