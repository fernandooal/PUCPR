#include "grafo.h"
#include <math.h>
#include <float.h>

float calcularDistancia(Pontos p1, Pontos p2) {
    return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

char* determinarDirecao(Pontos atual, Pontos proximo, Pontos seguinte) {
    float dx1 = proximo.x - atual.x;
    float dy1 = proximo.y - atual.y;
    float dx2 = seguinte.x - proximo.x;
    float dy2 = seguinte.y - proximo.y;

    float produtoVetorial = dx1 * dy2 - dy1 * dx2;

    if (produtoVetorial > 0) {
        return "vire à esquerda";
    } else if (produtoVetorial < 0) {
        return "vire à direita";
    } else {
        return "siga em frente";
    }
}

char* encontrarRuaComum(Pontos* pontoAtual, Pontos* pontoProximo) {
    if (strcmp(pontoAtual->rua1, pontoProximo->rua1) == 0 || strcmp(pontoAtual->rua1, pontoProximo->rua2) == 0) {
        return pontoAtual->rua1;
    } else if (strcmp(pontoAtual->rua2, pontoProximo->rua1) == 0 || strcmp(pontoAtual->rua2, pontoProximo->rua2) == 0) {
        return pontoAtual->rua2;
    }
    
    return NULL;
}

void dijkstra(Pontos* listaPontos, int tamanho, char origem, char destino) {
    int origemIndex = -1, destinoIndex = -1;
    
    for (int i = 0; i < tamanho; i++) {
        if (listaPontos[i].id == origem) origemIndex = i;
        if (listaPontos[i].id == destino) destinoIndex = i;
    }

    if (origemIndex == -1 || destinoIndex == -1) {
        printf("Pontos não encontrados\n");
        return;
    }

    float distancias[tamanho];
    int predecessores[tamanho];
    for (int i = 0; i < tamanho; i++) {
        distancias[i] = FLT_MAX;  
        predecessores[i] = -1;    
    }
    distancias[origemIndex] = 0;  

    int visitado[tamanho];
    for (int i = 0; i < tamanho; i++) visitado[i] = 0;

    // Dijkstra
    for (int i = 0; i < tamanho; i++) {
        int u = -1;
        float distMin = FLT_MAX;

        for (int j = 0; j < tamanho; j++) {
            if (!visitado[j] && distancias[j] < distMin) {
                distMin = distancias[j];
                // u é o ponto com a menor distancia nao visitado
                u = j;
            }
        }

        // Todos os pontos já foram visitados
        if (u == -1) break;  

        visitado[u] = 1;

        // Verifica os vizinhos do ponto u
        for (int j = 0; j < 4; j++) {
            if (listaPontos[u].vizinhos[j] == '\0') break; 

            char vizinhoId = listaPontos[u].vizinhos[j];
            int v = -1;
            for (int k = 0; k < tamanho; k++) {
                if (listaPontos[k].id == vizinhoId) {
                    v = k;
                    break;
                }
            }

            if (v != -1) {
                float dist = calcularDistancia(listaPontos[u], listaPontos[v]);
                if (distancias[u] + dist < distancias[v]) {
                    distancias[v] = distancias[u] + dist;
                    predecessores[v] = u;
                }
            }
        }
    }

    if (distancias[destinoIndex] == FLT_MAX) {
        printf("Não há caminho entre os pontos %c e %c.\n", origem, destino);
        return;
    }

    char caminho[tamanho];
    int atual = destinoIndex;
    int caminhoIndex = 0;

    while (atual != -1) {
        caminho[caminhoIndex++] = atual; 
        atual = predecessores[atual];
    }

    printf("Para realizar o percurso entre o ponto %c e o ponto %c, faça os seguintes movimentos:\n", origem, destino);

    // percorro de tras pra frente pq o algoritmo me retornou a ordem dos pontos ao contrario
    for (int i = caminhoIndex - 1; i > 0; i--) {
        int pontoAtual = caminho[i];
        int pontoProximo = caminho[i - 1];

        char* ruaComum = encontrarRuaComum(&listaPontos[pontoAtual], &listaPontos[pontoProximo]);
        if (ruaComum) {
            printf("(%d) Siga pela %s até o cruzamento com o ponto %c. ", caminhoIndex - i, ruaComum, listaPontos[pontoProximo].id);
        } else {
            printf("(%d) Não foi possível determinar a rua entre os pontos %c e %c.\n", caminhoIndex - i, listaPontos[pontoAtual].id, listaPontos[pontoProximo].id);
        }

        if (i > 1) { 
            int pontoSeguinte = caminho[i - 2];
            char* direcao = determinarDirecao(listaPontos[pontoAtual], listaPontos[pontoProximo], listaPontos[pontoSeguinte]);
            printf("Após o cruzamento, %s.\n", direcao);
        } else{
            puts("\n");
        }
    }
}

Pontos* lerGrafoBinario(int* tamanho, char* arquivo) {
    FILE* arquivo_binario = fopen(arquivo, "rb");
    if(!arquivo_binario) {puts("Erro ao abrir o arquivo binário");exit(1);}

    fread(tamanho, sizeof(int), 1, arquivo_binario);

    Pontos* listaPontos = malloc(*tamanho * sizeof(Pontos));
    if (!listaPontos) {puts("Erro ao alocar memória");fclose(arquivo_binario);exit(1);}

    fread(listaPontos, sizeof(Pontos), *tamanho, arquivo_binario);
    fclose(arquivo_binario);

    return listaPontos;
}

int main(int argc, char* argv[]) {

    if (argc != 2){
        puts("ERRO: número incorreto de argumentos!");
        puts("Uso: ./menorCaminho <arquivo-entrada-binario>");
        exit(1);
    }

    char* arquivoBinario = argv[1];

    int tamanho;

    Pontos* listaPontos = lerGrafoBinario(&tamanho, arquivoBinario);
    
    if (!listaPontos) exit(1); 

    char origem, destino;
    printf("Digite o ponto de origem: ");
    scanf("%c", &origem);

    getchar();

    printf("Digite o ponto de destino: ");
    scanf("%c", &destino);

    dijkstra(listaPontos, tamanho, origem, destino);

    free(listaPontos);
    
    return 0;
}
