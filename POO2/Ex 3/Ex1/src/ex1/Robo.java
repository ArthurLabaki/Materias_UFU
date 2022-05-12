
public class Robo implements Observador {
    private int x;
    private int y;
    
    public Robo(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    public void update(Sujeito s) {

        Bola bola = (Bola)s;
        
        //se estiver em distancia de chute
        if ( ( (this.x - bola.getX()) == 0) && ( (this.y - bola.getY()) == 0) ){
            System.out.println("Jogador: "+this+" chuta bola..." );
            if (Math.random() < 0.5){
                bola.setPos(bola.getX()+5, bola.getY()-5);
            }
            else {
                bola.setPos(bola.getX()-5, bola.getY()+5);
            }
        }
        //se precisar andar em direcao a bola
        else {
           //se precisa andar para frente 
           if (bola.getX() > this.x) this.x = this.x+1;
           else this.x = this.x-1;
           //se precisa andar para tras
           if (bola.getY() > this.y) this.y = this.y+1;
           else this.y = this.y-1;
     
        }                        
    }
}