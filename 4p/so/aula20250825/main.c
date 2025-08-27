#include <stdio.h>

int func() {
    static int i, estado = 0;

    // switch (estado){
    //     case 0: goto LABEL0;
    //     case 1: goto LABEL1;   
    // }

    // LABEL0:
    // for(i = 0; i < 10; i++){
    //     estado = 1;
    //     return i;
    //     LABEL1:;
    // }

    switch(estado){
        case 0:
            for(i = 0; i < 10; i++){
                estado = 1;
                return i;
                case 1:;
            }
    }

    return 0;
}

int main(){
    int a = func();
    printf("%d\n", a);

    int b = func();
    printf("%d\n", b);

    int c = func();
    printf("%d\n", c);
}