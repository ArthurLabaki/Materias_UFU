package automatofinito;

public class S3 extends Estado{
    
    public S3(AutomatoFinito af) {
        super(af);
    }

    protected void proximoAutomato(char cad) {
        if (cad == 'a') this.getAf().setEstado(new S1(this.getAf()));
        else{ if (cad == 'b') this.getAf().setEstado(new S4(this.getAf()));
        else{ this.getAf().setErro(true);}
        }
    }
}
