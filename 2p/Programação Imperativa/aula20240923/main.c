#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 10

int main(){
    char frase[MAX];

    printf("Digite uma frase: ");
    bool enter_nao_encontrado = true;

    do {
        fgets(frase, MAX, stdin);

        int tam = strlen(frase);
        printf("tam = %d\n", tam);

        int pos = strcspn(frase, "\r\n");
        printf("pos = %d\n", pos);

        if (pos < tam) enter_nao_encontrado = false;

        char ultimo = frase[tam-1];
        printf("ultimo: %c (%d)\n", ultimo, ultimo);

        frase[pos] = '\0';

        printf("%s\n\n", frase);
        
    } while (enter_nao_encontrado);
    return 0;
}