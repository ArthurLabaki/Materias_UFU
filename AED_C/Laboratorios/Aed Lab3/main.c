#include <stdio.h>
#include <stdlib.h>

struct dados{
    char nome[5];
    int num;
};

void manipula_um_par(struct dados *v){
    (*v).num = (*v).num/2;
}

void manipula_pares(struct dados v[], int m){
    int i;
    for(i=0;i<m;i++){
        if(v[i].num%2==0){
            manipula_um_par(&v[i]);
        }
    }
}

void define_struct(struct dados **p, int n){
    struct dados *d;
    *p = (struct dados*) malloc(n*sizeof(struct dados));
    d = *p;
    int i, x;
        printf("digite o nome e os numeros:\n");
        setbuf(stdin, NULL);
    for(i=0;i<n;i++){
         printf("digite o nome:\n");
        gets(d[i].nome);
        x++;
}
    for(i=0;i<n;i++){
            printf("Insira um numero\n");
        scanf("%d",&d[i].num);
    }
}

int main() {
    int n,i;
    struct dados *p;
     printf("Digite um valor n para as structs\n");
    scanf("%d",&n);
    define_struct(&p, n);
   manipula_pares(p,n);
   printf("valor dos vetores:");
   for(i=0;i<n;i++){
        printf("numero eh:%d\n",p[i].num);
   }
   free (p);
return 0;
}
