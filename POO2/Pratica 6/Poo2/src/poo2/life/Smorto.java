package poo2.life;

import poo2.Personagem;

public class Smorto extends Saude{
    
    // Construtor
    public Smorto(Personagem personagem){
        super(personagem);
        System.out.println("Personagem Morto");
    }

    protected void verificarEstado() {  // É possivel pular estados (caso ele esteja forte possa ir para o perigo sem passar pelo normal)
        if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 70)
            this.getPersonagem().setSaude(new Sforte(this.getPersonagem()));  
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 30)
            this.getPersonagem().setSaude(new Snormal(this.getPersonagem()));
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 0)
            this.getPersonagem().setSaude(new Sperigo(this.getPersonagem()));
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() == 0)
            System.out.println("Morto '-'"); // Esse estado
    }
    
}
