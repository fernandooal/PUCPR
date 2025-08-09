#include <stdio.h>

int main(){

    double vetor[8];
    double soma[8];

    for(int i = 0; i < 8; i++){
        printf("Digite o valor do %dº elemento do vetor: ", i+1);
        scanf("%lf", &vetor[i]);
    }

    for(int i = 0, j = 7; i < 8; i++, j--){
        soma[i] = vetor[i] + vetor[j];
    }

    puts("vetor soma: ");
    for(int i = 0; i < 8; i++)
        printf("%.2lf ", soma[i]);

    return 0;
}