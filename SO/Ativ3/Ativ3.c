#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/shm.h>
#include <pthread.h>
#include <signal.h>
#define MEM_SZ 40
#define BUFF_SZ MEM_SZ-sizeof(int)

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017

Não consegui fazer a parte dos sinais (SIGUSR1)
também não consegui criar as threads
*/

struct shared_area{ // struct da area compartilhada
    int num;
    int buffer[BUFF_SZ];
};

        // PARTE DA FILA
int inserir (struct shared_area *f, int x){
    if (f->num < 10){
        int e = f->num;
        f->buffer[e] = x;
        f->num ++;
        //printf("[%d] ", x);
        return 0; // sucesso
    }
    else{
    return -1; //fracasso
    }
}

void imprimir (struct shared_area *f){
    int i;
    for (i=0; i<10; i++){
        printf("%d / ", f->buffer[i]);
    }
    fflush(stdout);
    printf("\n");
}

int remover_ord(struct shared_area *f){
    if (f->num > 0){
        int e = f->buffer[0];
        int temp, cont;
        for (cont = 0; cont < 9; cont ++){
            temp = f->buffer[cont + 1];
            f->buffer[cont] = temp;
        }
        f->num --;
        return e;
    }
    else{
        return -1; // fracasso
    }
}

int remover_tod(struct shared_area *f){
    int cont=0;
    if (f->num > 0){
        for (cont=0; cont < 10; cont ++){
        f->buffer[cont] = 0;
        }
        f->num = 0;
        return 0; // sucesso
    }
    else{
        return -1; // fracasso
    }
}
        //FIM DA PARTE DA FILA

        //PARTE DO RELATORIO

int maxval (int num[10000]){
    int i;
    int n = -1;
    for (i = 0; i<10000 ; i++){
        if (n < num[i])
            n = num[i];
    }
    return n;
}

int minval (int num[10000]){
    int i;
    int n = 1001;
    for (i = 0; i<10000 ; i++){
        if (n > num[i])
            n = num[i];
    }
    return n;
}

int moda (int num[10000], int *val, int *qtd){
    int i, v;
    int j = 0;
    int n[1001];
    for (i=0; i<1001; i++){
        n[i] = 0;
    }
    for (i=0; i<10000; i++){
        n[num[i]] ++;
    }
    for (i=0; i<1001; i++){
        if (n[i] > j){
            j = n[i];
            v = i;
        }
    }
    *val = v;
    *qtd = j;

}
        //FIM DA PARTE DO RELATORIO

        //PARTE DOS PROCESSOS

void P1(struct shared_area *fila){ // P1, P2, P3
    srand(time(NULL));
    int numero;
    for(;;){
        if (fila->num < 10){
            numero = (rand() % 1000) +1;
            inserir(fila, numero);
            //printf("(%d) ", numero);
        }
        fflush(stdout);
    }
    _exit(0);
}

void P4(struct shared_area *fila, int *pip1, int *pip2){
    int cont;
    int val1[5];
    int val2[5];
    for(;;){
        if (fila->num == 10){
            for (cont = 0; cont < 5; cont ++){
                val1[cont] = fila->buffer[cont];
            }
            write(pip1[1], &val1, sizeof(int[5])); // escrevendo no pipe 1
            for (cont = 5; cont < 10; cont ++){
                val2[cont-5] = fila->buffer[cont];
            }
            write(pip2[1], &val2, sizeof(int[5])); // escrevendo no pipe 1
            remover_tod(fila);
        }
    }

    _exit(0);
}

void P5(int *pip1, struct shared_area *fila2){
    int val[5];
    int cont = 0;
    for (;;){
        read(pip1[0], &val, sizeof(int[5]));
        while (cont < 5){
            if (fila2->num < 10){
            inserir(fila2, val[cont]);
            cont ++;
            }

        }
        cont = 0;
        fflush(stdout);
    }
    _exit(0);
}
void P6(int *pip2, struct shared_area *fila2){
    int val[5];
    int cont = 0;
    for (;;){
        read(pip2[0], &val, sizeof(int[5]));
        while (cont < 5){
            if (fila2->num < 10){
            inserir(fila2, val[cont]);
            cont ++;
            }
        }
        cont = 0;
        //printf(" : Pipe 2\n");
        fflush(stdout);
    }
    _exit(0);
}

