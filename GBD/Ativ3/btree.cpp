#include "btree.h"

#include <sys/types.h>
#include <sys/stat.h>
#define ORDEM 511

bool fileExists(const char *filename) { struct stat statBuf; if (stat(filename,&statBuf) < 0) return false; return S_ISREG(statBuf.st_mode); }

btree::btree() {
    char *nomearquivo = "arvoreb.dat";

    // se arquivo ja existir, abrir e carregar cabecalho
    if (fileExists(nomearquivo)) {
        // abre arquivo
        arquivo = fopen(nomearquivo,"r+");
        leCabecalho();
    }
    // senao, criar novo arquivo e salvar o cabecalho
    else {
        // cria arquivo
        arquivo = fopen(nomearquivo,"w+");

        // atualiza cabecalho
        cabecalhoArvore.numeroElementos = 0;
        cabecalhoArvore.paginaRaiz = -1;
        cabecalhoArvore.numeroPaginas = 0;
        salvaCabecalho();
    }
}

btree::~btree() {
    // fechar arquivo
    fclose(arquivo);
}

int btree::computarTaxaOcupacao() {
    return 0;
}

void btree::insereChave(int chave, int offsetRegistro) {

    if (cabecalhoArvore.paginaRaiz == -1){   // Primeiro elemento inserido
        int idpagina;
        pagina *pg = new pagina;
        pg = novaPagina(&idpagina);
        pg->numeroPagina = 1;
        pg->chaves[0] = chave;
        pg->offset[0] = offsetRegistro;
        pg->numeroElementos = 1;

        salvaPagina(pg->numeroPagina, pg);   // Não funciona
        cabecalhoArvore.numeroElementos = 1;
        cabecalhoArvore.alturaArvore = 1;
        cabecalhoArvore.numeroPaginas ++;
        cabecalhoArvore.paginaRaiz = 1;
        salvaCabecalho();

    }

    if (cabecalhoArvore.paginaRaiz == 1){   // Raiz é a unica pagina
        pagina *pg = new pagina;
        pg = lePagina(cabecalhoArvore.paginaRaiz);
        if (pg->numeroElementos = ORDEM){  // SPLITAR

        }
        else{   //Insere ordenado
            int i = 0;
            while (chave > pg->chaves[i]){
                i++;
            }
            int pul1, pul2;
            pul1 = pg->chaves[i];
            pg->chaves[i] = chave;
            i++;
            for (;i < pg->numeroElementos; i++){
                pul2 = pg->chaves[i];
                pg->chaves[i] = pul1;
                pul1 = pul2;
            }
        }
        salvaPagina(pg->numeroPagina, pg);
    }
    if (cabecalhoArvore.paginaRaiz > 1 ){

        if (pg->numeroElementos = ORDEM){  // SPLITAR

        }
        else {

        }

    }

    //cabecalhoArvore.numeroElementos++;
    //salvaCabecalho();
}

void btree::removeChave(int chave) {

    // se remover, atualizar cabecalho
    if (true) {
        cabecalhoArvore.numeroElementos--;
        salvaCabecalho();
    }
}

int btree::buscaChave(int chave) {
    pagina *pg = lePagina(cabecalhoArvore.paginaRaiz);  // No raiz
    int i, j;
    int qnt = 1;
    int offset = 0;
    if (cabecalhoArvore.numeroPaginas <= 0){   // Nenhuma pagina
        return -1;
    }
    while (qnt <= cabecalhoArvore.numeroPaginas){   // Verifica todas as paginas
        printf("...");
        pagina *aux = lePagina(qnt);
        for (i=0; i <= ORDEM; i++){
            if (aux->chaves[i] == chave){
                return aux->offset[i];
            }
        }
        qnt ++;
    }

    return -1;
}

