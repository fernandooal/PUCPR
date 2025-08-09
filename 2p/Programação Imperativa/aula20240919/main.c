#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX 10

int main(){

    // SCANF - STRING
    // char nome[10];

    // printf("Entre com um nome: ");
    // scanf("%s", nome);
    // printf("nome = %s", nome);
    // printf("\n");
    
    // GETS - STRING
    // char texto[10];

    // gets(texto);
    // puts(texto);

    // STRLEN - tamanho da string

    // int tam;

    // tam = strlen("Terra");
    // printf("tam = %d\n", tam);
    
    // tam = strlen("Terra Azul");
    // printf("tam = %d\n", tam);
    
    // tam = strlen("");
    // printf("tam = %d\n", tam);

    // FGETS - STRING (Melhor)
    // char texto[MAX];
    // fgets(texto, MAX, stdin);

    // printf("%lu\n", strlen(texto));
    // puts(texto);

    // char ultimo = texto[strlen(texto)-1];
    // printf("ultimo carater: %c\n", ultimo);
    // printf("%d\n", ultimo);

    // STRCSPN - STRING POSITION
    // int pos;

    // pos = strcspn("Terra", "e");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "r");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "x");
    // printf("pos = %d\n", pos);

    // pos = strcspn("Terra", "t");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "T");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "rT");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "Tr");
    // printf("pos = %d\n", pos);
    
    // pos = strcspn("Terra", "aeiou");
    // printf("pos = %d\n", pos);

    
    // REMOVENDO O ENTER - STRCSPN
    // char texto[MAX];
    // fgets(texto, MAX, stdin);
    
    // int CRLF = strcspn(texto, "\r\n");
    // texto[CRLF] = '\0';
    
    // printf("%d\n", strlen(texto));
    // puts(texto);

    // char ultimo = texto[strlen(texto)-1];
    // printf("ultimo carater: %c\n", ultimo);

    char frase[MAX];

    printf("Digite uma frase: ");
    
    bool enter_nao_encontrado = true;
    do {
        fgets(frase, MAX, stdin);

        int tam = strlen(frase);
        printf("tam = %d\n", tam);

        int pos = strcspn(frase, "\r\n");
        printf("pos = %d\n", pos);
        
        if (pos < tam) enter_nao_encontrado = false;

        char ultimo = frase[tam-1];
        printf("ultimo: %c (%d)\n", ultimo, ultimo);
        
        frase[pos] = '\0';
        printf("%s\n\n", frase);

    } while (enter_nao_encontrado);
    return 0;
}