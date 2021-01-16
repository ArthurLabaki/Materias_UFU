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
    Lista ex2;
    ex2 = cria_lista();
    if (ex2 == NULL){
        printf("Nao foi possivel criar a lista.\n");
        return -1;
    }
    Lista ex3;
    ex3 = cria_lista();
    if (ex3 == NULL){
        printf("Nao foi possivel criar a lista.\n");
        return -1;
    }
    imprime_lista(ex);
    insere_ord(ex, 4);
    insere_ord(ex, 8);
    insere_ord(ex, 0);
    insere_ord(ex, 8);
    imprime_lista(ex);
    tamanho_lista(ex);
    menor_ord(ex);
    tamanho_lista(ex);
    imprime_lista(ex);
    insere_ord(ex2, 4);
    insere_ord(ex2, 1);
    insere_ord(ex2, 6);
    insere_ord(ex2, 77);
    imprime_lista(ex2);
    lista_igual(ex,ex2);
    imprime_lista(ex);
    imprime_lista(ex2);
    intercala_lista(ex,ex2,ex3);
    imprime_lista(ex3);
    remove_par(ex3);
    imprime_lista(ex3);
    tamanho_lista(ex3);
    free(ex);
    free(ex2);
    free(ex3);
    return 0;
}
