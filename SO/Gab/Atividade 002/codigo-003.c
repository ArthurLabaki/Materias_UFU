#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define numThreads 10

void *t1(void *threadid){

    printf("Ola, eu sou a thread 1!\n");
    pthread_exit(NULL);

}

void *t2(void *threadid){

    printf("Ola, eu sou a thread 2!\n");
    pthread_exit(NULL);

}

int main(int argc, char *argv[ ]){

    int i;
    pthread_t threads tid1, tid2;
    
    pthread_create(&threads[i], NULL, print, (void*)i);
    pthread_create(&threads[i], NULL, print, (void*)i);

    pthread_join(tid1, NULL);
    pthread_join(tid2, NULL);

    _exit(0);

}