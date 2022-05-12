package poo2;

import poo2.run.Crapido;
import poo2.jump.Palto;
import poo2.atk.Amedio;
import poo2.enemy.Inimigo;

public class Personagem2 extends Personagem{
    
    public Personagem2(Inimigo[] ini){
        setPulo(new Palto());
        setCorrida(new Crapido());
        setAtaque(new Amedio());
        this.i1 = ini[0];
        this.i2 = ini[1];
        this.i3 = ini[2];
    }
}
