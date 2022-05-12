package poo2.atk;

public abstract class Ataque {
    private int dano;
    
    public abstract void atacar();

    public int getDano() {
        return dano;
    }

    public void setDano(int dano) {
        this.dano = dano;
    }

    public Ataque() {
        this.dano = 12;
    }
}
