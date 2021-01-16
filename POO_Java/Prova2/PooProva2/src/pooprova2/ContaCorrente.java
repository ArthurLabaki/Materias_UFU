package pooprova2;

public class ContaCorrente extends ContaBancaria implements Imprimivel {
    public double taxaDeOperação;
    
    @Override
    public void sacar (double s){
        if(saldo - (s + taxaDeOperação) < 0){
            System.out.println("Saldo Insuficiente");
        }
        else{
            saldo = saldo - (s + taxaDeOperação);
            System.out.println("Seu novo Saldo é: " + saldo);
        }
    }
    @Override
    public void depositar (double d){
         if(d - taxaDeOperação < 0){
            System.out.println("Valor Invalido");
        }
        else{
            saldo = saldo + (d - taxaDeOperação);
            System.out.println("Seu novo Saldo é: " + saldo);
        }
    }

    @Override
    public void mostrarDados() {
        System.out.println("Numero da conta: " + nconta);
        System.out.println("Saldo atual: " + saldo);
        System.out.println("Taxa atual da conta: " + taxaDeOperação);
    }
}
