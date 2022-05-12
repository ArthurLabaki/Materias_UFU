package poo2.atk;

public abstract class Ataque {
    private int dano;   // Quantidade de dano
    
    // Ataque forte = 18
    // Ataque medio = 12
    // Ataque fraco = 8
    
    public abstract void atacar();

    public int getDano() {
        return dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }

}
