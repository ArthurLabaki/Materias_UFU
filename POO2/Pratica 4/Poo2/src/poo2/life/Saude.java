package poo2.life;

import poo2.Personagem;

public abstract class Saude {
    private Personagem personagem;
    
    public Saude (Personagem personagem){
        this.personagem = personagem;
    }

    public Personagem getPersonagem() {
        return personagem;
    }

    public void setPersonagem(Personagem personagem) {
        this.personagem = personagem;
    }

    public void perderVida(int quant){
        this.personagem.setVida(this.personagem.getVida() - quant);
        if(this.personagem.getVida() <= this.personagem.getVidaTot() && (this.personagem.getVidaTot() - this.personagem.getVida())>= 0)
            this.verificarEstado();
        else{
            System.out.println("Valor de vida minimo");
            this.personagem.setVida(0);
            this.verificarEstado();
        }
    }
    public void ganharVida(int quant){
        this.personagem.setVida(this.personagem.getVida() + quant);
        if(this.personagem.getVida() <= this.personagem.getVidaTot() && (this.personagem.getVidaTot() - this.personagem.getVida())>= 0)
            this.verificarEstado();
        else{
            System.out.println("Valor de vida maximo");
            this.personagem.setVida(this.personagem.getVidaTot());
            this.verificarEstado();
        }
    }
    protected abstract void verificarEstado();
}
