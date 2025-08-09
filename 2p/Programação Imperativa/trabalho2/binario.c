#include "grafo.h"

int main(int argc, char* argv[]){

    if (argc != 4 ){
        puts("ERRO: número incorreto de argumentos!");
        puts("Uso: ./geraBinario <arquivo-entrada-pontos> <arquivo-entrada-vizinhos> <arquivo-saida>");
        exit(1);
    }

    char* pontosEntrada = argv[1];
    char* vizinhosEntrada = argv[2];
    char* grafoSaida = argv[3];

    FILE* pontos = fopen(pontosEntrada, "r");
    if(!pontos) {puts("Erro ao abrir o arquivo de pontos"); exit(1);}

    int capacidade = CAPACIDADE_INICIAL; 
    int tamanho = 0;
    Pontos *listaPontos = malloc(capacidade * sizeof(Pontos));
    if(!listaPontos) {puts("Erro ao alocar memória");fclose(pontos);exit(1);}

    // MONTAGEM DA LISTA - SEM OS VIZINHOS
    while (fscanf(pontos, " %c", &listaPontos[tamanho].id) == 1) {
        fscanf(pontos, "%f %f", &listaPontos[tamanho].x, &listaPontos[tamanho].y);

        fgetc(pontos);

        fgets(listaPontos[tamanho].rua1, sizeof(listaPontos[tamanho].rua1), pontos);
        listaPontos[tamanho].rua1[strcspn(listaPontos[tamanho].rua1, "\n")] = '\0'; 
        fgets(listaPontos[tamanho].rua2, sizeof(listaPontos[tamanho].rua2), pontos);
        listaPontos[tamanho].rua2[strcspn(listaPontos[tamanho].rua2, "\n")] = '\0'; 

        tamanho++;

        if (tamanho == capacidade) {
            capacidade += AUMENTO_CAPACIDADE; 
            Pontos *temp = realloc(listaPontos, capacidade * sizeof(Pontos));
            if(!temp) {puts("Erro ao realocar memória");free(listaPontos);fclose(pontos);exit(1);}
            listaPontos = temp;
        }
    }

    fclose(pontos);

    FILE* vizinhos = fopen(vizinhosEntrada, "r");
    if(!vizinhos) {puts("Erro ao abrir o arquivo de vizinhos");free(listaPontos);exit(1);}

    char ponto1, ponto2, rua[50];
    while (fscanf(vizinhos, " %c %c %[^\n]", &ponto1, &ponto2, rua) == 3) {
        int index1 = -1;
        for (int i = 0; i < tamanho; i++) {
            if (listaPontos[i].id == ponto1) {
                index1 = i;
                break;
            }
        }

        if (index1 != -1) {
            for (int i = 0; i < 4; i++) {
                if (listaPontos[index1].vizinhos[i] == '\0') {
                    listaPontos[index1].vizinhos[i] = ponto2;
                    break;
                }
            }
        }
    }   

    fclose(vizinhos);

    // for (int i = 0; i < tamanho; i++) {
    //     printf("Ponto %c: (%.1f, %.1f)\n", listaPontos[i].id, listaPontos[i].x, listaPontos[i].y);
    //     printf("  Rua 1: %s\n", listaPontos[i].rua1);
    //     printf("  Rua 2: %s\n", listaPontos[i].rua2);
    //     printf("  Vizinho 1: %c\n", listaPontos[i].vizinhos[0]);
    //     printf("  Vizinho 2: %c\n", listaPontos[i].vizinhos[1]);
    //     printf("  Vizinho 3: %c\n", listaPontos[i].vizinhos[2]);
    //     printf("  Vizinho 4: %c\n", listaPontos[i].vizinhos[3]);
    //     printf("\n");
    // }

    FILE* arquivo_binario = fopen(grafoSaida, "wb");
    if(!arquivo_binario) {puts("Erro ao criar o arquivo de saída");free(listaPontos);exit(1);}

    fwrite(&tamanho, sizeof(int), 1, arquivo_binario);

    fwrite(listaPontos, sizeof(Pontos), tamanho, arquivo_binario);

    fclose(arquivo_binario);
    puts("Dados gravados com sucesso no arquivo binário");

    free(listaPontos);

    return 0;
}