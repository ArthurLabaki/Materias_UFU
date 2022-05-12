package automatofinito;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 1 POO2
*/

public class AutomatoFinito {
    private Estado estado;
    private String cadeia;
     private boolean erro; // caso não tenha a cadeia em suas transições (ex: S1 - b) - não existe essa transição, automato falha

    public Estado getEstado() {
        return estado;
    }

    public void setEstado(Estado estado) {
        this.estado = estado;
    }

    public String getCadeia() {
        return cadeia;
    }

    public void setCadeia(String cadeia) {
        this.cadeia = cadeia;
    }

    public boolean isErro() {
        return erro;
    }

    public void setErro(boolean erro) {
        this.erro = erro;
    }
    
    public AutomatoFinito() {
        this.estado = new S1(this);
    }
    
    public AutomatoFinito(String cadeia) {
        this.cadeia = cadeia;
        this.estado = new S1(this);
    }
    
    public void pertence(){
        char c;
        //System.out.println(estado.getClass().getName());   // Printar primeiro estado
        for (int i = 0; i < cadeia.length(); i++){
            c = cadeia.charAt(i);
            estado.proximoAutomato(c);
            //System.out.println(estado.getClass().getName());   // Printar estados
        }
        if (estado.getClass() == S4.class && this.erro == false){
            System.out.println(cadeia+" - Cadeia pertence ao automato!");
        }
        else {
            System.out.println(cadeia+" - Cadeia não pertence ao automato!");
        }
        this.setEstado(new S1(this)); // resetar automato (comeca em S1)
        this.setErro(false); 
    }
    
    public void testarCadeia(String c){
        this.setCadeia(c);
        pertence();
    }

    public static void main(String[] args) {
      AutomatoFinito af = new AutomatoFinito("aaacdb");
      af.pertence();
      //AutomatoFinito af1 = new AutomatoFinito();   //Tambem funciona
      //af.testarCadeia("aaacdb");
      af.testarCadeia("ababacdaaac");
      af.testarCadeia("abcdb");
      af.testarCadeia("acda");
      af.testarCadeia("acdbdb");
    }
    
}
