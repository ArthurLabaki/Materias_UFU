package client;

public class DepCompras { // Departamento de compras (invoker) 
    private PedRep[] slot = new PedRep[10];
    
    public DepCompras(){
    }
    
    public void setCommand(PedRep ped, int i){
        slot[i] = ped;
        //System.out.println(ped);
    }
    public void fazerCompra(int i) {
        slot[i].execute();
    }
    public void fazerCompraTodos(){ // Realiza todos os pedidos
        for (int i = 0; i < 10; i++){
            if (slot[i] != null){
                System.out.println("\nExecutando pedido " + i);
                slot[i].execute();
            }
        }
   
    }
    
}
