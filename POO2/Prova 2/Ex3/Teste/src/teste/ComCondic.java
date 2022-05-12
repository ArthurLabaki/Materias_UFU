package teste;

public class ComCondic extends Comandos{    // Concrete Composite - Comando Condicional
    
    public ComCondic(AnaSint com1, AnaSint com2) {
        super(com1, com2, null);
    }
    
    public String execute() {
        double num = Math.random();
        if(num < 0.5){
            return this.getCom1().execute();
        }
        else{
            return this.getCom2().execute();
        }
    }

}
