#include <stdio.h>

int main(){

    int codigoRetorno = 0;

    printf("Digite o limite inferior do intervalo: ");
    int limInf;
    scanf("%d", &limInf);

    printf("Digite o limite superior do intervalo: ");
    int limSup;
    scanf("%d", &limSup);

    int i = 1;
    while(limInf >= limSup && i < 3){
        printf("Valor inválido para o limite inferior! Digite um valor menor que o superior: ");
        scanf("%d", &limInf);
        i++;
        if(i == 3){
            codigoRetorno = 15;
        }
    }

    if(codigoRetorno == 0){
        for(int j = limInf; j <= limSup; j++){
            if(j % 3 == 0){
                printf("%d\n", j);
            }
        }
    }
    
    return codigoRetorno;
}