#include <stdio.h>
#include <stdlib.h>

#define CAPACIDADE_INICIAL 20
#define AUMENTO_GRADUAL_DA_CAPACIDADE 20

int main()
{
    FILE* arquivo = fopen("arquivo1.txt", "r");
    if (arquivo == NULL) { puts("Falha na abertura do arquivo."); exit(0); }

    size_t capacidade = CAPACIDADE_INICIAL;

    char* letras = (char*) malloc(capacidade * sizeof(char));
    if (letras == NULL) { puts("Erro na alocacao de memoria."); exit(0); }

    int contador = 0; 
    char letra;
    int vogais[5] = {0};
    while (fscanf(arquivo, "%c", &letra) != EOF) 
    {
        if (contador == capacidade)
        {
            capacidade += AUMENTO_GRADUAL_DA_CAPACIDADE;
            letras = (char*) realloc(letras, capacidade * sizeof(char));
            if (letras == NULL) { puts("Erro na realocacao de memoria."); exit(0); }
        }

        if(tolower(letra) == 'a') vogais[0]++;
        if(tolower(letra) == 'e') vogais[1]++;
        if(tolower(letra) == 'i') vogais[2]++;
        if(tolower(letra) == 'o') vogais[3]++;
        if(tolower(letra) == 'u') vogais[4]++;

        letras[contador] = letra;
        contador++;
    }
    fclose(arquivo);

    int max_freq = 0;
    char vogal_max = '\0';
    char vogais_char[5] = {'a', 'e', 'i', 'o', 'u'};

    for (int i = 0; i < 5; i++) {
        if (vogais[i] > max_freq) {
            max_freq = vogais[i];
            vogal_max = vogais_char[i];
        }
    }

    FILE *novo_arquivo = fopen("arquivo_modificado.txt", "w");
    if (novo_arquivo == NULL) { puts("Erro ao criar o novo arquivo.");exit(0);}

    

    return 0;
}