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
import poo2.shield.Escudo;

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
    public Escudo e1, e2, e3;
    
    
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
        dano = Math.abs(dano);
        if (e3.existe == false) dano = e3.reduzirDano(dano); /// e3, e3 e2, e3 e1, e3 e2 e1
        else {if (e2.existe == false) dano = e2.reduzirDano(dano); // e2, e2 e1
        else {if (e1.existe == false) dano = e1.reduzirDano(dano);}} // e1
        saude.perderVida(dano); // Numero sem sinal
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
        this.vidaTot = 1000;
        this.vida = (this.vidaTot *70)/100;
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
            if(((this.getX() - i1.getX()) == 0) && ((this.getY() - i1.getY()) == 0) && i1.getVida() > 0){
                i1.causarDano(a.getDano());
            }
            if(((this.getX() - i2.getX()) == 0) && ((this.getY() - i2.getY()) == 0)&& i2.getVida() > 0){
                i2.causarDano(a.getDano());
            }
            if(((this.getX() - i3.getX()) == 0) && ((this.getY() - i3.getY()) == 0)&& i3.getVida() > 0){
                i3.causarDano(a.getDano());
            }

        }
        
        if (e.getKeyCode() == KeyEvent.VK_E){ //PEGAR ESCUDO TECLA E
            if((Math.abs(this.getX() - e1.getX()) <= 10) && (Math.abs(this.getY() - e1.getY()) <= 10) && (e1.existe == true)){
                e1.existe = false;
                if (e3.existe == false && e2.existe == false){ // e3 e e2 existem;
                    //e3.setSucessor(e2);
                    e2.setSucessor(e1);
                    e1.setSucessor(null);
                }else {
                    if (e2.existe == false){  // so e2
                        e2.setSucessor(e1);
                        e1.setSucessor(null);
                    }
                    else{
                        if (e3.existe == false){ // so e3
                            e3.setSucessor(e1);
                            e1.setSucessor(null);
                        }
                        else{
                            e1.setSucessor(null); // nenhum
                        }
                    }
                }
            }
            if((Math.abs(this.getX() - e2.getX()) <= 10) && (Math.abs(this.getY() - e2.getY()) <= 10)&& (e2.existe == true)){
                e2.existe = false;
                if (e3.existe == false && e1.existe == false){ // e3 e e1 existem;
                    e3.setSucessor(e2);
                    e2.setSucessor(e1);
                    //e1.setSucessor(null);
                }else {
                    if (e1.existe == false){  // so e1
                        e2.setSucessor(e1);
                        //e1.setSucessor(null);
                    }
                    else{
                        if (e3.existe == false){ // so e3
                            e3.setSucessor(e2);
                            e2.setSucessor(null);
                        }
                        else{
                            e2.setSucessor(null); // nenhum
                        }
                    }
                }
            }
            if((Math.abs(this.getX() - e3.getX()) <= 10) && (Math.abs(this.getY() - e3.getY()) <= 10) && (e3.existe == true)){
                e3.existe = false;
                if (e2.existe == false && e1.existe == false){ // e2 e e1 existem;
                    e3.setSucessor(e2);
                    //e2.setSucessor(e1);
                    //e1.setSucessor(null);
                }else {
                    if (e1.existe == false){  // so e1
                        e3.setSucessor(e1);
                        //e1.setSucessor(null);
                    }
                    else{
                        if (e2.existe == false){ // so e2
                            e3.setSucessor(e2);
                            //e2.setSucessor(null);
                        }
                        else{
                            e3.setSucessor(null); // nenhum
                        }
                    }
                }
            }
            
        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) {}
}
