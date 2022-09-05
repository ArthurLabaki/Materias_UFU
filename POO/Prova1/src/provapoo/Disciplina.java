// Arthur do Prado Labaki
//11821BCC017
package provapoo;

import java.util.Arrays;

public class Disciplina {
    private int codigo;
    private String nome;
    Aluno[] maluno = new Aluno[5];     //Aray de alunos

    public Disciplina() {   //Construtor padrao
        this.codigo = this.codigo+1;
    }
    public Disciplina(String nome) {    //Contrutor com parametro
        this.nome =nome;
        this.codigo = this.codigo+1;
    }

    @Override
    public String toString() {
        return "Disciplina "+this.nome+":\n" +Arrays.toString(maluno);
    }
    
    public void matricular(Aluno aluno){ //Matricular
        for(int i=0;i< maluno.length;i++){
            if(maluno[i]==null){
                maluno[i] = aluno;
                break;
            }
            if(maluno[i] == aluno){
                aluno.AlunoMatriculadoException();
                break;
            }   
        }
    }
    public void cancelarMatricula(Aluno aluno){ //Cancelar Mtricula
        boolean j=true;
        for (int i=0;i<maluno.length;i++){
            if(maluno[i]==aluno){
                maluno[i] = null;
                j = false;
                break;
            }
        }
        if(j == true){
        aluno.AlunoInexistenteException();
        }
    }
  
    public int getCodigo() {
        return codigo;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    
}