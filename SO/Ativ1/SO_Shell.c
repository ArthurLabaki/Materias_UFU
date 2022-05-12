#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/types.h>
#include <dirent.h>

int main()
{
inicio:
	printf("Digite o comando (digite help para mostrar os comandos e exit para sair):\n");
	char x[10];
	gets(x);

	if (strcmp(x, "help") == 0 || strcmp(x, "HELP") == 0)
	{ //help
		printf("Comandos: cls, date, dir, time.\n");
		goto inicio;
	}
	if (strcmp(x, "exit") == 0 || strcmp(x, "EXIT") == 0)
	{ //exit
		return 0;
	}
	if (strcmp(x, "cls") == 0 || strcmp(x, "CLS") == 0)
	{						 // apagar a tela
		printf("\e[H\e[2J"); // tenta limpa a tela sem usar system(clear); Sequencia de escapes
        	goto inicio;
	}
	if (strcmp(x, "dir") == 0 || strcmp(x, "DIR") == 0)
	{						  // listar arquivos e pastas
		DIR *dir;			  //acessa o diretorio
		struct dirent *lsdir; //ponteiro de struct
		dir = opendir(".");	  // lista os arquivos e pasta do local onde o arquivo esta armazenado

		while ((lsdir = readdir(dir)) != NULL)
		{ //imprimir na tela
			printf(" %s\n", lsdir->d_name);
		}
		closedir(dir); //fecha o diretorio
		goto inicio;
	}
	if (strcmp(x, "date") == 0 || strcmp(x, "DATE") == 0)
	{ // mostra a data
		struct tm *data_hora_atual;
		time_t segundos;
		time(&segundos);
		data_hora_atual = localtime(&segundos);
		printf("\n %d/", data_hora_atual->tm_mday);		   //dia
		printf("%d/", data_hora_atual->tm_mon + 1);		   //mês (janeiro = 0, por isso o +1)
		printf("%d\n\n", data_hora_atual->tm_year + 1900); //ano(o tm_year começa em 1900)
		goto inicio;
	}
	if (strcmp(x, "time") == 0 || strcmp(x, "TIME") == 0)
	{ //mostra a hora
		struct tm *data_hora_atual;
		time_t segundos;
		time(&segundos);
		data_hora_atual = localtime(&segundos);
		printf("\n%d:", data_hora_atual->tm_hour); //hora
		printf("%d:", data_hora_atual->tm_min);	   //minuto
		printf("%d\n\n", data_hora_atual->tm_sec); //segundo
		goto inicio;
	}
	printf("Comando Invalido!\n");
	goto inicio;
}
