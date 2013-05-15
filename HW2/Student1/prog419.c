#include <unistd.h>
#include <string.h>
#include <stdio.h>


void tflag(char *sleeptime){
    printf("-t flag output.\nWaiting %d seconds\n",atoi(sleeptime));
    
    sleep(atoi(sleeptime));
    return;
}

void rflag(){
    printf("-r flag output.\n");
    return;
}

void sflag(){
    printf("-s flag output.\n");
    return;
}



int main(int argc, char *argv[]){
    int i;
    
    for(i=1; i<argc; i++){
//        printf("argument %d: %s\n",i,argv[i]);
        if(!strcmp(argv[i], "-t")){
            i++;
            tflag(argv[i]);
        }
        if(!strcmp(argv[i], "-r"))
            rflag();
            
        if(!strcmp(argv[i], "-s"))
            sflag();
        
    }
    return(0);
}

