package sistema_vendas;

public class Indisponivel extends Estados {

    public Indisponivel(Sistema_Vendas conta) {
        super(conta);
    }

    protected void verificarEstado() {
        if(this.getConta().getQuantidade() <= 10 && this.getConta().getQuantidade() > 0){  
            this.getConta().setEstado(new EstoqueCritico(this.getConta()));
        }
        else if (this.getConta().getQuantidade() > 10){  // perminte mudanca de disponivel direto para indisponivel
            this.getConta().setEstado(new Disponivel(this.getConta()));
        }
    }
      
}
