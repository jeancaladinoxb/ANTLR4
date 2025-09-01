from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser
import math

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitId(self, ctx):
        id_ = ctx.ID().getText()
        return self.memory.get(id_, 0)

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        else:
            return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        else:
            return left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitSinFunc(self, ctx):
        return math.sin(self.visit(ctx.expr()))

    def visitCosFunc(self, ctx):
        return math.cos(self.visit(ctx.expr()))

    def visitTanFunc(self, ctx):
        return math.tan(self.visit(ctx.expr()))

    def visitSqrtFunc(self, ctx):
        return math.sqrt(self.visit(ctx.expr()))

    def visitLnFunc(self, ctx):
        return math.log(self.visit(ctx.expr()))

    def visitLogFunc(self, ctx):
        return math.log10(self.visit(ctx.expr()))

    def visitFactorial(self, ctx):
        return math.factorial(self.visit(ctx.expr()))
