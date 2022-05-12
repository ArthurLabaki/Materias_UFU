package poo2;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import static java.lang.System.exit;
import java.util.Scanner;
import javax.swing.BoxLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.border.BevelBorder;
import poo2.abs_factory.FacFuturista;
import poo2.abs_factory.FacMedieval;
import poo2.enemy.Inimigo;
import poo2.enemy.Inimigo1;
import poo2.enemy.Inimigo2;
import poo2.enemy.Inimigo3;
import poo2.factory.SimplePersonagemFactoryA;
import poo2.factory.SimplePersonagemFactoryB;
import poo2.shield.Escudo;
import poo2.shield.Escudo1;
import poo2.shield.Escudo10;
import poo2.shield.Escudo5;

public class Jogo extends JPanel {
    
    // Criando personagens, inimigos e escudos (usei um lugar fixo para poderes, para facilitar o codigo)
    public Personagem pers;
    //Inimigo inimigos[];
    public Inimigo inimigos[] = new Inimigo[10];
    public Escudo e1 = new Escudo1(0,0);
    public Escudo e5 = new Escudo1(0,0);
    public Escudo e10 = new Escudo1(0,0);
    

    public Jogo(){ // Escolher o personagem e adicionar o KeyListener
        /*
        System.out.println("Deseja jogar como qual personagem?"); // não entendi o porque do pulo, se o jogo é visto de cima
        System.out.println("1 - Personagem A, movimento medio e ataque forte");
        System.out.println("2 - Personagem B, movimento rapido e ataque medio");
        System.out.println("3 - Personagem C, movimento rapido e ataque forte");
        Scanner input = new Scanner(System.in);
        String s = input.next();
        */
        
        // Instanciando inimigos
        //inimigos[0] = new Inimigo1(10,450);
        //inimigos[1] = new Inimigo2(30,30);
        //inimigos[2] = new Inimigo3(1500,800);
        /*
        if ("a".equals(s) || "A".equals(s) || "1".equals(s)){
            pers = new Personagem1(inimigos, e1, e5, e10);}
        else{ if ("b".equals(s) || "B".equals(s) || "2".equals(s)){
                pers = new Personagem2(inimigos, e1, e5, e10);}
            else{ if ("c".equals(s) || "C".equals(s) || "3".equals(s)){
                    pers = new Personagem3(inimigos, e1, e5, e10);}
                else {
                    System.out.println("Erro no input");
                    exit(1);}}}
        */
         /*
        SimplePersonagemFactoryA facB = SimplePersonagemFactoryA.getInstance();
        SimplePersonagemFactoryB facB = SimplePersonagemFactoryB.getInstance();
        facB.jogar();
        facB.createInimigo(1);
        inimigos = facB.ini;
        e1 = facB.e1;
        e5 = facB.e2;
        e10 = facB.e3;
        pers = facB.pers;
       */
         /*
        FacFuturista fmed = FacFuturista.getInstance(); // futurista
        //FacMedieval fmed = FacMedieval.getInstance(); // medieval
        this.inimigos[0] = fmed.criarIni(0);
        this.inimigos[1] = fmed.criarIni(1);
        this.inimigos[2] = fmed.criarIni(2);
        this.inimigos[3] = fmed.criarIni(2);
        this.inimigos[3].setVida(0);
        this.e1 = fmed.criarEsc(1);
        this.e5 = fmed.criarEsc(2);
        this.e10 = fmed.criarEsc(3);
        this.pers = fmed.criarPers();
        */
        
        //pers.status();
        //addKeyListener(pers);
        //setFocusable(true);
    }
    
    
     public void paint(Graphics g){ // Desenhar todos os objetos, tanto inimigos, escudos, poderes e o personagem
        super.paint(g); 

        Graphics2D g2d = (Graphics2D) g;
        //g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Personagem
        g2d.setColor(Color.BLACK);
        g2d.fillOval(pers.getX(), pers.getY(), 30, 30);
        
        // Inimigos 
        for (int i = 0; i < 10; i++){
            if(inimigos[i].getVida() > 0){
                g2d.setColor(new Color((int)(Math.random() * 0x1000000)));
                g2d.fillOval(inimigos[i].getX(), inimigos[i].getY(), 30, 30);
            }
        }
        /*
        if (inimigos[0].getVida() > 0){ // Se a vida de um inimigo chegar em 0, ele não é mais desenhado
            g2d.setColor(Color.CYAN);
            g2d.fillOval(inimigos[0].getX(), inimigos[0].getY(), 30, 30);}
        
        if (inimigos[1].getVida() > 0){
            g2d.setColor(Color.GREEN);
            g2d.fillOval(inimigos[1].getX(), inimigos[1].getY(), 20, 20);}
        
        if (inimigos[2].getVida() > 0){
            g2d.setColor(Color.magenta);
            g2d.fillOval(inimigos[2].getX(), inimigos[2].getY(),40, 40);}
        
        if (inimigos[3].getVida() > 0){
            g2d.setColor(Color.magenta);
            g2d.fillOval(inimigos[3].getX(), inimigos[3].getY(),40, 40);}
            */
        // Escudos
        if(e1.existe == true){ // Se o escudo for pego, ele não é mais desenhado
            g2d.setColor(Color.blue);
            g2d.fillRect(e1.getX(), e1.getY(),10, 10);}
        
        if(e5.existe == true){
            g2d.setColor(Color.blue);
            g2d.fillRect(e5.getX(), e5.getY(),15, 15);}
        
        if(e10.existe == true) {
            g2d.setColor(Color.blue);
            g2d.fillRect(e10.getX(), e10.getY(),20, 20);}
        
        // Poderes com lugares fixos
        if(pers.p1 == true) { // Se o poder for pego, ele não é mais desenhado
            g2d.setColor(Color.orange);
            g2d.fillRect(500, 50 ,10, 10);}
        
        if(pers.p2 == true) {
            g2d.setColor(Color.orange);
            g2d.fillRect(1500, 300 ,15, 15);}
        
        if(pers.p3 == true) {
            g2d.setColor(Color.orange);
            g2d.fillRect(190, 650 ,20, 20);}
     }
         
         
    public void jogar (Jogo jogo) throws InterruptedException{
        //criar o o frame do jogo
        JFrame frame = new JFrame("Jogo Poo"); 
        frame.setLayout(new BorderLayout());
        frame.setSize(1600,900);
        jogo.setBackground(Color.white);
        
        // Informações da Label
        int vida = pers.getVida();
        int qntini = pers.countObservers();
        int forca = pers.a.getDano();
        int escud = pers.qntescudo();
        
        // Criando a Label e o Panel e configurando seus layouts, alem do prorpio frame
        JPanel painel = new JPanel();
        JLabel l1 = new JLabel();
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
        
        // Adicionando os observadores inimigos no personagem 
        for (int addobs = 0; addobs < 10; addobs++){
            if(inimigos[addobs].getVida()>0)
                pers.addObserver(inimigos[addobs]);
        }
        //pers.addObserver(inimigos[0]);
        //pers.addObserver(inimigos[1]);
        //pers.addObserver(inimigos[2]);
        // Loop para rodar o jogo;
        while (true) { 
            
            // Atualizando informações da Label
            vida = pers.getVida();
            qntini = pers.countObservers();
            forca = pers.a.getDano();
            escud = pers.qntescudo();
            
            // Mostrar jogo e atualiza-lo nas suas novas posições
            pers.show(); 
            jogo.repaint();
            Thread.sleep(50); // delay entre novas informações de 50 ms (ticks)
            
            // Loop para remover observadores inimigos mortos
            for (int i=0; i < 10; i++){
                if (inimigos[i].getVida() == 0){
                    pers.deleteObserver(inimigos[i]);
                }
            }
            
            // Imprimir na tela as informações da Label
            l1.setText("                        Quantidade de inimigos restantes: "+qntini+ "                         "+
                   "                Dano: "+forca+"                                        Escudo: "+escud+"                         "+
                   "           Vida do personagem: "+vida);
            
            // Terminar o jogo caso a vida do personagem cheme em 0;
            if (pers.getVida() == 0){
                vida = pers.getVida();
                l1.setText("                        Quantidade de inimigos restantes: "+qntini+ "                         "+
                   "                Dano: "+forca+"                                        Escudo: "+escud+"                         "+
                   "           Vida do personagem: "+vida);
                System.out.println("FIM DO JOGO"); // colocar a layer de fim de jogo
                Thread.sleep(2000);// Esperar 2 segundos apos a morte do personagem e fechar a tela e o programa
                frame.setVisible(false);
                System.exit(0);
                //break;
            }
            
            if (qntini == 0){
                Thread.sleep(2000);
                frame.setVisible(false);
                frame.dispose();
                System.out.println("Parabens, voce ganhou esta fase");
                break;
            }
        } 
        
        

    }
}
