#include <stdio.h>
#include <stdlib.h>
#include "fila.h"
                    //Fila de prioridade descendente (REMOVE O MAIOR)
                    //Fila com encadeamento simples e ordenada
struct no{
    int info;
    struct no *prox;
};

struct fila{
    struct no *ini;
    struct no *fim;
};

Fila cria_fila(){
    Fila f;
    f = (Fila)malloc(sizeof(struct fila));
    if(f!= NULL){
        f->ini = NULL;
        f->fim = NULL;
    }
    return f;
}

int fila_vazia(Fila f){
    if(f->ini == NULL)
        return 1;
    else
        return 0;
}

int insere_ord(Fila f, int elem){       //insere decrescente
   struct no *N;
   N = (struct no*)malloc(sizeof(struct no));
   if(N==NULL)
        return 0;
   N->info = elem;
   if(fila_vazia(f)==1){
    N->prox = NULL;
    f->ini = N;
    f->fim = N;
    return 1;
   }
   else{
        if(elem >= (f->ini)->info){
            N->prox = (f->ini);
            f->ini = N;
            return 1;
        }
        else{
            struct no *aux = f->ini;
            while(aux->prox != NULL && aux->prox->info > elem)
                aux = aux->prox;
            if(aux->prox ==NULL){
                N->prox = NULL;
                aux->prox = N;
                f->fim = N;
                return 1;
            }
            else{
                N->prox = aux->prox;
                aux->prox = N;
                return 1;
            }

        }
   }
}
int remove_ini(Fila f, int *elem){
     if(fila_vazia(f)==1)
        return 0;
    struct no *aux = f->ini;
    *elem = aux->info;
    if(f->ini == f->fim)
        f->fim = NULL;
    f->ini = aux->prox;
    free(aux);
    return 1;
}



int imprime_fila(Fila f){
    if(fila_vazia(f)==1){
        printf("Fila vazia!\n");
        return 0;
    }
    struct no *aux = f->ini;
    printf("-[");
    while(aux->prox != NULL){
        printf(" %d",aux->info);
        aux = aux->prox;
    }
    printf(" %d ]-\n",aux->info);
    return 1;
}
