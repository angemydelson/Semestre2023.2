module Interpreter where

import Lexer

step :: Expr -> Expr
step (Add (Num n1)(Num n2)) = Num (n1 + n2)
step (Add (Num n) e) = Add (Num n) (step e)
step (Add e1 e2) = Add (step e1) e2
step (And BFalse_) = BFalse
step (And BTrue e) = e
step (And e1 e2) = And (step e1) e2