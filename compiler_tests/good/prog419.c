#include <unistd.h>
#include <string.h>
#include <stdio.h>



void tflag(int sleeptime){
    printf("-t flag output.\nWaiting %d seconds\n",sleeptime);
    
    sleep(sleeptime);
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
    int opt;
    
    while((opt = getopt(argc, argv, "srt:")) != -1){
        switch(opt){
            case 't':
                tflag(atoi(optarg));
                break;
            case 'r':
                rflag();
                break;
            case 's':
                sflag();
                break;
        }
    }
    return(0);
}

