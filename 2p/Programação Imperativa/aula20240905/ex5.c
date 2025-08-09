#include <stdio.h>
#include <stdlib.h>

int main(){

    int comprimento;
    printf("Digite o comprimento da string: ");
    scanf("%d", &comprimento);

    setbuf(stdin, NULL);

    char palindromo[comprimento];
    puts("Digite a string: ");
    for(int i = 0; i < comprimento; i++){
        palindromo[i] = getchar();
    }

    int ehPalindromo = 1;
    for(int i = 0, j = comprimento-1; i < comprimento/2 && ehPalindromo == 1; i++, j--){
        if(palindromo[i] != palindromo[j]){
            ehPalindromo = 0;
        }
    }

    if(ehPalindromo == 1){
        printf("String fornecida é palindromo\n");
    } else{
        printf("String fornecida não é palindromo\n");
    }

    return 0;
}