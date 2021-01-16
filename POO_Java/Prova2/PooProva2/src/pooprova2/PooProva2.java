/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pooprova2;

/**
 *
 * @author Arthur
 */
public class PooProva2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ContaCorrente a = new ContaCorrente();
        ContaEspecial b = new ContaEspecial();
        a.depositar(500);
        b.depositar(1000);
        a.sacar(10);
        b.sacar(2000);
        b.limite = 2000;
        b.sacar(2000);
        a.transferir(20, b);
        Relatorio r = new Relatorio();
        r.gerarRelatorio(a);
        r.gerarRelatorio(b);
    }
    
}
