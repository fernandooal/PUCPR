#include <stdio.h>

int main(){

    int capacidade;
    printf("Digite a capacidade do vetor: ");
    scanf("%d", &capacidade);

    int vetor[capacidade];
    for(int i = 0; i < capacidade; i++){
        printf("Digite o %dº valor: ", i+1);
        scanf("%d", &vetor[i]);

        int j = 0;
        int igual = 0;
        while(j < i && igual == 0){
            if(vetor[j] == vetor[i]){
                printf("Valor repetido!!\n");
                igual = 1;
                i--;
            }
            j++;
        }
    }

    for(int i = 0; i < capacidade; i++){
        printf("Vetor: %d\n", vetor[i]);
    }

    return 0;
}