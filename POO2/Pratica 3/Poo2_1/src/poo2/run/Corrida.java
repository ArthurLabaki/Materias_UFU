package poo2.run;

public abstract class Corrida{
    private int velocidade;
    
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
