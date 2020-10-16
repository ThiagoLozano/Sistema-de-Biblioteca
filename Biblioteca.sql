-- Cria o Banco de Dados.
CREATE DATABASE IF NOT EXISTS Biblioteca;
USE Biblioteca;

-- Tabela de Login do Admintrador.
CREATE TABLE IF NOT EXISTS Login_adm(
id INT AUTO_INCREMENT,
nome CHAR(3) NOT NULL,
senha CHAR(8) NOT NULL,
PRIMARY KEY(id)
);

-- Tabela para registras Livros.
CREATE TABLE IF NOT EXISTS Livros(
id INT AUTO_INCREMENT,
id_livro INT NOT NULL UNIQUE,
nome_livro VARCHAR(100) NOT NULL,
autor VARCHAR(100) NOT NULL,
genero VARCHAR(50) NOT NULL,
paginas INT,
data_publicacao DATE NOT NULL,
quant_disponivel INT NOT NULL,
quant_uso INT NOT NULL,
PRIMARY KEY(id)
);

-- Tabela para registrar Clientes.
CREATE TABLE IF NOT EXISTS Clientes(
id INT AUTO_INCREMENT,
id_cliente INT NOT NULL,
nome VARCHAR(50) NOT NULL,
sobrenome VARCHAR(50) NOT NULL,
data_nasc DATE NOT NULL,
sexo CHAR(1) NOT NULL,
PRIMARY KEY(id)
);

-- Tabela para registrar Emprestimo de Livro.
CREATE TABLE IF NOT EXISTS Emprestimo(
id INT AUTO_INCREMENT, 
id_cliente INT NOT NULL,
id_livro INT NOT NULL,
data_pegou DATE NOT NULL,
data_entrega DATE NOT NULL,
status_entrega INT NOT NULL,
PRIMARY KEY(id)
);

-- Tabela para mostrar o Status de Devolução.
CREATE TABLE IF NOT EXISTS `Status`(
id INT AUTO_INCREMENT,
status_entrega VARCHAR(13) NOT NULL UNIQUE,
PRIMARY KEY(id)
);

-- Insere e mostra os valores da tabela 'login_adm';
INSERT INTO login_adm VALUES(DEFAULT, 'ADM','12345678');
SELECT * FROM login_adm;

-- Insere e mostra os valores da tabela 'Livros';
INSERT INTO Livros VALUES(DEFAULT, 1234, 'Livro ABCD','Autor ABCDEF', 'Educacional', 111, CURDATE(), 10, 0);
SELECT * FROM Livros;

-- Insere e mostra os valores da tabela 'Clientes';
INSERT INTO Clientes VALUES(DEFAULT, 1122, 'Nome_Cliente', 'Sobrenome_Cliente', '2000-10-10', 'M');
SELECT * FROM Clientes;

-- Insere e mostra os valores da tabela 'status';
INSERT INTO `status` VALUES (DEFAULT, 'Não Devolvido'), (DEFAULT, 'Devolvido');

-- Mostra a junção da tabela 'Emprestimo' com a tabela 'Status';
SELECT Emprestimo.id_cliente, emprestimo.id_livro, emprestimo.data_pegou, emprestimo.data_entrega, Status.status_entrega FROM Emprestimo
INNER JOIN `Status`
ON `Status`.id = Emprestimo.status_entrega;
