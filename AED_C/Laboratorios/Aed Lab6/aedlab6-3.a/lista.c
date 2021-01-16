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
// Aloca um novo n�
Lista N = (Lista) malloc(sizeof(struct no));
if (N == NULL) { return 0; } // Falha: n� n�o alocado
N->info = elem; // Insere o conte�do (valor do elem)
if (lista_vazia(*lst) || elem <= (*lst)->info) {
N->prox = *lst; // Aponta para o 1on� atual da lista
*lst = N; // Faz a lista apontar para o novo n�
return 1; }
// Percorrimento da lista (elem > 1o n� da lista)
Lista aux = *lst; // Faz aux apontar para 1o n�
while (aux->prox != NULL && aux->prox->info <
elem)
aux = aux->prox; // Avan�a
// Insere o novo elemento na lista
N->prox = aux->prox;
aux->prox = N;
return 1;
}

int remove_ord (Lista *lst, int elem) {
if (lista_vazia(*lst) == 1 || elem < (*lst)->info)
return 0; // Falha
Lista aux = *lst; // Ponteiro auxiliar para o 1o n�
if (elem == (*lst)->info) { // Remove elemento 1o n� da lista
*lst = aux->prox; // Lista aponta para o 2o n�
free(aux); // Libera mem�ria alocada
return 1; }
while (aux->prox != NULL && aux->prox->info < elem)
aux = aux->prox;
if (aux->prox == NULL || aux->prox->info > elem)
return 0; // Falha
// Remove elemento (ap�s o 1o n� da lista)
Lista aux2 = aux->prox; // Aponta n� a ser removido
aux->prox = aux2->prox; // Retira n� da lista
free(aux2); // Libera mem�ria alocada
return 1;
}

void imprime_lista(Lista lst){
        Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf("Lista vazia! \n");
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

int tamanho_lista(Lista lst){
    Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf("0 elementos! \n");
        return 0;}
    int x=1;            //x = 1 pois quando for o ultimo elemento, ele vai sair do while e nao ira somar 1 no x
    while(aux->prox != NULL){
        x++;
        aux = aux->prox;
    }
    printf("A lista tem %d elementos\n",x);
}

int menor_lista(Lista *lst){
    Lista aux = *lst;
     if (lista_vazia(*lst) == 1){
        printf("Nenhum elemento retirado! \n");
        return 0;
    }                   //como eh lista ordenada, basta retirar o primeiro elemeno dela
    Lista aux2 = *lst;
    *lst = aux->prox;
    free(aux2);
    return 1;
}
