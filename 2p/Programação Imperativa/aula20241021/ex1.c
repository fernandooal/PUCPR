#include <stdio.h>
#include <stdlib.h>

#define CAPACIDADE_INICIAL 20
#define AUMENTO_CAPACIDADE 20

typedef struct 
{
    char nome[100];
    int idade;
} Pessoa;

int main(){

    FILE* arquivo = fopen("pessoas.txt", "r");
    if (arquivo == NULL) {puts("Falha na abertura do arquivo."); exit(0);}
    
    size_t capacidade = CAPACIDADE_INICIAL;
    Pessoa* pessoas = (Pessoa*) malloc(capacidade * sizeof(Pessoa));
    if (pessoas == NULL) {puts("Falha na alocação de memória."); exit(1);}

    int quantidade = 0;
    int soma_idades = 0;

    while (fscanf(arquivo, "%s %d", pessoas[quantidade].nome, &pessoas[quantidade].idade) != EOF) {
        soma_idades += pessoas[quantidade].idade;
        quantidade++;

        if (quantidade == capacidade) {
            capacidade += AUMENTO_CAPACIDADE;
            pessoas = (Pessoa*) realloc(pessoas, capacidade * sizeof(Pessoa));
            if (pessoas == NULL) {puts("Falha na realocação de memória."); exit(1);}
        }
    }
    fclose(arquivo);

    double media_idades = (double)soma_idades / quantidade;

    printf("Pessoas com idade acima da média (%.2f anos):\n", media_idades);
    for (int i = 0; i < quantidade; i++) {
        if (pessoas[i].idade > media_idades) {
            printf("%s\n", pessoas[i].nome);
        }
    }

    free(pessoas);
    return 0;
}