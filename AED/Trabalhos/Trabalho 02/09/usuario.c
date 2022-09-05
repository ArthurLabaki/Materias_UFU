#include <stdio.h>
#include <stdlib.h>
#include "deque.h"

int main()
{
    Deque ex;
    ex = cria_deque();
    imprime_deque(ex);
    insere_fim(ex, 2);
    imprime_deque(ex);
    insere_fim(ex, 3);
    imprime_deque(ex);
    insere_ini(ex, 4);
    imprime_deque(ex);
    insere_ini(ex, 5);
    imprime_deque(ex);
    insere_fim(ex, 6);
    imprime_deque(ex);
    insere_fim(ex, 7);
    imprime_deque(ex);
    insere_fim(ex, 8);
    imprime_deque(ex);
    insere_ini(ex, 9);
    imprime_deque(ex);
    insere_fim(ex, 10);
    imprime_deque(ex);
    int x;
    remove_fim(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_ini(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_fim(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_ini(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_ini(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_fim(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
    remove_fim(ex, &x);
    printf("o elemento %d foi removido\n");
    imprime_deque(ex);
}
