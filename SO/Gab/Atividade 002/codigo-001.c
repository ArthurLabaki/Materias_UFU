#include <stdio.h>
#include <unistd.h> // Arquivo header para syscalls
#include <sys/types.h> // Necessária pra o uso do pid_t

int main( ){

    pid_t pids[2];
    int i, status;

    printf("PID = %d: processo pai\n", getpid( ));

    for(i = 0; i < 2; i++){

        pids[i] = fork( );
        printf("PID = %d: i = %d\n", getpid( ), i);

    }

    printf("Finalizando - PID = %d: i = %d\n", getpid( ), i);

    getchar( );

    return 0;

}