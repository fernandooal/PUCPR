#include <stdio.h>

void invert(char* p){
    if(*p != '\0'){
        invert(p + 1);
        printf("%c", *p);
    }
}

int main(){

    invert("Primavera");

    return 0;
}