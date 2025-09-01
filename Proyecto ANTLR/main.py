import sys
from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from EvalVisitor import EvalVisitor

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1], encoding="utf-8")
    else:
        input_stream = InputStream(sys.stdin.read())
    lexer = LabeledExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
