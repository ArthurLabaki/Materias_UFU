package poo2.shield;

public class Escudo1 extends Escudo {

    public int reduzirDano(int dano) {
        int resto = dano - 1;  // valor negativo, escudo absorveu
                                // valor positivo, escudo quebrou      
        if (resto <= 0){
            System.out.println("Dano absorvido");
            return 0;
        }
        
        if (resto > 0 && getSucessor() != null){
           int x =getSucessor().reduzirDano(resto);
           return x;
        }
        
        if (resto > 0 && getSucessor() == null){
            System.out.println("Dano amenizado para "+ resto);
            return resto;
        }
        return -1111111;
            
    }
    
    public Escudo1(int x, int y) {
        this.setX(x);
        this.setY(y);
    }
    
}
