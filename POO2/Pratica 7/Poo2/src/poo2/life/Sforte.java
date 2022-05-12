package poo2.life;

import poo2.Personagem;
import poo2.atk.Aforte;
import poo2.jump.Palto;
import poo2.run.Crapido;

public class Sforte extends Saude{
    
    // Construtor
    public Sforte(Personagem personagem){
        super(personagem);
        this.getPersonagem().setPulo(new Palto());
        this.getPersonagem().setCorrida(new Crapido());
        this.getPersonagem().setAtaque(new Aforte());
        System.out.println("Estado forte");
    }

    protected void verificarEstado() {  // É possivel pular estados (caso ele esteja forte possa ir para o perigo sem passar pelo normal)
        if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot()> 70){}
            //System.out.println("Estado forte"); // Esse estado
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 30)
             this.getPersonagem().setSaude(new Snormal(this.getPersonagem()));  
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() > 0)
            this.getPersonagem().setSaude(new Sperigo(this.getPersonagem()));
        else if ((this.getPersonagem().getVida() *100 ) / this.getPersonagem().getVidaTot() == 0)
            this.getPersonagem().setSaude(new Smorto(this.getPersonagem()));
    }
    
}

