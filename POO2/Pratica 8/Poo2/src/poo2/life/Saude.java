package poo2.life;

import poo2.Personagem;

public abstract class Saude {
    private Personagem personagem;
    
    // Saude forte: vida maior que 70% - atk forte, velocidade rapido pulo alto
    // Saude normal: vida entre 70% e 30% - atk normal, velocidade media e pulo o que estava anteriormente
    // Saude perigo: vida abaixo de 30% - atk fraco, velocidade devagar e pulo baixo
    // Saude morto: vida zero - mesmos atributos, mas o jogo termina
    
    public Saude (Personagem personagem){
        this.personagem = personagem;
    }

    public Personagem getPersonagem() {
        return personagem;
    }

    public void setPersonagem(Personagem personagem) {
        this.personagem = personagem;
    }
    
    // Metodo perder e ganhar vida 
    public void perderVida(int quant){  
        this.personagem.setVida(this.personagem.getVida() - quant);
        if(this.personagem.getVida() <= this.personagem.getVidaTot() && (this.personagem.getVida())>= 0)
            this.verificarEstado();
        else{   // Caso o personagem fique com vida negativa
            System.out.println("Valor de vida minimo");
            this.personagem.setVida(0);
            this.verificarEstado();
        }
    }
    public void ganharVida(int quant){
        this.personagem.setVida(this.personagem.getVida() + quant);
        if(this.personagem.getVida() <= this.personagem.getVidaTot() && (this.personagem.getVida())>= 0)
            this.verificarEstado();
        else{   // Caso o personagem fique com vida maior que o maximo
            System.out.println("Valor de vida maximo");
            this.personagem.setVida(this.personagem.getVidaTot());
            this.verificarEstado();
        }
    }
    
    protected abstract void verificarEstado();
    
}
