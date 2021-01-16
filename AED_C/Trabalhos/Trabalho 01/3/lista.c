#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10

struct lista {
int no[max];
int Fim;
};

Lista cria_lista() {            //Criando a lista(alocando)
    Lista lst;
    lst = (Lista) malloc(sizeof(struct lista));
    if (lst != NULL)
        lst->Fim = 0; // Lista vazia
    return lst;
}

int lista_vazia(Lista lst) {        //Verificando se a lista esta vazia
    if (lst->Fim == 0)
        return 1; // Lista vazia
    else
        return 0; // Lista NÃO vazia
}

int lista_cheia(Lista lst) {           //Verificando se a lista esta cheia
    if (lst->Fim == max)
        return 1; // Lista cheia
    else
        return 0; // Lista NÃO cheia
}

int insere_ord(Lista lst, int elem) {
    if (lst == NULL || lista_cheia(lst) == 1)
        return 0; // Falha
    if (lista_vazia(lst) == 1 || elem >= lst->no[lst->Fim-1]) {
    lst->no[lst->Fim] = elem; // Insere no final
    }
    else {
        int i, aux = 0;
        while (elem >= lst->no[aux]) // Percorrimento
            aux++;
        for (i = lst->Fim; i > aux; i--) // Deslocamento
            lst->no[i] = lst->no[i-1];
        lst->no[aux] = elem; // Inclui o elemento na lista
    }
    lst->Fim++; // Avança o Fim
    return 1; // Sucesso
}

int remove_ord (Lista lst, int elem) {
    if (lst == NULL || lista_vazia(lst) == 1 || elem < lst->no[0] || elem > lst->no[lst->Fim-1])
        return 0; // Falha
    int i, Aux = 0;
    while (Aux < lst->Fim && lst->no[Aux] < elem)
        Aux++;
    if (Aux == lst->Fim || lst->no[Aux] > elem) // elem
        return 0; // Falha
    for (i = Aux+1; i < lst->Fim; i++)
        lst->no[i-1] = lst->no[i];
    lst->Fim--; // Decremento do campo Fim
    return 1; // Sucesso
}

void imprime_lista (Lista lst){
    int x;
    printf(" -[ ");
    for (x = 0; x < lst->Fim; x++)  {
        printf("%d ",lst->no[x]);
        }
    printf("]-\n");
}

void tamanho_lista (Lista lst){
    int x=0;
    if(lst ==NULL || lista_vazia(lst) == 1){
        printf("0 elementos\n");
        return 0;
    }
    x = lst->Fim;
    printf("A lista tem %d elementos\n",x);
}

int menor_ord(Lista lst){
    if (lst == NULL || lista_vazia(lst)==1)
        return 0;
    int x = 0;
    while (x < lst->Fim){
        lst->no[x] = lst->no[x+1];
        x++;
    }
    lst->Fim --;
    return 1;
}

void lista_igual(Lista p, Lista q){
    if (p == NULL||q == NULL)
        return 0;
    if (lista_vazia(p)==1 && lista_vazia(q)==1){
        printf("Listas Vazias Iguais\n");
        return 0;}
    int x=0;
    if (p->Fim != q->Fim){
        printf("Listas de tamanhos diferentes nao sao iguais\n");
        return 0;
    }
    while(x < p->Fim){
        if (p->no[x] != q->no[x]){
            printf("Listas Diferentes na %d posicao\n",x); // posiçao comeca no 0
            return 0;
        }
        x++;
    }
    printf("Listas perfeitamentes iguais\n");
    return 1;
}

int intercala_lista(Lista p, Lista q,Lista r){
    if (p == NULL || q==NULL ||r == NULL)
        return 0;
    int x=0,y=0,f=0,z=0;
    if (p->Fim + p->Fim > max)
        return 0;
    if(lista_vazia(p) == 1){
        while(x<q->Fim){
            r->no[x] = q->no[x];
            x++;
        }
        return 0;
    }
    if (lista_vazia(q)==1){
          while(x<p->Fim){
            r->no[x] = p->no[x];
            x++;
        }
        return 0;
    }
    while(f< (p->Fim)+(q->Fim)){
        if (x == p->Fim){
            r->no[z] = q->no[y];
            y++;
            z++;
        }
        if (y == q->Fim){
            r->no[z] = p->no[x];
            x++;
            z++;
        }
        if(x != p->Fim && y != q->Fim){
            if(p->no[x]<q->no[y]){
                r->no[z] = p->no[x];
                x++;
                z++;
            }
            else{
                r->no[z] = q->no[y];
                y++;
                z++;
            }
        }
        f++;

    }
    r->Fim = p->Fim+q->Fim;
    return 1;
}

int remove_par(Lista lst){
 if (lst == NULL || lista_vazia(lst) == 1)
        return 0;
        int i, Aux = 0;
    while (Aux < lst->Fim ){  // Percorrimento até achar o  final de lista
        if(lst->no[Aux]%2==0){
                for(i=Aux+1;i< lst->Fim;i++){
            lst->no[i-1] = lst ->no[i];}
        lst->Fim --;
        Aux--;
        }
        Aux++;}
        return 1;
}

