#include <stdio.h>
#include <stdlib.h>
#include "fila.h"

int main()
{
    Fila ex;
    ex = cria_fila();
    imprime_fila(ex);
    insere_fim(ex,5);
    insere_fim(ex,4);
    insere_fim(ex,6);
    insere_fim(ex,3);
    imprime_fila(ex);
    int elem_rem;
    remove_ini(ex,&elem_rem);
    printf("O elemento removido foi o [ %d ]\n",elem_rem);
    imprime_fila(ex);
    remove_ini(ex,&elem_rem);
    printf("O elemento removido foi o [ %d ]\n",elem_rem);
    imprime_fila(ex);
}
