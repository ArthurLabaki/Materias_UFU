package poo2.shield;

public class Escudo5 extends Escudo {
    
    public int reduzirDano(int dano) {
        int resto = dano - qntescudo;     
        
        if (resto <= 0){        // Valor negativo, escudo absorveu 
            System.out.println("Dano absorvido");
            return 0;
        }
        
        if (resto > 0 && getSucessor() != null){    // Escudo não absorveu, mas tem outros escudos
           int x =getSucessor().reduzirDano(resto);
           return x;
        }
        
        if (resto > 0 && getSucessor() == null){        // Valor positivo, escudo não absorveu
            System.out.println("Dano amenizado para "+ resto);
            return resto;
        }
        return -1111111;    // ERRO       
    }
    
     // Construtor
    public Escudo5(int x, int y) {
        this.setX(x);
        this.setY(y);
        this.qntescudo = 5;
    }
    
}
