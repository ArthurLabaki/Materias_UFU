package poo2.power;

import poo2.atk.Ataque;

public class Poder2 extends Poder{

    // Construtor
    public Poder2(Ataque ataqueDecorado) {
        super(ataqueDecorado);
        this.setDano(2); // aumentar em +2 o atk
        System.out.println("Ataque aumentado em 2");
    }
    
}
