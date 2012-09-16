#!/bin/sh

cd g
mv ../lib/sau/QueryParser.py ../lib/sau/QueryParser.py.bk
mv ../lib/sau/QueryLexder.py ../lib/sau/QueryLexer.py.bk
java -jar /Users/pb/opt/antlr/antlr.jar -o ../lib/sau QueryLexer.g QueryParser.g
