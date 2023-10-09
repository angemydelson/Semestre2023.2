import A
import B
import C
import D

main :: IO()
main = do 
    num1 <- readLn
    num2 <- readLn
    num3 <- readLn
    putStrLn ("A media das notas eh: " ++ show(mediaAluno num1 num2 num3))
    putStrLn (show(dobro 2))
    putStrLn (show(quadradoDobro 2))

   