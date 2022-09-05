#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"
# define max 20


int main(){
    int x,y,z=0;
    inicio:
    printf("Digite o numero em decimal\n");
    scanf("%d",&x);
        converter:
        printf("Digite 1 para converter para binario \nDigite 2 para converter para octal \nDigite 3 para converter para hexadecimal\n");
        scanf("%d",&y);
        if(y==1){
            dec_to_bin(x);
        }
        if(y==2){
            dec_to_oct(x);
        }
        if(y==3){
            dec_to_hexa(x);
        }
        if(y>3 || y <1){
            printf("Numero invalido!!\n");
            return 0;}
    printf("Digite 1 para converter para outra base \nDigite 2 para mudar o numero \nDigite 3 para finalizar\n");
    scanf("%d",&y);
    if(y==1){
            goto converter;
        }
        if(y==2){
            goto inicio;
        }
        if(y==3){
            return 1;
        }
        if(y>3 || y <1){
            printf("Numero invalido!!\n");
            return 0;}
}
