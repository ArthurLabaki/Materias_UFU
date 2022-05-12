package poo2.factory;

import poo2.Personagem;
import poo2.Personagem1;
import poo2.Personagem2;
import poo2.Personagem3;
import poo2.Personagem4;
import poo2.Personagem5;
import poo2.enemy.Inimigo;
import poo2.enemy.Inimigo1;
import poo2.enemy.Inimigo2;
import poo2.enemy.Inimigo3;
import poo2.power.Poder1;
import poo2.power.Poder2;
import poo2.power.Poder3;
import poo2.shield.Escudo;

public class SimplePersonagemFactoryB extends AbsFactory{
    private static SimplePersonagemFactoryB inst;
    
    public Personagem createPersonagem(int pers){
        Personagem p = null;      
        if (pers == 1)
            p = new Personagem1(ini, e1, e2, e3);
        else if (pers == 2)
            p = new Personagem2(ini, e1, e2, e3);
        else if (pers == 3)
            p = new Personagem3(ini, e1, e2, e3);
        else if (pers == 4)
            p = new Personagem4(ini, e1, e2, e3);
        else 
            p = new Personagem5(ini, e1, e2, e3);
        //System.out.println(tipo);
        double tipo = Math.random();
        if (tipo <=0.3){
            p.a = new Poder1(p.a);
            p.p1 = false; }
        else if (tipo <= 0.6) {
            p.a = new Poder2(p.a);
            p.p2 = false; }
        else {
            p.a = new Poder3(p.a);
            p.p3 = false;}
        System.out.println(tipo);
        //p.status();
        return p;
    }
    
     public Inimigo createInimigo(int ini){
         Inimigo i = null;
         int x = (int) (Math.random() * ( 1600 - 1));
         int y  = (int) (Math.random() * ( 900 - 1));
         
         // impede de nascer em cima do personagem
         if(x == 800)
             x = 1600;
         if(y == 450)
             y = 900;
         
         if (ini == 1)
             i = new Inimigo1(x, y);
         else if (ini == 2)
             i = new Inimigo2(x, y);
         else
             i = new Inimigo3(x, y);
         return i;
     }
     
    public static synchronized AbsFactory getInstance(){
        if (inst == null){
            inst = new SimplePersonagemFactoryB();
        }
        return inst;
    }
}
