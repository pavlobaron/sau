from cmd2 import Cmd
from sau_processor import SauProcessor

class SauShell(Cmd):
    """Sau shell"""
    
    prompt = "oink> "
    intro = "Sau shell. Created by Pavlo Baron (pb@pbit.org)"
    doc_header = "Available commands (type 'help <command>' for help)"
    ruler = '-'
    misc_header = ""
    undoc_header = ""

    def __init__(self):
        Cmd.__init__(self)
        self.sau = SauProcessor()
    
    def do_version(self, line):
        print "Sau v0.1, sau shell v0.1"
    
    def help_version(self):
        print "Shows the version information"

    def help_q(self):
        print "Exit the shell"

    def help_quit(self):
        help_q()

    def help_exit(self):
        help_q()

    def help_eof(self):
        help_q()

    def help_EOF(self):
        help_q()

    def help_help(self):
        print "Prints the shell help"

    def default(self, line):
        self.sau.execute(line)
        return line

if __name__ == '__main__':
    SauShell().cmdloop()
