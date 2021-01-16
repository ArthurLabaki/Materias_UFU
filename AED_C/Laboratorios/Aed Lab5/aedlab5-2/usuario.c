#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10

int main() {
    Lista ex;
    ex = cria_lista();
    if (ex == NULL){
        printf("Nao foi possivel criar a lista.\n");
        return -1;
    }
    imprime_lista(ex);
    insere_ord(ex, 4);
    insere_ord(ex, 8);
    insere_ord(ex, 0);
    insere_ord(ex, 19);
    insere_ord(ex, 2);
    insere_ord(ex, 7);
    insere_ord(ex, 9);
    insere_ord(ex, 22);
    insere_ord(ex, 8);
    imprime_lista(ex);
    remove_ord(ex, 8);
    imprime_lista(ex);
    ex = cria_lista();
    imprime_lista(ex);
    free(ex);
    return 0;
}
