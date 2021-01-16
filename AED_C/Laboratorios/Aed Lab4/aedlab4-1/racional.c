#include <stdio.h>
#include <stdlib.h>
#include "racional.h"

struct rac{
int num;
int den;
};

racional *generate() {
racional *p;
p = (racional *) malloc(sizeof(racional));
return p; }

int set_value(racional *R, int N, int D) {
if(R==NULL||D==0) return (0);
R->num=N;
R->den=D;
return(1); }

racional *sum(racional *R1,racional *R2){
racional *R;
R = generate();
if (R != NULL) {
R->num = (R1->num*R2->den) + (R2->num*R1->den);
R->den = (R1->den * R2->den);
}
return(R); }

int print_value(racional *R) {
printf("%d/%d",R->num,R->den); }

racional *prod(racional *R3, racional*R6){
racional *M;
M = generate();
if (M != NULL){
    M->num = (R3->num * R6->num);
    M->den = (R3->den * R6->den);
    }
    return (M);
    }
