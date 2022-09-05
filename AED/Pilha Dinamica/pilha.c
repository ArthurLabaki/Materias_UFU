#include <stdlib.h>
#include <stdio.h>
#include "pilha.h"


struct no {
    int info;
    struct no* prox;
};

Pilha cria_pilha () {           //Cria a pilha
    return NULL;
}

int pilha_vazia (Pilha p) {         //Verifica se a pilha esta vazia
    if (p == NULL)
        return 1;
    else
        return 0;
}

int push (Pilha *p, int elem) {         //Insere o elemento no topo da pilha
    Pilha N = (Pilha) malloc(sizeof(struct no));
    if (N == NULL)
        return 0;
    N->info = elem;
    N->prox = *p;
    *p = N;
    return 1;
}

int pop (Pilha *p, int *elem) {         //Remove o elemento do topo da pilha
    if (pilha_vazia(*p) == 1)
        return 0;
    Pilha aux = *p;
    *elem = aux->info;
    *p = aux->prox;
    free(aux);
    return 1;
}

int le_topo (Pilha p, int *elem) {          //Retorna o elemento do topo da pilha
    if (pilha_vazia(p) == 1)
        return 0;
    *elem = (p)->info;
    return 1;
}

int imprime_pilha (Pilha p) {           //Imprime a pilha
    if (pilha_vazia (p) == 1){
        printf("Pilha vazia!\n");
        return 0;
    }
    Pilha aux = p;
    printf("(topo) -");
    while(aux->prox != NULL){
        printf(" %d -",aux->info);
        aux = aux->prox;
    }
    printf(" %d ]- base\n",aux->info);
    return 1;
}

int palindrome (char x[100], int tam){          //Verifica se a string eh um palindromo
    int k,a,b;
    Pilha p,q;
    p = cria_pilha();
    q = cria_pilha();
    for(k=0;k<tam;k++){
        push(&p,x[k]);
    }
    for(k=tam-1;k>=0;k--){
        push(&q, x[k]);
    }
    k=0;
    while(k<=tam){
        pop(&p,&a);
        pop(&q,&b);
        if(a != b){
            printf("Nao sao palindromos\n");
            return 0;
        }
        k++;
    }
    printf("Sao palindromos\n");
    return 1;
}

int pares_e_impares (Pilha *a, Pilha *par, Pilha *impar){           //Separa uma pilha em duas com pares ou impares
    if (pilha_vazia (*a) == 1){
        printf("Pilha vazia!\n");
        return 0;}
    int x;
    while(pilha_vazia (*a) != 1){
        pop(a,&x);
        if(x%2==0){
            push(par,x);
        }
        else{
            push(impar,x);
        }
    }
    return 1;
}

                                        //Retorna 1 para sucesso e 0 para erro
