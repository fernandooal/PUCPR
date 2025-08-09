#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define CAPACIDADE_INICIAL 10
#define AUMENTO_CAPACIDADE 10

typedef struct {
    char marca[20];
    char modelo[30];
    int anoFabricacao;
    int km;
    float preco;
} Carros;

Carros* inserirCarroOrdenado(Carros* carros, int* totalCarros, size_t* capacidade, Carros novoCarro) {
    if (*totalCarros == *capacidade) {
        *capacidade += AUMENTO_CAPACIDADE;
        carros = (Carros*) realloc(carros, *capacidade * sizeof(Carros));
        if (!carros) {puts("Erro na realocação de memória.");exit(0);}
    }

    int j = *totalCarros - 1;
    while (j >= 0 && carros[j].preco >= novoCarro.preco) {
        carros[j + 1] = carros[j];
        j--;
    }
    carros[j + 1] = novoCarro;
    (*totalCarros)++;

    return carros;
}

void imprimirMenu(){
    puts("Qual das seguintes funções você gostaria de executar?\n");
    puts("0 - Sair;");
    puts("1 - Exibir a relação completa de veículos;");
    puts("2 - Exibir a relação de veículos de uma marca específica;");
    puts("3 - Exibir a relação de veículos entre um valor mínimo e máximo;");
    puts("4 - Inserir um novo veículo;");
    puts("5 - Remover veículos cuja quilometragem excedam um valor;");
}

void imprimirVeiculos(int totalCarros, Carros* carros){
    puts("-------------");    
    
    for (int i = 0; i < totalCarros; i++) {
        printf("Marca: %s\n", carros[i].marca);
        printf("Modelo: %s\n", carros[i].modelo);
        printf("Ano de Fabricação: %d\n", carros[i].anoFabricacao);
        printf("Quilometragem: %d\n", carros[i].km);
        printf("Preço: %.2f\n", carros[i].preco);
        puts("-------------");
    }
}

void imprimirVeiculosMarca(int totalCarros, Carros* carros){
    char marca[20];
    getchar();
    printf("Digite a marca que você gostaria de filtrar: ");
    fgets(marca, sizeof(marca), stdin);
    marca[strcspn(marca, "\n")] = '\0';

    puts("-------------");

    for(int i = 0; i < totalCarros; i++){
        if(strcmp(carros[i].marca, marca) == 0){
            printf("Marca: %s\n", carros[i].marca);
            printf("Modelo: %s\n", carros[i].modelo);
            printf("Ano de Fabricação: %d\n", carros[i].anoFabricacao);
            printf("Quilometragem: %d\n", carros[i].km);
            printf("Preço: %.2f\n", carros[i].preco);
            puts("-------------");
        }
    }
}

void imprimirVeiculosPreco(int totalCarros, Carros* carros){
    printf("Digite um valor mínimo para a busca: ");
    float minimo;
    scanf("%f", &minimo);

    printf("Digite um valor máximo para a busca: ");
    float maximo;
    scanf("%f", &maximo);
    puts("-------------");

    
    for (int i = 0; i < totalCarros; i++) {
        if(carros[i].preco > minimo && carros[i].preco < maximo){
            printf("Marca: %s\n", carros[i].marca);
            printf("Modelo: %s\n", carros[i].modelo);
            printf("Ano de Fabricação: %d\n", carros[i].anoFabricacao);
            printf("Quilometragem: %d\n", carros[i].km);
            printf("Preço: %.2f\n", carros[i].preco);
            puts("-------------");
        }
    }
}

Carros* inserirVeiculo(int* totalCarros, Carros* carros, size_t* capacidade){
    Carros novoCarro;
    printf("Digite a marca do veículo: ");
    getchar();
    fgets(novoCarro.marca, sizeof(novoCarro.marca), stdin);
    novoCarro.marca[strcspn(novoCarro.marca, "\n")] = '\0'; 

    printf("Digite o modelo do veículo: ");
    fgets(novoCarro.modelo, sizeof(novoCarro.modelo), stdin);
    novoCarro.modelo[strcspn(novoCarro.modelo, "\n")] = '\0';

    printf("Digite o ano de fabricação do veículo: ");
    scanf("%d", &novoCarro.anoFabricacao);
    printf("Digite a quilometragem do veículo: ");
    scanf("%d", &novoCarro.km);
    printf("Digite o preço do veículo: ");
    scanf("%f", &novoCarro.preco);

    return inserirCarroOrdenado(carros, totalCarros, capacidade, novoCarro);
}

void removerVeiculo(int* totalCarros, Carros* carros){
    printf("Digite a quilometragem máxima: ");
    int kmMax;
    scanf("%d", &kmMax);

    int novoTotal = 0;
    for(int i = 0; i < *totalCarros; i++){
        if(carros[i].km <= kmMax){
            carros[novoTotal] = carros[i];
            novoTotal++;
        }
    }

    *totalCarros = novoTotal;
}

int main() {
    FILE* arquivo = fopen("carros.txt", "r");
    if (!arquivo) {puts("Erro ao abrir o arquivo.");exit(0);}

    size_t capacidade = CAPACIDADE_INICIAL;
    Carros* carros = (Carros*) malloc(capacidade * sizeof(Carros));
    if (!carros) {puts("Erro na alocação de memória.");fclose(arquivo);exit(0);}

    int totalCarros = 0;
    Carros novoCarro;
    while (fgets(novoCarro.marca, sizeof(novoCarro.marca), arquivo) != NULL) {
        novoCarro.marca[strcspn(novoCarro.marca, "\n")] = '\0';
        fgets(novoCarro.modelo, sizeof(novoCarro.modelo), arquivo);
        novoCarro.modelo[strcspn(novoCarro.modelo, "\n")] = '\0';

        fscanf(arquivo, "%d\n", &novoCarro.anoFabricacao);
        fscanf(arquivo, "%d\n", &novoCarro.km);
        fscanf(arquivo, "%f\n", &novoCarro.preco);

        carros = inserirCarroOrdenado(carros, &totalCarros, &capacidade, novoCarro);
    }
    fclose(arquivo);

    int opcaoMenu = 1;
    while(opcaoMenu != 0){
        imprimirMenu();
        scanf("%d", &opcaoMenu);

        switch (opcaoMenu)
        {
        case 1:
            imprimirVeiculos(totalCarros, carros);
            break;
        case 2:
            imprimirVeiculosMarca(totalCarros, carros);
            break;
        case 3:
            imprimirVeiculosPreco(totalCarros, carros);
            break;
        case 4:
            carros = inserirVeiculo(&totalCarros, carros, &capacidade);
            break;
        case 5:
            removerVeiculo(&totalCarros, carros);
            break;
        case 0:
        default:
            break;
        }
    }

    free(carros);
    return 0;
}
