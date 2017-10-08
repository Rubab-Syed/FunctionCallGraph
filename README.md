This assignment is a simple implementation of making function call flow. I have used Antlr4 as my parser generator and Python as my source language. It looks at the file according to my given lexer and parser rules. Parses function definitions and detect function calls and as a result generate a dot file which can be viewed using graphviz. I have written grammar for Python2 which can be seen in "python2.g4". It is compiled using:

Testing:

I have provided a file which extends listener class and does the required job of parsing tree and making call graph. It is "FCG.py". Also, there's a input file "test.py" for testing my parser. It contains some random functions. Enclosed in the folder contains the dot file "output.dot" and output.png containing the directed graph.

> python FCG.py test.py 

Note: Python's version used is 2.7.


