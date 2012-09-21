from sau_parser import parse, lexer

class SauProcessor(object):
    def __init__(self):
        self.lexer = lexer()

    def execute(self, line):
        bla = parse(line, self.lexer)
        print "tokenized %s" % bla
