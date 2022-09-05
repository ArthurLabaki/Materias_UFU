#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10            //max eh o tamanho da Lista


struct lista {
    int no[max];
    int Fim;
};


Lista cria_lista() {            //Criando a lista(alocando)
    Lista lst;
    lst = (Lista) malloc(sizeof(struct lista));
    if (lst != NULL)
        lst->Fim = 0;
    return lst;
}


int lista_vazia(Lista lst) {            //Verificando se a lista esta vazia
    if (lst->Fim == 0)
        return 1;
    else
        return 0;
}


int lista_cheia(Lista lst) {            //Verificando se a lista esta cheia
    if (lst->Fim == max)
        return 1;
    else
        return 0;
}


int insere_elem(Lista lst, int elem) {            //Insere o elemento no final da lista
    if (lst == NULL || lista_cheia(lst) == 1)
        return 0;
    lst->no[lst->Fim] = elem;
    lst->Fim++;
    return 1;
}


int insere_inicio(Lista lst, int elem){         //Insere o elemento no começo da lista
     if (lst == NULL || lista_cheia(lst) == 1)
        return 0;
    int Aux;
   for(Aux = lst->Fim-1;Aux>=0;Aux--)
        lst->no[Aux+1] = lst->no[Aux];
   lst->no[0] = elem;
   lst->Fim ++;
   return 1;
}


int insere_ord(Lista lst, int elem) {            //Insere o elemento ordenado
    if (lst == NULL || lista_cheia(lst) == 1)
        return 0;
    if (lista_vazia(lst) == 1 || elem >= lst->no[lst->Fim-1])
    lst->no[lst->Fim] = elem;
    else {
        int i, aux = 0;
        while (elem >= lst->no[aux])
            aux++;
        for (i = lst->Fim; i > aux; i--)
            lst->no[i] = lst->no[i-1];
        lst->no[aux] = elem;
    }
    lst->Fim++;
    return 1;
}


int remove_elem (Lista lst, int elem) {            //Remove um elemento escolhido
    if (lst == NULL || lista_vazia(lst) == 1)
        return 0;
    int i, Aux = 0;
    while (Aux < lst->Fim && lst->no[Aux] != elem)
        Aux++;
    if (Aux == lst->Fim)
        return 0;
    for (i = Aux+1; i < lst->Fim; i++)
        lst->no[i-1] = lst->no[i];
    lst->Fim--;
    return 1;
}


int remove_ord (Lista lst, int elem) {          //Remove o elemento ordenado
    if (lst == NULL || lista_vazia(lst) == 1 || elem < lst->no[0] || elem > lst->no[lst->Fim-1])
        return 0;
    int i, Aux = 0;
    while (Aux < lst->Fim && lst->no[Aux] < elem)
        Aux++;
    if (Aux == lst->Fim || lst->no[Aux] > elem)
        return 0;
    for (i = Aux+1; i < lst->Fim; i++)
        lst->no[i-1] = lst->no[i];
    lst->Fim--;
    return 1;
}


int menor_elem(Lista lst){                      //Remove o menor elemento da lista
    if (lst == NULL || lista_vazia(lst) == 1)
        return 0;
    int x, Aux = 0;
    Aux = lst->no[0];
    for (x=0;x< lst->Fim;x++){
        if(Aux > lst->no[x])
            Aux = lst->no[x];
    }
    remove_elem(lst, Aux);
    return 1;
}


int remove_par(Lista lst){          //Remove todos os elementos pares
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


int remove_todos(Lista lst, int elem){          //Remove todos
     if (lst == NULL || lista_vazia(lst) == 1)
        return 0;
        int i, Aux = 0;
    while (Aux < lst->Fim ){
        if(lst->no[Aux]==elem){
                for(i=Aux+1;i< lst->Fim;i++){
            lst->no[i-1] = lst ->no[i];}
        lst->Fim --;
        Aux--;
        }
        Aux++;}
        return 1;
}


int imprime_lista (Lista lst){            //Imprime a lista
    int x;
    printf(" -[ ");
    for (x = 0; x < lst->Fim; x++)
        printf("%d ",lst->no[x]);
    printf("]-");
    return 1;
}


int tamanho_lista(Lista lst){                   //Imprime o tamanho da lista
    if (lista_vazia(lst) == 1) {
        printf("A lista tem [0] elementos\n");
        return 0;
        }
        int x,y=0;
    for(x=0; x<lst->Fim; x++)
        y++;
    printf("A lista tem [%d] elementos\n ",y);
}


int concatena_lista(Lista p, Lista q, Lista r){      //Concatena 2 listas
    int Aux=0,Aux2=0;
    if(p->Fim + q->Fim > 10)
        return 0;
    r->Fim = p->Fim + q->Fim;
    while(Aux < p->Fim){
        r->no[Aux] = p->no[Aux];
        Aux++;
    }
    while(Aux2 < q->Fim){
        r->no[Aux] = q->no[Aux2];
        Aux2++;
        Aux++;
    }
    return 0;
}


void lista_igual(Lista p, Lista q){         //Verifica se 2 listas sao iguais
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


int intercala_lista(Lista p, Lista q,Lista r){          //Intercala elementos de 2 listas ordenadamente
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
                        //Retorna 1 para sucesso e 0 para erro
                        //Nao usar o ordenado e o nao ordenado no mesmo user
