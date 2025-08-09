#include <stdio.h>

int main(){

    printf("Digite o valor n: ");
    int n;
    scanf("%d", &n);

    int num1 = 0;
    int num2 = 1;

    printf("0\n");
    printf("1\n");

    for(int i = 2; i <= n; i++){
        int fib = num1 + num2;

        num1 = num2;
        num2 = fib;

        printf("%d\n", fib);
    }

    return 0;
}