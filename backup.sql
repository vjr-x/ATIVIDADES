CREATE DATABASE empresa_db;
USE empresa_db;

CREATE TABLE `localidade` (
  `id_localidade` int NOT NULL AUTO_INCREMENT,
  `nome_localidade` varchar(30) NOT NULL,
  PRIMARY KEY (`id_localidade`),
  UNIQUE KEY `nome_localidade_UNIQUE` (`nome_localidade`)
);

CREATE TABLE `departamento` (
  `id_departamento` int NOT NULL AUTO_INCREMENT,
  `nome_departamento` varchar(30) NOT NULL,
  `id_localidade` int NOT NULL,
  PRIMARY KEY (`id_departamento`),
  UNIQUE KEY `nome_departamento_UNIQUE` (`nome_departamento`),
  KEY `fk_departamento_localidade` (`id_localidade`),
  CONSTRAINT `fk_departamento_localidade`
    FOREIGN KEY (`id_localidade`)
    REFERENCES `localidade` (`id_localidade`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

CREATE TABLE `empregado` (
  `cpf_empregado` char(14) NOT NULL,
  `nome_empregado` varchar(30) NOT NULL,
  `sobrenome_empregado` varchar(50) NOT NULL,
  `salario_empregado` decimal(7,2) NOT NULL,
  `data_nascimento_empregado` date NOT NULL,
  `data_contratacao_empregado` date NOT NULL,
  `genero_empregado` enum('MASCULINO','FEMININO','OUTROS') DEFAULT 'OUTROS',
  `id_departamento` int NOT NULL,
  `cpf_gerente` char(14) DEFAULT NULL,
  PRIMARY KEY (`cpf_empregado`),
  UNIQUE KEY `cpf_empregado_UNIQUE` (`cpf_empregado`),
  KEY `fk_empregado_departamento` (`id_departamento`),
  KEY `fk_empregado_gerente` (`cpf_gerente`),
  CONSTRAINT `fk_empregado_departamento`
    FOREIGN KEY (`id_departamento`)
    REFERENCES `departamento` (`id_departamento`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `fk_empregado_gerente`
    FOREIGN KEY (`cpf_gerente`)
    REFERENCES `empregado` (`cpf_empregado`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);

INSERT INTO `localidade` (`nome_localidade`) VALUES
('Florianópolis'),
('Joinville'),
('Blumenau'),
('Chapecó'),
('Criciuma'),
('Itajai'),
('Lages'),
('Jaragua do Sul'),
('Balneario Camboriu'),
('Sao Jose'),
('Brusque'),
('Tubarao'),
('Palhoca'),
('Rio do Sul'),
('Caçador'),
('Mafra'),
('Canoinhas'),
('Concórdia'),
('Ararangua'),
('Videira');

INSERT INTO `departamento`
(`nome_departamento`, `id_localidade`) VALUES
('Recursos Humanos', 1),
('Financeiro', 2),
('Tecnologia da Informacao', 3),
('Marketing', 4),
('Vendas', 5),
('Logistica', 6),
('Compras', 7),
('Jurídico', 8),
('Atendimento ao Cliente', 9),
('Producao', 10),
('Qualidade', 11),
('Pesquisa e Desenvolvimento', 12),
('Administracao', 13),
('Operacoes', 14),
('Planejamento', 15),
('Controladoria', 16),
('Auditoria', 17),
('Treinamento', 18),
('Seguranca do Trabalho', 19),
('Engenharia', 20),
('Suporte Tecnico', 1),
('Infraestrutura', 2),
('Banco de Dados', 3),
('Desenvolvimento', 4),
('UX Design', 5),
('Business Intelligence', 6),
('Comercial', 7),
('Exportacao', 8),
('Importacao', 9),
('Gestao de Projetos', 10);

INSERT INTO `empregado`
(`cpf_empregado`,
 `nome_empregado`,
 `sobrenome_empregado`,
 `salario_empregado`,
 `data_nascimento_empregado`,
 `data_contratacao_empregado`,
 `genero_empregado`,
 `id_departamento`,
 `cpf_gerente`)
VALUES

('123.456.789-01','Lucas','Silva',5500.00,'1988-05-12','2015-03-10','MASCULINO',1,NULL),
('987.654.321-00','Mariana','Oliveira',6200.00,'1990-07-20','2016-04-11','FEMININO',2,'123.456.789-01'),
('741.852.963-11','Carlos','Souza',7200.00,'1985-02-14','2012-01-15','MASCULINO',3,'123.456.789-01'),
('159.357.258-22','Fernanda','Costa',4800.00,'1993-11-30','2019-06-01','FEMININO',4,'987.654.321-00'),
('258.369.147-33','Ricardo','Pereira',5100.00,'1991-09-10','2018-08-20','MASCULINO',5,'987.654.321-00'),

('357.159.486-44','Patricia','Rodrigues',6800.00,'1987-04-25','2014-05-17','FEMININO',6,'741.852.963-11'),
('654.987.123-55','Bruno','Almeida',5300.00,'1992-12-02','2020-02-10','MASCULINO',7,'741.852.963-11'),
('852.741.369-66','Juliana','Martins',6100.00,'1989-08-15','2017-09-14','FEMININO',8,'123.456.789-01'),
('951.753.852-77','Eduardo','Lima',4500.00,'1995-01-21','2021-01-08','MASCULINO',9,'159.357.258-22'),
('753.951.456-88','Amanda','Gomes',7600.00,'1984-06-17','2010-10-10','FEMININO',10,'258.369.147-33'),

('321.654.987-99','Felipe','Ribeiro',5800.00,'1990-03-19','2016-12-12','MASCULINO',11,'258.369.147-33'),
('147.258.369-10','Camila','Fernandes',4900.00,'1994-07-28','2019-11-01','FEMININO',12,'357.159.486-44'),
('369.258.147-21','Rafael','Carvalho',6700.00,'1988-10-05','2013-04-07','MASCULINO',13,'357.159.486-44'),
('951.456.753-32','Larissa','Barbosa',5400.00,'1991-05-22','2017-08-18','FEMININO',14,'654.987.123-55'),
('852.963.741-43','Thiago','Rocha',7100.00,'1986-02-11','2011-06-30','MASCULINO',15,'654.987.123-55'),

('159.753.486-54','Aline','Dias',5200.00,'1993-09-09','2020-03-02','FEMININO',16,'852.741.369-66'),
('753.258.951-65','Gabriel','Teixeira',6000.00,'1989-12-25','2015-05-15','MASCULINO',17,'852.741.369-66'),
('456.123.789-76','Bianca','Moreira',4700.00,'1996-01-18','2021-07-19','FEMININO',18,'951.753.852-77'),
('654.321.987-87','Vinicius','Correia',6900.00,'1987-11-03','2014-02-25','MASCULINO',19,'951.753.852-77'),
('852.159.357-98','Natália','Melo',7400.00,'1985-08-08','2012-09-09','FEMININO',20,'753.951.456-88'),

('111.222.333-01','Leonardo','Nunes',5300.00,'1992-03-27','2018-01-20','MASCULINO',21,'753.951.456-88'),
('222.333.444-12','Priscila','Cardoso',5900.00,'1990-06-14','2016-05-16','FEMININO',22,'321.654.987-99'),
('333.444.555-23','André','Machado',6100.00,'1988-07-01','2015-10-11','MASCULINO',23,'321.654.987-99'),
('444.555.666-34','Renata','Araujo',5500.00,'1991-04-18','2017-07-07','FEMININO',24,'147.258.369-10'),
('555.666.777-45','Diego','Freitas',7200.00,'1986-09-09','2013-12-03','MASCULINO',25,'147.258.369-10'),

('666.777.888-56','Vanessa','Monteiro',5100.00,'1994-12-12','2020-09-01','FEMININO',26,'369.258.147-21'),
('777.888.999-67','Gustavo','Moura',6400.00,'1989-02-20','2014-08-08','MASCULINO',27,'369.258.147-21'),
('888.999.111-78','Tatiane','Cavalcante',5000.00,'1993-05-29','2019-04-14','FEMININO',28,'951.456.753-32'),
('999.111.222-89','Caio','Pinto',6800.00,'1987-01-30','2012-02-20','MASCULINO',29,'951.456.753-32'),
('101.202.303-90','Sabrina','Campos',5600.00,'1992-10-16','2018-11-22','FEMININO',30,'852.963.741-43'),

('202.303.404-91','Joao','Batista',4700.00,'1995-07-07','2021-03-03','MASCULINO',1,'852.963.741-43'),
('303.404.505-92','Elisa','Rezende',6200.00,'1988-06-06','2014-07-01','FEMININO',2,'159.753.486-54'),
('404.505.606-93','Mateus','Santana',7100.00,'1985-03-05','2010-01-12','MASCULINO',3,'159.753.486-54'),
('505.606.707-94','Roberta','Farias',5300.00,'1991-08-08','2017-02-09','FEMININO',4,'753.258.951-65'),
('606.707.808-95','Pedro','Vieira',5900.00,'1990-09-01','2016-06-06','MASCULINO',5,'753.258.951-65'),

('707.808.909-96','Claudia','Assis',6500.00,'1987-11-11','2013-03-13','FEMININO',6,'456.123.789-76'),
('808.909.101-97','Henrique','Queiroz',5100.00,'1993-04-14','2020-05-05','MASCULINO',7,'456.123.789-76'),
('909.101.202-98','Isabela','Peixoto',7000.00,'1986-12-24','2011-09-17','FEMININO',8,'654.321.987-87'),
('112.223.334-99','Murilo','Duarte',5400.00,'1992-01-13','2018-10-30','MASCULINO',9,'654.321.987-87'),
('223.334.445-00','Daniela','Tavares',7300.00,'1985-05-05','2010-11-25','FEMININO',10,'852.159.357-98'),

('334.445.556-11','Alex','Leite',4900.00,'1994-06-26','2021-02-15','MASCULINO',11,'852.159.357-98'),
('445.556.667-22','Paula','Borges',6600.00,'1988-09-19','2014-04-21','FEMININO',12,'111.222.333-01'),
('556.667.778-33','Igor','Mendes',5800.00,'1991-07-02','2017-08-08','MASCULINO',13,'111.222.333-01'),
('667.778.889-44','Cristina','Neves',5200.00,'1993-02-28','2019-12-12','FEMININO',14,'222.333.444-12'),
('778.889.990-55','Marcelo','Fonseca',6900.00,'1987-10-10','2013-07-07','MASCULINO',15,'222.333.444-12'),

('889.990.101-66','Helena','Macedo',6100.00,'1989-04-04','2015-05-19','FEMININO',16,'333.444.555-23'),
('990.101.212-77','Samuel','Rezende',5000.00,'1994-01-17','2020-08-24','MASCULINO',17,'333.444.555-23'),
('121.314.151-88','Beatriz','Lopes',7200.00,'1986-08-12','2012-06-18','FEMININO',18,'444.555.666-34'),
('131.415.161-99','Otavio','Sales',5500.00,'1992-05-03','2018-03-01','MASCULINO',19,'444.555.666-34'),
('141.516.171-10','Carolina','Alves',7600.00,'1985-12-22','2010-02-02','FEMININO',20,'555.666.777-45');
