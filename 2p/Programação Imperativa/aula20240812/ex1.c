#include <stdio.h>

int main(){

    int n1 = -1;
    printf("Digite um número inteiro: ");
    scanf("%d", &n1);

    int n2 = -1;
    printf("Digite um segundo número inteiro: ");
    scanf("%d", &n2);

    while(n2 == n1){
        printf("O segundo número não pode ser igual ao primeiro, insira um novo valor para n2: ");
        scanf("%d", &n2);
    }

    if(n1 > n2){
        printf("Números em ordem crescente: %d  %d\n", n2, n1);
    } else{
        printf("Números em ordem crescente: %d  %d\n", n1, n2);
    }

    return 0;
}