module D where
calculTotalEnergia :: Float -> Float -> Float
calculTotalEnergia salario energia = preco * energia
    where 
        preco = salario * (1 / 5)