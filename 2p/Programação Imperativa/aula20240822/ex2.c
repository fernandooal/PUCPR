#include <stdio.h>

// Escreva um programa em C para calcular o fatorial de um número N fornecido
// pelo usuário. Use a estrutura for para gerar a sequência de termos.

int main(){

    printf("Digite o valor N: ");
    int n;
    scanf("%d", &n);

    int fatorial = 1;
    for(int i = 1; i <= n; i++){
        fatorial = fatorial * i;
    }

    printf("%d\n", fatorial);

    return 0;
}