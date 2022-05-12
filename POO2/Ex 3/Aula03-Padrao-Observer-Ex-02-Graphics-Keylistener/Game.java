import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Game extends JPanel {

    private Bola bola;
    private Robo j1;
    private Robo j2;
    private Robo j3;
    private Robo j4;
    private Robo j5;
    private Robo j6;
    private Robo j7;
    private Jogador j8;

    
    public Game() {
        KeyListener listener = new MyKeyListener();
        addKeyListener(listener);
        setFocusable(true); //So that the JPanel object receives the keyboard notifications it is necessary to include the instruction setFocusable(true), which allows KeyboardExample to receive the focus.
    }       
    
    public class MyKeyListener implements KeyListener {
        @Override
        public void keyTyped(KeyEvent e) {}

        @Override
        public void keyPressed(KeyEvent e) {
            //System.out.println("keyPressed="+KeyEvent.getKeyText(e.getKeyCode()));

            if (e.getKeyCode() == KeyEvent.VK_LEFT)
               j8.setX(j8.getX()-10);
               
            if (e.getKeyCode() == KeyEvent.VK_RIGHT)
               j8.setX(j8.getX()+10);
               
            if (e.getKeyCode() == KeyEvent.VK_UP)
            j8.setY(j8.getY()-10);
            
            if (e.getKeyCode() == KeyEvent.VK_DOWN)
               j8.setY(j8.getY()+10);    
               
            if (e.getKeyCode() == KeyEvent.VK_SPACE)
               j8.chuta(bola);        
               
        }

        @Override
        public void keyReleased(KeyEvent e) {
            //System.out.println("keyReleased="+KeyEvent.getKeyText(e.getKeyCode()));
        }
}    
    
    public void paint(Graphics g) {
        super.paint(g); //The call to "super.paint(g)", cleans the screen 

        Graphics2D g2d = (Graphics2D) g;
        //The instruction; "g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON)" makes the borders of the figures smoother

        //g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        g2d.setColor(Color.BLACK);
        g2d.fillOval(bola.getX(), bola.getY(), 20, 20);

        g2d.setColor(Color.GREEN);        
        g2d.fillOval(j1.getX(), j1.getY(), 20, 20);

        g2d.setColor(Color.RED);                
        g2d.fillOval(j2.getX(), j2.getY(), 20, 20);

        g2d.setColor(Color.WHITE);        
        g2d.fillOval(j3.getX(), j3.getY(), 20, 20);

        g2d.setColor(Color.BLUE);        
        g2d.fillOval(j4.getX(), j4.getY(), 20, 20);

        g2d.setColor(Color.DARK_GRAY);                
        g2d.fillOval(j5.getX(), j5.getY(), 20, 20);

        g2d.setColor(Color.CYAN);                
        g2d.fillOval(j6.getX(), j6.getY(), 20, 20);

        g2d.setColor(Color.MAGENTA);                        
        g2d.fillOval(j7.getX(), j7.getY(), 20, 20);

        g2d.setColor(Color.ORANGE);                        
        g2d.fillOval(j8.getX(), j8.getY(), 20, 20);
               
    }

    public void jogar (Game game) throws InterruptedException {
        JFrame frame = new JFrame("RoboCup");
        frame.add(game);
        frame.setSize(700, 700);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);        
        
        bola = new Bola(250,250);
        j1 = new Robo(10,450);
        j2 = new Robo(400,20);
        j3 = new Robo(50,50);
        j4 = new Robo(100,100);
        j5 = new Robo(350,100);
        j6 = new Robo(20,300);
        j7 = new Robo(400,400);
        j8 = new Jogador(100,400, "FABIANO");
        
        bola.addObserver(j1);
        bola.addObserver(j2);
        bola.addObserver(j3);        
        bola.addObserver(j4);        
        bola.addObserver(j5);        
        bola.addObserver(j6);        
        bola.addObserver(j7);        

        
        while (true) {
            bola.show();           
            game.repaint();
            Thread.sleep(50);
        }
    }
}
