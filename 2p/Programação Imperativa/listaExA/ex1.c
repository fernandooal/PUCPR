#include <stdio.h>

// Escreva um programa na Linguagem C que efetue o cálculo do salário líquido
// de um funcionário horista. Os dados fornecidos pelo usuário via teclado devem ser:
// valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS e
// o percentual de desconto do Imposto de Renda.

int main(){
    printf("Digite o valor da sua hora aula: \n");
    int horaAula = -1;
    scanf("%d", &horaAula);

    printf("Digite o número de aulas dadas no mês: \n");
    int aulas = -1;
    scanf("%d", &aulas);

    printf("Digite o percentual de desconto do INSS: \n");
    double descontoINSS = -1;
    scanf("%lf", &descontoINSS);

    printf("Digite o percentual de desconto do Imposto de Renda: \n");
    double descontoRenda = -1;
    scanf("%lf", &descontoRenda);

    double descontoTotal = descontoRenda + descontoINSS;
    double salario = (horaAula * aulas) * (1 - (descontoTotal/100));

    printf("Seu salário líquido é de R$%.2lf\n", salario);

    return 0;
}