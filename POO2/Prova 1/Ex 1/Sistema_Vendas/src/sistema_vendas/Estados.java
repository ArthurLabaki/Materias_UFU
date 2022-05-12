package sistema_vendas;

public abstract class Estados {
    private Sistema_Vendas conta;
    
    public Estados(Sistema_Vendas conta){
        this.conta = conta;
    }

    public Sistema_Vendas getConta() {
        return conta;
    }

    public void setConta(Sistema_Vendas conta) {
        this.conta = conta;
    }
    
    public void compra(int qnt) {    // reposição de estoque
        if(qnt < 0) System.out.println("Impossivel quantidade negativa");
        else{
            this.conta.setQuantidade(this.conta.getQuantidade() + qnt);
            this.verificarEstado();
        }
    }
    public void venda(int qnt){     // abate de estoque
        if(qnt < 0) System.out.println("Impossivel quantidade negativa");
        else if (this.conta.getQuantidade() < qnt){
            System.out.println("Venda maior que a quantidade disponivel, venda revogada!");
        }
        else{
            this.conta.setQuantidade(this.conta.getQuantidade() - qnt);
            this.verificarEstado();

        }
    
    }
    protected abstract void verificarEstado();
}
