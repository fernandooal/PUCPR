#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node 
{
    int valor;
    struct Node* anterior;
    struct Node* prox;
};

void inserirOrdenado(Node** head, int valor) {
    Node* novo = (Node*) malloc(sizeof(Node));
    novo->valor = valor;
    novo->anterior = NULL;
    novo->prox = NULL;

    if (*head == NULL || (*head)->valor >= valor) { 
        novo->prox = *head;
        if (*head) {
            (*head)->anterior = novo;
        }
        *head = novo;
    } else {
        Node* atual = *head;
        while (atual->prox && atual->prox->valor < valor) {
            atual = atual->prox;
        }
        novo->prox = atual->prox;

        if (atual->prox) {
            atual->prox->anterior = novo;
        }

        atual->prox = novo;
        novo->anterior = atual;

    }
}

int main(){

    FILE* arquivo = fopen("arquivo.txt", "r");
    if(!arquivo) {puts("erro ao abrir o arquivo"); exit(0);}

    Node* head = NULL;

    int valorNum;
    int contador = 0;
    while(fscanf(arquivo, "%d", &valorNum) != EOF){
        inserirOrdenado(&head, valorNum);
    }

    fclose(arquivo);

    Node* atual = head->prox;
    while(atual){
        printf("%d\n", atual->valor);
        atual = atual->prox;
    }

    return 0;
}