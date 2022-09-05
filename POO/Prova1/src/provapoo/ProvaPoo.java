// Arthur do Prado Labaki 
//11821BCC017
package provapoo;

public class ProvaPoo {

    public static void main(String[] args) {
       Disciplina d1 = new Disciplina("Aed2");
       Disciplina d2 = new Disciplina("Poo");
       Disciplina d3 = new Disciplina("C3");
       //
       Aluno a1 = new Aluno("Renata");
       Aluno a2 = new Aluno("Henrique");
       Aluno a3 = new Aluno("Pedro");
       Aluno a4 = new Aluno("Arthur");
       Aluno a5 = new Aluno("Bruna");
       //
       d1.matricular(a1);
       d1.matricular(a2);
       d1.matricular(a3);
       d1.matricular(a4);
       d1.matricular(a5);
       
       d2.matricular(a1);
       d2.matricular(a2);
       d2.matricular(a3);
       d2.matricular(a4);
       d2.matricular(a5);
       
       d3.matricular(a1);
       d3.matricular(a2);
       d3.matricular(a3);
       d3.matricular(a4);
       d3.matricular(a5);
       //
       System.out.println();    //\n
       //
       d2.matricular(a2); //Rematricular o mesmo
       //
       System.out.println();    //\n
       //
       System.out.println(d1.toString()); //Aed2
       System.out.println();    //\n       
       System.out.println(d2.toString()); //Poo
       System.out.println();    //\n
       System.out.println(d3.toString()); //C3
       //
       System.out.println();    //\n
       //
       d1.cancelarMatricula(a1);
       d2.cancelarMatricula(a2);
       d3.cancelarMatricula(a5);
       //
       d1.cancelarMatricula(a1); //Recancelamento
       //
       System.out.println();    //\n
       //
        System.out.println(d1.toString()); //Aed2
       System.out.println();    //\n       
       System.out.println(d2.toString()); //Poo
       System.out.println();    //\n
       System.out.println(d3.toString()); //C3
       //
       System.out.println();    //\n
    }
}
