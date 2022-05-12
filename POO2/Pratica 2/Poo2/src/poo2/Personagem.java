package poo2;

import poo2.life.Saude;
import poo2.life.Snormal;
import poo2.run.Corrida;
import poo2.jump.Pulo;
import poo2.atk.Ataque;

public abstract class Personagem {
    private Pulo p;
    private Corrida c;
    private Ataque a;
    private Saude saude;
    private int vida;   // Vida atual
    private int vidaTot;    // Vida total
    
    public void setPulo(Pulo p){
        this.p = p;
    }
    
    public void setCorrida(Corrida c){
        this.c = c;
    }
    
    public void setAtaque(Ataque a){
        this.a = a;
    }
    
    public void pular(){
        p.pular();
    }
    
    public void correr(){
        c.correr();
    }
    
    public void atacar(){
        a.atacar();
    }
    public void status(){
        System.out.println(this.a);
        System.out.println(this.c);
        System.out.println(this.p);
        System.out.println(this.vida);
        System.out.println(this.saude);
        System.out.println("\n");
    }

    public int getVida() {
        return vida;
    }

    public void setVida(int vida) {
        this.vida = vida;
    }

    public int getVidaTot() {
        return vidaTot;
    }

    public void setVidaTot(int vidaTot) {
        this.vidaTot = vidaTot;
    }

    public Saude getSaude() {
        return saude;
    }

    public void setSaude(Saude saude) {
        this.saude = saude;
    }
    
    public void perderVida(int dano){
        saude.perderVida(Math.abs(dano)); // Numero se sinal
    }
    public void ganharVida(int dano){
        saude.ganharVida(Math.abs(dano));
    }
    public Personagem(){
        this.saude = new Snormal(this);
        this.vidaTot = 100;
        this.vida = 70;
    }
}
