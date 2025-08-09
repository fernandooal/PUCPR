#ifndef GRAFO_H
#define GRAFO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAPACIDADE_INICIAL 10
#define AUMENTO_CAPACIDADE 10

typedef struct {
    char id;
    float x, y;
    char rua1[50], rua2[50];
    char vizinhos[4];
} Pontos;

#endif
