#include <stdio.h>
#include <stdlib.h>
#include "fila.h"

int main()
{
    Fila ex;
    ex = cria_fila();
    imprime_fila(ex);
    insere_ord(ex,5);
    insere_ord(ex,4);
    insere_ord(ex,3);
    insere_ord(ex,10);
    imprime_fila(ex);
    int x;
    remove_ini(ex,&x);
    printf("O numero %d foi removido\n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O numero %d foi removido\n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O numero %d foi removido\n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O numero %d foi removido\n",x);
    imprime_fila(ex);
}
