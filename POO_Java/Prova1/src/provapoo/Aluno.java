// Arthur do Prado Labaki
//11821BCC017
package provapoo;

public class Aluno {
    private int matricula;
    private String nome;
    Disciplina disciplinaMatriculada = new Disciplina();
    

    public Aluno(String nome) { //Contrutor com parametro
        setNome(nome);
    }

    @Override
    public String toString() {
        return "\nAluno - "+ matricula + ": " + nome;
    }

    public int getMatricula() {
        return matricula;
    }

    public String getNome() {
        return nome;
    }
    private void setNome(String nome){
        if(nome != null && nome.length() > 0){
            this.nome = nome;
        }
        else{
            this.NomeInvalido();
        }
    }
    
    private void NomeInvalido(){        //Exceções 
        System.out.println("Nome Invalido!");
    }
    void AlunoMatriculadoException (){
        System.out.println("Aluno já matriculado!");
    }
    void AlunoInexistenteException(){
        System.out.println("Aluno não encontrado!");
    }
    //catch (AlunoMatriculadoException){
    //  System.out.println("Aluno já matriculado!");
    // }
    //catch (AlunoInexistenteException){
    //  System.out.println("Aluno não encontrado!");
    //}
}