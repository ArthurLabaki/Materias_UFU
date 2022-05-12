package sistema_vendas;

public class EstoqueCritico extends Estados{

    public EstoqueCritico(Sistema_Vendas conta) {
        super(conta);
    }

    protected void verificarEstado() {
        if(this.getConta().getQuantidade() > 10){  
            this.getConta().setEstado(new Disponivel(this.getConta()));
        }
        else if (this.getConta().getQuantidade() == 0){  // permite mudanca de disponivel direto para indisponivel
            this.getConta().setEstado(new Indisponivel(this.getConta()));
        }
    }
    
}
