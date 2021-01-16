#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){
    Lista ex;
    ex = cria_lista();
    insere_final(&ex,5);
    insere_final(&ex,4);
    insere_final(&ex,6);
    imprime(ex);
    remove_inicio(&ex,5);
    printf("O elemento removido foi o 5\n");
    imprime(ex);
    remove_inicio(&ex,4);
    printf("O elemento removido foi o 4\n");
    imprime(ex);
    remove_inicio(&ex,6);
    printf("O elemento removido foi o 6\n");
    imprime(ex);
    free(ex);
    return 0;
}
