#include <stdio.h>
#include <stdlib.h>
#include "lista.h"


struct no {
    int info;
    struct no *prox;
};


Lista cria_lista(){         //Cria lista
    return NULL;
}


int lista_vazia(Lista lst){         //Verifica se a lista esta vazia
    if (lst == NULL)
        return 1;
    else
        return 0;
}


int insere_elem(Lista *lst, int elem){          //Insere o elemento (alocando)
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = *lst;
    *lst = N;
    return 1;
}


int insere_ord (Lista *lst, int elem) {         //Insere ordenado (alocando)
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    if (lista_vazia(*lst) || elem <= (*lst)->info) {
        N->prox = *lst;
        *lst = N;
        return 1; }
    Lista aux = *lst;
    while (aux->prox != NULL && aux->prox->info < elem)
        aux = aux->prox;
    N->prox = aux->prox;
    aux->prox = N;
    return 1;
}


int insere_fim(Lista *lst, int elem){           //Insere o elemento no final da lista
    Lista N = (Lista) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = NULL;
    if((*lst) == NULL){
        *lst = N;
        return 1;
    }else{
        Lista aux = *lst;
        while(aux->prox != NULL){
            aux = aux->prox;
        }
        aux->prox = N;
    }
    return 1;
}


int remove_elem (Lista *lst, int elem) {            //Remove o elemento (desalocando)
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


int remove_ord (Lista *lst, int elem) {         //Remove ordenado (desalocando)
    if (lista_vazia(*lst) == 1 || elem < (*lst)->info)
        return 0;
    Lista aux = *lst;
    if (elem == (*lst)->info) {
        *lst = aux->prox;
        free(aux);
        return 1; }
    while (aux->prox != NULL && aux->prox->info < elem)
        aux = aux->prox;
    if (aux->prox == NULL || aux->prox->info > elem)
        return 0;
    Lista aux2 = aux->prox;
    aux->prox = aux2->prox;
    free(aux2);
    return 1;
}


int menor_elem(Lista *lst){         //Remove o menor elemento
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


int remover_todos(Lista *lst, int elem){            //Remove todos elementos
    if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux3 = *lst;
    Lista aux2 = *lst;
    if (elem == (*lst)->info) {
        while(aux3->info == aux3->prox->info){
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


int remove_par(Lista *lst){         //Remove todos os pares
        if (lista_vazia(*lst) == 1)
        return 0;
    Lista aux3 = *lst;
    Lista aux2 = *lst;
if ((*lst)->info%2==0) {
        while(aux3->prox->info%2==0){
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


int remove_impar(Lista *lst){           //Remove todos os impares
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


void imprime_lista(Lista lst){          //Imprime a lista
    Lista aux = lst;
    if (lista_vazia(lst) == 1){
        printf(" -[ ]-\n");
        return 0;}
    printf(" -[");
    while (aux!= NULL){
        printf(" %d",aux->info);
        aux = aux->prox;
        }
        printf(" ]- \n");
}


void tamanho_lista(Lista lst){           //Imprime o tamanho da lista
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


int concatena_lista(Lista p, Lista q, Lista *r){      //Concatena 2 listas
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


int igual(Lista p, Lista q){            //Verifica se 2 listas sao iguais
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


int intercala_lista(Lista p, Lista q, Lista *r){            //Intercala 2 listas em uma terceira lista
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

                        //Retorna 1 para sucesso e 0 para erro
                        //Nao usar o ordenado e o nao ordenado no mesmo user
