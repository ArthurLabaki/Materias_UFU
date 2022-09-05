#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){

Lista *ex;
ex = cria_lista();
menor_lista(&ex);
tamanho_lista(ex);
imprime_lista(ex);
//{4,8,19,2,7,9,22,8}
insere_ord (&ex, 4);
insere_ord (&ex, 8);
insere_ord (&ex, 19);
insere_ord (&ex, 2);
insere_ord (&ex, 7);
insere_ord (&ex, 9);
insere_ord (&ex, 22);
insere_ord (&ex, 8);
menor_lista(&ex);       //retira o 2
tamanho_lista(ex);
imprime_lista(ex);
remove_ord(&ex, 8);
menor_lista(&ex);       //retira o 4
tamanho_lista(ex);
imprime_lista(ex);
remove_ord(&ex, 4);
menor_lista(&ex);       //retira o 7
tamanho_lista(ex);
imprime_lista(ex);
remove_ord(&ex, 8);
menor_lista(&ex);       //retira o 9
tamanho_lista(ex);
imprime_lista(ex);
free(ex);
return 0;
}
