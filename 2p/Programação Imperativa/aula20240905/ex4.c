#include <stdio.h>
#include <stdlib.h>

int main(){

    int capacidade;
    printf("Digite o número de caracteres do vetor: ");
    scanf("%d", &capacidade);

    setbuf(stdin, NULL);

    char vetor[capacidade];
    char vetorInverso[capacidade];

    printf("Digite a string: ");
    for(int i = 0, j = capacidade-1; i < capacidade; i++, j--){
        vetor[i] = getchar();
        vetorInverso[j] = vetor[i];
    }
    
    puts("\nvetor inverso: ");
    for(int i = 0; i < capacidade; i++)
        printf("%c", vetorInverso[i]);

    puts("\n");

    return 0;
}