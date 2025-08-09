#include <stdio.h>

int main(){

    int capacidade;
    printf("Digite a capacidade do vetor: ");
    scanf("%d", &capacidade);

    int vetor[capacidade];
    for(int i = 0; i < capacidade; i++){
        printf("Digite o %dº valor: ", i+1);
        scanf("%d", &vetor[i]);
    }

    //bubble sort
    for(int i = 0; i < capacidade; i++){
        int menor = vetor[i];
        int indice = i;
        for(int j = i+1; j < capacidade; j++){
            if(vetor[j] < menor){
                menor = vetor[j];
                indice = j;
            }
        }

        vetor[indice] = vetor[i];
        vetor[i] = menor;
    }

    printf("vetor ordem crescente: ");
    for(int i = 0; i < capacidade; i++)
        printf("%d", vetor[i]);
    
    puts("\n");
    return 0;
}