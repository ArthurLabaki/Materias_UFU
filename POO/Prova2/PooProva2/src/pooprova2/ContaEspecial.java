
package pooprova2;

/**
 *
 * @author Arthur
 */
public class ContaEspecial extends ContaBancaria implements Imprimivel{
    public double limite;
    
    @Override
    public void sacar(double s) {
      if(saldo - s < 0){
          if(saldo + limite - s < 0)
            System.out.println("Saldo e limite Insuficiente");
          else{
              saldo = saldo - s;
              System.out.println("Seu novo Saldo é: " + saldo);
              System.out.println("Limite Utilizado");
          }    
        }
        else{
            saldo = saldo - s;
            System.out.println("Seu novo Saldo é: " + saldo);
        }
    }

    @Override
    public void depositar(double d) {
        if(d < 0){
            System.out.println("Valor Invalido");
        }
        else{
            saldo = saldo + d;
            System.out.println("Seu novo Saldo é: " + saldo);
        }
    }

    @Override
    public void mostrarDados() {
        System.out.println("Numero da conta: " + nconta);
        System.out.println("Saldo atual: " + saldo);
        System.out.println("Limite disponivel: " + limite);
    }
    
}
