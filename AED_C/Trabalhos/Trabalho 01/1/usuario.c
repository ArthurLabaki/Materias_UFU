#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "ponto.h"

int main()
{
    int j=1,i;
    int x[4],y[4];
    printf("Digite o x1:\n");
    scanf("%d",&x[0]);
    printf("Digite o y1:\n");
    scanf("%d",&y[0]);
    printf("Digite o x2:\n");
    scanf("%d",&x[1]);
    printf("Digite o y2:\n");
    scanf("%d",&y[1]);
    printf("Digite o x3:\n");
    scanf("%d",&x[2]);
    printf("Digite o x3:\n");
    scanf("%d",&y[2]);
    printf("Digite o x4:\n");
    scanf("%d",&x[3]);
    printf("Digite o y4:\n");
    scanf("%d",&y[3]);
    ponto P[4];
    P[0] = criaPonto(P[0],x[0],y[0]);
    P[1] = criaPonto(P[1],x[1],y[1]);
    P[2] = criaPonto(P[2],x[2],y[2]);
    P[3] = criaPonto(P[3],x[3],y[3]);
    float maior=0;
    float menor = calculaDistancia(P[0],P[1]);
    for(i=0;i<4;i++){
        while(j<4){
            if(j!=i){
                printf("Distancia entre P%d e P%d: %f\n",i+1,j+1,calculaDistancia(P[i],P[j]));
                if(maior<calculaDistancia(P[i],P[j])){
                    maior = calculaDistancia(P[i],P[j]);
                }
                if(menor>calculaDistancia(P[i],P[j])){
                    menor = calculaDistancia(P[i],P[j]);
                }
            }
            j++;
        }
        j=i+1;
    }
    printf("maior distancia: %f\n", maior);
    printf("menor distancia: %f\n", menor);
    liberarPonto(P[0]);
    liberarPonto(P[1]);
    liberarPonto(P[2]);
    liberarPonto(P[3]);
}
