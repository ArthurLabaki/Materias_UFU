
#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

struct no {
    int info;
    struct no *prox;
};

Lista cria_lista(){
    return NULL;
}

int lista_vazia(Lista lst){
    if (lst == NULL)
        return 1;
    else
        return 0;
}

int insere_elem(Lista *lst, int elem){
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = *lst;
    *lst = N;
    return 1;
}

int remove_elem (Lista *lst, int elem) {
    if (lista_vazia(*lst) == 1) {return 0;}
    Lista aux = *lst;
    if (elem == (*lst)->info) {
        *lst = aux->prox;
        free(aux);
        return 1;
    }
    while (aux->prox != NULL && aux->prox->info != elem)
        aux = aux->prox;
    if (aux->prox == NULL)
        return 0;
    Lista aux2 = aux->prox;
    aux->prox = aux2->prox;
    free(aux2);
    return 1;
}

int imprime_lista(Lista lst){
    Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf(" -[ ]-\n");
        return 0;
    }
    printf(" -[");
    while (aux!= NULL){
        printf(" %d",aux->info);
        aux = aux->prox;
        }
        printf(" ]- \n");
}

int tamanho_lista(Lista lst){
    Lista aux = lst;
    if (lista_vazia(lst)==1){
        printf("A lista tem 0 elementos\n");
        return 0;
        }
    int x=0;
    while(aux!= NULL){
        x++;
        aux = aux->prox;
    }
    printf("A lista tem %d elementos\n",x);
}

int menor_elem(Lista *lst){
    if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux = *lst;
    int x;
    x = aux->info;
    while (aux->prox != NULL){
        if (aux->info < x)
            x = aux->info;
        aux = aux->prox;
    }
    remove_elem(lst, x);
    return 1;
}

int insere_fim(Lista *lst, int elem){
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = NULL;
    if((*lst) == NULL){
        *lst = N;
        return 1;
    }else{
        Lista aux = *lst
;        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = N;
    }
    return 1;
}

int remover_todos(Lista *lst, int elem){
    if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux3 = *lst;
    Lista aux2 = *lst;
    if (elem == (*lst)->info) {
        while(aux3->info == aux3->prox->info){              //caso o elemento seguinte tambem for retirado
                aux2=aux3;
                aux3=aux3->prox;
                free(aux2);
            }
        *lst = aux3->prox;
        free(aux3);
    }
    Lista aux = *lst;
    while(aux->prox != NULL){
        if(aux->prox->info == elem){
            Lista aux2 = aux->prox;
            aux->prox = aux2->prox;
            free(aux2);

        }else{
        aux = aux->prox;}
    }
    return 1;
}

int remove_par(Lista *lst){
        if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux3 = *lst;
    Lista aux2 = *lst;
if ((*lst)->info%2==0) {
        while(aux3->prox->info%2==0){              //caso o elemento seguinte tambem for par
                aux2=aux3;
                aux3=aux3->prox;
                free(aux2);
            }
        *lst = aux3->prox;
        free(aux3);
    }
    Lista aux = *lst;
    while(aux->prox != NULL){
        if(aux->prox->info %2 == 0){
            Lista aux2 = aux->prox;
            aux->prox = aux2->prox;
            free(aux2);

        }else{
        aux = aux->prox;}
    }
    return 1;
}

int concatena_lista(Lista p, Lista q, Lista *r){      ///Concatena 2 listas
    Lista aux1 = p;
    Lista aux2 = q;
    Lista aux3 = (*r);
    Lista novo;
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
