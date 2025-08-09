#include <stdio.h>
#include <stdbool.h>

int main()
{
    // ############# BOOLEANO
    // bool frio = true;
    // bool calor = false;

    // printf("%d\n", frio);
    // printf("%d\n", calor);

    // ############# PONTEIRO INT
    int a = 10;
    printf("endereco de a: %p\n", &a);
    printf("tamanho de a: %zu\n", sizeof(a));

    int* p = &a;
    printf("valor de p: %p\n", p);
    printf("valor apontado por p: %d\n", *p);
    printf("endereco de p: %p\n", &p);
    printf("tamanho de p: %zu\n", sizeof(p));

    // ############# ARITMETICA DE PONTEIRO
    // int a = 1, b = 2, c = 3;

    // printf("endereco de a: %p\n", &a);
    // printf("endereco de b: %p\n", &b);
    // printf("endereco de c: %p\n", &c);

    // int* p = &c;
    // printf("p: %p\n", p);
    // printf("conteudo de p: %d\n", *p);

    // p = p + 1;
    // printf("p: %p\n", p);
    // printf("conteudo de p: %d\n", *p);

    // p = p + 1;
    // printf("p: %p\n", p);
    // printf("conteudo de p: %d\n", *p);

    // ################# EX 3.4

    // short a = 10;
    // double b = 45.9;
    // char c = '$';
    // bool d = true;

    // printf("%p\n", &a);
    // printf("%zu\n", sizeof(a));

    // printf("------\n");

    // printf("%p\n", &b);
    // printf("%zu\n", sizeof(b));

    // printf("------\n");
    
    // printf("%p\n", &c);
    // printf("%zu\n", sizeof(c));
    
    // printf("------\n");

    // printf("%p\n", &d);
    // printf("%zu\n", sizeof(d));
    

    return 0;
}