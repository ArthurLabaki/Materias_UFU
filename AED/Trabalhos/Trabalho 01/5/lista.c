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
N->prox = *lst; /// Aponta para o 1onó atual da lista
*lst = N; /// Faz a lista apontar para o novo nó
return 1; }
// Percorrimento da lista (elem > 1o nó da lista)
Lista aux = *lst; // Faz aux apontar para 1o nó
while (aux->prox != NULL && aux->prox->info < elem)
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

int imprime_lista(Lista lst){
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
    return 1;
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
    return 1;
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

int remove_impar(Lista *lst){
        if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux3 = *lst;
    if ((*lst)->info%2!=0) {
        *lst = aux3->prox;
        free(aux3);
    }
    Lista aux = *lst;
    while(aux->prox != NULL){
        if(aux->prox->info %2 != 0){
            Lista aux2 = aux->prox;
            aux->prox = aux2->prox;
            free(aux2);

        }else{
        aux = aux->prox;}
    }
    return 1;
}

int igual(Lista p, Lista q){
     if (lista_vazia(p) == 1 && lista_vazia(q) == 1){
        printf("Listas Vazias iguais\n");
        return 0;
     }
     if (lista_vazia(p) == 0 &&  lista_vazia(q) == 1 || lista_vazia(p) == 1 &&  lista_vazia(q) == 0 ){
        printf("Uma lista eh vazia e a outra n \n");
        return 0;
     }
     Lista auxp = p;
     Lista auxq = q;
     while(auxp->prox != NULL && auxq->prox != NULL){
        if(auxp->info != auxq->info){
            printf("listas diferentes\n");
            return 0;
        }
        auxp = auxp->prox;
        auxq = auxq->prox;
     }
     if(auxp->prox == NULL && auxq->prox == NULL){
     printf("Listas iguais \n");
     return 0;}
     else{
        printf("Listas com tamanhos diferentes nao sao iguais\n");
        return 0;
     }
}

int intercala_lista(Lista p, Lista q, Lista *r){
    Lista aux3 = (*r);
    Lista aux1 = p;
    Lista aux2 = q;
    Lista novo;
    while(aux1!=NULL && aux2 != NULL){
        novo = (Lista) malloc(sizeof(struct no));
        if (novo == NULL) { return 0; }
        if(aux1->info <= aux2->info){
            novo->info = aux1->info;
            aux1=aux1->prox;
        }else{
        novo->info = aux2->info;
        aux2=aux2->prox;
        }
        if((*r) == NULL){
            (*r)=novo;
        }else
        aux3->prox=novo;
    aux3 = novo;

    }
    while(aux1!=NULL){
        novo = (Lista) malloc(sizeof(struct no));
        if (novo == NULL) { return 0; }
        novo->info = aux1->info;
        aux1 = aux1->prox;
        if((*r)==NULL)
            (*r)=novo;
        else
            aux3->prox = novo;
        aux3 = novo;

    }
    while(aux2!=NULL){
        novo = (Lista) malloc(sizeof(struct no));
        if (novo == NULL) { return 0; }
        novo->info = aux2->info;
        aux2 = aux2->prox;
        if((*r)==NULL)
            (*r)=novo;
        else
            aux3->prox = novo;
        aux3 = novo;

    }
    if(aux3 != NULL)
        aux3->prox = NULL;
    return 1;
}


