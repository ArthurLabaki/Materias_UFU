package client;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 2 POO2
*/

public class Client { // Aplicação cliente (client)

    public static void main(String[] args) {
        
        // Criando os objetos
        Fornecedor f1 = new Fornecedor();
        Fornecedor f2 = new Fornecedor();
        DepCompras dep = new DepCompras();
        Pedido p1 = new Pedido(f1);
        Pedido p2 = new Pedido(f2);
        
        // Criando os pedidos no departamento de compras
        //p.execute();
        dep.setCommand(p1, 1); // pedido 1
        dep.setCommand(p2, 2); // pedido 2
        dep.setCommand(p2, 6); // pedido 6
        
        // Departamento de compras realizando os pedidos
        dep.fazerCompra(1);
        dep.fazerCompra(2); 
        dep.fazerCompra(6); 
        dep.fazerCompraTodos(); // Realiza todos os pedidos
        
    }
    
}
