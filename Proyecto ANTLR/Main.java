import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Leer entrada desde consola (System.in)
        CharStream input = CharStreams.fromStream(System.in);

        // Lexer
        LabeledExprLexer lexer = new LabeledExprLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // Parser
        LabeledExprParser parser = new LabeledExprParser(tokens);
        ParseTree tree = parser.prog(); // prog es la regla inicial

        // Visitor
        EvalVisitor eval = new EvalVisitor();
        eval.visit(tree);
    }
}
