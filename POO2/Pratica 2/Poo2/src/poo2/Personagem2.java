package poo2;

import poo2.run.Crapido;
import poo2.jump.Palto;
import poo2.atk.Amedio;

public class Personagem2 extends Personagem{
    
    public Personagem2(){
        setPulo(new Palto());
        setCorrida(new Crapido());
        setAtaque(new Amedio());
    }
}
