package poo2.shield;

public abstract class Escudo {
    
    // Atributos
    private Escudo sucessor;
    private int x;
    private int y;
    public boolean existe = true; // Escudo ja foi ou não pego
    public int qntescudo;  // Valor do escudo

    // Escudo 1: protege 1 de dano
    // Escudo 5: protege 5 de dano
    // Escudo 10: protege 10 de dano
    // PS: Escudos podem estar sumiltaneamente ativos e não se quebram
    
    public abstract int reduzirDano(int dano);
    
    // Getter e setters
    public Escudo getSucessor() {
        return sucessor;
    }

    public void setSucessor(Escudo sucessor) {
        this.sucessor = sucessor;
    }

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
