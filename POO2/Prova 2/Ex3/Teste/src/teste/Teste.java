package teste;

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Prova 2 POO2
*/

public class Teste {

    public static void main(String[] args) {
        
        AnaSint comando = new Texto("Comando1");
        System.out.println(comando.execute());
        
        Texto[] comandos = new Texto[3];
        comandos[0] = new Texto("Com1 ");
        comandos[1] = new Texto("Com3 ");
        comandos[2] = new Texto("Com3 ");
         
        comando = new ComSimples(new Texto("Comando Simples"));
        System.out.println(comando.execute());
        
        comando = new ComComp(comandos);
        System.out.println(comando.execute());
        
        comando = new ComCondic(new Texto("Comando IF"), new Texto("Comando ELSE"));
        System.out.println(comando.execute());
        
        comando = new ComCondic(new ComSimples(new Texto("Comando Simples")), new ComComp(comandos));
        System.out.println(comando.execute());
    }
    
}
