#include <stdio.h>
#include <stdlib.h>

/*
//PRIMEIRO EXECICIO

int main()
{
    int a[10],x;
    for(x=0;x<10;x++){
        printf("Digite o %d valor\n",x+1);
        scanf("%d",&a[x]);
    }
    x=0;
    while(x<10){
        if(a[x]%2==0){
            a[x] = a[x]/2;
            }
        x++;
    }
    printf("\n");
    for(x=0;x<10;x++){
        printf("- %d  -",a[x]);
    }
    printf("\n");
    return 0;
}

//SEGUNDO EXERCICIO

int* manipula_pares (int a[], int n){
    for (n=0;n<10;n++){
        if (a[n]%2==0){
            a[n] = a[n] /2;
        }
    }
    return *a;
}

int main(){
    int a[10],x;
    for(x=0;x<10;x++){
        printf("Digite o %d numero\n",x+1);
        scanf("%d",&a[x]);
        }
    *a = manipula_pares(a, x);
    printf("\n");
    for(x=0;x<10;x++){
        printf("- %d  -",a[x]);
        }
    printf("\n");
    return 0;

}

//TERCEIRO EXERCICIO

void manipula_um_par (int *a){
    *a = *a/2;
}

int* manipula_pares (int a[], int x){
    int n1;
    for (n1=0;n1<x;n1++){
        if (a[n1]%2==0){
            manipula_um_par(&a[n1]);
        }
    }
    return *a;
}

int main(){
    int a[10],x;
    for(x=0;x<10;x++){
        printf("Digite o %d numero\n",x+1);
        scanf("%d",&a[x]);
        }
    *a = manipula_pares(&a, 10);
    printf("\n");
    for(x=0;x<10;x++){
        printf("- %d  -",a[x]);
        }
    printf("\n");
    return 0;
}

*/
