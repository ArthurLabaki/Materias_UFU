package prova3poo;


public class Material implements Comparable {

    private String descrição;
    private float preço;
    private int quantidade;
    private final String codigoMat;  // 5 + DV

    public Material(String codigoMat) {
        this.codigoMat = setCodigoBarra(codigoMat);
    }

    public int getDV(String num) {
        int soma = 0;
        int resto = 0;
        int dv = 0;
        String[] numeros = new String[num.length() + 1];
        int multiplicador = 2;
        String aux;
        String aux2;
        String aux3;
        for (int i = num.length(); i > 0; i--) {
            //Multiplica da direita pra esquerda, alternando os algarismos 2 e 1
            if (multiplicador % 2 == 0) {
                // pega cada numero isoladamente  
                numeros[i] = String.valueOf(Integer.valueOf(num.substring(i - 1, i)) * 2);
                multiplicador = 1;
            } else {
                numeros[i] = String.valueOf(Integer.valueOf(num.substring(i - 1, i)) * 1);
                multiplicador = 2;
            }
        }
        // Realiza a soma dos campos de acordo com a regra
        for (int i = (numeros.length - 1); i > 0; i--) {
            aux = String.valueOf(Integer.valueOf(numeros[i]));

            if (aux.length() > 1) {
                aux2 = aux.substring(0, aux.length() - 1);
                aux3 = aux.substring(aux.length() - 1, aux.length());
                numeros[i] = String.valueOf(Integer.valueOf(aux2) + Integer.valueOf(aux3));
            } else {
                numeros[i] = aux;
            }
        }
        //Realiza a soma de todos os elementos do array e calcula o digito verificador
        //na base 10 de acordo com a regra.	    
        for (int i = numeros.length; i > 0; i--) {
            if (numeros[i - 1] != null) {
                soma += Integer.valueOf(numeros[i - 1]);
            }
        }
        resto = soma % 10;
        dv = 10 - resto;
        return dv;
    }
    public boolean validaDV(String num, int dv) {
        if(getDV(num) == dv){
            return true;
        }
        else{
            return false;
        }
    }
    public String setCodigoBarra (String cod) {
        String num = cod.substring(0, cod.length() - 1);
        int DV = Character.getNumericValue(cod.charAt(cod.length() -1));
        if(validaDV(num, DV) == false){
            throw new IllegalArgumentException("Codigo Invalido!");
        }
        else{
            return cod;
        }
    }
    public boolean equals(Material a){
        if(a.codigoMat.equals(this.codigoMat)){
            return true;
        }
        else{
            return false;
        }
    }

    public String getDescrição() {
        return descrição;
    }

    public void setDescrição(String descrição) {
        this.descrição = descrição;
    }

    public float getPreço() {
        return preço;
    }

    public void setPreço(float preço) {
        this.preço = preço;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
    @Override
    public String toString (){
        return "Descreição: "+ this.descrição + "Preça: "+ this.preço + "Quantidade: "+ this.quantidade + "Codigo: "+ this.codigoMat ;
    }

    public String getCodigoMat() {
        return codigoMat;
    }

    @Override
    public int compareTo(Object t) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    //Tempo
    
}
