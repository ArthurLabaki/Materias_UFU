package poo2.power;

import poo2.atk.Ataque;

public class Poder3 extends Poder{

    // Construtor
    public Poder3(Ataque ataqueDecorado) {
        super(ataqueDecorado);
        this.setDano(5); // aumentar em +5 o atk
        System.out.println("Ataque aumentado em 5");
    }
    
}
