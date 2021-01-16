#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"

struct no {
    int info;
    struct no* prox;
};

Pilha cria_pilha () {
    return NULL;
}

int pilha_vazia (Pilha p) {
    if (p == NULL)
        return 1;
    else
        return 0;
}

int push (Pilha *p, int elem) {
    Pilha N = (Pilha) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = *p;
    *p = N;
    return 1;
}

int pop (Pilha *p, int *elem) {
    if (pilha_vazia(*p) == 1)
        return 0;
    Pilha aux = *p;
    *elem = aux->info;
    *p = aux->prox;
    free(aux);
    return 1;
}

int le_topo (Pilha *p, int *elem) {
    if (pilha_vazia(*p) == 1)
        return 0;
    *elem = (*p)->info;
    return 1;
}

int imprime (Pilha p){
    if (pilha_vazia(p) == 1){
        printf("Lista vazia\n");
        return 0;}
        Pilha aux = p;
        printf("\n");
    while(aux->prox != NULL){
        printf("| %d |\n",aux->info);
        aux = aux->prox;
    }
    printf("| %d |\n",aux->info);
    printf(" ___ \n\n");
}

int respectivo (A,F){
    if ((A == '(' && F == ')') || (A == '[' && F == ']' )||( A == '{' && F == '}'))
        return 1;
    else
        return 0;
}

int valida_escopo(char S[100]){
    Pilha p;
    p = cria_pilha();
    int i = 0,C;
    while(S[i]!= '\0'){
        if (S[i]=='(' || S[i]=='{' || S[i]=='[')
            push(&p,S[i]);
        else{
            if(S[i]==')' || S[i]=='}' || S[i]==']' ){
                if(pop(&p,&C)==0){
                    return 0;}
                else{
                    if(respectivo(C,S[i])==0 )
                        return 0;
                }
            }
        }
        i++;
    }
    if(pilha_vazia(p)==1)
        return 1;
    else
        return 0;
}
