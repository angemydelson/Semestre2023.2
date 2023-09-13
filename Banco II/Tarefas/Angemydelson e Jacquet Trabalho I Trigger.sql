-- Jacquet Leme && Angemydelson saint Bert


--1- Armazenar o histórico de alterações dos salários. Ou seja, deve ser criado uma tabela adicional para armazenar o usuário que fez a alteração, data, salário antigo e o novo salário.

CREATE TABLE empregados (
 emp_id int NOT NULL,
 dep_id int DEFAULT NULL,
 supervisor_id int DEFAULT NULL,
 nome varchar(255) DEFAULT NULL,
 salario int DEFAULT NULL
);

CREATE TABLE departamentos (
 dep_id int NOT NULL ,
 nome varchar(255) DEFAULT NULL
);



-- Criação da tabela para o histórico de salários
CREATE TABLE historico_salario (
    emp_id int,
    alterado_por varchar(255),
    data_alteracao timestamp,
    salario_antigo int,
    novo_salario int
);

-- Criação da função de gatilho
CREATE OR REPLACE FUNCTION f_alteracao_salario()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salario <> OLD.salario THEN
        INSERT INTO historico_salario (emp_id, alterado_por, data_alteracao, salario_antigo, novo_salario)
        VALUES (OLD.emp_id, CURRENT_USER, NOW(), OLD.salario, NEW.salario);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associação do gatilho à tabela empregados
CREATE TRIGGER t_alteracao_salario
BEFORE UPDATE ON empregados
FOR EACH ROW
EXECUTE FUNCTION f_alteracao_salario();



--#2- Armazenar o histórico de alterações do departamento. 
-- Criação da tabela para o histórico de departamentos
CREATE TABLE historico_departamento (
    emp_id int,
    alterado_por varchar(255),
    data_alteracao timestamp,
    departamento_antigo int,
    novo_departamento int
);

-- Criação da função de gatilho
CREATE OR REPLACE FUNCTION f_alteracao_departamento()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.dep_id <> OLD.dep_id THEN
        INSERT INTO historico_departamento (emp_id, alterado_por, data_alteracao, departamento_antigo, novo_departamento)
        VALUES (OLD.emp_id, CURRENT_USER, NOW(), OLD.dep_id, NEW.dep_id);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associação do gatilho à tabela empregados
CREATE TRIGGER t_alteracao_departamento
BEFORE UPDATE ON empregados
FOR EACH ROW
EXECUTE FUNCTION f_alteracao_departamento();

-- Criação da função de gatilho de verificação
CREATE OR REPLACE FUNCTION verificar_salario_chefe()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salario > (SELECT salario FROM empregados WHERE emp_id = NEW.supervisor_id) THEN
        RAISE EXCEPTION 'O salário não pode ser maior do que o salário do chefe';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associação do gatilho à tabela empregados para INSERT e UPDATE
CREATE TRIGGER t_salario_chefe
BEFORE INSERT OR UPDATE ON empregados
FOR EACH ROW
EXECUTE FUNCTION verificar_salario_chefe();


--#3- Evite a inserção ou atualização de um salário do  empregado que seja maior do que seu chefe. 

-- Criação da função de gatilho de verificação de salário
CREATE OR REPLACE FUNCTION f_salario_chefe()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.salario > (SELECT salario FROM empregados WHERE emp_id = NEW.supervisor_id) THEN
        RAISE EXCEPTION 'O salário não pode ser maior do que o salário do chefe';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associação do gatilho à tabela empregados para INSERT e UPDATE
CREATE TRIGGER t_salario_chefe
BEFORE INSERT OR UPDATE ON empregados
FOR EACH ROW
EXECUTE FUNCTION f_salario_chefe();



--4)-- Criação da função de gatilho para atualização do total de salário do departamento

CREATE OR REPLACE FUNCTION f_salario_departamento()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' OR (TG_OP = 'UPDATE' AND NEW.salario <> OLD.salario) THEN
        UPDATE departamentos
        SET total_salary = (
            SELECT SUM(salario) FROM empregados WHERE dep_id = NEW.dep_id
        )
        WHERE dep_id = NEW.dep_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associação do gatilho à tabela empregados para INSERT e UPDATE
CREATE TRIGGER t_total_salario_departamento
AFTER INSERT OR UPDATE ON empregados
FOR EACH ROW
EXECUTE FUNCTION f_salario_departamento();

