#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
# define max 20

struct pilha {
int no[max];
int topo;
};

Pilha cria_pilha () {
    Pilha p;
    p = (Pilha) malloc (sizeof (struct pilha));
    if (p != NULL)
        p->topo = -1;
    return p;
}

int pilha_vazia (Pilha p) {
    if (p->topo == -1)
        return 1;
    else
        return 0;
}

int pilha_cheia (Pilha p) {
    if (p->topo == max-1)
        return 1;
    else
        return 0;
}

int push (Pilha p, int elem) {
    if (p == NULL || pilha_cheia(p) == 1)
        return 0;
    p->topo++;
    p->no[p->topo] = elem;
    return 1;
}

int pop (Pilha p, int *elem) {
    if (p == NULL || pilha_vazia(p) == 1)
        return 0;
    *elem = p->no[p->topo];
    p->topo--;
    return 1;
}

int le_topo (Pilha p, int *elem) {
    if (p == NULL || pilha_vazia(p) == 1)
        return 0;
    *elem = p->no[p->topo];
    return 1;
}

int imprime(Pilha p){
    if (p == NULL || pilha_vazia(p) == 1){
        printf("Pilha vazia\n");
        return 0;}
    int x = 0;
    printf(" ___\n");
    while(x<=p->topo){
        printf("| %d |\n",p->no[x]);
        x++;
    }
    printf("\n");
    return 1;
}

int Dec_to_Bin(int elem){
    Pilha p;
    p = cria_pilha();
    int R;
    while(elem != 0 && pilha_cheia(p)==0){
        R=elem%2;
        elem = elem /2;
        push(p,R);
    }
    if(pilha_cheia(p)==1){
        printf("Estouro de pilha\n");
        return 0;
    }else{
        while(pilha_vazia(p)==0){
            pop(p,&R);
            printf("%d",R);
        }
        return 1;
    }
}


