package poo2.life;

import poo2.Personagem;
import poo2.atk.Aforte;
import poo2.jump.Palto;
import poo2.run.Crapido;

public class Sforte extends Saude{
    public Sforte(Personagem personagem){
        super(personagem);
        this.getPersonagem().setPulo(new Palto());
        this.getPersonagem().setCorrida(new Crapido());
        this.getPersonagem().setAtaque(new Aforte());
    }

    protected void verificarEstado() {
        if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 70)
            System.out.println("Estado forte"); // Esse estado
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 30)
             this.getPersonagem().setSaude(new Snormal(this.getPersonagem()));  
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 0)
            this.getPersonagem().setSaude(new Sperigo(this.getPersonagem()));
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() == 0)
            this.getPersonagem().setSaude(new Smorto(this.getPersonagem()));
    }
}

