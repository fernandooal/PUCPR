#include <stdio.h>

// Fazer um programa em C para calcular o valor da série S abaixo. O valor de N
// deve ser fornecido pelo usuário. Use a estrutura do-while para somar a sequência de
// termos.
// S = 1/N + 2/N-1 + 3/N-2 + ...+ N-1/2 + N/1

int main(){

    printf("Digite o valor N: ");
    int n;
    scanf("%d", &n);

    double S;
    double i = 0.0;

    do{
        S = S + (i+1)/(n-i);
        i++;
    } while(i < n);

    printf("%lf\n", S);

    return 0;
}