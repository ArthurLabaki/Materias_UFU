package poo2.abs_factory;

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
import poo2.power.Poder;
import poo2.shield.Escudo;
import poo2.shield.Escudo1;
import poo2.shield.Escudo10;
import poo2.shield.Escudo5;

public class FacFuturista extends AbstractFactory{
    private static FacFuturista inst;
    
    @Override
    public Personagem criarPers() {
        Personagem p = null;
        double tipo = Math.random();
        if (tipo <= 0.2){
            p = new Personagem2(ini, e1, e2, e3);
            p.tipo = "CyberCavaleiro";}
        else if (tipo <= 0.4){
            p = new Personagem2(ini, e1, e2, e3);
            p.tipo = "Mecha";}
        else if (tipo <= 0.6){
            p = new Personagem2(ini, e1, e2, e3);
            p.tipo = "Robo";}
        else if (tipo <= 0.8){
            p = new Personagem2(ini, e1, e2, e3);
            p.tipo = "Ciborgue";}
        else {
            p = new Personagem2(ini, e1, e2, e3);
            p.tipo = "Rebelde";}
        this.pers = p;
        //p.status();
        return p;
    }

    @Override
    public Inimigo criarIni(int n) {
         Inimigo i = null;
         int x = (int) (Math.random() * ( 1600 - 1));
         int y  = (int) (Math.random() * ( 900 - 1));
         
         // impede de nascer em cima do personagem
         if(x == 800)
             x = 1600;
         if(y == 450)
             y = 900;
         
         double t = Math.random();
         if (t <= 0.33){
             i = new Inimigo1(x, y);
             i.tipo = "Robo";}
         else if (t <= 0.66){
             i = new Inimigo2(x, y);
             i.tipo = "Rebelde";}
         else{
             i = new Inimigo3(x, y);
             i.tipo = "Mecha";}
         this.ini[n] = i;
         return i;   
    }

    //public Poder criarPod() {}

    @Override
    public Escudo criarEsc(int n) {
        Escudo i = null;
        int x = (int) (Math.random() * ( 1500 - 50));
        int y  = (int) (Math.random() * ( 900 - 50));
         
        // impede de nascer em cima do personagem
        if(x == 800)
            x = 1600;
        if(y == 450)
            y = 900;
        
        if (n == 1){
            i = new Escudo1(x, y);
            i.tipo = "Placa de metal +1";
            this.e1 = i;}
        else if (n == 2){
            System.out.println("oi\n");
            i = new Escudo5(x, y);
            i.tipo = "Escudo de titânio +5";
            this.e2 = i;}
        else{
            i = new Escudo10(x, y);
            i.tipo = "Armadura nuclear de adamantite +10";
            this.e3 = i;}
        return i;
    }  
    
    public static synchronized FacFuturista getInstance(){
        if (inst == null){
            inst = new FacFuturista();
        }
        return inst;
    }
    
}
