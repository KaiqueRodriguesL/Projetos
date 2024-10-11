-- Tabela Alunos
CREATE TABLE Alunos (
    id_aluno INT PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    cidade VARCHAR(50)
);
 insert into Alunos (id_aluno, nome, data_nascimento, cidade)
 VALUES
 (1, 'Alice', '2000-08-30', 'Mogi das Cruzes'),
 (2, 'Marcos', '1990-05-29', 'Suzano'),
 (3, 'Jose', '1970-09-22', 'Poa'),
 (4, 'Ana', '2005-05-02', 'Aruja'),
 (5, 'Joao', '2010-02-16', 'Itaquaquecetuba');
 
 select * from Alunos;
-- Tabela Disciplinas
CREATE TABLE Disciplinas (
    id_disciplina INT PRIMARY KEY,
    nome_disciplina VARCHAR(100)
);
 insert into Disciplinas (id_disciplina, nome_disciplina)
 VALUES
 (1, 'Artes'),
 (2, 'Matematica'),
 (3, 'Historia'),
 (4, 'Geografia'),
 (5, 'Ciencias');
 
-- Tabela Notas
CREATE TABLE Notas (
    id_nota INT PRIMARY KEY,
    id_aluno INT,
    id_disciplina INT,
    nota DECIMAL(5,2),
    data_avaliacao DATE,
    FOREIGN KEY (id_aluno) REFERENCES Alunos(id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES Disciplinas (id_disciplina)
);
 INSERT INTO Notas (id_nota, id_aluno, id_disciplina, nota, data_avaliacao)
 VALUES
 (1, 1, 1, 10.0, '2024-05-02'),
 (2, 2, 2, 9.9, '2024-05-02' ),
 (3, 3, 3, 4.1, '2024-05-02'),
 (4, 4, 4, 7.5, '2024-05-02'),
 (5, 5, 5, 5.5, '2024-05-02');
 
 drop table Notas;
 select * from Notas;
 
 -- exe2--
 alter table Alunos add telefone varchar(15);

-- exe3-- 
ALTER TABLE Alunos MODIFY cidade VARCHAR(100); 
-- exe4--
ALTER TABLE Alunos DROP COLUMN cidade;

-- exe5--
SELECT nome, data_nascimento FROM Alunos;

-- exe6--
SELECT * FROM Notas WHERE nota >= 7;

-- exe7--
SELECT * FROM Notas WHERE id_disciplina = 2 ;
-- exe8--
SELECT * FROM Alunos WHERE data_nascimento > '2000-01-01';
-- exe9--
SELECT * FROM Notas n, Alunos a WHERE n.id_aluno = a.id_aluno AND (n.nota < 5 OR a.data_nascimento < '1990-01-01' );
-- exe10--
SELECT * FROM Notas WHERE id_disciplina IN (1,3,5);
-- exe11--
SELECT * FROM Notas WHERE nota BETWEEN 7 AND 10;
-- exe12--
UPDATE Disciplinas SET nome_disciplina = 'Matematica Avançada' WHERE nome_disciplina = 'Matematica';
-- exe13--
UPDATE Notas SET nota = (nota+0.5) WHERE nota < 6;
-- exe14--
DELETE FROM Notas WHERE nota < 4;
-- exe15--
DELETE FROM Alunos WHERE data_nascimento <'1990-01-01';
-- exe16--
SELECT * FROM Alunos a, Disciplinas d, Notas n WHERE a.id_aluno = n.id_aluno AND d.id_disciplina = n.id_disciplina;
-- exe17--
SELECT count(id_aluno) FROM Alunos;
-- exe18--
SELECT * FROM Notas WHERE nota >6;
-- exe19--
SELECT d.nome_disciplina, count(a.id_aluno) FROM Alunos a, Disciplinas d, Notas n WHERE a.id_aluno = n.id_aluno AND d.id_disciplina = n.id_disciplina group by a.id_aluno;
-- exe20--
SELECT avg(nota) FROM Notas;