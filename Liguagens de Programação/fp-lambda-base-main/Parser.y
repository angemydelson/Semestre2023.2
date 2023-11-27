{
module Parser where

import Lexer 
}

%name parser 
%tokentype { Token }
%error { parserError } 

%left '+'

%token 
    num         { TokenNum $$ }
    '+'         { TokenAdd }
    "&&"        { TokenAnd }
    true        { TokenTrue }
    false       { TokenFalse }
    if          { TokenIf }
    then        { TokenThen }
    else        { TokenElse }
    var         { TokenVar $$ }
    '\\'        { TokenLam }
    "->"        { TokenArrow }
    '('         { TokenLParen }
    ')'         { TokenRParen }

%%

Exp         : num                       { Num $1 }
            | true                      { BTrue }
            | false                     { BFalse }
            | Exp '+' Exp               { Add $1 $3 }
            | Exp "&&" Exp              { And $1 $3 }
            | if Exp then Exp else Exp  { If $2 $4 $6 }
            | var                       { Var $1 }
            | '\\' var "->" Exp         { Lam $2 $4 }
            | Exp Exp                   { App $1 $2 }
            | '(' Exp ')'               { Paren $2 }

{

parserError :: [Token] -> a 
parserError _ = error "Syntax error!"

}
