#include <stdio.h>

int main(){
    printf("Digite três caracteres e então ENTER: ");

    char c1 = getchar();
    char c2 = getchar();
    char c3 = getchar();

    while(c1 == c2 || c1 == c3 || c2 == c3){
        printf("Caracteres inválidos, insira 3 letras diferentes: ");
        c1 = getchar();
        c2 = getchar();
        c3 = getchar();
    }

    //######## SELEÇÃO DIRETA
    // char* menor = &c1;

    // if(c2 < *menor){
    //     menor = &c2;
    // }

    // if(c3 < *menor){
    //     menor = &c3;
    // }

    // char aux = c1;

    // c1 = *menor;

    // *menor = aux;

    //####### BUBBLE SORT
    if(c1 > c2){
        char aux = c1;
        c1 = c2;
        c2 = aux;
    }

    if(c2 > c3){
        char aux = c2;
        c2 = c3;
        c3 = aux;
    }

    if(c1 > c2){
        char aux = c1;
        c1 = c2;
        c2 = aux;
    }

    printf("%c %c %c\n", c1, c2, c3);

    //###### "BRUTEFORCE"
    // if(c1 > c2){
    //     if(c2 > c3){
    //         printf("%c %c %c\n", c3, c2, c1);
    //     } else{
    //         if(c1 > c3){
    //             printf("%c %c %c\n", c2, c3, c1);
    //         } else{
    //             printf("%c %c %c\n", c2, c1, c3);
    //         }
    //     }
    // }else{
    //     if(c1 > c3){
    //         printf("%c %c %c\n", c3, c1, c2);
    //     } else{
    //         if(c2 > c3){
    //             printf("%c %c %c\n", c1, c3, c2);
    //         } else{
    //             printf("%c %c %c\n", c1, c2, c3);
    //         }
    //     }
    // }

    return 0;
}