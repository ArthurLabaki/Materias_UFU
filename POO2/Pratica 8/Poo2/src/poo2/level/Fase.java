package poo2.level;

import java.util.logging.Level;
import java.util.logging.Logger;
import poo2.Jogo;
import poo2.abs_factory.FacFuturista;
import poo2.enemy.Inimigo;
import poo2.shield.Escudo;
import poo2.shield.Escudo1;

public class Fase implements Component{
    private int qntIni;
    private int velIni;  //de 0 a 9
    public String nomeFase;
    public Inimigo inimigos[] = new Inimigo[10];
    Escudo e1 = new Escudo1(0,0);
    Escudo e5 = new Escudo1(0,0);
    Escudo e10 = new Escudo1(0,0);
    public Fase prox1;
    public Fase prox2;

    public Fase(int qntIni, int velIni, String nomeFase, Fase prox1, Fase prox2) {
        this.qntIni = qntIni;
        this.velIni = velIni;
        this.nomeFase = nomeFase;
        this.prox1 = prox1;
        this.prox2 = prox2;
    }
    
    
    @Override
    public void jogarFase() {
        Jogo j = new Jogo();
        
        FacFuturista fmed = FacFuturista.getInstance(); // futurista
        //FacMedieval fmed = FacMedieval.getInstance(); // medieval
        
        int i = 0;
        for (i = 0; i < this.qntIni; i++){
            this.inimigos[i] = fmed.criarIni(i);
            this.inimigos[i].vel = this.velIni;
            j.inimigos[i] = this.inimigos[i];
        }
        for (i = i; i < 10; i++){
            this.inimigos[i] = fmed.criarIni(i);
            this.inimigos[i].setVida(0);
            j.inimigos[i] = this.inimigos[i];
        }
        
       j.e1 = fmed.criarEsc(1);
       j.e5 = fmed.criarEsc(2);
       j.e10 = fmed.criarEsc(3);
       j.pers = fmed.criarPers();
       j.pers.status();
       j.addKeyListener(j.pers);
       j.setFocusable(true);
        System.out.println("oi");
        try {
            j.jogar(j);
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            Logger.getLogger(Fase.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
    
    
}

