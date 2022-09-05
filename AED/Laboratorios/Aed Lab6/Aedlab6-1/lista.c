#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct no {
int info;
struct no * prox;
};

Lista cria_lista() {
return NULL;
}

int lista_vazia(Lista lst) {
if (lst == NULL)
return 1;
else
return 0;
}

int insere_ord (Lista *lst, int elem) {
// Aloca um novo nó
Lista N = (Lista) malloc(sizeof(struct no));
if (N == NULL) { return 0; } // Falha: nó não alocado
N->info = elem; // Insere o conteúdo (valor do elem)
if (lista_vazia(*lst) || elem <= (*lst)->info) {
N->prox = *lst; // Aponta para o 1onó atual da lista
*lst = N; // Faz a lista apontar para o novo nó
return 1; }
// Percorrimento da lista (elem > 1o nó da lista)
Lista aux = *lst; // Faz aux apontar para 1o nó
while (aux->prox != NULL && aux->prox->info <
elem)
aux = aux->prox; // Avança
// Insere o novo elemento na lista
N->prox = aux->prox;
aux->prox = N;
return 1;
}

int remove_ord (Lista *lst, int elem) {
if (lista_vazia(*lst) == 1 || elem < (*lst)->info)
return 0; // Falha
Lista aux = *lst; // Ponteiro auxiliar para o 1o nó
if (elem == (*lst)->info) { // Remove elemento 1o nó da lista
*lst = aux->prox; // Lista aponta para o 2o nó
free(aux); // Libera memória alocada
return 1; }
while (aux->prox != NULL && aux->prox->info < elem)
aux = aux->prox;
if (aux->prox == NULL || aux->prox->info > elem)
return 0; // Falha
// Remove elemento (após o 1o nó da lista)
Lista aux2 = aux->prox; // Aponta nó a ser removido
aux->prox = aux2->prox; // Retira nó da lista
free(aux2); // Libera memória alocada
return 1;
}

void imprime_lista(Lista lst){
    Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf("0 elementos! \n");
        return 0;
    }
    printf(" -[");
    while(aux->prox != NULL){
        printf(" %d",aux->info);
        aux = aux->prox;
    }
    printf(" %d",aux->info);
    printf(" ]- \n");
}
