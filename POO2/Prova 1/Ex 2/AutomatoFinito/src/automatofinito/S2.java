package automatofinito;

public class S2 extends Estado{
    
    public S2(AutomatoFinito af) {
        super(af);
    }

    protected void proximoAutomato(char cad) {
        if (cad == 'a') this.getAf().setEstado(new S2(this.getAf()));
        else{ if (cad == 'b') this.getAf().setEstado(new S1(this.getAf()));
            else{ if (cad == 'c') this.getAf().setEstado(new S4(this.getAf()));
            else{ this.getAf().setErro(true); }
            }
        }
    }
}


