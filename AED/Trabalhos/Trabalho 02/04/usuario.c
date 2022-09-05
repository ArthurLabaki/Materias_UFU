#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pilha.h"


int main()
{
    Pilha ex1;
    ex1 = cria_pilha();
    Pilha ex2;
    ex2 = cria_pilha();
    Pilha ex3;
    ex3 = cria_pilha();
    //char x[100];
    //int tam;
    //printf("Digite a palavra(X)\n");
    //gets(x);
    //tam = strlen(x);
    //palindrome(x, tam);
    push(&ex1,3);
    push(&ex1,3);
    push(&ex1,7);
    push(&ex1,4);
    push(&ex1,1);
    push(&ex1,0);
    pares_e_impares(&ex1,&ex2,&ex3);
    imprime_pilha(ex1);
    imprime_pilha(ex2); //par
    imprime_pilha(ex3); //impar
}
