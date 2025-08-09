#include <stdio.h>

// const short DOMINGO = 0;
// const short SEGUNDA = 1;
// const short TERCA = 2;
// const short QUARTA = 3;
// const short QUINTA = 4;
// const short SEXTA = 5;
// const short SABADO = 6;

#define DOMINGO 0
#define SEGUNDA 1
#define TERCA 2
#define QUARTA 3
#define QUINTA 4
#define SEXTA 5
#define SABADO 6

int main(){

    short s1 = QUINTA;

    switch(s1){
        case DOMINGO: printf("domingo\n");break;
        case SEGUNDA: printf("segunda\n");break;
        case TERCA: printf("terca\n");break;
        case QUARTA: printf("quarta, %d\n", s1);break;
        case QUINTA: printf("quinta, %c\n", s1);break;
        case SEXTA: printf("sexta\n");break;
        case SABADO: printf("sabado\n");break;
        default: printf("valor invalido");
    }

    return 0;
}