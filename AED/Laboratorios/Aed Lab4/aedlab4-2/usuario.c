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
print_lista(ex);
printf("\n");
for(x=0;x<= max; x++){
    insere_elem(ex, x);             // nao vai colocar o 10 na lista pois o maximo dela sao 10 elementos
}
print_lista(ex);
printf("\n");
remove_elem(ex, 8);
print_lista(ex);
printf("\n");
ex = cria_lista();
print_lista(ex);
printf("\n");
return 0;
}
