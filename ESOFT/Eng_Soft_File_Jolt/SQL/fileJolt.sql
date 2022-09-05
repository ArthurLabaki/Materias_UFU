CREATE SCHEMA fileJolt;

SET search_path TO fileJolt;

CREATE TABLE usuario
(
	identificador smallint NOT NULL,
	email varchar(100) NOT NULL UNIQUE,
	nome varchar(100) NOT NULL,
	senha varchar(100) NOT NULL,
	CONSTRAINT usuario_pk PRIMARY KEY (identificador)
);

CREATE TABLE arquivo
(
	identificador smallint NOT NULL,
	nome varchar(100) NOT NULL,
	versao smallint NOT NULL,
	local varchar(150) NOT NULL,
	CONSTRAINT arquivo_pk PRIMARY KEY (identificador, nome, versao),
	CONSTRAINT arquivo_fk
	FOREIGN KEY (identificador)
	REFERENCES usuario (identificador)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION
);

CREATE TABLE avalia
(
	identificador_criador smallint NOT NULL,
	identificador_avaliador smallint NOT NULL,
	nome varchar(100) NOT NULL,
	versao smallint NOT NULL,
	nota smallint NOT NULL,
	CONSTRAINT avalia_pk PRIMARY KEY (identificador_criador, identificador_avaliador, nome, versao),
	CONSTRAINT avalia_fk1
	FOREIGN KEY (identificador_avaliador)
	REFERENCES usuario (identificador)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION,
	CONSTRAINT avalia_fk2
	FOREIGN KEY (identificador_criador, nome, versao)
	REFERENCES arquivo (identificador, nome, versao)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION
);

CREATE TABLE comenta
(
	identificador_criador smallint NOT NULL,
	identificador_avaliador smallint NOT NULL,
	nome varchar(100) NOT NULL,
	versao smallint NOT NULL,
	comentario varchar(500) NOT NULL,
	CONSTRAINT comenta_pk PRIMARY KEY (identificador_criador, identificador_avaliador, nome, versao),
	CONSTRAINT comenta_fk1
	FOREIGN KEY (identificador_avaliador)
	REFERENCES usuario (identificador)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION,
	CONSTRAINT comenta_fk2
	FOREIGN KEY (identificador_criador, nome, versao)
	REFERENCES arquivo (identificador, nome, versao)
	ON DELETE NO ACTION
	ON UPDATE NO ACTION
);

INSERT INTO usuario VALUES (0, 'teste@teste.com', 'Fulano de Paula', 'senha');
INSERT INTO arquivo VALUES (0, 'test file', 1, 'local do arquivo');
INSERT INTO avalia VALUES (0, 0, 'test file', 1, 10);
INSERT INTO comenta VALUES (0, 0, 'test file', 1, 'Muito bom!');