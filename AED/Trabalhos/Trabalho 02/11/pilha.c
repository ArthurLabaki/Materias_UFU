#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
#include <math.h>


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

int pushf (Pilha *p, float elem) {
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

int popf (Pilha *p, float *elem) {
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


int inf_para_pos(char *S, char *R){
    char posf[100];
    int x=0,elem,c,i=0;
    Pilha p;
    p = cria_pilha();
    push(&p, '(');
    while(S[x] != '\0'){
        if(S[x]== '('){
            push(&p,S[x]);
        }else{
            if(S[x] == ')'){
                le_topo(&p, &elem);
                while(elem != '('){
                      pop(&p, &c);
                      posf[i] = c;
                      i++;
                      le_topo(&p, &elem);
                }
                pop(&p,&c);
            }else{
                if(S[x] == '+' || S[x] == '-' ){
                    le_topo(&p, &elem);
                    while(elem != '('){
                        pop(&p, &c);
                        posf[i] = c;
                        i++;
                        le_topo(&p, &elem);
                    }
                    push(&p,S[x]);
                }else{
                    if(S[x] == '*' || S[x] == '/' ){
                        le_topo(&p, &elem);
                        while(elem != '(' && elem != '+' && elem != '-' ){
                            pop(&p, &c);
                            posf[i] = c;
                            i++;
                            le_topo(&p, &elem);
                        }
                        push(&p,S[x]);
                    }else{
                        if(S[x] == '^'){
                        le_topo(&p, &elem);
                        while(elem != '(' && elem != '+' && elem != '-' && elem != '*' && elem != '/' ){
                            pop(&p, &c);
                            posf[i] = c;
                            i++;
                            le_topo(&p, &elem);
                        }
                        push(&p,S[x]);
                        }else{
                        posf[i] = S[x];
                        i++;
                        }
                    }
                }
            }
        }
        x++;
    }
    posf[i] = '\0'; //
    int test = 0;
    while(posf[test] != '\0'){
        R[test] = posf[test];
        test++;
    }
    R[test] = '\0';
    return 1;
}
int resolver_eq(char *S, int a[]){
    int x=0;
    float elem1,elem2,eq;
    Pilha p;
    p = cria_pilha();
    while(S[x] != '\0'){
        if(S[x] == 'a')
            pushf(&p, a[0]);
        if(S[x] == 'b')
            pushf(&p, a[1]);
        if(S[x] == 'c')
            pushf(&p, a[2]);
        if(S[x] == 'd')
            pushf(&p, a[3]);
        if(S[x] == 'e')
            pushf(&p, a[4]);
        if(S[x] == 'f')
            pushf(&p, a[5]);
        if(S[x] == 'g')
            pushf(&p, a[6]);
        if(S[x] == 'h')
            pushf(&p, a[7]);
        if(S[x] == 'i')
            pushf(&p, a[8]);
        if(S[x] == 'j')
            pushf(&p, a[9]);
        if(S[x] == '+'){
            popf(&p, &elem1);
            popf(&p, &elem2);
            eq = elem2 + elem1;
            pushf(&p, eq);
        }
        if(S[x] == '-'){
            popf(&p, &elem1);
            popf(&p, &elem2);
            eq = elem2 - elem1;
            pushf(&p, eq);
        }
        if(S[x] == '*'){
            popf(&p, &elem1);
            popf(&p, &elem2);
            eq = elem2 * elem1;
            pushf(&p, eq);
        }
        if(S[x] == '/'){
            popf(&p, &elem1);
            popf(&p, &elem2);
            eq = elem2 / elem1;
            pushf(&p, eq);
        }
        if(S[x] == '^'){
            popf(&p, &elem1);
            popf(&p, &elem2);
            eq = pow(elem2, elem1);
            pushf(&p, eq);
        }
    x++;
    }
    popf(&p, &eq);
    printf("O RESULTADO ARREDONDADO EH :%.2f\n",eq);
    return 1;
}


