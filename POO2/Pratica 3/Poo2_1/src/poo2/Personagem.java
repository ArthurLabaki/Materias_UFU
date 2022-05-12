package poo2;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Observable;
import poo2.life.Saude;
import poo2.life.Snormal;
import poo2.run.Corrida;
import poo2.jump.Pulo;
import poo2.atk.Ataque;
import poo2.enemy.Inimigo;

public abstract class Personagem extends Observable implements KeyListener {
    private Pulo p;
    private Corrida c;
    private Ataque a;
    private Saude saude;
    private int vida;   // Vida atual
    private int vidaTot;    // Vida total
    private int x;
    private int y;
    public Inimigo i1, i2, i3;
    
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
        saude.perderVida(Math.abs(dano)); // Numero sem sinal
    }
    public void ganharVida(int dano){
        saude.ganharVida(Math.abs(dano));
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

    
    public Personagem(){
        this.saude = new Snormal(this);
        this.vidaTot = 100;
        this.vida = 70;
        this.x = 800;
        this.y = 450;
    }
    
    public void show(){
        setChanged();
        notifyObservers();
    }
    
    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_LEFT){
            c.correr();
            this.setX(this.getX()- c.getVelocidade());
        }
               
        if (e.getKeyCode() == KeyEvent.VK_RIGHT){
            c.correr();
            this.setX(this.getX()+ c.getVelocidade());
        }
               
        if (e.getKeyCode() == KeyEvent.VK_UP){
            c.correr();
            this.setY(this.getY()- c.getVelocidade());
        }
            
        if (e.getKeyCode() == KeyEvent.VK_DOWN){
            c.correr();
            this.setY(this.getY()+ c.getVelocidade());
        }
               
        if (e.getKeyCode() == KeyEvent.VK_SPACE){
            a.atacar();
            if(((this.getX() - i1.getX()) == 0) && ((this.getY() - i1.getY()) == 0)){
                i1.causarDano(a.getDano());
            }
            if(((this.getX() - i2.getX()) == 0) && ((this.getY() - i2.getY()) == 0)){
                i2.causarDano(a.getDano());
            }
            if(((this.getX() - i3.getX()) == 0) && ((this.getY() - i3.getY()) == 0)){
                i3.causarDano(a.getDano());
            }

        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) {}
}
