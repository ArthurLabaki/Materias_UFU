package formas;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 1 POO2
*/

public abstract class Formas {
    private String tipo;

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    
    public String desenhar(){ // getTipo
        return tipo;
    }
    
    public void mostrar (){ // Metodo que printa na tela
        System.out.println(this.desenhar());
    }
    
    public static void main(String[] args) {
        // Criando os ConcreteComponent
        Formas forma1 = new Quadrado(); 
        Formas forma2 = new Circulo();
        // Mostrando na tela
        forma1.mostrar();    
        forma2.mostrar();
        // Intanciando os ConcreteDecorator
        forma1 = new Preenchimento(forma1); 
        forma2 = new Preenchimento(forma2);
        forma2 = new Luz(forma2);
        // Mostrando na tela 
        forma1.mostrar();   
        forma2.mostrar();
    }
    
}
