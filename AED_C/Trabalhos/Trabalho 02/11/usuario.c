#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
#include <string.h>


int main(){
    int a[10],x=0,tam;
    while(x<=10){
        a[x]=0;
        x++;
    }
    char expr1[100],expr2[100];
    printf("ENTRADA DE VALORES\n");
    printf("Digite o valor para a variavel A: ");
    scanf("%d",&a[0]);
    printf("Digite o valor para a variavel B: ");
    scanf("%d",&a[1]);
    printf("Digite o valor para a variavel C: ");
    scanf("%d",&a[2]);
    printf("Digite o valor para a variavel D: ");
    scanf("%d",&a[3]);
    printf("Digite o valor para a variavel E: ");
    scanf("%d",&a[4]);
    printf("Digite o valor para a variavel F: ");
    scanf("%d",&a[5]);
    printf("Digite o valor para a variavel G: ");
    scanf("%d",&a[6]);
    printf("Digite o valor para a variavel H: ");
    scanf("%d",&a[7]);
    printf("Digite o valor para a variavel I: ");
    scanf("%d",&a[8]);
    printf("Digite o valor para a variavel J: ");
    scanf("%d",&a[9]);
    inicio:
    printf("ENTRADA DA EXPRESSAO\n");
    printf("A expressao a ser resolvida sera na forma de:\n1-Pos-fixa;\n2-Infixa com o uso de parenteses em todas as operacoes;\n3-Infixa com o uso de parenteses quando necessario;\n");
    scanf("%d",&x);
    if(x > 3 || x <1){
        printf("Escolha Invalida!\n");
        return 0;
    }
    printf("Digite a expressao:\n");
    setbuf(stdin, NULL);
    gets(expr1);
    if(x == 2 || x ==3){
    printf("Convertendo:\n");
    tam = strlen(expr1);
    expr1[tam] = ')';
    expr1[tam+1] = '\0';
    inf_para_pos(expr1, expr2);
    printf("%s\n",expr2);
    printf("\nAVALIANDO A EXPRESSAO\n");
    resolver_eq(expr2,&a);
    printf("Deseja colocar outra expressao?( 1-sim 0-nao )\n");
    scanf("%d",&x);
    if(x > 1 || x <0){
        printf("Escolha Invalida!\n");
        return 0;
    }
    if(x==0){
        return 1;
    }
    if(x==1){
        goto inicio;
    }
    }
    printf("\nAVALIANDO A EXPRESSAO\n");
    resolver_eq(expr1, &a);
    printf("Deseja colocar outra expressao?( 1-sim 0-nao )\n");
    scanf("%d",&x);
    if(x > 1 || x <0){
        printf("Escolha Invalida!\n");
        return 0;
    }
    if(x==0){
        return 1;
    }
    if(x==1){
        goto inicio;
    }
}
