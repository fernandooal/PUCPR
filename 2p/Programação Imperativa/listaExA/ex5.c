#include <stdio.h>

// Escreva um programa na Linguagem C que efetue o cálculo do volume de
// combustível gasto em uma viagem, sabendo-se que o carro faz 12 km com um litro de
// combustível. Deverão ser fornecidos como entrada do programa os seguintes dados: o
// tempo gasto na viagem e a velocidade média.
// Distância = Tempo x Velocidade
// Volume = Distância / 12
// O programa deverá exibir a distância percorrida e o volume de combustível gasto na
// viagem

int main(){
    printf("Digite o tempo gasto na viagem em minutos: ");
    double tempoMinutos = -1;
    scanf("%lf", &tempoMinutos);

    printf("Digite a velocidade média em km/h: ");
    double velocidadeKm = -1;
    scanf("%lf", &velocidadeKm);

    double distancia = (tempoMinutos * 60) * (velocidadeKm/3.6);

    double consumo = (distancia/1000)/12;

    printf("A distância percorrida foi de %.2lf metros e o consumo foi de %lf litros de combustível.\n", distancia, consumo);

    return 0;
}