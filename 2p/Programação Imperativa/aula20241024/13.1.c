#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Planeta Planeta;
struct Planeta {
    char nome[16];
    double raio;
    double distancia_do_sol;
    Planeta* proximo;
};

int main(){

    const size_t TAMANHO_ELEMENTO = sizeof(Planeta);

    Planeta* terra = (Planeta*) calloc(1, TAMANHO_ELEMENTO);
    strcpy(terra->nome, "Terra");
    terra->raio = 6378.0;
    terra->distancia_do_sol = 149600000.0;
    terra->proximo = NULL;

    Planeta* marte = (Planeta*) calloc(1, TAMANHO_ELEMENTO);
    strcpy(marte->nome, "Marte");
    marte->raio = 3396.0;
    marte->distancia_do_sol = 227940000.0;
    marte->proximo = terra;

    Planeta* jupiter = (Planeta*) calloc(1, TAMANHO_ELEMENTO);
    strcpy(jupiter->nome, "Jupiter");
    jupiter->raio = 71492.0;
    jupiter->distancia_do_sol = 778330000.0;
    jupiter->proximo = marte;

    Planeta* p = jupiter;
    while (p) 
    {
        printf("%s\n", p->nome);
        p = p->proximo;
    }

    p = jupiter;
    while(p){
        Planeta* temp = p;
        p = p->proximo;

        free(temp);
    }

    printf("%p\n", jupiter->proximo);
    printf("%p\n", marte->proximo);
    printf("%p\n", terra->proximo);


    return 0;
}