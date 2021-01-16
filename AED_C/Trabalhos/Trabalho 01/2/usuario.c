#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10

int main(){

Lista ex;
ex = cria_lista();
if (ex == NULL) {
    printf ("Nao foi possivel criar a lista.\n");
    return -1;
}
Lista ex2;
ex2 = cria_lista();
if (ex2 == NULL) {
    printf ("Nao foi possivel criar a lista.\n");
    return -1;
}
Lista ex3;
ex3 = cria_lista();
if (ex3 == NULL) {
    printf ("Nao foi possivel criar a lista.\n");
    return -1;
}
insere_elem(ex,1);
insere_elem(ex,4);
insere_elem(ex,12);
insere_elem(ex,6);
insere_elem(ex,4);
insere_elem(ex,0);
print_lista(ex);
tamanho_lista(ex);
remove_elem(ex,4);
print_lista(ex);
tamanho_lista(ex);
remove_impar(ex);
print_lista(ex);
tamanho_lista(ex);
insere_elem(ex2,2);
insere_elem(ex2,66);
insere_elem(ex2,6);
insere_elem(ex2,4);
insere_inicio(ex2,4);
print_lista(ex2);
tamanho_lista(ex2);
menor_elem(ex2);
print_lista(ex2);
tamanho_lista(ex2);
remove_todos(ex2,4);
print_lista(ex2);
tamanho_lista(ex2);
printf("\n");
print_lista(ex);
print_lista(ex2);
print_lista(ex3);
concatena_lista(ex,ex2,ex3);
print_lista(ex3);
free(ex);
free(ex2);
free(ex3);
return 0;


}

