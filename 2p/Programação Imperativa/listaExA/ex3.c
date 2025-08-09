#include <stdio.h>

// Escreva um programa na Linguagem C para calcular e apresentar o valor do
// volume de uma lata de óleo cilíndrica utilizando a seguinte fórmula:
// sendo V é o volume, R é o raio e h é a altura da lata.

int main(){
    printf("Digite o raio da lata: \n");
    double raio = -1;
    scanf("%lf", &raio);

    printf("Digite a altura da lata: \n");
    double altura = -1;
    scanf("%lf", &altura);

    double volume = 3.14159 * (raio * raio) * altura;

    printf("O volume da lata com as dimensões digitas é de %.2lf\n", volume);

    return 0;
}   