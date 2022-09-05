#include <stdio.h>
#include <stdlib.h>
#include "deque.h"

struct no{
    int info;
    struct no *prox;
    struct no *ant;
};

struct fila{
    struct no *ini;
    struct no *fim;
};

Deque cria_deque(){
    Deque f;
    f = (Deque)malloc(sizeof(struct fila));
    if(f!=NULL){
        f->ini = NULL;
        f->fim = NULL;
    }
    return f;
}

int deque_vazio(Deque d){
    if (d->ini == NULL)
        return 1;
    else
        return 0;
}

int insere_ini(Deque d, int elem){
    struct no *N;
    N = (Deque)malloc(sizeof(struct no));
    if(N!=NULL){
        if(d->ini == NULL){
            N->info = elem;
            N->prox = NULL;
            N->ant = NULL;
            d->ini = N;
            d->fim = N;
            return 1;
        }
        N->info = elem;
        N->prox = d->ini;
        N->ant = NULL;
        (d->ini)->ant = N;
        d->ini = N;
        return 1;
    }
    else
        return 0;
}

int insere_fim(Deque d, int elem){
    struct no *N;
    N = (Deque)malloc(sizeof(struct no));
    if(N!=NULL){
            if(d->fim == NULL){
            N->info = elem;
            N->prox = NULL;
            N->ant = NULL;
            d->ini = N;
            d->fim = N;
            return 1;
        }
        N->info = elem;
        N->prox = NULL;
        N->ant = d->fim;
        (d->fim)->prox = N;
        d->fim = N;
        return 1;
    }
    else
        return 0;
}

int remove_ini(Deque d, int *elem){
    if (deque_vazio(d)==1)
        return 0;
    struct no *aux = d->ini;
    elem = aux->info;
    if(aux->prox==NULL){
        d->ini = NULL;
        d->fim = NULL;
        free(aux);
        return 1;
    }
    d->ini = aux->prox;
    (d->ini)->ant = NULL;
    free(aux);
    return 1;
}

int remove_fim(Deque d, int *elem){
    if (deque_vazio(d)==1)
        return 0;
    struct no *aux = d->fim;
    elem = aux->info;
    if(aux->ant==NULL){
        d->ini = NULL;
        d->fim = NULL;
        free(aux);
        return 1;
    }
    d->fim = aux->ant;
    (d->fim)->prox = NULL;
    free(aux);
    return 1;
}

int imprime_deque(Deque d){
    if (deque_vazio(d)==1){
        printf("Deque vazio\n");
        return 0;}
        printf(" -[ ");
    struct no *aux = d->ini;
    while(aux->prox != NULL){
        printf("%d ",aux->info);
        aux = aux->prox;
    }
    printf("%d ]-\n",aux->info);
    return 1;
}


