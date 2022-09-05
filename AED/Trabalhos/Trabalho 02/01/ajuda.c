#include <stdio.h>
#include <stdlib.h>

int f(int *x, int *y){
    *x = 2*(*x);
    *y = 2*(*y);
    int j;
    j = (*x)+(*y);
    return j;

}
int main(){
    int *a,N=5;
    a = (int*)malloc(N*sizeof(int));

}
