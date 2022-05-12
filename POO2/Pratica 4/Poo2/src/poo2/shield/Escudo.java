package poo2.shield;

public abstract class Escudo {
    private Escudo sucessor;
    private int x;
    private int y;
    public boolean existe = true; // escudo ja foi ou não pego

    public Escudo getSucessor() {
        return sucessor;
    }

    public void setSucessor(Escudo sucessor) {
        this.sucessor = sucessor;
    }
    
    public abstract int reduzirDano(int dano);

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
 
}
