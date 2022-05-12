package poo2;

import poo2.run.Crapido;
import poo2.jump.Pbaixo;
import poo2.atk.Aforte;
import poo2.enemy.Inimigo;

public class Personagem3 extends Personagem{
    
    public Personagem3(Inimigo[] ini){
        setPulo(new Pbaixo());
        setCorrida(new Crapido());
        setAtaque(new Aforte());
        this.i1 = ini[0];
        this.i2 = ini[1];
        this.i3 = ini[2];
    }
}
