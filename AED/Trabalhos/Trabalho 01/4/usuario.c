#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){
    Lista *ex;
    Lista *ex2;
    Lista *ex3;
    ex = cria_lista();
    ex2 = cria_lista();
    ex3 = cria_lista();
    insere_elem(&ex,1);
    insere_elem(&ex,3);
    insere_elem(&ex,1);
    insere_elem(&ex,2);
    insere_fim(&ex2,1);
    insere_fim(&ex2,6);
    insere_fim(&ex2,5);
    insere_fim(&ex2,4);
    imprime_lista(ex);
    imprime_lista(ex2);
    remover_todos(&ex,1);
    remove_par(&ex2);
    imprime_lista(ex);
    imprime_lista(ex2);
    imprime_lista(ex3);
    concatena_lista(ex,ex2,&ex3);
    imprime_lista(ex);
    imprime_lista(ex2);
    imprime_lista(ex3);
    free(ex);
    free(ex2);
    free(ex3);
    return 0;
}
