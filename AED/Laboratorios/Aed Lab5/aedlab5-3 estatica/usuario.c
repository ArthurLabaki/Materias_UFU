#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10

int main(){
int x;
Lista ex;
ex = cria_lista();
if (ex == NULL) {
    printf ("Nao foi possivel criar a lista.\n");
    return -1;
}
menor_elem(ex);                 //Nao remove nenhum elemento
tamanho_lista(ex);              //0 elementos
print_lista(ex);
for(x=0;x<= max; x++){
    insere_elem(ex, x);             // nao vai colocar o 10 na lista pois o maximo dela sao 10 elementos
}
menor_elem(ex);                 //retira o elemento 0
tamanho_lista(ex);              //printa 9 elementos
print_lista(ex);
remove_elem(ex, 8);             //retira o 8
menor_elem(ex);                 //retira o elemento 1
tamanho_lista(ex);              //printa 7 elementos
print_lista(ex);
ex = cria_lista();
if (ex == NULL) {
    printf ("Nao foi possivel criar a lista.\n");
    return -1;
}
menor_elem(ex);                 //nao remove nenhum elemento
tamanho_lista(ex);              //printa 0 elementos
print_lista(ex);
free(ex);

return 0;
}
