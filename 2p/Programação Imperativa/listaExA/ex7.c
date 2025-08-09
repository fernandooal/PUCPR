#include <stdio.h>

// Em certo país, as placas dos veículos possuem quatro algarismos, sendo:
// • O primeiro algarismo corresponde a um estado do país
// • O segundo algarismo corresponde a uma cidade daquele estado
// • O terceiro e o quarto algarismos formam o número do veículo em sua
// cidade
// Por exemplo, o veículo com placa 5832 indica que está registrado no estado 5, na
// cidade 8 (do estado 5) e tem o número 32 na cidade.
// Escreva um programa na Linguagem C (contendo apenas a função main) que leia um
// valor inteiro de quatro algarismos correspondente à placa de um veículo e imprima
// separadamente o número do estado, o número da cidade no estado e o número do
// veículo na cidade.
// IMPORTANTE: O resultado da leitura do número da placa do veículo tem,
// necessariamente, que ser armazenado em uma variável de um dos seguintes tipos:
// unsigned int ou unsigned short. Assim, o programa deverá usar as operações de
// divisão inteira e resto de divisão.

int main(){
    printf("Digite o número da placa do veículo: ");
    unsigned int placa = 0;
    scanf("%i", &placa);

    int estado = placa / 1000;
    int cidade = (placa - (1000*estado)) / 100;
    int veiculo = placa - (1000*estado) - (100*cidade);

    printf("Estado: %i;\nCidade: %i;\nVeículo: %i.\n", estado, cidade, veiculo);

    return 0;
}