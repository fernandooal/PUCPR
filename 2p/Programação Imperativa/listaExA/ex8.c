#include <stdio.h>

// Elabore um programa em C para ler uma sequência de caráteres até que o
// caráter 0 (zero) seja digitado. Enquanto os caráteres são lidos, o programa deverá
// verificar se o caráter lido é uma vogal ou uma consoante e deverá acrescentar uma
// unidade ao contador de vogais ou ao contador de consoantes, dependendo do que foi
// lido. Ao final, o programa deverá imprimir o número de vogais e o número de
// consoantes lidas.

int main(){
    
    char c;
    int vogais = 0;
    int consoantes = 0;

    while(c != '0'){
        printf("Digite uma letra: ");
        c = getchar();
        getchar();

        if((c >= 65 && c <= 90) || (c >= 97 && c <= 122)){
            if(c == 'A' || c == 'a' || c == 'E' || c == 'e' || c == 'I' || c == 'i' || c == 'O' || c == 'o' || c == 'U' || c == 'u'){
                vogais++;
            } else{
                consoantes++;
            }
        } else{
            if(c != '0'){
                printf("Caracter digitado não é uma letra!\n");
            }
        }
    }

    printf("Vogais digitadas: %d\nConsoantes digitadas: %d\n", vogais, consoantes);

    return 0;
}