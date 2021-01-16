#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

int main(){

Lista *ex;
ex = cria_lista();
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
imprime_lista(ex);
remove_ord(&ex, 8);
imprime_lista(ex);
remove_ord(&ex, 4);
imprime_lista(ex);
remove_ord(&ex, 8);
imprime_lista(ex);
free(ex);
return 0;
}
