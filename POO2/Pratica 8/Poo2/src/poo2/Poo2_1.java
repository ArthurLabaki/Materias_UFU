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

import java.util.ArrayList;
import poo2.level.Component;
import poo2.level.Fase;
import poo2.level.Projeto;

public class Poo2_1 {

    public static void main(String[] args) throws InterruptedException {
        Projeto p = new Projeto(new ArrayList<Component>());
        Fase ffinal = new Fase(10, 9, "fasef", null, null);
        Fase f9 = new Fase(7, 9, "fase9", ffinal, ffinal);
        Fase f8 = new Fase(7, 8, "fase8", f9, f9);
        Fase f7 = new Fase(6, 5, "fase7", f8, f9);
        Fase f6 = new Fase(5, 5, "fase6", f7, f8);
        Fase f5 = new Fase(5, 2, "fase5", f6, f7);
        Fase f4 = new Fase(3, 1, "fase4", f5, f6);
        Fase f3 = new Fase(3, 0, "fase3", f4, f5);
        Fase f2 = new Fase(2, 0, "fase2", f3, f4);
        Fase f1 = new Fase(1, 0, "fase1", f2, f3);
        p.addComps(f1);
        p.addComps(f2);
        p.addComps(f3);
        p.addComps(f4);
        p.addComps(f5);
        p.addComps(f6);
        p.addComps(f7);
        p.addComps(f8);
        p.addComps(f9);
        p.addComps(ffinal);
        
        p.jogarFase();
       //j.jogar(j);
    }
    
}
