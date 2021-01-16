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


