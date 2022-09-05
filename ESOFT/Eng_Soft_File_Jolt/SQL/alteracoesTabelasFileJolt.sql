SET search_path TO fileJolt;

ALTER TABLE filejolt.arquivo
  DROP COLUMN versao cascade;
 
ALTER TABLE filejolt.arquivo
  DROP COLUMN local;
  
ALTER TABLE filejolt.arquivo
  ADD COLUMN descricao VARCHAR(500);
  
ALTER TABLE filejolt.arquivo
  ADD COLUMN titulo VARCHAR(30) NOT NULL;

 ALTER TABLE filejolt.arquivo
  ADD COLUMN qtd_downloads INTEGER NOT NULL;
  
ALTER TABLE avalia
 ALTER COLUMN versao TYPE INTEGER;
 
