#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

/*
Nome: Arthur do Prado Labaki
Matricula: 11821BCC017
*/

int contador(char *path) {
    DIR *dir_ptr = NULL;
    struct dirent *direntp;
    char *npath;
    if (!path)      //erro ao abrir diretorio
        return 0;
    if( (dir_ptr = opendir(path)) == NULL )     //não tem outros diretorios
        return 0;

    int count=0;    //contador
    while( (direntp = readdir(dir_ptr)))    //loop no diretorio atual
    {
        if (strcmp(direntp->d_name,".")==0 || strcmp(direntp->d_name,"..")==0) //existe diretorio
            continue;
        switch (direntp->d_type) {
            case DT_REG:    //registro
                ++count;
                break;
            case DT_DIR:    //diretorio
                npath=malloc(strlen(path)+strlen(direntp->d_name)+2);
                sprintf(npath,"%s/%s",path, direntp->d_name);
                count += contador(npath);   //recursão
                free(npath);
                break;
        }
    }
    closedir(dir_ptr);
    return count;
}

int main(){
    printf("%d", contador("/"));
}
