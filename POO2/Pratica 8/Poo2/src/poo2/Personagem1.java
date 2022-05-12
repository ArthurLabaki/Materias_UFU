package poo2;

import poo2.run.Cmedio;
import poo2.jump.Pmedio;
import poo2.atk.Aforte;
import poo2.enemy.Inimigo;
import poo2.shield.Escudo;

public class Personagem1 extends Personagem{
    
    // Construtor
    public Personagem1(Inimigo[] ini, Escudo e1, Escudo e2, Escudo e3){
        setPulo(new Pmedio());
        setCorrida(new Cmedio());
        setAtaque(new Aforte());
        this.inimigos = ini;
        this.e1 = e1;
        this.e2 = e2;
        this.e3 = e3;
        a.atacar();
    }
}
