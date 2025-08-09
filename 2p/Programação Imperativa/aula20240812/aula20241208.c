#include <stdio.h>
#include <stdbool.h>

int main(){


    //########### INPUT DE CHAR
    // printf("Digite dois caracteres e ENTER: ");
    // char d1 = getchar();

    // char d2 = getchar();

    // int v1 = d1 - '0';

    // int v2 = d2 - '0';

    // int valorFinal = v1*10 + v2;

    // printf("%d\n", v1);
    // printf("%d\n", v2);

    // printf("\n%d\n", valorFinal);


    //########### INPUT DE DADOS FORMATADOS

    // int idade = -1;
    // printf("Digite a sua idade: ");

    // scanf("%d", &idade);
    // printf("Sua idade: %d", idade);
    // printf("\n");
    
    // double altura = -1;

    // printf("Digite a sua altura: ");
    // scanf("%5lf", &altura);

    // printf("Sua altura: %f", altura);
    // printf("\n");

    // int idade = -1;
    // double altura = -1;

    // printf("Digite a sua idade e a sua altura: ");
    // scanf("%3d %5lf", &idade, &altura);

    // printf("Sua idade: %d", idade);
    // printf("\n");

    // printf("Sua altura: %f", altura);
    // printf("\n");

    // ################### IF

    int a = 10;
    int b = 30;
    int c = 20;

    bool resultado1 = a < b;
    printf("resultado1: %d\n", resultado1);

    bool resultado2 = (a < b) && (b < c);
    printf("resultado2: %d\n", resultado2);

    bool resultado3 = resultado1 || resultado2;
    printf("resultado3: %d\n", resultado3);

    bool resultado4 = (a < b || b < c) && a < c;
    printf("resultado4: %d\n", resultado4);

    return 0;
}   