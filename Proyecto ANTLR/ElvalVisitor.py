import math
from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitId(self, ctx):
        id = ctx.ID().getText()
        return self.memory.get(id, 0)

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right if ctx.op.type == LabeledExprParser.MUL else left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right if ctx.op.type == LabeledExprParser.ADD else left - right

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    # Funciones matemáticas
    def visitSinFunc(self, ctx):
        return math.sin(math.radians(self.visit(ctx.expr())))

    def visitCosFunc(self, ctx):
        return math.cos(math.radians(self.visit(ctx.expr())))

    def visitTanFunc(self, ctx):
        return math.tan(math.radians(self.visit(ctx.expr())))

    def visitSqrtFunc(self, ctx):
        return math.sqrt(self.visit(ctx.expr()))

    def visitLnFunc(self, ctx):
        return math.log(self.visit(ctx.expr()))

    def visitLogFunc(self, ctx):
        return math.log10(self.visit(ctx.expr()))

    def visitFactorial(self, ctx):
        n = self.visit(ctx.expr())
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact
