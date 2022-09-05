package prova3poo;

import javax.swing.JOptionPane;
 
//Aluno -- Matricula
//Arthur do Prado Labaki -- 11821BCC017
//Carlos Augusto Gomes Neto -- 11821BCC016

public class Papelaria {


    public static void main(String[] args) {
         Material[] array = new Material[5];
         array[0] = new Material("615336");
         array[1] = new Material("2615334");
         array[2] = new Material("225706");
         array[3] = new Material("131573");
         array[4] = new Material("981753");
         System.out.println(array[0].toString());
         System.out.println(array[1].toString());
         System.out.println(array[2].toString());
         System.out.println(array[3].toString());
         System.out.println(array[4].toString());
         Material a = new Material("131573");   //Elemento criado é igual ao array [3]
         Material b = new Material("772319");   //Elemento criado é valido, mas não esta no array
         if(busca(a, array) != -1){
             System.out.println("Elemento na posição " + (busca(a, array) +1)); //Posição de 1 a 5 (ou tirar o +1 para ser de 0 a 4)
         }
        if(busca(b, array) != -1){
             System.out.println("Elemento na posição " + (busca(a, array) +1)); //Posição de 1 a 5 (ou tirar o +1 para ser de 0 a 4)
         }
        
    }
    
     public static int busca (Material a, Material[] array){
         for(int i =0; i < 5;i++){ // Tamanho do array eh 5
          if(a.getCodigoMat().equals(array[i].getCodigoMat())){
              return i;
          }
        }
         JOptionPane.showMessageDialog(null,"\n Buca não encontrou o material!\n");
        return -1; //Erro
     }
}