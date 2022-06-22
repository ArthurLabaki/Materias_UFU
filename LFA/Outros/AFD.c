#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int perntence(char E[], char t) // Verifica se o teste t existe nos simbolos E
{
    int tam = strlen(E);
    for (int i = 0; i < tam; i++)
    {
        if (E[i] == t)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    char a[10] = "abcd";      //Simbolos de entrada
    char teste[100] = "abba"; // Cadeia de teste

    int existe = perntence(a, b);
    printf("%d", existe);
}