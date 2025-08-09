#include <stdio.h>
#include <math.h>

int main(){

    int alunosTurma;
    printf("Digite a quantidade de alunos na turma (máximo de 50): ");
    scanf("%d", &alunosTurma);

    while(alunosTurma > 50){
        printf("Quantidade de alunos inválida! Informe um número menor que 50: ");
        scanf("%d", &alunosTurma);
    }

    double soma = 0.0;
    double notasAlunos[alunosTurma];
    for(int i = 0; i < alunosTurma; i++){
        printf("Digite a nota do %dº aluno: ", i+1);
        scanf("%lf", &notasAlunos[i]);
        soma += notasAlunos[i];
    }

    double media = soma/alunosTurma;
    double somatoriaDesvio = 0.0;
    for(int i = 0; i < alunosTurma; i++){
        double temp = pow(notasAlunos[i] - media, 2);
        somatoriaDesvio += temp;
    }

    double desvioPadrao = sqrt(somatoriaDesvio/alunosTurma);

    printf("O desvio padrão é %.2lf\n", desvioPadrao);

    return 0;
}