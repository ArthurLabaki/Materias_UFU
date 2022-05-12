package poo2;

import poo2.run.Crapido;
import poo2.jump.Pbaixo;
import poo2.atk.Aforte;
import poo2.enemy.Inimigo;
import poo2.shield.Escudo;

public class Personagem3 extends Personagem{
    
    // Construtor
    public Personagem3(Inimigo[] ini, Escudo e1, Escudo e2, Escudo e3){
        setPulo(new Pbaixo());
        setCorrida(new Crapido());
        setAtaque(new Aforte());
        this.i1 = ini[0];
        this.i2 = ini[1];
        this.i3 = ini[2];
        this.e1 = e1;
        this.e2 = e2;
        this.e3 = e3;
        a.atacar();
    }
}
