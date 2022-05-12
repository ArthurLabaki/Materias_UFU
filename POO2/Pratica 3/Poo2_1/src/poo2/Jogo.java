package poo2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.BoxLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.border.BevelBorder;
import poo2.enemy.Inimigo;
import poo2.enemy.Inimigo1;
import poo2.enemy.Inimigo2;
import poo2.enemy.Inimigo3;

public class Jogo extends JPanel {
    
    private Personagem1 pers;
    Inimigo inimigos[] = new Inimigo[3];
    //JLabel l1, l2;
    

    public Jogo() {
        inimigos[0] = new Inimigo1(10,450);
        inimigos[1] = new Inimigo2(30,30);
        inimigos[2] = new Inimigo3(1500,800);
        pers = new Personagem1(inimigos);
        addKeyListener(pers);
        setFocusable(true);
    }
    
    
     public void paint(Graphics g){
        super.paint(g); 

        Graphics2D g2d = (Graphics2D) g;
        //g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        g2d.setColor(Color.BLACK);
        g2d.fillOval(pers.getX(), pers.getY(), 30, 30);
        
        g2d.setColor(Color.CYAN);
        g2d.fillOval(inimigos[0].getX(), inimigos[0].getY(), 30, 30);
        
        g2d.setColor(Color.GREEN);
        g2d.fillOval(inimigos[1].getX(), inimigos[1].getY(), 20, 20);
        
        g2d.setColor(Color.RED);
        g2d.fillOval(inimigos[2].getX(), inimigos[2].getY(),40, 40);
        
         
     }
         
    public void jogar (Jogo jogo) throws InterruptedException{
        JFrame frame = new JFrame("Jogo Poo");
        frame.setLayout(new BorderLayout());
        frame.setSize(1600,900);
        int vida = pers.getVida();
        int qntini = pers.countObservers();
        JPanel painel = new JPanel();
        JLabel l1 = new JLabel(" Quantidade de inimigos restantes: "+qntini+" Vida do personagem: "+vida);
        l1.setFont(new Font("Serif", Font.BOLD, 20));
        
        painel.setBorder(new BevelBorder(BevelBorder.LOWERED));
        frame.add(painel, BorderLayout.SOUTH);
        painel.setPreferredSize(new Dimension(frame.getWidth(), 50));
        painel.setLayout(new BoxLayout(painel, BoxLayout.X_AXIS));
        
        l1.setHorizontalAlignment(SwingConstants.LEFT);
        painel.add(l1);
        
        frame.add(jogo);
        
        
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
        
        
        
        pers.addObserver(inimigos[0]);
        pers.addObserver(inimigos[1]);
        pers.addObserver(inimigos[2]);
       
        
        while (true) {
            pers.show(); 
            vida = pers.getVida();
            qntini = pers.countObservers();
            jogo.repaint();
            Thread.sleep(50);
            for (int i=0; i < 3; i++){
                if (inimigos[i].getVida() == 0){
                    pers.deleteObserver(inimigos[i]);
                }
            }
           l1.setText("                             Quantidade de inimigos restantes: "+qntini+ "                         "+
                   "                                                                                                       "+
                   "           Vida do personagem: "+vida);
            
            if (pers.getVida() == 0){
                System.out.println("FIM DO JOGO"); // colocar a layer de fim de jogo
                break;
            }
            
        } 
        Thread.sleep(2000);
        //frame.setVisible(false);
        System.exit(0);
    }
}
