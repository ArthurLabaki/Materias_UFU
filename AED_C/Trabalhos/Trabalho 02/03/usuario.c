#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
#include <string.h>
# define max 20

int main()
{
   Pilha ex;
   ex = cria_pilha();
   char x[100];
   int tam;
   imprime_pilha(ex);
   push(ex,5);
   push(ex,2);
   push(ex,30);
   push(ex,5);
   imprime_pilha(ex);  //-topo-[ 5 30 2 5]-base-
   imprime_reverso(ex);
   //printf("Digite a palavra\n");
   //gets(x);
   //printf("%s\n",x);
   //tam = strlen(x);
   //palindrome(x, tam);
}
