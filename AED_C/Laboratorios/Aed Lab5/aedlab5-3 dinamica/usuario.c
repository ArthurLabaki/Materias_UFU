#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){
    Lista *ex;
    ex = cria_lista();
    menor_elem(&ex);        //nao remove nenhum elemento
    tamanho_lista(ex);      //printa 0;
    imprime_lista(ex);
    insere_elem(&ex, 4);
    insere_elem(&ex, 8);
    insere_elem(&ex, 0);
    insere_elem(&ex, 19);
    insere_elem(&ex, 2);
    insere_elem(&ex, 7);
    insere_elem(&ex, 9);
    insere_elem(&ex, 22);
    insere_elem(&ex, 8);
    menor_elem(&ex);        //remove o 0
    tamanho_lista(ex);      //printa 8
    imprime_lista(ex);
    remove_elem(&ex, 8);
    menor_elem(&ex);        //remove o 2
    tamanho_lista(ex);      //printa 6
    imprime_lista(ex);
    free(ex);
}
