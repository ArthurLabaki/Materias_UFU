package poo2.abs_factory;

import poo2.Personagem;
import poo2.enemy.Inimigo;
import poo2.power.Poder;
import poo2.shield.Escudo;
import poo2.shield.Escudo1;

public abstract class AbstractFactory {
    public Inimigo ini[] = new Inimigo[3];
    public Escudo e1 = new Escudo1(0,0);
    public Escudo e2= new Escudo1(0,0);
    public Escudo e3= new Escudo1(0,0);
    public Personagem pers;
    
    public abstract Personagem criarPers();
    public abstract Inimigo criarIni(int n);
    //public abstract Poder criarPod();
    public abstract Escudo criarEsc(int n);
}
