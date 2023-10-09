module Main where

import Prova

main :: IO ()
main = do
  putStrLn "Exemplo de Turma:"
  print exemplo

  putStrLn "\nMédias dos estudantes:"
  print (mediaAlunoTurma exemplo)

  putStrLn "\nMédia da Turma:"
  print (mediaTurma exemplo)

  putStrLn "\nEstudantes Aprovados:"
  print (obtemAprovados exemplo)

  let outraTurma = [ (6, "Lucas", (7.0, 8.0, 6.5))
                   , (7, "Carla", (8.0, 9.0, 7.5))
                   , (8, "Mariana", (6.0, 5.0, 7.0))
                   ]

  putStrLn "\nOutra Turma:"
  print outraTurma

  putStrLn "\nMaior Média entre duas Turmas:"
  print (maiorMedia exemplo outraTurma)

  putStrLn "\nMédias dos estudantes da outra Turma:"
  print (mediaAlunoTurma outraTurma)

  putStrLn "\nMédias dos estudantes individuais da outra Turma:"
  print (mediaEstudanteInd outraTurma)
