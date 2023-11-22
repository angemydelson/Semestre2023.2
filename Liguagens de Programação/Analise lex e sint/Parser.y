{
module Parser where

import Lexer 
}

%name parser 
%tokentype { Token }
%error { parserError } 

%token 
    num         { TokenNum $$ }
    '+'         { TokenAdd }
    "&&"        { TokenAnd }
    true        { TokenTrue }
    false       { TokenFalse }
    if          { TokenIf }
    then        { TokenThen }
    else        { TokenElse }

%%

Exp         : num                       { Num $1 }
            | true                      { BTrue }
            | false                     { BFalse }
            | Exp '+' Exp               { Add $1 $3 }
            | Exp "&&" Exp              { And $1 $3 }
            | if Exp then Exp else Exp  { If $2 $4 $6 }

{

parserError :: [Token] -> a 
parserError _ = error "Syntax error!"

}
