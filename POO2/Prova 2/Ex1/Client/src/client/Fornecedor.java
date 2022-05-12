package client;

public class Fornecedor { // Fornecedor correto (receiver) 
    public void venda(){ // imprime o objeto fornecedor, indicando que entrou em objetos diferentes
        System.out.println("Pedido chego ao fornecedor " + this.toString());
    }
}
