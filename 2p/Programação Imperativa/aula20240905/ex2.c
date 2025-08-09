#include <stdio.h>
#include <stdlib.h>

int main(){

    int a[5];
    int b[5];
    int s[5];

    for(int i = 0; i < 5; i++){
        printf("Digite o %dº valor de A: ", i+1);
        scanf("%d", &a[i]);

        setbuf(stdin, NULL);

        printf("Digite o %dº valor de B: ", i+1);
        scanf("%d", &b[i]);

        setbuf(stdin, NULL);

        s[i] = a[i] + b[i];
    }

    puts("\nvetor a:");
    for(int i = 0; i < 5; i++)
        printf("%d ", a[i]);

    puts("\nvetor b:");
    for(int i = 0; i < 5; i++)
        printf("%d ", b[i]);

    puts("\nvetor s:");
    for(int i = 0; i < 5; i++)
        printf("%d ", s[i]);

    return 0;
}