package poo2.run;

public abstract class Corrida{
    private int velocidade; // Velocidade de movimento
    
    // Velocidade rapida = 15
    // Velocidade media = 10
    // Velocidade devagar = 5
    
    public abstract void correr();

    public int getVelocidade() {
        return velocidade;
    }

    public void setVelocidade(int velocidade) {
        this.velocidade = velocidade;
    }
    
    public Corrida() {
        this.velocidade = 10;
    }
       
}
