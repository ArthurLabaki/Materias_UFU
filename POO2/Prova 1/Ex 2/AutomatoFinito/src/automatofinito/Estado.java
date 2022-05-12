package automatofinito;

/*
Estados| S1 | S2 | S3 | S4
  ->S1 | {} |  a | {} | {}
    S2 |  b |  a | {} |  c
    S3 |  a | {} | {} |  b
   *S4 | {} | {} |  d | {}

*/

public abstract class Estado {
    private AutomatoFinito af;

    public Estado(AutomatoFinito af) {
        this.af = af;
        this.af.setErro(af.isErro());
    }

    public AutomatoFinito getAf() {
        return af;
    }

    public void setAf(AutomatoFinito af) {
        this.af = af;
    }

    protected abstract void proximoAutomato(char cad);
}
