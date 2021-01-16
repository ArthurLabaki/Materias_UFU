
package pooprova2;

import java.util.ArrayList;

public class Banco implements Imprimivel {
    public int tamanho;
       ArrayList<ContaBancaria> listaDeContas = new ArrayList<>();

    public Banco() {     // Construtor para o tamanho
        this.tamanho = 0;
    }
       
       public void inserir(ContaCorrente o){  // Não sei se o ContaBancaria conta como os 2 tipos de conta
           listaDeContas.add(o);
           tamanho ++;
       }
       public void inserir(ContaEspecial o){  // Por isso criei 2 metodos 
           listaDeContas.add(o);
           tamanho ++;
       }
       
       public void remover (ContaCorrente o){
           listaDeContas.remove(o);
           tamanho --;
       }
       public void remover (ContaEspecial o){
           listaDeContas.remove(o);
           tamanho --;
       }
       
       public ContaBancaria procurarConta(int num){
           for(int x = 0; x<= tamanho; x++){
               if((listaDeContas.get(x)).nconta == num ){
                   return listaDeContas.get(x);
               }
           }
                System.out.println("Erro! Numero não existe"); // Não consegui fazer o erro
        return null;
        }

    @Override
    public void mostrarDados() {
        
    }
       
          
       
       
}
