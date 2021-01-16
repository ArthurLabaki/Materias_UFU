#include <stdio.h>
#include <stdlib.h>
#include "pilha.h"

int main()
{
    char A[100];
   printf("Digite a Operacao\n");
   gets(A);
   if(valida_escopo(A)==1)
    printf("Escopos feitos com Sucesso!(1)\n");
   else{
    printf("Erro nos Escopos!(0)\n");
   }
}
