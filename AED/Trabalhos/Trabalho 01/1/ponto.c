#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "ponto.h"

struct coordenadas{
    int x;
    int y;
};

ponto criaPonto(ponto A,int x,int y){
    A = (ponto) malloc(sizeof(ponto));
    if(A == NULL){
        printf("Não foi possivel criar o ponto.\n");
        return NULL;
    }
    else{
        A->x = x;
        A->y = y;
        return A;
    }
}

int getValorX(ponto A){
    return A->x;
}

int getValorY(ponto A){
    return A->y;
}

float calculaDistancia(ponto A, ponto B){
    float D;
    D = sqrt(((B->x)-(A->x))*((B->x)-(A->x))+((B->y)-(A->y))*((B->y)-(A->y)));
    return D;
}

void liberarPonto(ponto A){
    free(A);
}
