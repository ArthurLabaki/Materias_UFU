#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
# define max 20


struct pilha {
    int no [max];
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

int imprime_pilha (Pilha p){        // x y z] -> ] significa fim da pilha
    if (p == NULL )
        return 0;
    if (pilha_vazia(p) == 1){
        printf("Pilha vazia.\n");
        return 0;
    }
    int x = p->topo;
    printf("-topo-[");
    while(x > -1){
        printf(" %d",p->no[x]);
        x--;
    }
    printf("]-base-\n");
    return 1;
}

int imprime_reverso (Pilha p){
    if (p == NULL )
        return 0;
    if (pilha_vazia(p) == 1){
        printf("Pilha vazia.\n");
        return 0;
    }
    int x = 0;
    printf("-base-[");
    while(x <= p->topo){
        printf(" %d",p->no[x]);
        x++;
    }
    printf(" ]-topo-\n");
    return 1;
}

int palindrome(char x[100],int tam){
    int k,t=0,a,b;
    Pilha p,q;
    p = cria_pilha();
    q = cria_pilha();
    for(k=0;k<tam;k++){
        push(p,x[k]);   //transforma letras em numeros (decimal) (ASCII)
    }
    for(k=tam-1;k>=0;k--){
        push(q,x[k]);
    }
    while(t<=tam){
        pop(p,&a);
        pop(q,&b);
        if(a != b){
            printf("Nao sao palindromos\n");
            return 0;
        }
        t++;
    }
    printf("Sao palindomos!\n");
    return 1;
}
