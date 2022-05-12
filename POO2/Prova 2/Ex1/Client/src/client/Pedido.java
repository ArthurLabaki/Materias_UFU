package client;

public class Pedido implements PedRep{ // Pedidos (concrete comandos)
    private Fornecedor f;
    
    public Pedido(Fornecedor forn){
        this.f = forn;
    }
    
    @Override
    public void execute() {
        f.venda();
    }
    
}
