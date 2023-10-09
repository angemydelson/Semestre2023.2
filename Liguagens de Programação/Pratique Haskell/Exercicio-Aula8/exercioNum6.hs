-- Função para calcular o salário atual
salarioAtual :: Double -> Int -> Int -> Double
salarioAtual salarioInicial anoContratacao anoAtual = calculaSalario salarioInicial anoContratacao anoAtual 1.015

-- Função auxiliar para calcular o salário com base no ano
calculaSalario :: Double -> Int -> Int -> Double -> Double
calculaSalario salario anoContratacao anoAtual percentualAumento
  | anoContratacao > anoAtual = salario -- Não houve aumento até o ano atual
  | anoContratacao == anoAtual = salario * percentualAumento -- Primeiro aumento
  | otherwise = calculaSalario (salario * percentualAumento) (anoContratacao + 1) anoAtual (percentualAumento * 2)

main :: IO ()
main = do
  putStrLn "Informe o salário inicial do funcionário: "
  salarioInicialStr <- getLine
  let salarioInicial = read salarioInicialStr :: Double

  putStrLn "Informe o ano de contratação do funcionário: "
  anoContratacaoStr <- getLine
  let anoContratacao = read anoContratacaoStr :: Int

  putStrLn "Informe o ano atual: "
  anoAtualStr <- getLine
  let anoAtual = read anoAtualStr :: Int

  let salario = salarioAtual salarioInicial anoContratacao anoAtual
  putStrLn $ "O salário atual do funcionário é: " ++ show salario
