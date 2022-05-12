#include <stdio.h>
#include <unistd.h> // Arquivo de header para syscalls
#include <sys/types.h> 

int main( ){

    pid_t x;

    printf("PID = %d - processo pai\n", getpid( ));
    
    getchar( );

    x = fork( );

    getchar( );

    if(x > 0){

        printf("Processo PID = %d\n", getpid( ));

        getchar( );

    }else if(x == 0){

        printf("Processo PID = %d\n", getpid( ));

        getchar( );

    }

    getchar( );

    _exit(0); // Essa é system call
//   exit(0); // Essa é chamada de biblioteca (stdlib)  

}