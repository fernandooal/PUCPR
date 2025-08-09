#include <stdio.h>

// Uma P.A. (progressão aritmética) é uma sequência de números reais na qual a
// diferença entre dois números consecutivos quaisquer é constante, denominada a razão
// da P.A. Como exemplos, temos as seguintes sequências como P.A.:
// { 2, 5, 8, 11, 14, 17, 20 }
// o primeiro termo da P.A. é 2 e a razão da P.A. é 3
// { -4.5, -3.0, -1.5, 0, 1.5, 3.0, 4.5 }
// o primeiro termo da P.A. é -4.5 e a razão é 1.5
// { 10, 6, 2, -2, -6, -10 }
// o primeiro termo da P.A. é 10 e a razão é -4
// Escreva um programa na Linguagem C (contendo apenas a função main) que calcule
// e imprima (na tela do computador) o n-ésimo termo de uma P.A., dados (via leitura
// do teclado) o primeiro termo e a razão da P.A., além do próprio n. Por exemplo, se os
// dados fornecidos para o programa forem:
// • primeiro termo: 2
// • razão: 3
// • n: 4
// o valor impresso pelo programa será 11.
// IMPORTANTE: O programa não pode usar qualquer comando de repetição!

int main(){
    printf("Digite o primeiro termo da P.A: ");
    int termo1 = -1;
    scanf("%d", &termo1);

    printf("Digite a razão da P.A: ");
    int razao = -1;
    scanf("%d", &razao);

    printf("Digite o valor N: ");
    int n = -1;
    scanf("%d", &n);


    int valorFinalN = (razao*(n-1))+termo1;

    printf("O valor N é %d\n", valorFinalN);

    return 0;
}