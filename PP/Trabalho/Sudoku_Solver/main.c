#include <stdio.h>

void le_arquivo(char *nome, int mat[][9]) {     //Leitura do Arquivo em txt (sudoku.txt)
    FILE *arq = fopen(nome,"r");
    if(arq == NULL) {
        printf(" Erro de leitura\n");
        system("pause");
        exit(1);
    }
    int i,j;
    for(i=0; i< 9; i++)
        for(j=0; j< 9; j++)
            fscanf(arq,"%d",&mat[i][j]);

    fclose(arq);
}

int main()
{
    int mat[9][9];
    le_arquivo("sudoku.txt", mat);
    int i,j;
    for(i=0; i< 9; i++) {
        for(j=0; j< 9; j++)
            printf(" %d",mat[i][j]);            //Define a matriz lida em txt e salva em uma matrix 9x9 (mat[9][9])
        printf("\n");
    }
    printf("\n");
    int vazio[9][9],linha,coluna,quad,retorno,rep,k,l;
    linha = 1;
    coluna = 1;
    quad = 1;
    retorno = 1;
    for(i=0;i<9;i++) {                      //Cria uma matriz [9][9] com 0 e 1, de acordo com a matriz original(mat[9][9])
        for(j=0;j<9;j++) {                  // em que o 1 � um valor ja estabelecido e que nao pode ser alterado
            if(mat[i][j]==0) {              // e o 0 um valor a ser descoberto, e que deve ser alterado
                    vazio[i][j]=0;}
            else{vazio[i][j]=1;}
        }
    }
    for(i=0;i<9;i++) {                      //Comeco da resolucao do sudoku por forca bruta (metodo das tentativas)
        for(j=0;j<9;j++) {
            if(vazio[i][j]==0){
                do {
                    retorno=0;
                    while((linha==1 || coluna==1 || quad==1) && mat[i][j]<=9) {
                        linha=0; coluna=0; quad=0;
                        mat[i][j]++;                        //Modifica o valor do elemento
                        for(k=0;k<9;k++) {
                            if(k!=j && mat[i][j]==mat[i][k]) {       //Checa Linhas
                                linha=1;
                                printf(" Erro na L %d  C %d  - - -  O Valor %d eh o mesmo na : L %d  C %d\n",i,j,mat[i][j],i,k);
                                break;
                            }
                        }
                        if(linha==0) {
                            for(l=0;l<9;l++) {
                                if(l!=i && mat[i][j]==mat[l][j]) {     //Checa Colunas
                                    coluna=1;
                                    printf(" Erro na L %d  C %d  - - -  O valor %d eh o mesmo na : L %d  C %d\n",i,j,mat[i][j],l,j);
                                    break;
                                }
                            }
                        }
                        if(linha==0 && coluna==0) {                 //L = linha e C = coluna
                            for(k=0;k<9;k++) {
                                for(l=0;l<9;l++) {
                                    if(k!=j && l!=i && (10*(i/3)+j/3==10*(l/3)+k/3) && mat[i][j]==mat[l][k]) {  //Checa Quadrantes (3x3)
                                        quad=1;
                                        printf(" Erro na L %d  C %d  - - -  O Valor %d eh o mesmo na : L %d  C %d\n",i,j,mat[i][j],l,k);
                                        break;
                                    }
                                }
                            }
                        }
                    }
                    linha=1; coluna=1; quad=1;
                    if(mat[i][j]>9) {                     //Retorna no mesmo elemento (excedeu o maximo valor possivel dos elemento [9])
                        mat[i][j]=0;
                        do {
                            j--;
                            if(j<0) {
                                j=8; i--;
                            }
                        }
                        while(vazio[i][j]==1);           //Retorna para continuar o checar as linhas, colunas e quadrantes
                        retorno=1;
                        printf("\n Retorno\n\n");
                    }
                }
                while(retorno==1);
            }
        }
    }
    printf("\n A solucao do SUDOKU eh:\n\n");           //Printf do sudoku resolvido
    for(i=0;i<9;i++) {
        for(j=0;j<9;j++) {
            printf(" %d",mat[i][j]);
        }
        printf("\n");
    }
    system("pause");
    return 0;
}
//OBS : EU DEIXEI OS PRINTF'S CHECANDO LINHAS, COLUNAS, QUADRANTES E RETORNANDO PARA UM MELHOR ENTERNDIMENTO DA EXEUCAO DO PROGRAMA!
//CASO DESEJE REMOVE-LAS BASTA RETIRAR (APAGAR) AS LINHAS  60, 68, 78, 96.

