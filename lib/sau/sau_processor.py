from sau_parser import parse

class SauProcessor(object):
    def execute(self, cmd):
        print "parsing: %s" % cmd
        res = parse(cmd)
        print "tree: %s" % str(res)
