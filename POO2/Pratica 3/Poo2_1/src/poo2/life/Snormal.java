package poo2.life;

import poo2.Personagem;
import poo2.atk.Amedio;
import poo2.run.Cmedio;

public class Snormal extends Saude{
    public Snormal(Personagem personagem){
        super(personagem);
        this.getPersonagem().setCorrida(new Cmedio());
        this.getPersonagem().setAtaque(new Amedio());
    }

    protected void verificarEstado() {
        if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 70)
            this.getPersonagem().setSaude(new Sforte(this.getPersonagem()));  
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 30)
            System.out.println("Estado normal"); // Esse estado
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() > 0)
            this.getPersonagem().setSaude(new Sperigo(this.getPersonagem()));
        else if ((100 / this.getPersonagem().getVidaTot())*this.getPersonagem().getVida() == 0)
            this.getPersonagem().setSaude(new Smorto(this.getPersonagem()));
    }
}
