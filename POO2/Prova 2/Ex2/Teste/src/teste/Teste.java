package teste;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 2 POO2
*/

public class Teste {

    public static void main(String[] args) {
        
        // Caso queira usar por linha de comando
        //AbstractFactory fac = obterFactory(args[0]);
        
        // Criando fábricas aleatárias
        AbstractFactory facr1 = obterFactoryrandom();
        AbstractFactory facr2 = obterFactoryrandom();
        AbstractFactory facr3 = obterFactoryrandom();
        
        //contruindo o copo
        //Copo copo = fac.fabricarCopo();   //Por linha de comando
        Copo copo = facr1.fabricarCopo();
        copo.construir();
        
        //contruindo a garrafa
        //Garrafa garrafa = fac.fabricarGarrafa();   //Por linha de comando
        Garrafa garrafa = facr2.fabricarGarrafa();
        garrafa.construir();
        
        //contruindo o prato
        //Prato prato = fac.fabricarPrato();  //Por linha de comando
        Prato prato = facr3.fabricarPrato();
        prato.construir();
    }
    
    public static AbstractFactory obterFactory(String s) {  // Obter fábrica
         if (s.equals("2")) {
             return new Factory2D();
         }
         else {
             return new Factory3D();
         }
    }
     
    public static AbstractFactory  obterFactoryrandom(){  // Obter fábrica aleatória
        double random = Math.random();
        if (random <= 0.5) {
             return new Factory2D();
         }
         else {
             return new Factory3D();
         }
    }
    
}
