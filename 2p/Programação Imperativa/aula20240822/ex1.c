#include <stdio.h>

// Sendo H = 1 + 1/2 + 1/3 + ¼ + ... 1/N, elaborar um programa. em C para
// gerar o número H. O valor de N deverá ser fornecido pelo usuário. Use a estrutura for
// para somar a sequência de termos.

int main(){

    printf("Digite o valor de N: ");
    int N;
    scanf("%d", &N);

    double H = 0;
    for(int i = 1; i <= N; i++){
        H = H + 1.0/i;
    }

    printf("%lf\n", H);

    return 0;
}