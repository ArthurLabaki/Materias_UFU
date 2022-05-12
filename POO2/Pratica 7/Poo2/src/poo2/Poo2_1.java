/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
Programação Orientada a Objetos 2
//
Depois de escolher o personagem, clique na nova janela para jogar
Circulo preto é o personagem
Outros circulos são os inimigos
Quadrados azuis são os escudos
Quadrados laranjas são os poderes
//
Controles:
Movimentos são as setinhas (Arrow keys)
Atacar inimigos é o espaço
Pegar escudos e poderes é a tecla E
*/
package poo2;

public class Poo2_1 {

    public static void main(String[] args) throws InterruptedException {
       Jogo j = new Jogo();
       j.jogar(j);
    }
    
}
