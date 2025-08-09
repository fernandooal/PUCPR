#include <stdio.h>
#include <stdlib.h>

int main(){

    double faturamentoDias[6];
    double faturamentoSemana = 0.0;

    for(int i = 0; i < 6; i++){
        printf("Digite o valor arrecadado no %dº dia: ", i+1);
        scanf("%lf", &faturamentoDias[i]);

        setbuf(stdin, NULL);

        faturamentoSemana += faturamentoDias[i];
    }

    double menor = faturamentoDias[0];
    double maior = faturamentoDias[0];
    int diaMenor = 0;
    int diaMaior = 0;

    for(int i = 1; i < 6; i++){
        if(faturamentoDias[i] < menor){
            menor = faturamentoDias[i];
            diaMenor = i;
        }
        if(faturamentoDias[i] > maior){
            maior = faturamentoDias[i];
            diaMaior = i;
        }
    }

    double mediaDiaria = faturamentoSemana/6.0;

    printf("Faturamento total da semana: R$ %.2lf\n", faturamentoSemana);
    printf("Faturamento diário médio: R$ %.2lf\n", mediaDiaria);
    printf("Dia da semana com o menor faturamento: %dº dia\n", diaMenor+1);
    printf("Dia da semana com o maior faturamento: %dº dia\n", diaMaior+1);

    return 0;
}