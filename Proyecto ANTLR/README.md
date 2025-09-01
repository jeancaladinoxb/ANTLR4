## Proyecto ANTLR – Calculadora con Funciones

Este proyecto implementa una calculadora interactiva capaz de reconocer expresiones aritméticas y algunas funciones matemáticas (seno, coseno, tangente, logaritmos, raíz cuadrada, factorial, etc.) utilizando ANTLR4.

El proyecto está basado en el libro "The Definitive ANTLR 4 Reference" de Terence Parr, creador de ANTLR. La idea principal es mostrar cómo un lenguaje pequeño (en este caso, expresiones matemáticas) puede definirse con una gramática y ejecutarse mediante el patrón Visitor.

## Características

Operaciones básicas: +, -, *, /

Uso de paréntesis ( )

Variables con asignación:

x = 10
x * 3


Funciones matemáticas:

sin(expr)

cos(expr)

tan(expr)

sqrt(expr)

ln(expr)

log(expr)

expr! (factorial)

## Requisitos

Java 11 o superior

Python 3.8 o superior

ANTLR4 instalado en el sistema:

sudo apt install antlr4


Runtime de ANTLR para Python:

pip3 install antlr4-python3-runtime --user

## Ejecución en Java

Generar el lexer y parser:

antlr4 -visitor LabeledExpr.g4
javac *.java


Ejecutar en modo interactivo:

java Main


Ejemplo:

x = 10
x * 3
(5+2)*2


Ejecutar usando un archivo con expresiones:

java Main < input.txt

## Ejecución en Python

Generar el lexer y parser para Python:

antlr4 -Dlanguage=Python3 -visitor LabeledExpr.g4


Ejecutar el programa:

python3 main.py input.txt


Donde input.txt contiene las expresiones, por ejemplo:

2 + 3
5!
sqrt(16)
sin(3.1416/2)