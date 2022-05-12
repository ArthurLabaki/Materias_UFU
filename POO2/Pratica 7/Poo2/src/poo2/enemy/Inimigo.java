package poo2.enemy;

import java.util.Observer;

public abstract class Inimigo implements Observer {
    
    // Atributos
    private int x;
    private int y;
    private int vida;
    public String tipo;

    // Inimigo 1 - dano 5 vida 20 velocidade normal
    // Inimigo 2 - dano 1 vida 8 velocidade rapida
    // Inimigo 3 - dano 15 vida 35 velocidade lenta
    
    // Getters e setters
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

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }
    
    // Construtor
    public Inimigo(int x, int y) {
        this.setX(x);
        this.setY(y);
        this.setVida(20);
    }
    
    // Causar dano no inimigo
    public void causarDano(int dano){
        System.out.println("Voce causou "+ dano +" no "+ this.tipo);
        if (this.getVida() > dano){
            this.setVida(this.getVida() - dano); }
        else{
            System.out.println(this.tipo+" morto");
            this.setVida(0);}
    }
      
}
