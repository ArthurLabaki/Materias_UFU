#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main()
{
    Lista ex;
    ex = cria_lista();
    insere_elemento(&ex,5);
    insere_elemento(&ex,4);
    insere_elemento(&ex,5);
    insere_elemento(&ex,6);
    insere_elemento(&ex,3);
    imprime(ex);
    remove_elemento(&ex,5);
    imprime(ex);
    remove_elemento(&ex,5);
    imprime(ex);
    free(ex);
    return 0;
}
