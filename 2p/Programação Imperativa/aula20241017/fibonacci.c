#include <stdio.h>

int fib(int n){
    int resultado = 0;

    if(n == 0 || n == 1){
        return n;
    }

    return fib(n-1) + fib(n-2);
}

int main(){
    int n = fib(9);

    printf("%d\n", n);

    return 0;
}