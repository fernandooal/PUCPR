#include <stdio.h>

int main(){

    int quantidade;
    float preco;
    int estoque[10];
    char palavra[10];

    for (int i = 0; i < 10; i++)
        printf("endereco de palavra[%d]: %lu\n", i, &palavra[i]);

    // int teste = 13/2;

    // printf("%d", teste);

    return 0;
}