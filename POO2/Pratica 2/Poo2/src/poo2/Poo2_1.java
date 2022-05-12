/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Programação Orientada a Objetos 2
*/
// OBS: Não foi feito o tratamento de pular de estado, como do perigo para o forte.
package poo2;

public class Poo2_1 {

    public static void main(String[] args) {
        // TODO code application logic here
        Personagem1 p1 = new Personagem1();
        Personagem2 p2 = new Personagem2();
        Personagem3 p3 = new Personagem3();
        p1.status();
        p1.perderVida(10);
        p1.status();
        p1.perderVida(40);
        p1.status();
        p1.perderVida(20);
        p1.status();
        p1.perderVida(20);
        p1.status();
        p1.ganharVida(30);
        p1.status();
        p1.ganharVida(1);
        p1.status();
        p1.ganharVida(20);
        p1.status();
        p1.ganharVida(400);
        p1.status();
        p1.ganharVida(400);
        p1.status();
        p1.ganharVida(20);
        p1.status();
    }
    
}
