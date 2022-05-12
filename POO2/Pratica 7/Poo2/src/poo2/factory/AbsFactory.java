package poo2.factory;

import poo2.Jogo;
import poo2.Personagem;
import poo2.enemy.Inimigo;
import poo2.enemy.Inimigo1;
import poo2.enemy.Inimigo2;
import poo2.enemy.Inimigo3;
import poo2.shield.Escudo;
import poo2.shield.Escudo1;
import poo2.shield.Escudo10;
import poo2.shield.Escudo5;


public abstract class AbsFactory {  // Ativ 6
    public abstract Personagem createPersonagem(int pers);
    public abstract Inimigo createInimigo(int pers);
    
    public Inimigo ini[] = new Inimigo[3];
    public Escudo e1;
    public Escudo e2;
    public Escudo e3;
    public Personagem pers;
    
    public void jogar(){
        ini[0] = new Inimigo1(10,450);
        ini[1] = new Inimigo2(30,30);
        ini[2] = new Inimigo3(1500,800);
        e1 = new Escudo1(1000, 40);
        e2 = new Escudo5(250, 250);
        e3 = new Escudo10(1000, 700);
        
        // Personagens
        
        //this.pers = createPersonagem(2);
        //this.pers = createPersonagem(3);
        //this.pers = createPersonagem(4);
        //this.pers = createPersonagem(5);
        
        // Inimigos
        this.ini[0] = createInimigo(1);
        this.ini[1] = createInimigo(2);
        this.ini[2] = createInimigo(3);
        //p1.status();
        this.pers = createPersonagem(1);
    }
    
}
