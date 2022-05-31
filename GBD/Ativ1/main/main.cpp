/*
 * File:   main.cpp
 * Author: Arthur do Prado Labaki / 11821BCC017
 * Fiz o trabalho sozinho
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <locale.h>

class MeuArquivo {
public:
    struct cabecalho { int quantidade=0; int disponivel=0; int lista[100]={};} cabecalho;;

    // construtor: abre arquivo. Essa aplicacao deveria ler o arquivo se existente ou criar um novo.
    // Entretando recriaremos o arquivo a cada execucao ("w+").
    MeuArquivo() {
        fd = fopen("dados.dat","w+");
        fprintf(fd, "Total: %d -/- Disponivel: %d                                          \n", cabecalho.quantidade, cabecalho.disponivel);
        // O espaço extra adicionado permite colocar o cabeçalho no arquivo
    }

    // Destrutor: fecha arquivo
    ~MeuArquivo() {
        fclose(fd);
    }

    // Insere uma nova palavra, consulta se há espaco disponível ou se deve inserir no final
    void inserePalavra(char *palavra) {
        this->substituiBarraNporBarraZero(palavra); // Funcao auxiliar substitui terminador por \0

        if (cabecalho.disponivel == 0) {   // Insere no final do arquivo
            final:
            atualizaCabecalho(0);
            if(strlen(palavra) < sizeof(int)+1 ) {
            fputc('5', fd);
            int i;
            for (i=0; i<5; i++){
                if (i < strlen(palavra)) {
                    fputc(palavra[i], fd);
                }
                else{
                    fputc('\0', fd);
                }
            }
            }else{
            fprintf(fd, "%d%s", strlen(palavra),palavra);
            }
        }
        else{   // Procura lugar para inserir
            rewind(fd);
            char c;
            while (true){   // Pula o cabeçalho
                c = fgetc(fd);
                if (c == '\n'){
                    break;
                }
            }
            int i = 0;
            bool test = true;
            while (i != cabecalho.disponivel){  // Encontra a posição no disponivel do cabeçalho
                c = fgetc(fd);
                if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9'){
                    if (test == true){
                        i++;
                        test = false;
                    }
                }
                else{
                    test = true;
                }
            }
            char tam[2] = {};
            tam[0] = c;
            c = fgetc(fd);   // Verifica o tamanho do registro disponivel
            if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9'){
                tam[1] = c;
            }
            else{
                fseek(fd, -1, SEEK_CUR);
            }
            if (atol(tam) < strlen(palavra)){   // Verifica se a palavra eh maior que o possivel
                goto final;   // Se a palavra for maior, insere no final
            }
            for (i=0; i<atol(tam); i++){   // Se não, insere no lugar e insere com '\0'
                fseek(fd, 0, SEEK_CUR);
                if (i < strlen(palavra)) {
                    fputc(palavra[i], fd);
                }
                else{
                    fputc('\0', fd);
                }
            }
        atualizaCabecalho(-1);   // Atualiza
        }
        fseek(fd, 0, SEEK_CUR);

    }

    // Marca registro como removido, atualiza lista de disponíveis, incluindo o cabecalho
    void removePalavra(int offset) {

        rewind(fd);
        char c;
        while (true){   // Pula o cabeçalho
            c = fgetc(fd);
            if (c == '\n'){
                break;
            }
        }
        int i = 0;
        bool test = true;
        while (i != offset){   // Busca o registro que vai ser apagado (offset)
            c = fgetc(fd);
            if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9'){
                if (test == true){
                    i++;
                    test = false;
                }
            }
            else{
                test = true;
            }
            if (test == false){
                c = fgetc(fd);
                if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9'){
                    fseek(fd, 1, SEEK_CUR);
                }
            }
        }
        fseek(fd, -1, SEEK_CUR);
        fputc('*',fd);   // Coloca o * no inicio da palavra excluida
        fseek(fd, -1, SEEK_CUR);

        atualizaCabecalho(offset);
    }

    // BuscaPalavra: retorno é o offset para o registro
    // Nao deve considerar registro removido
    int buscaPalavra(char *palavra) {
        this->substituiBarraNporBarraZero(palavra); // Funcao auxiliar substitui terminador por \0

        if (palavra[0] == '*'){   // Impede palavras começadas com *
            return -1;
        }
        rewind(fd);
        char c;
        while (true){   // Pula o cabeçalho
            c = fgetc(fd);
            if (c == '\n'){
                break;
            }
        }

        int offset = 0;
        bool test = true; //offset
        int tam = strlen(palavra);
        int i = 0;
        bool err =  false;
        while (!feof(fd)){   // Busca a palavra inteira, se uma letra não corresponder na sequencia, vai pra proxima palavra
            c = fgetc(fd);
            if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9'){
                if (tam == i && err == false){
                    return offset;
                }
                else{
                    if (test == true){
                        i = 0;
                        offset ++;
                        test = false;
                    }
                    else{
                        i = 0;
                    }
                }

                err = false;
            }
            else{
                test = true;
                if (err == false){
                    if (c == palavra[i] & c != '\0'){
                        i++;
                    }
                    else{
                        if (c == '\0'){
                             //jump
                        }
                        else{
                            err = true;
                        }
                    }
                }
            }

        }

        // retornar -1 caso nao encontrar
        return -1;
    }

    void atualizaCabecalho (int i){
        if (i == 0){   // Aumenta a quantidade se for inserido no final
            cabecalho.quantidade ++;
        }
        if (i > 0){
            cabecalho.quantidade --;   // Diminui a quantidade e adiciona o offset na lista dos removidos
            int j=0;
            while(cabecalho.lista[j] != 0){
                j++;
            }
            cabecalho.lista[j] = i;  // Coloca o offset no primeiro lugar disponivel
            printf("%d", cabecalho.lista[j]);
        }
        if (i < 0){   // Aumenta a quantidade e remove o offset da lista dos removidos
            cabecalho.quantidade ++;
            int i;
            for(i=0; i<100; i++){
                if (cabecalho.lista[i] == cabecalho.disponivel){
                    cabecalho.lista[i] = 0;
                }
            }
        }
        cabecalho.disponivel = maior();   // Coloca o maior registro no disponivel
        rewind(fd);
        fprintf(fd, "Total: %d -/- Disponivel: %d ", cabecalho.quantidade, cabecalho.disponivel);
        fseek(fd,0,SEEK_END);
    }

    int maior (){   // Busca o registro mais recente (Essa função ia buscar o maior registro excluido, mas o programa estava lento)
        int i;
        int val = 0;
        for(i=0; i<100; i++){
            if (cabecalho.lista[i] > val){
                val = cabecalho.lista[i];
            }
        }
        return val;
    }


private:
    // descritor do arquivo é privado, apenas métodos da classe podem acessa-lo
    FILE *fd;

    // funcao auxiliar substitui terminador por \0
    void substituiBarraNporBarraZero(char *str) {
        int tam = strlen(str); for (int i = 0; i < tam; i++) if (str[i] == '\n') str[i] = '\0';
    }
};

int main(int argc, char** argv) {
    // abrindo arquivo dicionario.txt
    FILE *f = fopen("dicionario.txt","rt");

    // se não abriu
    if (f == NULL) {
        printf("Erro ao abrir arquivo.\n\n");
        return 0;
    }
    setlocale(LC_ALL, "Portuguese_Brazil");
    char *palavra = new char[50];

    // criando arquivo de dados
    MeuArquivo *arquivo = new MeuArquivo();
    while (!feof(f)) {
        fgets(palavra,50,f);
        arquivo->inserePalavra(palavra);
    }

    // fechar arquivo dicionario.txt
    fclose(f);

    printf("Arquivo criado.\n\n");

    char opcao;
    do {
        printf("\n\n1-Insere\n2-Remove\n3-Busca\n4-Sair\nOpcao:");
        opcao = getchar();
        if (opcao == '1') {
            printf("Palavra: ");
            scanf("%s",palavra);
            arquivo->inserePalavra(palavra);
        }
        else if (opcao == '2') {
            printf("Palavra: ");
            scanf("%s",palavra);
            int offset = arquivo->buscaPalavra(palavra);
            if (offset >= 0) {
                arquivo->removePalavra(offset);
                printf("Removido.\n\n");
            }
        }
        else if (opcao == '3') {
            printf("Palavra: ");
            scanf("%s",palavra);
            int offset = arquivo->buscaPalavra(palavra);
            if (offset >= 0)
                printf("Encontrou %s na posição %d\n\n",palavra,offset);
            else
                printf("Não encontrou %s\n\n",palavra);
        }
        if (opcao != '4') opcao = getchar();
    } while (opcao != '4');

    printf("\n\nAte mais!\n\n");

    return (EXIT_SUCCESS);
}