void P7(struct shared_area *fila2){
    int cont = 0;
    int test = 0;
    int numero[10000];
    while (cont < 10000) {
        //imprimir(fila2);
        if (fila2->num > 0){
            numero[test] = remover_ord(fila2);
            printf("%d  ", numero[test]);
            fflush(stdout);
            cont ++;
            test ++;
        }
    }
    int qtd, val;
    printf("\nValores imprimidos: %d\n", cont);
    printf("Maior valor: %d\n", maxval(numero));
    printf("Menor valor: %d\n", minval(numero));
    moda(numero, &val, &qtd);
    printf("Moda: %d, repetindo %d vezes\n", val, qtd);
    //_exit(0);
}

            //FIM DA PARTE DOS PROCESSOS


int main() {
    float tempo;
    clock_t temp;
    temp = clock();

    pid_t x, filho4;
    int i;

    // Memoria compartilhada F1
    key_t key=1234;
    struct shared_area *shared_area_ptr;
    void *shared_memory = (void *)0;
    int shmid;
    shmid = shmget(key, MEM_SZ, 0666|IPC_CREAT);
    if (shmid == -1){
        printf("shmget falhou\n");
        exit(-1);
    }
    //printf("shmid=%d\n",shmid);
    shared_memory = shmat(shmid, (void*)0,0);
    if (shared_memory == (void *) -1){
        printf("shmat falhou\n");
        exit(-1);
    }
    //printf("Memoria compartilhada no edereco=%p\n", shared_memory);
    shared_area_ptr = (struct shared_area *) shared_memory;
    shared_area_ptr->num=0;
    for(i=0;i<BUFF_SZ;i++){
        shared_area_ptr->buffer[i] = 0;
        }
    // Fim da memoria compartilhada

    // Criando os pipes
    int canal1[2];
    int canal2[2];
    if (pipe(canal1) == -1) {printf("Erro pipe1()"); return -1;}
    if (pipe(canal2) == -1) {printf("Erro pipe2()"); return -1;}
    // Fim dos pipes

    // Memoria compartilhada F2
    key_t key2=4321;
    struct shared_area *shared_area_ptr2;
    void *shared_memory2 = (void *)0;
    int shmid2;
    shmid2 = shmget(key2, MEM_SZ, 0666|IPC_CREAT);
    if (shmid2 == -1){
        printf("shmget falhou\n");
        exit(-1);
    }
    //printf("shmid=%d\n",shmid);
    shared_memory2 = shmat(shmid2, (void*)0,0);
    if (shared_memory2 == (void *) -1){
        printf("shmat falhou\n");
        exit(-1);
    }
    //printf("Memoria compartilhada no edereco=%p\n", shared_memory);
    shared_area_ptr2 = (struct shared_area *) shared_memory2;
    shared_area_ptr2->num=0;
    for(i=0;i<BUFF_SZ;i++){
        shared_area_ptr2->buffer[i] = 0;
        }
    // Fim da memoria compartilhada

    // Criando os processos filhos
    for (i=1; i<7; i++){
        if (fork() == 0 )
            break;
    }
    switch (i){
        case 1: P1(shared_area_ptr); break;
        case 2: P1(shared_area_ptr); break;
        case 3: P1(shared_area_ptr); break;
        case 4: P4(shared_area_ptr, canal1, canal2); break;
        case 5: P5(canal1, shared_area_ptr2); break;
        case 6: P6(canal2, shared_area_ptr2); break;
        case 7: P7(shared_area_ptr2); // pai

    }
    fflush(stdout);

    temp = clock() - temp;
    printf("Tempo de execução: %f s\n",((float)temp)/CLOCKS_PER_SEC);

    exit(0);
    _exit(0);
}
