#include <stdio.h>

// Elabore um programa em C para imprimir os 30 primeiros números naturais
// pares. Use a estrutura for para gerar a sequência de termos.

int main(){

    for(int i = 0; i < 60; i++){
        if(i % 2 == 0){
            printf("%d\n", i);
        } 
    }

    return 0;
}