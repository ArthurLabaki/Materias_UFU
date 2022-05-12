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
import poo2.power.Poder1;
import poo2.power.Poder2;
import poo2.power.Poder3;
import poo2.shield.Escudo;

public abstract class Personagem extends Observable implements KeyListener {
    
    // Criando os atributos
    private Pulo p;
    private Corrida c;
    public Ataque a;
    private Saude saude;
    private int vida;       // Vida atual
    private int vidaTot;    // Vida total
    private int x;
    private int y;
    public Inimigo i1, i2, i3;
    public Escudo e1, e2, e3;
    public boolean p1, p2, p3; // Poderes
    
    // Metodos do pulo, corrida e ataque
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
    
    // Status para mostrar na tela algumas informações para teste
    public void status(){
        System.out.println(this.a);
        System.out.println(this.c);
        System.out.println(this.p);
        System.out.println(this.vida);
        System.out.println(this.saude);
        System.out.println("\n");
    }
    
    // Getters e setters de vida, vida total e saude
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
        if (this.p1 == false) // Mesmo se mudar o estado do personagem, o poder ainda continua
            a = new Poder1(a);
        if (this.p2 == false)
            a = new Poder2(a);
        if (this.p3 == false)
            a = new Poder3(a);
    }
    
    // Metodos de perder e ganhar vida do personagem, reduzindo dos escudos pegos
    public void perderVida(int dano){
        dano = Math.abs(dano);
        if (e3.existe == false) dano = e3.reduzirDano(dano); /// e3, e3 e2, e3 e1, e3 e2 e1
        else {if (e2.existe == false) dano = e2.reduzirDano(dano); // e2, e2 e1
        else {if (e1.existe == false) dano = e1.reduzirDano(dano);}} // e1
        saude.perderVida(dano); // Numero sem sinal
    }
    
    public void ganharVida(int dano){ // ainda não foi feito
        saude.ganharVida(Math.abs(dano));
    }
    
    // getters e setters de X e Y
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
    
    // Construtor do personagem
    public Personagem(){
        this.saude = new Snormal(this);
        this.vidaTot = 1000;
        this.vida = (this.vidaTot *70)/100;
        this.x = 800;
        this.y = 450;
        this.p1 = true;
        this.p2 = true;
        this.p3 = true;
    }
    
    // Metodo do Observable
    public void show(){
        setChanged();
        notifyObservers();
    }
    
    // Metodos do KeyListener
    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        
        // Movimento do personagem
        if (e.getKeyCode() == KeyEvent.VK_LEFT){
            c.correr();     // Atualizar velocidade de movimento caso personagem mude de estado
            this.setX(this.getX()- c.getVelocidade());}
               
        if (e.getKeyCode() == KeyEvent.VK_RIGHT){
            c.correr();
            this.setX(this.getX()+ c.getVelocidade());}
               
        if (e.getKeyCode() == KeyEvent.VK_UP){
            c.correr();
            this.setY(this.getY()- c.getVelocidade());}
            
        if (e.getKeyCode() == KeyEvent.VK_DOWN){
            c.correr();
            this.setY(this.getY()+ c.getVelocidade());}
        
        // Ataque do personagem
        if (e.getKeyCode() == KeyEvent.VK_SPACE){
            a.atacar(); // Atualizar ataque caso personagem mude de estado ou pegue poderes
            if(((this.getX() - i1.getX()) == 0) && ((this.getY() - i1.getY()) == 0) && i1.getVida() > 0){
                i1.causarDano(a.getDano());}
            
            if(((this.getX() - i2.getX()) == 0) && ((this.getY() - i2.getY()) == 0)&& i2.getVida() > 0){
                i2.causarDano(a.getDano());}
            
            if(((this.getX() - i3.getX()) == 0) && ((this.getY() - i3.getY()) == 0)&& i3.getVida() > 0){
                i3.causarDano(a.getDano());}
        }
        
        // Pegar escudos e poderes com a tecla E
        if (e.getKeyCode() == KeyEvent.VK_E){
            
            // Parte dos escudos
            if((Math.abs(this.getX() - e1.getX()) <= 10) && (Math.abs(this.getY() - e1.getY()) <= 10) && (e1.existe == true)){
                e1.existe = false;      // Escudo 1
                if (e3.existe == false && e2.existe == false){ // e3 e e2 existem;
                    //e3.setSucessor(e2);
                    e2.setSucessor(e1);
                    e1.setSucessor(null);
                }else{
                    if (e2.existe == false){  // so e2
                        e2.setSucessor(e1);
                        e1.setSucessor(null);
                    }
                    else{
                        if (e3.existe == false){ // so e3
                            e3.setSucessor(e1);
                            e1.setSucessor(null);
                        }
                        else{e1.setSucessor(null); }// nenhum
                    }
                }
            }  // Estrutura complicada para manter a ordem entre os escudos ja pegos
            
            if((Math.abs(this.getX() - e2.getX()) <= 10) && (Math.abs(this.getY() - e2.getY()) <= 10)&& (e2.existe == true)){
                e2.existe = false;      // Escudo 2
                if (e3.existe == false && e1.existe == false){ // e3 e e1 existem;
                    e3.setSucessor(e2);
                    e2.setSucessor(e1);
                    //e1.setSucessor(null);
                }else{
                    if (e1.existe == false){  // so e1
                        e2.setSucessor(e1);
                        //e1.setSucessor(null);
                    }
                    else{
                        if (e3.existe == false){ // so e3
                            e3.setSucessor(e2);
                            e2.setSucessor(null);
                        }
                        else{e2.setSucessor(null); } // nenhum
                    }
                }
            }
            
            if((Math.abs(this.getX() - e3.getX()) <= 10) && (Math.abs(this.getY() - e3.getY()) <= 10) && (e3.existe == true)){
                e3.existe = false;      // Escudo 3
                if (e2.existe == false && e1.existe == false){ // e2 e e1 existem;
                    e3.setSucessor(e2);
                    //e2.setSucessor(e1);
                    //e1.setSucessor(null);
                }else{
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
                            e3.setSucessor(null); } // nenhum
                    }
                }
            }
            
            // Parte dos poderes com lugares fixos
            if ((Math.abs(this.getX() - 500) <= 15) && (Math.abs(this.getY() - 50) <= 15)){  // Poder 1 500, 50
                if (this.p1 == true){   //Poder 1
                    a = new Poder1(a);
                    this.p1 = false; }
            }
            
            if ((Math.abs(this.getX() - 1500) <= 10) && (Math.abs(this.getY() - 300) <= 10)){  // Poder 2 1500, 300
                if (this.p2 == true){   //Poder 2
                    a = new Poder2(a);
                    this.p2 = false; }

            }
            if ((Math.abs(this.getX() - 190) <= 10) && (Math.abs(this.getY() - 650) <= 10)){  // Poder 3 190, 650
                if (this.p3 == true){   // Poder 3
                    a = new Poder3(a);
                    this.p3 = false; }
            }         
        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) {}
    
    // Metodo para mostrar quantos estudos o personagem tem ( não a quantidade e sim o tanto de defesa)
    public int qntescudo (){
        int qnt = 0;
        if (this.e1.existe == false)
            qnt = qnt + this.e1.qntescudo;
        if (this.e2.existe == false)
            qnt = qnt + this.e2.qntescudo;
        if (this.e3.existe == false)
            qnt = qnt + this.e3.qntescudo;
        return qnt; 
    }
    
}
