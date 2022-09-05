#include <stdio.h>
#include <stdlib.h>
#include "fila.h"
#define max5


struct fila{
    int no[max];
    int ini,cont;
};

Deque cria_deque(){
    Deque d;
    d = (Deque)malloc(sizeof(struct fila));
    if(d!=NULL){
        d->ini=0;
        d->cont=0;
    }
    return d;
}

int deque_vazio (Deque d){
    if(d->cont==0)
        return 1;
    else
        return 0;
}

int deque_cheio (Deque d){
    if(d->cont==max)
        return 1;
    else
        return 0;
}

int insere_fim(Deque f, int elem){
    if(deque_cheio(f)==1)
        return 0;
    f->no[(f->ini + f->cont)%max] = elem;
    f->cont++;
    return 1;
}

int insere_ini(Deque f, int elem){
    if(deque_cheio(f)==1)
        return 0;
    f->ini--;
    if(f->ini <0)
        f->ini = max - 1;
    f->no[f->ini] = elem;
    f->cont ++;
    return 1;
}


int remove_fim(Deque f, int *elem){
    if(deque_vazio(f)==1)
        return 0;
    *elem = f->no[(f->ini + f->cont)%max-1];
    f->cont--;
    return 1;
}


int remove_ini(Deque f, int *elem){
    if(deque_vazio(f)==1)
        return 0;
    *elem = f->no[f->ini];
    f->ini = (f->ini+1)%max;
    f->cont--;
    return 1;
}

int imprime_fila(Deque f){
    if(deque_vazio(f) == 1){
        printf("Deque vazio\n");
        return 0;}
   int x = f->ini;
   int y = f->cont;
   printf("-[");
   while (y != 0){
        printf(" %d",f->no[x]);
        x++;
        if(x > (max-1))
            x = 0;
        y--;
   }
   printf(" ]-\n");
    return 1;
}
