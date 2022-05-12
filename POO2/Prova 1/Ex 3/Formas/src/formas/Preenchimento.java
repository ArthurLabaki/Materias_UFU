package formas;

public class Preenchimento extends FormasDecorador{

    public Preenchimento(Formas formaDecorada) {
        super(formaDecorada);
        setTipo("Preenchimento");
    }
    
}
