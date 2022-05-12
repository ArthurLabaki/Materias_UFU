package teste;

public class ComComp extends Comandos{  // Concrete Composite - Comando Composto
    
    public ComComp(AnaSint[] com) {  
        super(null, null, com);
    }
    
    public String execute() {
        String t = "";  // inicia a tring vazia
        for (int i = 0; i < this.getComT().length; i++){
            t =  t + this.getComT()[i].execute();  // executa todos os comandos e guarda a string
        }
        return t;
    }

}
