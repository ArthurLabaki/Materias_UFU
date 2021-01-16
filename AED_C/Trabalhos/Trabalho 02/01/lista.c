#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

                                        //Lista com encadeamento circular
struct no {
    int info;
    struct no * prox;
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

int insere_final (Lista *lst, int elem) {
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    if (lista_vazia(*lst) == 1) {
        N->prox = N;
        *lst = N;
    }
    else {
        N->prox = (*lst)->prox;
        (*lst)->prox = N;
        *lst = N;
    }
    return 1;
}

int remove_inicio (Lista *lst, int *elem) {
    if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux = (*lst)->prox;
    *elem = aux->info;
    if (*lst == (*lst)->prox)
        *lst = NULL;
    else
        (*lst)->prox = aux->prox;
    free(aux);
    return 1;
}

int imprime_lista(Lista lst){
    if (lista_vazia(lst) == 1){
        printf("Lista vazia!\n");
        return 0;}
    Lista aux = (lst)->prox;
    printf("-[");
    while(aux->prox != (lst)->prox){
        printf(" %d -",aux->info);
        aux = aux->prox;
    }
    printf(" %d ]-\n",aux->info);
    return 1;
}

int tamanho(Lista lst){
    if (lista_vazia(lst) == 1){
        printf("Lista com 0 elementos!\n");
        return 0;}
    Lista aux = lst->prox;
    int tam =0;
    while(aux->prox != (lst)->prox){
        tam++;
        aux = aux->prox;
    }
    tam++;  //o while nao conta o ultimo elemento
    printf("A lista tem %d elementos.\n",tam);
    return 1;
}

int maior(Lista lst, int *elem){
    if (lista_vazia (lst) == 1)
        return 0;
    int x = lst->info;
    Lista aux = lst->prox;
    while(aux->prox != lst->prox){
        if(x< aux->info)
            x = aux->info;
        aux = aux->prox;
    }
    *elem = x;
    return 1;
}
