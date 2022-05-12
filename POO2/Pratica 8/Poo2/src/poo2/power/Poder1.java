package poo2.power;

import poo2.atk.Ataque;

public class Poder1 extends Poder{

    // Construtor
    public Poder1(Ataque ataqueDecorado) {
        super(ataqueDecorado);
        this.setDano(1); // aumentar em +1 o atk
        System.out.println("Ataque aumentado em 1");
    }
    
}
