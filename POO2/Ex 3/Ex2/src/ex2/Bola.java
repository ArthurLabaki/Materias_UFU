import java.util.Observable;

public class Bola extends Observable {

    private int x = 0;
    private int y = 0;  
    
    public Bola(int x, int y){
        this.x = x;
        this.y = y;
    }    
        
    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }    
    
    public void setPos(int x, int y) {
        this.x = x;
        this.y = y;        
        System.out.println("Posicao da Bola: ("+this.x+","+this.y+")");
    }
    
    public void show(){
        setChanged();
        notifyObservers();
    }
}