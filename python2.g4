grammar python2;

// parser rules

top: (funcdef | vardec | funccall)+ EOF;
funcdef: DEF ID OPEN_PR params? CLOSE_PR COLON body;
params: ID (',' ID)*; 
funccall: ID OPEN_PR exprList? CLOSE_PR;
body: expand_body*;
expand_body: vardec | 'if' expr COLON expr 'else' COLON expr 
	     | expr '=' expr 
	     | funccall | RETURN expr ; //function call
vardec: ID ('=' expr)? ;  
expr:   ID OPEN_PR exprList? CLOSE_PR    
    |   expr '[' expr ']'              
    |   '-' expr                       
    |   '!' expr
    |   expr '>' expr | expr '<' expr | expr '>=' expr | expr '<=' expr
    |   expr '*' expr                  
    |   expr ('+'|'-') expr            
    |   expr '==' expr                 
    |   ID            
    |   NUMBER                 
    |   '(' expr ')'            
    |   RETURN expr
    ;

exprList : expr (',' expr)* ;   // argument list


// lexer rules

DEF: 'def';
RETURN: 'return';
INDENT: '\t';
COLON: ':';
OPEN_PR: '(';
CLOSE_PR: ')';
ID: NAME (NAME | [0-9])*;
NAME : [a-zA-Z] ;
NUMBER: [0-9]+;
WS : [ \n\r]+ -> skip ; // skip spaces, tabs, newlines
COMMENT: '#'+ -> skip ;


