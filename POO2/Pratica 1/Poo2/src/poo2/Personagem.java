package poo2;

import poo2.run.Corrida;
import poo2.jump.Pulo;
import poo2.atk.Ataque;

public abstract class Personagem {
    private Pulo p;
    private Corrida c;
    private Ataque a;
    
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
        System.out.println("\n");
    }
}
