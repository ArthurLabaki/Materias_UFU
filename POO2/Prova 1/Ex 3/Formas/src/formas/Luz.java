package formas;

public class Luz extends FormasDecorador{

    public Luz(Formas formaDecorada) {
        super(formaDecorada);
        setTipo("Luz");
    }
    
}
