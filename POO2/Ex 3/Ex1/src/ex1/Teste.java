

public class Teste
{
    public static void main(String args[])throws InterruptedException {
        Bola bola = new Bola(0,0);
        Robo j1 = new Robo(15,20);
        Robo j2 = new Robo(20,20);
        Robo j3 = new Robo(5,5);
        Robo j4 = new Robo(10,20);
        Robo j5 = new Robo(1,5);
        Robo j6 = new Robo(20,10);
        Robo j7 = new Robo(2,15);
        
        bola.addObserver(j1);
        bola.addObserver(j2);
        bola.addObserver(j3);        
        bola.addObserver(j4);        
        bola.addObserver(j5);        
        bola.addObserver(j6);        
        bola.addObserver(j7);        
        
        while(true){
            bola.show();
            Thread.sleep(200);
        }
    }
}
