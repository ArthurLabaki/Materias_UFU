package poo2.life;

import poo2.Personagem;
import poo2.atk.Afraco;
import poo2.jump.Pbaixo;
import poo2.run.Cdevagar;

public class Sperigo extends Saude{
    
    // Construtor
    public Sperigo(Personagem personagem){
        super(personagem);
        this.getPersonagem().setPulo(new Pbaixo());
        this.getPersonagem().setCorrida(new Cdevagar());
        this.getPersonagem().setAtaque(new Afraco());
        System.out.println("Estado perigo");
    }

    protected void verificarEstado() {  // É possivel pular estados (caso ele esteja forte possa ir para o perigo sem passar pelo normal)
        if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 70)
            this.getPersonagem().setSaude(new Sforte(this.getPersonagem()));  
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 30)
            this.getPersonagem().setSaude(new Snormal(this.getPersonagem()));
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 0){}
            //System.out.println("Estado perigo"); // Esse estado
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() == 0)
            this.getPersonagem().setSaude(new Smorto(this.getPersonagem()));
    }
    
}
