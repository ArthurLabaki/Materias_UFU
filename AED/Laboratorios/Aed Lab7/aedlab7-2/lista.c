#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct no {
int info;
struct no * prox;
struct no * ant;
};

Lista cria_lista() {
return NULL;
}

int lista_vazia (Lista lst) {
if (lst == NULL)
return 1;
else
return 0;
}

int insere_elemento (Lista *lst, int elem) {
Lista N = (Lista) malloc(sizeof(struct no));
if (N == NULL) { return 0; }
N->info = elem;
N->ant = NULL;
N->prox = *lst;
if (lista_vazia(*lst) == 0)
(*lst)->ant = N;
*lst = N;
return 1;
}

int remove_elemento (Lista *lst, int elem) {
if (lista_vazia(*lst)==1) return 0;
Lista aux = *lst;
while (aux->prox != NULL && aux->info != elem)
aux = aux->prox;
if (aux->info != elem) return 0;
if (aux->prox != NULL) (aux)->prox->ant = aux->ant;
if (aux->ant != NULL) (aux)->ant->prox = aux->prox;
if (aux == *lst) *lst = aux->prox;
free(aux);
return 1;
}

int imprime (Lista lst){
    if (lista_vazia(lst)==1){
        printf(" -[ ]- \n");
        return 0;}
    Lista aux = lst;
    printf(" -[");
    while(aux->prox != NULL){
        printf(" %d-",aux->info);
        aux = aux->prox;
    }
    printf(" %d",aux->info);
    printf(" ]-\n");
    return 1;
}
