package teste;

public class ComSimples extends Comandos{   // Concrete Composite - Comando Simples

    public ComSimples(AnaSint comandos) {
        super(comandos, null, null);
    }
    
    public String execute() {
        return this.getCom1().execute();
    }
    
}
