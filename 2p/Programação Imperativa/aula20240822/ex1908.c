#include <stdio.h>
#include <math.h>

// #Python
// # Cálculo do volume de uma esfera de raio R
// PI = 3.1416
// R = 0
// while R <= 6:
// VOLUME = 4/3 * PI * (R**3)
// print(R, VOLUME)
// R = R + 2

int main(){


    double pi = 3.1416;

    // ############### WHILE
    // while(R <= 6){
    //     double volume = 4.0/3 * pi * pow(R, 3);
    //     printf("%d, %lf\n", R, volume);

    //     R = R + 2;
    // }

    // ############### FOR
    for(short R = 0; R <= 6; R = R+2){
        double volume = 4.0/3 * pi * pow(R,3);
        printf("%d, %lf\n", R, volume);
    }

    return 0;
}