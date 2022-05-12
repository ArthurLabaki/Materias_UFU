
/**
 * Write a description of class Jogador here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Jogador extends Robo
{
    private String nome;
    public Jogador(int x, int y, String nome){
        super(x,y);
        this.nome = nome;
    }

    public void chuta(Bola bola){
    
        //se estiver em distancia de chute
        if ( ( (this.getX() - bola.getX()) <2) && ((this.getY() - bola.getY()) <2) ){
            System.out.println("Jogador: "+this+" chuta bola..." );
            if (Math.random() < 0.5){
                bola.setPos(bola.getX()+(int)(100*Math.random()), bola.getY()-(int)(100*Math.random()));
            }
            else {
                bola.setPos(bola.getX()-(int)(100*Math.random()), bola.getY()+(int)(100*Math.random()));
            }
        }
        
    }
    
    public String toString(){
        return this.nome;
    }    
}
