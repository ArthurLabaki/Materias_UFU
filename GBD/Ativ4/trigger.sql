SET search_path TO novovendas;
CREATE TRIGGER  t_att_ValorTotal
BEFORE INSERT OR UPDATE OR DELETE ON itemped
FOR EACH ROW
EXECUTE PROCEDURE att_ValorTotal();

CREATE OR REPLACE FUNCTION att_ValorTotal() RETURNS TRIGGER
AS
$$
DECLARE
	vf integer;  --  quantidade total de cada item pedido
	np integer;  --  novo valor do numped
BEGIN
	np = NEW numped;
	SELECT SUM(p.valunit * i.quant) FROM produto as p, itemped as i 
	WHERE p.codprod = i.codprod AND i.numped = np GROUP BY i.numped INTO vf;
	update pedido set valortotal = vf WHERE pedido.numped = np;

END
$$ LANGUAGE plpgsql;