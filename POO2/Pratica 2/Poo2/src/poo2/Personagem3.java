package poo2;

import poo2.run.Crapido;
import poo2.jump.Pbaixo;
import poo2.atk.Aforte;

public class Personagem3 extends Personagem{
    
    public Personagem3(){
        setPulo(new Pbaixo());
        setCorrida(new Crapido());
        setAtaque(new Aforte());
    }
}
