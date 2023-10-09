-- import prelude
-- module Teste where

-- soma :: Int -> Int -> Int
-- soma x y = x + y

-- (+++) :: Int -> Int -> Int
-- (+++) x y = x + y

-- areaCirculo r = pi * r^2
-- -- max' = 1000
-- teste x = if x >= 0 then 
--             "Numero Positivo"
--             else 
--             "Negativo"


-- -- vabs :: Int -> Int
-- -- vabs n | n >= 0 = n 
-- --         | ortherwise = 1

-- numero :: Int -> Int
-- numero a | a < 0 = -1
--          | a == 0 = 0
--          | ortherwise = 1

dobro :: Int -> Int
dobro n = dobro n * 4
main :: IO()
main = do
    -- putStrLn "Qual é o seu nome? "
    -- nome <- getLine
    -- putStrLn (nome ++ ", seja bem-vindo!")
    -- num1 <- readLn
    -- num2 <- readLn
    -- putStrLn (show (num1 + num2))
    putStrLn (show(dobro 2))