#include <stdio.h>
#include <stdlib.h>
#define NUM_ALUNOS 10           //Usado no 1 e no 2 exercicio

/*
//                  Primeiro Exercicio

struct dados{
    int numero;
    char nome[5];
};

void manipula_um_par (int *a){
    *a = *a/2;
}

void manipula_pares(struct dados *x, int w){
    int z;
    for(z=0;z<w;z++){
        if (x[z].numero % 2 == 0){
            manipula_um_par(&x[z].numero);
        }
    }
}

int main() {
    struct dados v[NUM_ALUNOS];
    int x;
    for(x = 0; x < NUM_ALUNOS; x++){
        printf("\nDigite o nome do %d aluno: ",x+1);
        scanf("%s", v[x].nome);
        printf("\nDigite o %d numero: ",x+1);
        scanf("%d",&v[x].numero);
    }
    manipula_pares(v, NUM_ALUNOS);
    for(x=0;x<NUM_ALUNOS;x++){
        printf("--- %d ", v[x].numero);
    }
    return 0;
}

//                  Segundo Exercicio

struct dados{
    int numero;
    char nome[5];
};

void manipula_um_par (struct dados *a, int b){
    a[b].numero = a[b].numero /2;
}

void manipula_pares(struct dados *x, int w){
    int z;
    for(z=0;z<w;z++){
        if (x[z].numero % 2 == 0){
            manipula_um_par(x,z);
        }
    }
}

int main() {
    struct dados v[NUM_ALUNOS];
    int x;
    for(x = 0; x < NUM_ALUNOS; x++){
        printf("\nDigite o nome do %d aluno: ",x+1);
        scanf("%s", v[x].nome);
        printf("\nDigite o %d numero: ",x+1);
        scanf("%d",&v[x].numero);
    }
    manipula_pares(v, NUM_ALUNOS);
    for(x=0;x<NUM_ALUNOS;x++){
        printf("--- %d ", v[x].numero);
    }
    return 0;
}

//                  Terceiro Exercicio

int main(){
    int num = 5;
    float real = 4.9;
    unsigned int end_num, end_real;
    end_num = &num;
    end_real = &real;
    //Primeiro Bloco
    printf("O valor de NUM eh: %d\n",num);
    printf("O endereco do NUM sem usar a variavel (hexadecimal) eh: %x \n",&num);
    printf("O endereco do NUM usando a variavel (hexadecimal) eh: %x \n",end_num);
    printf("O valor da variavel (hexadecimal) eh %x\n",end_num);
    printf("O valor de REAL eh: %f\n",real);
    printf("O endereco do REAL sem usar a variavel (hexadecimal) eh: %x \n",&real);
    printf("O endereco do REAL usando a variavel (hexadecimal) eh: %x \n",end_real);
    printf("O valor da variavel (hexadecimal) eh %x\n",end_real);
    //Segundo Bloco
    scanf("%d",6356740);    //endereco de num
    scanf("%f",6356736);    //endereco de real
    //Terceiro Bloco
    printf("O valor de NUM eh: %d\n",num);
    printf("O endereco do NUM sem usar a variavel (hexadecimal) eh: %x \n",&num);
    printf("O endereco do NUM usando a variavel (hexadecimal) eh: %x \n",end_num);
    printf("O valor da variavel (hexadecimal) eh %x \n",end_num);
    printf("O valor de REAL eh: %f\n",real);
    printf("O endereco do REAL sem usar a variavel (hexadecimal) eh: %x \n",&real);
    printf("O endereco do REAL usando a variavel (hexadecimal) eh: %x \n",end_real);
    printf("O valor da variavel (hexadecimal) eh %x\n",end_real);
    return 0;
}

//                  Quarto Exercicio

int main(){
    int num = 5;
    float real = 4.9;
    int *a;
    float *b;
    a = &num;
    b = &real;

    //Primeiro Bloco
    printf("O valor de NUM eh: %d\n",num);
    printf("O endereco do NUM sem usar o ponteiro (hexadecimal) eh: %p \n",&num);
    printf("O endereco do NUM usando o ponteiro (hexadecimal) eh: %x \n",a);
    printf("O valor do ponteiro (hexadecimal) eh %x\n",*a);
    printf("O valor de REAL eh: %f\n",real);
    printf("O endereco do REAL sem usar a variavel (hexadecimal) eh: %x \n",&real);
    printf("O endereco do REAL usando a variavel (hexadecimal) eh: %x \n",b);
    printf("O valor da variavel (hexadecimal) eh %x\n",*b);
    //Segundo Bloco
    scanf("%d",6356740);    //endereco de num
    scanf("%f",6356736);    //endereco de real
    //Terceiro Bloco
    printf("O valor de NUM eh: %d\n",num);
    printf("O endereco do NUM sem usar a variavel (hexadecimal) eh: %x \n",&num);
    printf("O endereco do NUM usando a variavel (hexadecimal) eh: %x \n",a);
    printf("O valor da variavel (hexadecimal) eh %x \n",*a);
    printf("O valor de REAL eh: %f\n",real);
    printf("O endereco do REAL sem usar a variavel (hexadecimal) eh: %x \n",&real);
    printf("O endereco do REAL usando a variavel (hexadecimal) eh: %x \n",b);
    printf("O valor da variavel (hexadecimal) eh %x\n",*b);
    return 0;
}

*/

struct dados{
    int numero;
    char nome[5];
};
typedef struct dados Das;

void manipula_um_par (struct dados *a, int b){
    a[b].numero = a[b].numero /2;
}

void manipula_pares(struct dados *x, int w){
    int z;
    for(z=0;z<w;z++){
        if (x[z].numero % 2 == 0){
            manipula_um_par(x,z);
        }
    }
}

int main() {
    Das *p;
    int k;
    printf("Qual sera o numero de alunos?\n");
    scanf("%d",&k);
    p = (Das*)malloc(k*sizeof(Das));
    Das v[p];
    int x;
    for(x = 0; x < k; x++){
        printf("\nDigite o nome do %d aluno: ",x+1);
        scanf("%s", v[p].nome);
        printf("\nDigite o %d numero: ",x+1);
        scanf("%d",&v[p].numero);
    }
    manipula_pares(v, k);
    for(x=0;x<k;x++){
        printf("--- %d ", v[p].numero);
    }
    return 0;
}








