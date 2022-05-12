package poo2.power;

import poo2.atk.Ataque;

public abstract class Poder extends Ataque { // Decorador
    private Ataque ataqueDecorado;
    
    // Poder 1: aumenta ataque em 1
    // Poder 2: aumenta ataque em 2
    // Poder 3: aumenta ataque em 5

    public Poder(Ataque ataqueDecorado) {
        this.ataqueDecorado = ataqueDecorado;
    }
    public int getDano(){
        return ataqueDecorado.getDano() + super.getDano();
    }
    
    @Override
    public void atacar() {
    }
    
}
