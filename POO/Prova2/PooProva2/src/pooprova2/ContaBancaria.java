/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pooprova2;

public abstract class ContaBancaria {
    public int nconta;
    public double saldo;
    public abstract void sacar (double s);
    public abstract void depositar (double d);
    
    public void transferir (double v,ContaBancaria a){
        double x = this.saldo;  // Criei uma variavel para verificar se sao iguais depois de sacar
        this.sacar(v);
        if(x != saldo){     // Se forem iguais significa que não foi sacado e não sera depositado
        a.depositar(v);
       }
        else {
            System.out.println("Erro ao sacar");
        }
    }
}
