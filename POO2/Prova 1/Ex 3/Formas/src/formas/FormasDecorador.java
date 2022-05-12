package formas;

public abstract class FormasDecorador extends Formas{
    private Formas formaDecorada;

    public FormasDecorador(Formas formaDecorada) {
        this.formaDecorada = formaDecorada;
    }

    public String desenhar(){
        return formaDecorada.desenhar() + ", "+super.desenhar();
    }
    
}
