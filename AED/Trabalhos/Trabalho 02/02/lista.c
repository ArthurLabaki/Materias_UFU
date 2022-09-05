#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

                    //Lista com encadeamento duplo
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
    if (N == NULL)
        return 0;
    N->info = elem;
    N->ant = NULL;
    N->prox = *lst;
    if (lista_vazia(*lst) == 0)
        (*lst)->ant = N;
    *lst = N;
    return 1;
}

int remove_elemento (Lista *lst, int elem) {
    if (lista_vazia(*lst) ==1)
        return 0;
    Lista aux = *lst;
    while (aux->prox != NULL && aux->info != elem)
        aux = aux->prox;
    if (aux->info != elem)
        return 0;
    if (aux->prox != NULL)
        (aux)->prox->ant = aux->ant;
    if (aux->ant != NULL)
        (aux)->ant->prox = aux->prox;
    if (aux == *lst)
        *lst = aux->prox;
    free(aux);
    return 1;
}

int imprime_lista(Lista lst){
    if(lista_vazia(lst) == 1){
        printf("Lista vazia.\n");
        return 0;
    }
    Lista aux = lst;
    printf("-[");
    while(aux->prox != NULL){
        printf(" %d -",aux->info);
        aux = aux->prox;
    }
    printf(" %d ]-\n",aux->info);
    return 1;
}

int tamanho(Lista lst){
    if(lista_vazia(lst) == 1){
        printf("Lista com 0 elementos.\n");
        return 0;
    }
    Lista aux = lst;
    int x=0;
    while(aux->prox != NULL){
        x++;
        aux = aux->prox;
    }
    x++;    //nao conta o ultimo elem
    printf("A lista tem %d elementos\n",x);
    return 1;
}

int remove_maior(Lista *lst){
     if(lista_vazia(*lst) == 1)
        return 0;
    Lista aux = (*lst);
    int x = (*lst)->info;
    while(aux->prox != NULL){  //avancando -> Encontrando o maior
        if(x<aux->info)
            x = aux->info;
        aux = aux->prox;
    }
    if(aux->info > x)
        x = aux->info;
    while (aux->ant != NULL && aux->info != x) //voltando <- Remover o x
        aux = aux->ant;
    if (aux->info != x)
        return 0;
    if (aux->prox != NULL)
        (aux)->prox->ant = aux->ant;
    if (aux->ant != NULL)
        (aux)->ant->prox = aux->prox;
    if (aux == *lst)
        *lst = aux->prox;
    free(aux);
    return 1;
}
