#include <stdio.h>
#include <stdlib.h>

int main(){

    int capacidade;
    printf("Digite a capacidade do vetor: ");
    scanf("%d", &capacidade);

    int v[capacidade];
    for(int i = 0; i < capacidade; i++){
        printf("Digite o %dº valor: ", i+1);
        scanf("%d", &v[i]);
    }

    int x;
    printf("Digite o valor x que deseja verificar se está no vetor: ");
    scanf("%d", &x);

    int temX = 0;
    for(int i = 0; i < capacidade && temX == 0; i++){
        if(v[i] == x){
            temX = 1;
            printf("O valor x foi encontrado no índice %d!\n", i);
        }
    }

    if(temX == 0)
        printf("O valor x não foi encontrado no vetor :(\n");

    return 0;
}