#include <stdio.h>

// Escreva um programa na Linguagem C que leia um valor de hora no formato
// hora:minutos e informe (calcule) o total de minutos que se passaram desde o
// início do dia (0:00h).

int main(){
    printf("Digite um horário no formato hora:minuto (00:00): ");

    char h1 = getchar();
    char h2 = getchar();
    char skip = getchar();
    char m1 = getchar();
    char m2 = getchar();

    h1 = h1 - '0';
    h2 = h2 - '0';

    m1 = m1 - '0';
    m2 = m2 - '0';

    int minutosFinal = (((h1*10)+h2)*60) + (m1*10) + m2;

    printf("O tempo final em minutos é %d\n", minutosFinal);

    return 0;
}