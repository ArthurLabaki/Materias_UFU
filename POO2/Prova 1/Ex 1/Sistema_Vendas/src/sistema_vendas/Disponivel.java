package sistema_vendas;

public class Disponivel extends Estados{

    public Disponivel(Sistema_Vendas conta) {
        super(conta);
    }

    protected void verificarEstado() {
        if(this.getConta().getQuantidade() <= 10 && this.getConta().getQuantidade() > 0){  
            this.getConta().setEstado(new EstoqueCritico(this.getConta()));
        }
        else if (this.getConta().getQuantidade() == 0){  // permite mudanca de disponivel direto para indisponivel
            this.getConta().setEstado(new Indisponivel(this.getConta()));
        }
    }
    
}
