#include <stdio.h>
#include <stdlib.h>
#include "fila.h"
#define max 20


int main()
{
    Fila ex;
    ex = cria_fila();
    int elem_ret;
    imprime_fila(ex);
    insere_fim(ex,5);
    insere_fim(ex,4);
    insere_fim(ex,6);
    insere_fim(ex,3);
    imprime_fila(ex);
    remove_ini(ex,&elem_ret);
    printf("O elemento retirado foi %d\n",elem_ret);
    imprime_fila(ex);
    remove_ini(ex,&elem_ret);
    remove_ini(ex,&elem_ret);
    remove_ini(ex,&elem_ret);
    imprime_fila(ex);
}
