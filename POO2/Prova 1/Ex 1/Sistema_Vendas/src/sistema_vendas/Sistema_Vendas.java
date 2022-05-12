package sistema_vendas;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 1 POO2
*/

public class Sistema_Vendas {
    private int quantidade;
    private Estados estado;

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public Estados getEstado() {
        return estado;
    }

    public void setEstado(Estados estado) {
        this.estado = estado;
    }
    

    public Sistema_Vendas() {
        this.quantidade = 0; // setando quanttidade
        this.estado = new Indisponivel(this); // comeca no indisponivel
    }
    
    public void compra(int qnt){
        System.out.println("Compra de "+qnt+" Unidades");
        estado.compra(qnt);
        System.out.println("Nova quantidade: "+this.quantidade);
        System.out.println("Estado: "+ this.estado.getClass().getName());
        System.out.println("\n");
    }
    
    public void venda(int qnt){
        System.out.println("Venda de "+qnt+" Unidades");
        estado.venda(qnt);
        if(this.estado.getClass() == EstoqueCritico.class){
            System.out.println("Estoque critico! É necessario repor o estoque!");}
        System.out.println("Nova quantidade: "+this.quantidade);
        System.out.println("Estado: "+ this.estado.getClass().getName());
        System.out.println("\n");
    } 
    
    public static void main(String[] args) {
       Sistema_Vendas conta = new Sistema_Vendas();
       
       conta.venda(1);  // venda maior que o disponivel
       conta.compra(4); // estoqueCritico
       conta.compra(1); 
       conta.venda(12); // venda maior que o disponivel
       conta.venda(2);  
       conta.venda(1);  
       conta.compra(12);// disponivel
       conta.venda(3);  
       conta.venda(1);  // estoqueCritico
       conta.venda(1);
       conta.compra(90);// disponivel
       conta.venda(98); // estoqueCritico
       conta.venda(2);  // venda maior que o disponivel
       conta.venda(1);  // indisponivel
       conta.compra(-7);
       conta.compra(17); // consegue passar de Indisponivel para disponivel sem passar pelo estoque critico
       conta.venda(-2);
    }
    
}
