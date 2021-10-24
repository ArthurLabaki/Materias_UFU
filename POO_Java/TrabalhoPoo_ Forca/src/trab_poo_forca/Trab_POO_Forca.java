package trab_poo_forca;

import java.util.Random; // numero aleatorio
import java.util.Scanner; // Leitura do teclado

public class Trab_POO_Forca {

    public static void main(String[] args) {
        System.out.println("Bem-Vindo ao Jogo da Forca!");
        System.out.println("Utilize apenas letras minúsculas (a,b,c,...,y,x,z)");
        System.out.println("Fique tranquilo, as palavras não tem nenhum acento (´,^,~,`)\n");

        String[] Palavra = {"ouro", "gladiador", "humano", "carnaval", "palavras", "roda", "abacaxi", "carta", "tocha", "escova",
            "trevo", "mulher", "alarme", "romance", "professor", "java", "pinturas", "soma", "mosquito", "rio", "brasil", "laranja", "filhote",
            "rins", "sol", "vida", "foguete", "guitarra", "coruja", "nicotina"};  // Array de Palavras (30)

        Random random = new Random();
        int num_ale = random.nextInt(30);    // Sorteia um numero aleatorio ateh 30 (0->29)

        int tamanho = Palavra[num_ale].length();   // Cria um inteiro com o tamanho da palavra escolhida

        char[] l = new char[26];    // Cria um array de char para mostrar as leras digitadas
        
        int limite = (Palavra[num_ale].length() / 2) + 1;  // Numero de tentativas
        
        char[] unders = new char[Palavra[num_ale].length()];
        for (int i = 0; i < Palavra[num_ale].length(); i++) {   // Cria um vetor de char para cada letra da palavra e salva-os como '_'
            unders[i] = '_';
        }
        
        int k = 0;      // Numero de Rodadas Jogadas
        
        while (tamanho > 0 && limite != 0) {    //Repete até acertar todas ou acabar o limite
            System.out.println("O número de tentativas é: " + limite);  // imprime as tentativas
            
            for (int i = 0; i < Palavra[num_ale].length(); i++) {   // Imprime o vetor de char
                System.out.print(" " + unders[i] + " ");
            }
 
            System.out.println("\n ");
            
            Scanner letra = new Scanner(System.in);
            System.out.println("Digite uma letra: ");   // Le uma letra do teclado e salva em l[]
            l[k] = letra.nextLine().charAt(0);
            
            boolean acerto = false;    
            boolean repetida = false;
            
            for(int i = 0; i < k; i++){     // Loop para ver se a letra digitada é repetida
                if (l[k] == l[i]){
                    repetida = true;
                    System.out.println("\nLetra Repetida!");
                }
            }
            
            for (int j = 0; j < Palavra[num_ale].length(); j++) {   // Loop do tamanho da palavra a ser descoberta
                if(repetida == true){   // Se a letra for repetida, o jogo ira ignora-la, ou seja, não diminuira o tamanho e o limite
                    acerto = true;
                }
                else if (l[k] == Palavra[num_ale].charAt(j)) {  // Loop para verificar se a letra digitada existe na palavra
                    unders[j] = l[k];       // Se ela existe, diminuira 1 do tamanho, substitui a o traco pela letra (respectivamente)
                    tamanho--;              // E garante um acerto true
                    acerto = true;
                }
                
            }
            
            k++;    // Soma 1 no numero da rodada
            
            if (acerto == false) {      //Se não foi acertado a letra, é tirado 1 do limite
                limite--;
            }
            
            System.out.print("\nLetras Digitadas: ");   // Imprime as letras digitadas
            for(int i = 0; i != k; i++){
                System.out.print(l[i]+ " ");
            }
            System.out.println();
        }
        System.out.println();
        
        if(limite == 0){ // Verifica se foi vitoria ou derrota
            System.out.println("Infelizmente você perdeu!");
            System.out.println("A palavra era: "+Palavra[num_ale]);
        }
        else{
            System.out.println("Parabéns!!! Você ganhouu!!");
        }
    }
}
