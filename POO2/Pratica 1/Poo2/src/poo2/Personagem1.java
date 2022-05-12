package poo2;

import poo2.run.Cmedio;
import poo2.jump.Pmedio;
import poo2.atk.Aforte;

public class Personagem1 extends Personagem{
    
    public Personagem1(){
        setPulo(new Pmedio());
        setCorrida(new Cmedio());
        setAtaque(new Aforte());
    }
}
