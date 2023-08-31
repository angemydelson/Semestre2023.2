1  Listar os empregados (nomes) que tem salário maior que seu chefe (usar o join)



--  empregado | 
-- -----------+
--  Maria     |
--  Claudia   |
--  Ana       |
--  Luiz      |

SELECT e1.nome AS empregado
FROM empregados e1
JOIN empregados e2 ON e1.supervisor_id = e2.emp_id
WHERE e1.salario > e2.salario;

Time1 = 1776,500 ms
Time2 = 1761,369 ms
Time3 = 1758,856 ms

2 Listar o maior salario de cada departamento (usa o group by )

--  dep_id |  max  
-- --------+-------
--       1 | 10000
--       2 |  8000
--       3 |  6000
--       4 | 12200
SELECT dep_id, (
SELECT MAX(salario)
FROM empregados e2
WHERE e2.dep_id = e1.dep_id
) AS max
FROM empregados e1
GROUP BY dep_id;

Time1 = 10815,683 ms
Time2 = 11052,226 ms
Time3 = 11612,380 ms


3 Listar o dep_id, nome e o salario do funcionario com maior salario dentro de cada departamento (usar o with)
--  dep_id |  nome   | salario 
-- --------+---------+---------
--       3 | Joao    |    6000
--       1 | Claudia |   10000
--       4 | Ana     |   12200
--       2 | Luiz    |    8000
WITH FuncionarioMaiorSalario AS (
SELECT dep_id,
MAX(salario) AS max_salario
FROM empregados
GROUP BY dep_id
)
SELECT e.dep_id, e.nome, e.salario
FROM empregados e
JOIN FuncionarioMaiorSalario fms ON e.dep_id = fms.dep_id AND e.salario = fms.max_salario;

Time1 = 1076,476 ms
Time2 = 1075,344 ms
Time3 = 1078,332 ms


4 Listar os nomes departamentos que tem menos de 3 empregados;

--    nome    
-- -----------
--  Marketing
--  RH
--  Vendas
SELECT nome
FROM departamentos
WHERE dep_id IN (
SELECT dep_id
FROM empregados
GROUP BY dep_id
HAVING COUNT(emp_id) < 3
);

Time1 = 454,721 ms
Time2 = 448,429 ms
Time3 = 444,930 ms

5 Listar os departamentos  com o número de colaboradores

    
--    nome    | count 
-- -----------+-------
--  Marketing |     1
--  RH        |     2
--  TI        |     4
--  Vendas    |     1

WITH ColaboradoresPorDepartamento AS (
SELECT d.nome AS nome_departamento, COUNT(e.emp_id) AS count
FROM departamentos d
LEFT JOIN empregados e ON d.dep_id = e.dep_id
GROUP BY d.nome
)
SELECT nome_departamento, count
FROM ColaboradoresPorDepartamento;

Time1 = 1934,969 ms
Time2 = 1916,680 ms
Time3 = 1936,206 ms

6 Listar os empregados que não possue o seu  chefe no mesmo departamento/ 

--  nome | dep_id 
-- ------+--------
--  Joao |      3
--  Ana  |      4

SELECT e.nome, e.dep_id
FROM empregados e
WHERE NOT EXISTS (
SELECT 1
FROM empregados chefe
WHERE e.supervisor_id = chefe.emp_id AND e.dep_id = chefe.dep_id
);

Time1 = 2461,544 ms
Time2 = 2308,379 ms
Time3 = 2399,933 ms

7 Listar os nomes dos  departamentos com o total de salários pagos (sliding windows function)

--   sum  |   nome    
-- -------+-----------
--   6000 | Vendas
--  12200 | Marketing
--  15500 | RH
--  32500 | TI

SELECT SUM(salario) OVER (PARTITION BY d.nome) AS sum, d.nome
FROM empregados e
JOIN departamentos d ON e.dep_id = d.dep_id
GROUP BY d.nome, d.dep_id, e.salario
ORDER BY d.dep_id;

Time1 = 852,806 ms
Time2 = 836,382 ms
Time3 = 844,238 ms


8 Listar os nomes dos colaboradores com salario maior que a média do seu departamento (dica: usar subconsultas);

--   Nome   | Salário 
-- ---------+---------
--  Maria   |    9500
--  Claudia |   10000
--  Luiz    |    8000
SELECT e.nome, e.salario
FROM empregados e
WHERE e.salario > (
SELECT AVG(salario)
FROM empregados e2
WHERE e2.dep_id = e.dep_id
);

Time1 = + que 208823,153 ms
Time2 = + que 208823,153 ms
Time3 = + que 208823,153 ms

 9  Faça uma consulta capaz de listar os dep_id, nome, salario, e as médias de cada departamento utilizando o windows function;

--  dep_id |   nome    | salario |  avg  
-- --------+-----------+---------+-------
--       1 | Jose      |    8000 |  8125
--       1 | Claudia   |   10000 |  8125
--       1 | Guilherme |    5000 |  8125
--       1 | Maria     |    9500 |  8125
--       2 | Luiz      |    8000 |  7750
--       2 | Pedro     |    7500 |  7750
--       3 | Joao      |    6000 |  6000
--       4 | Ana       |   12200 | 12200

SELECT dep_id, nome, salario,
AVG(salario) OVER (PARTITION BY dep_id) AS avg
FROM empregados;

Time1 = 5551,790 ms
Time2 = 5730,328 ms
Time3 = 5591,703 ms

10 - Encontre os empregados com salario maior ou igual a média do seu departamento. Deve ser reportado o salario do empregado e a média do departamento (dica: usar window function com subconsulta)

--   nome   | salario | dep_id |       avg_salary       
-- ---------+---------+--------+------------------------
--  Claudia |   10000 |      1 |  8125.0000000000000000
--  Maria   |    9500 |      1 |  8125.0000000000000000
--  Luiz    |    8000 |      2 |  7750.0000000000000000
--  Joao    |    6000 |      3 |  6000.0000000000000000
--  Ana     |   12200 |      4 | 12200.

WITH MediaPorDepartamento AS (
SELECT dep_id, AVG(salario) AS avg_salary
FROM empregados
GROUP BY dep_id
)
SELECT e.nome, e.salario, e.dep_id, m.avg_salary
FROM empregados e
JOIN MediaPorDepartamento m ON e.dep_id = m.dep_id
WHERE e.salario >= m.avg_salary;

Time1 = 3364,820 ms
Time2 = 3372,964 ms
Time3 = 3354,146 ms
