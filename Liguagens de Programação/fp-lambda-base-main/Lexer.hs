module Lexer where 

import Data.Char 

data Expr = BTrue
          | BFalse 
          | Num Int 
          | Add Expr Expr 
          | And Expr Expr 
          | If Expr Expr Expr 
          | Var String
          | Lam String Expr 
          | App Expr Expr
          | Paren Expr
          deriving Show

data Ty = TBool 
        | TNum 
        deriving (Show, Eq)

data Token = TokenTrue 
           | TokenFalse 
           | TokenNum Int 
           | TokenAdd
           | TokenAnd 
           | TokenIf 
           | TokenThen 
           | TokenElse
           | TokenVar String 
           | TokenLam
           | TokenArrow
           | TokenLParen
           | TokenRParen
           deriving (Show, Eq)

isSymb :: Char -> Bool 
isSymb c = c `elem` "+&\\->()"

lexer :: String -> [Token]
lexer [] = [] 
lexer ('(':cs) = TokenLParen : lexer cs
lexer (')':cs) = TokenRParen : lexer cs
lexer (c:cs) | isSpace c = lexer cs 
             | isDigit c = lexNum (c:cs)
             | isSymb c = lexSymbol (c:cs)
             | isAlpha c = lexKW (c:cs)
lexer _ = error "Lexical error!"

lexNum :: String -> [Token]
lexNum cs = case span isDigit cs of 
              (num, rest) -> TokenNum (read num) : lexer rest

lexSymbol :: String -> [Token]
lexSymbol cs = case span isSymb cs of 
                 ("+", rest)  -> TokenAdd : lexer rest 
                 ("&&", rest) -> TokenAnd : lexer rest 
                 ("\\", rest) -> TokenLam : lexer rest 
                 ("->", rest) -> TokenArrow : lexer rest 
                 _ -> error "Lexical error: invalid symbol!"

lexKW :: String -> [Token]
lexKW cs = case span isAlpha cs of 
             ("true", rest) -> TokenTrue : lexer rest 
             ("false", rest) -> TokenFalse : lexer rest
             ("if", rest) -> TokenIf : lexer rest 
             ("then", rest) -> TokenThen : lexer rest 
             ("else", rest) -> TokenElse : lexer rest 
             (var, rest) -> TokenVar var : lexer rest 
