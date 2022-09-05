#include <stdio.h>
#include <stdlib.h>
#include "lista.h"
#define max 10
                                            ///Lista Nao Ordenada
struct lista {
    int no[max];
    int Fim;
};

Lista cria_lista() {            ///Criando a lista(alocando)
    Lista lst;
    lst = (Lista) malloc(sizeof(struct lista));
    if (lst != NULL)
        lst->Fim = 0; // Lista vazia
    return lst;
}

int lista_vazia(Lista lst) {        ///Verificando se a lista esta vazia
    if (lst->Fim == 0)
        return 1; /// Lista vazia
    else
        return 0; /// Lista NÃO vazia
}

int lista_cheia(Lista lst) {           ///Verificando se a lista esta cheia
    if (lst->Fim == max)
        return 1; // Lista cheia
    else
        return 0; // Lista NÃO cheia
}

int insere_elem(Lista lst, int elem) {          ///Insere um elemento na lista(no final, pois nao eh ordenada)
    if (lst == NULL || lista_cheia(lst) == 1)  //verifica se ocorreu um erro na alocacao ou se a lista esta cheia
        return 0;
    lst->no[lst->Fim] = elem; // Insere elemento
    lst->Fim++; // Avança o Fim
    return 1;
}

int remove_elem (Lista lst, int elem) {         ///Remove um elemento escolhido (int elem)
    if (lst == NULL || lista_vazia(lst) == 1)
        return 0; // Falha
    int i, Aux = 0;
    while (Aux < lst->Fim && lst->no[Aux] != elem)  // Percorrimento até achar o elem ou final de lista
        Aux++;
    if (Aux == lst->Fim) // Final de lista (elem)
        return 0; // Falha
    for (i = Aux+1; i < lst->Fim; i++)  // Deslocamento à esq. do sucessor até o final da lista
        lst->no[i-1] = lst->no[i];
    lst->Fim--; // Decremento do campo Fim
    return 1; // Sucesso
}

int print_lista (Lista lst){                    ///Imprime a lista
    int x;
    printf(" -[ ");
    for (x = 0; x < lst->Fim; x++)  {
        printf("%d ",lst->no[x]);
    }
    printf("]-\n");
}

int tamanho_lista(Lista lst){                   ///Imprime o tamanho da lista
    if (lista_vazia(lst) == 1) {
        printf("A lista tem [0] elementos\n");
        return 0;
        }
        int x,y=0;
    for(x=0; x<lst->Fim; x++)
        y++;
    printf("A lista tem [%d] elementos\n ",y);
}

int menor_elem(Lista lst){                      ///Retira o menor elemento da lista
    if (lst == NULL || lista_vazia(lst) == 1)
        return 0; // Falha
    int x, Aux = 0;
    Aux = lst->no[0];
    for (x=0;x< lst->Fim;x++){
        if(Aux > lst->no[x])
            Aux = lst->no[x];
    }
    remove_elem(lst, Aux);
    return 1;
}

int insere_inicio(Lista lst, int elem){         ///Insere elemento no começo da lista
     if (lst == NULL || lista_cheia(lst) == 1)
        return 0;
    int Aux;
   for(Aux = lst->Fim-1;Aux>=0;Aux--)
        lst->no[Aux+1] = lst->no[Aux];
   lst->no[0] = elem;
   lst->Fim ++;
   return 1;
}

int remove_todos(Lista lst, int elem){          ///Remove todos
     if (lst == NULL || lista_vazia(lst) == 1)
        return 0;
        int i, Aux = 0;
    while (Aux < lst->Fim ){  // Percorrimento até achar o  final de lista
        if(lst->no[Aux]==elem){
                for(i=Aux+1;i< lst->Fim;i++){
            lst->no[i-1] = lst ->no[i];}
        lst->Fim --;
        Aux--;
        }
        Aux++;}
        return 1;
}


int concatena_lista(Lista p, Lista q, Lista r){      ///Concatena 2 listas
    int Aux=0,Aux2=0;
    if(p->Fim + q->Fim > 10)
        return 0;
    r->Fim = p->Fim + q->Fim;
    while(Aux < p->Fim){               // Percorrimento até achar o  final de lista p
        r->no[Aux] = p->no[Aux];
        Aux++;
    }
    while(Aux2 < q->Fim){               // Percorrimento até achar o  final de lista q
        r->no[Aux] = q->no[Aux2];
        Aux2++;
        Aux++;
    }
    return 0;
}
