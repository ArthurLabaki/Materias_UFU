package automatofinito;

public class S1 extends Estado{

    public S1(AutomatoFinito af) {
        super(af);
    }

    protected void proximoAutomato(char cad) {
        if (cad == 'a'){
            this.getAf().setEstado(new S2(this.getAf()));
        }
        else{
            this.getAf().setErro(true);}
    }
    
}
