package poo2.level;

import java.util.List;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Projeto implements Component{
    private List<Component> comp;

    public Projeto(List<Component> comp) {
        this.comp = comp;
    }
    
    public void addComps(Component comp){
        this.comp.add(comp);
    }

    public void jogarFase() {
        Fase compi = (Fase) comp.get(0);
        do{
            if (compi == null)
                break;
            compi.jogarFase();
            System.out.println("Deseja ir pelo caminho seguro (s) pelo dificil (d)?");
            Scanner input = new Scanner(System.in);
            String s = input.next();
            if(s == "s" || s == "seguro" )
                compi=compi.prox1;
            else{
                compi=compi.prox1;    }
        }while(true);
        System.out.println("Parabens, voce venceu o jogo!!");
        try {
            Thread.sleep(2000);
            
        } catch (InterruptedException ex) {
            Logger.getLogger(Projeto.class.getName()).log(Level.SEVERE, null, ex);
        }
    }   
    
}
