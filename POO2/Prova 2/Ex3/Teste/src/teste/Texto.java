package teste;

public class Texto implements AnaSint{ // Leaf
    private String s;
    
    public Texto(String s) {
        this.s = s;
    }
    public String execute() {
        return this.s;
    }
    
}
