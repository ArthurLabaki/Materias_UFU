package poo2.enemy;

import java.util.Observable;
import poo2.Personagem;

public class Inimigo2 extends Inimigo{
    
    public Inimigo2(int x, int y) {
        super(x, y);
        this.setVida(8) ;
    }
    
    public void update(Observable subject, Object arg) {
        
        Personagem pers = (Personagem)subject;
        
        // Se estiver em distancia de ataque
        if ( ( (this.getX() - pers.getX()) == 0) && ((this.getY() - pers.getY()) == 0) ){
            System.out.println("Inimigo causou 1 de dano");
            pers.perderVida(1); }
        
        // Se estiver muito proximo do personagem (para não ficar sambando no personagem)
        if(( Math.abs(this.getX() - pers.getX()) < 5) && (Math.abs(this.getY() - pers.getY()) < 5)){
            this.setX(pers.getX());
            this.setY(pers.getY()); }
        
        // Se precisar andar
        else { 
            
           // Se precisa andar para frente 
           if (pers.getX() > this.getX()) this.setX(this.getX()+(int)((15+this.vel)*Math.random()));
           else this.setX(this.getX()-(int)((15+this.vel)*Math.random()));
           
           // Se precisa andar para tras
           if (pers.getY() > this.getY()) this.setY(this.getY()+(int)((15+this.vel)*Math.random()));
           else this.setY(this.getY()-(int)((15+this.vel)*Math.random()));
        }    
    }  
    
}
