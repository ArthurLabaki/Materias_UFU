package poo2;

import poo2.run.Cmedio;
import poo2.jump.Pmedio;
import poo2.atk.Aforte;
import poo2.enemy.Inimigo;

public class Personagem1 extends Personagem{
    
    public Personagem1(Inimigo[] ini){
        setPulo(new Pmedio());
        setCorrida(new Cmedio());
        setAtaque(new Aforte());
        this.i1 = ini[0];
        this.i2 = ini[1];
        this.i3 = ini[2];
    }

}
