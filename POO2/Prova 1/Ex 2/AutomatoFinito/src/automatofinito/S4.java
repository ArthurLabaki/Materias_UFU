package automatofinito;

public class S4 extends Estado{
    public S4(AutomatoFinito af) {
        super(af);
    }

    protected void proximoAutomato(char cad) {
        if (cad == 'd') this.getAf().setEstado(new S3(this.getAf()));
        else{this.getAf().setErro(true);}
    }
}
