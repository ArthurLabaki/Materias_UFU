package poo2.enemy;

import java.util.Observer;

public abstract class Inimigo implements Observer {
    private int x;
    private int y;
    private int vida;

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
    
    public Inimigo(int x, int y) {
        this.setX(x);
        this.setY(y);
        this.setVida(20);
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }
    public void causarDano(int dano){
        if (this.getVida() > dano){
            System.out.println("Causou "+ dano +" no inimigo");
            this.setVida(this.getVida() - dano);
        }
        else{
            System.out.println("Inimigo morto");
            this.setVida(0);
        }
    }
    
    
}
