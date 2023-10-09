-- Função para calcular o produto de duas listas
produtoDeListas :: Num a => [a] -> [a] -> [a]
produtoDeListas lista1 lista2 = zipWith (*) lista1 lista2

main :: IO ()
main = do
  putStrLn "Informe a primeira lista (números separados por espaço):"
  input1 <- getLine
  let lista1 = map read (words input1) :: [Double]

  putStrLn "Informe a segunda lista (números separados por espaço):"
  input2 <- getLine
  let lista2 = map read (words input2) :: [Double]

  let resultado = produtoDeListas lista1 lista2
  putStrLn $ "O produto das duas listas é: " ++ show resultado
