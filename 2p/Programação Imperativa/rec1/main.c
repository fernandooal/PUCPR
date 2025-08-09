#include <stdio.h>

#define MAX 100

int main(){

    FILE *fileDados;
    int valores[MAX];

    fileDados = fopen("dados.txt", "r");

    int qntdNumeros = 0;
    fscanf(fileDados, "%d", &qntdNumeros);

    // VALIDAÇÃO QUANTIDADE DE NUMEROS
    if(qntdNumeros > MAX){
        return -1;
    }

    // LENDO OS DADOS DO TXT
    int positivos = 0;
    int negativos = 0;
    int zeros = 0;
    int pares = 0;
    int impares = 0;
    for(int i = 0; i < qntdNumeros; i++){
        fscanf(fileDados, "%d", &valores[i]);

        if(valores[i] > 0){
            positivos++;
        } else{
            if(valores[i] == 0){
                zeros++;
            } else{
                negativos++;
            }
        }

        if(valores[i] % 2 == 0){
            pares++;
        } else{
            impares++;
        }
    }
    fclose(fileDados);

    // CRIANDO E PREENCHENDO O TXT DE ESTATISTICAS
    FILE *fileEstatisticas;
    fileEstatisticas = fopen("estatisticas.txt", "w");

    fprintf(fileEstatisticas, "Quantidade de numeros positivos: %d\n", positivos);
    fprintf(fileEstatisticas, "Quantidade de numeros negativos: %d\n", negativos);
    fprintf(fileEstatisticas, "Quantidade de numeros zero: %d\n", zeros);
    fprintf(fileEstatisticas, "Quantidade de numeros pares: %d\n", pares);
    fprintf(fileEstatisticas, "Quantidade de numeros impares: %d\n", impares);
    
    fclose(fileEstatisticas);

    // CRIANDO E PREENCHENDO O TXT DE NUMEROS DISTINTOS

    FILE *fileDistintos;
    fileDistintos = fopen("distintos.txt", "w");

    for(int i = 0; i < qntdNumeros; i++){
        int igual = 0;
        for(int j = i+1; j < qntdNumeros; j++){
            if(valores[j] == valores[i]){
                igual = 1;
            }
        }

        if(!igual){ 
            fprintf(fileDistintos, "%d ", valores[i]);
        }
    }

    fclose(fileDistintos);

    // CRIANDO E PREENCHENDO O TXT COM OS NUMEROS ORDENADOS

    FILE *fileOrdenados;
    fileOrdenados = fopen("ordenado.txt", "w");

    for(int i = 0; i < qntdNumeros; i++){
        for(int j = i+1; j < qntdNumeros; j++){
            if(valores[i] > valores[j]){
                int temp = valores[j];
                valores[j] = valores[i];
                valores[i] = temp;
            }
        }
    }

    for(int i = 0; i < qntdNumeros; i++){
        fprintf(fileOrdenados, "%d ", valores[i]);
    }

    fclose(fileOrdenados);

    // CRIANDO E PREENCHENDO O TXT COM OS NUMEROS DISTINTOS E ORDENADOS

    FILE *fileDistOrd;
    fileDistOrd = fopen("distintos_ordenado.txt", "w");

    for(int i = 0; i < qntdNumeros; i++){
        int igual = 0;
        for(int j = i+1; j < qntdNumeros; j++){
            if(valores[j] == valores[i]){
                igual = 1;
            }
        }

        if(!igual){ 
            fprintf(fileDistOrd, "%d ", valores[i]);
        }
    }

    fclose(fileDistOrd);

    return 0;
}