import java.util.HashMap;
import java.util.Map;

public class EvalVisitor extends LabeledExprBaseVisitor<Double> {

    Map<String, Double> memory = new HashMap<>();

    @Override
    public Double visitAssign(LabeledExprParser.AssignContext ctx) {
        String id = ctx.ID().getText();  
        double value = visit(ctx.expr());   
        memory.put(id, value);
        return value;
    }

    @Override
    public Double visitPrintExpr(LabeledExprParser.PrintExprContext ctx) {
        Double value = visit(ctx.expr()); 
        System.out.println(value);        
        return 0.0;                          
    }

    @Override
    public Double visitInt(LabeledExprParser.IntContext ctx) {
        return Double.valueOf(ctx.INT().getText());
    }

    @Override
    public Double visitId(LabeledExprParser.IdContext ctx) {
        String id = ctx.ID().getText();
        if (memory.containsKey(id)) return memory.get(id);
        return 0.0;
    }

    @Override
    public Double visitMulDiv(LabeledExprParser.MulDivContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == LabeledExprParser.MUL) return left * right;
        return left / right;
    }

    @Override
    public Double visitAddSub(LabeledExprParser.AddSubContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == LabeledExprParser.ADD) return left + right;
        return left - right;
    }

    @Override
    public Double visitParens(LabeledExprParser.ParensContext ctx) {
        return visit(ctx.expr()); 
    }

    // ===============================
    // Funciones matemáticas extendidas
    // ===============================

    @Override
    public Double visitSinFunc(LabeledExprParser.SinFuncContext ctx) {
        return Math.sin(Math.toRadians(visit(ctx.expr())));
    }

    @Override
    public Double visitCosFunc(LabeledExprParser.CosFuncContext ctx) {
        return Math.cos(Math.toRadians(visit(ctx.expr())));
    }

    @Override
    public Double visitTanFunc(LabeledExprParser.TanFuncContext ctx) {
        return Math.tan(Math.toRadians(visit(ctx.expr())));
    }

    @Override
    public Double visitSqrtFunc(LabeledExprParser.SqrtFuncContext ctx) {
        return Math.sqrt(visit(ctx.expr()));
    }

    @Override
    public Double visitLnFunc(LabeledExprParser.LnFuncContext ctx) {
        return Math.log(visit(ctx.expr()));
    }

    @Override
    public Double visitLogFunc(LabeledExprParser.LogFuncContext ctx) {
        return Math.log10(visit(ctx.expr()));
    }

    @Override
    public Double visitFactorial(LabeledExprParser.FactorialContext ctx) {
        int n = (int)Math.round(visit(ctx.expr()));
        double fact = 1;
        for (int i = 2; i <= n; i++) fact *= i;
        return fact;
    }
}

