#include <stdio.h>

// Escreva um programa na Linguagem C que leia uma temperatura em gruas
// Celsius e apresente a temperatura convertida em graus Fahrenheit. A fórmula de
// conversão é:
// sendo que F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

int main(){
    printf("Digite a temperatura em Celsius: \n");
    double tempCelsius = -1;
    scanf("%lf", &tempCelsius);

    double tempFahrenheit = ((9 * tempCelsius) + 160)/5;

    printf("A temperatura digitada em Fahrenheit é de F %.2lf\n", tempFahrenheit);

    return 0;
}