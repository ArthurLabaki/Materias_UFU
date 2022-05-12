import java.util.Observer;
import java.util.Observable;

public class Robo implements Observer {
    private int x;
    private int y;
    
    public int getX() {return this.x;}
    public int getY() {return this.y;}    

    public void setX(int x){this.x = x; }           
    
    public void setY(int y){this.y = y; }           
    
    
    public Robo(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    public void update(Observable subject, Object arg) {

        Bola bola = (Bola)subject;
        
        //se estiver em distancia de chute
        if ( ( (this.x - bola.getX()) ==0) && ((this.y - bola.getY()) ==0) ){
            System.out.println("Jogador: "+this+" chuta bola..." );
            if (Math.random() < 0.5){
                bola.setPos(bola.getX()+(int)(100*Math.random()), bola.getY()-(int)(100*Math.random()));
            }
            else {
                bola.setPos(bola.getX()-(int)(100*Math.random()), bola.getY()+(int)(100*Math.random()));
            }
        }
        //se precisar andar em direcao a bola
        else {
           //se precisa andar para frente 
           if (bola.getX() > this.x) this.x = this.x+(int)(5*Math.random());
           else this.x = this.x-(int)(5*Math.random());
           //se precisa andar para tras
           if (bola.getY() > this.y) this.y = this.y+(int)(5*Math.random());
           else this.y = this.y-(int)(5*Math.random());
     
        }
        
        if (bola.getX() < 0) bola.setX(100);
        if (bola.getY() < 0) bola.setY(100);
        
    }
}