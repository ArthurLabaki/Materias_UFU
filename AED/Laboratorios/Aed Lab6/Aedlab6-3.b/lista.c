
#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct no {
int info;
struct no * prox;
};

Lista cria_lista() {
// Aloca nó cabeçalho
Lista cab;
cab = (Lista) malloc(sizeof(struct no));
// Coloca lista no estado de vazia
if (cab != NULL) { // Só se alocação NÃO falhar
cab->prox = NULL;
cab->info = 0; } // Opcional: guardar qtde
return cab;
}

int lista_vazia(Lista lst) {
if (lst->prox == NULL)
return 1; // Lista vazia
else
return 0; // Lista NÃO vazia
}

int insere_ord (Lista *lst, int elem) {
// Aloca um novo nó
Lista N = (Lista) malloc(sizeof(struct no));
if (N == NULL) { return 0; } // Falha: nó não alocado
N->info = elem; // Insere o conteúdo (valor do elem)
Lista aux = *lst; // Faz aux apontar para nó cabeçalho
while (aux->prox != NULL && aux->prox->info <
elem)
aux = aux->prox; // Avança
// Insere o novo nó na lista
N->prox = aux->prox;
aux->prox = N;
(*lst)->info++; // Opcional: Incrementa qtde de nós na lista
return 1; }

int remove_ord (Lista *lst, int elem) {
if (lista_vazia(*lst) == 1)
return 0; // Falha
Lista aux = *lst; // Ponteiro auxiliar para nó cabeçalho
while (aux->prox != NULL && aux->prox->info < elem)// Percorrimento
aux = aux->prox; // até o final de lista, achar elem ou nó maior
if (aux->prox == NULL || aux->prox->info > elem)
return 0; // Falha
// Remove elemento da lista
Lista aux2 = aux->prox; // Aponta nó a ser removido
aux->prox = aux2->prox; // Retira nó da lista
free(aux2); // Libera memória alocada
(*lst)->info--; // Opcional: Decrementa qtde de nós na lista
return 1;
}


int imprime_lista(Lista lst){
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

int tamanho_lista(Lista lst){
    Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf("Lista vazia! \n");
        return 0;}
    printf("A lista tem %d elementos \n",(aux->info) +1); //cabeçalho informa o tamanho da lista
    return 1;
}

int menor_elem(Lista *lst){
    Lista aux = *lst;
    Lista aux2 = *lst;
    if (lista_vazia(*lst) == 1){
        printf("Lista vazia! \n");
        return 0;}
        //aponta para o cabeçalho
    aux2 = aux2->prox;      //aponta para o primeiro elemento
    aux->prox = aux2->prox; //retira o primeiro elemento pois eh ordenado
    printf("%d retirado\n",aux2->info);
    (*lst)->info--; //diminui 1 do cabeçalho
    free(aux2);
    return 1;
}
