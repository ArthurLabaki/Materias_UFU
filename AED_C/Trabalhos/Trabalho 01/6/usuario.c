#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){

Lista *ex;
ex = cria_lista();
Lista *ex2;
ex2 = cria_lista();
Lista *ex3;
ex3 = cria_lista();
menor_elem(&ex);
tamanho_lista(ex);
imprime_lista(ex);
//{4,8,19,2,7,9,22,8}
insere_ord (&ex, 8);
insere_ord (&ex2, 4);
insere_ord (&ex2, 2);
insere_ord (&ex2, 8);
imprime_lista(ex);
remove_impar(&ex);
imprime_lista(ex);
imprime_lista(ex2);
intercala_lista(ex,ex2,&ex3);
imprime_lista(ex3);
free(ex);
free(ex2);
free(ex3);
return 0;
}
