#include <stdio.h>
#include <stdlib.h>
#include "fila.h"
#define max 20

int main()
{
    Deque ex;
    ex = cria_deque();
    imprime_fila(ex);
    insere_ini(ex,5);
    insere_ini(ex,4);
    insere_ini(ex,6);
    insere_fim(ex,3);
    imprime_fila(ex);
    int x;
    remove_ini(ex,&x);
    printf("O elemento %d foi removido \n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O elemento %d foi removido \n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O elemento %d foi removido \n",x);
    imprime_fila(ex);
    remove_ini(ex,&x);
    printf("O elemento %d foi removido \n",x);
    imprime_fila(ex);
}
