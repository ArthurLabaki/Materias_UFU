#include <stdio.h>
#include <stdlib.h>
#include "lista.h"


int main()
{
    Lista ex;
    ex = cria_lista();
    imprime_lista(ex);
    insere_elemento(&ex, 4);
    insere_elemento(&ex, 4);
    insere_elemento(&ex, 36);
    insere_elemento(&ex, 3);
    insere_elemento(&ex, 40);
    insere_elemento(&ex, 41);
    imprime_lista(ex);
    tamanho(ex);
    remove_maior(&ex);
    imprime_lista(ex);

}
