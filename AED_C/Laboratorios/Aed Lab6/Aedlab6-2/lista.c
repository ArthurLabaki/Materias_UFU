#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct no {
int info;
struct no * prox;
};

Lista cria_lista() {
// Aloca n� cabe�alho
Lista cab;
cab = (Lista) malloc(sizeof(struct no));
// Coloca lista no estado de vazia
if (cab != NULL) { // S� se aloca��o N�O falhar
cab->prox = NULL;
cab->info = 0; } // Opcional: guardar qtde
return cab;
}

int lista_vazia(Lista lst) {
if (lst->prox == NULL)
return 1; // Lista vazia
else
return 0; // Lista N�O vazia
}

int insere_ord (Lista *lst, int elem) {
// Aloca um novo n�
Lista N = (Lista) malloc(sizeof(struct no));
if (N == NULL) { return 0; } // Falha: n� n�o alocado
N->info = elem; // Insere o conte�do (valor do elem)
Lista aux = *lst; // Faz aux apontar para n� cabe�alho
while (aux->prox != NULL && aux->prox->info <
elem)
aux = aux->prox; // Avan�a
// Insere o novo n� na lista
N->prox = aux->prox;
aux->prox = N;
(*lst)->info++; // Opcional: Incrementa qtde de n�s na lista
return 1; }

int remove_ord (Lista *lst, int elem) {
if (lista_vazia(*lst) == 1)
return 0; // Falha
Lista aux = *lst; // Ponteiro auxiliar para n� cabe�alho
while (aux->prox != NULL && aux->prox->info < elem)// Percorrimento
aux = aux->prox; // at� o final de lista, achar elem ou n� maior
if (aux->prox == NULL || aux->prox->info > elem)
return 0; // Falha
// Remove elemento da lista
Lista aux2 = aux->prox; // Aponta n� a ser removido
aux->prox = aux2->prox; // Retira n� da lista
free(aux2); // Libera mem�ria alocada
(*lst)->info--; // Opcional: Decrementa qtde de n�s na lista
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
