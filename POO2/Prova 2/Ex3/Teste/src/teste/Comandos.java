package teste;

public abstract class Comandos implements AnaSint{  // Composite
    private AnaSint com1;
    private AnaSint com2;
    public AnaSint[] comT;

    public Comandos(AnaSint com1, AnaSint com2, AnaSint comT[]) {
        this.com1 = com1;
        this.com2 = com2;
        this.comT = comT;
    }
    
    public AnaSint getCom1(){
        return this.com1;
    }
    
    public AnaSint getCom2(){
        return this.com2;
    }
    
    public AnaSint[] getComT(){
        return this.comT;
    }
}
