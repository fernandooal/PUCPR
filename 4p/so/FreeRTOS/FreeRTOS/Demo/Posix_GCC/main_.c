/*
Curso: Bacharelado em Ciência da Computação
Disciplina: Sistemas Operacionais Ciberfísicos
Período: 4
Turma: U
Aluno: Fernando Alonso Piroga da Silva
*/

#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

void controladorManobras(void *param);
void arfagem(void *param);
void guinada(void *param);
void rolagem(void *param);
char *printMotores();

static int motor0, motor1, motor2, motor3;

#define VALOR_INICIAL_MOTORES 5000

void main_(void){
    motor0 = VALOR_INICIAL_MOTORES;
    motor1 = VALOR_INICIAL_MOTORES;
    motor2 = VALOR_INICIAL_MOTORES;
    motor3 = VALOR_INICIAL_MOTORES;


    vSemaphoreCreateBinary();
	srand(time(NULL));

    xTaskCreate(controladorManobras, "controlador", 1000, NULL, 1, NULL);

    vTaskStartScheduler();

	for (;;);
}

void controladorManobras(void *param){
    // possíveis parâmetros
    const char *arfagemOpts[] = {"para frente", "para trás"};
    const char *guinadaOpts[] = {"horário", "anti-horário"};
    const char *rolagemOpts[] = {"direita", "esquerda"};

    for(;;){
        // sorteio um valor aleatorio e pego o resto da divisão por 3
        // (tenho 3 manobras, então só existem 3 cases)
        int sorteio = rand() % 3;

        // como cada manobra possui 2 possibilidades de parâmetro, vou pegar o resto do mesmo 
        // sorteio por 2 (0 ou 1) para achar o indice do parametro
        switch(sorteio){
            case 0: {
                int i = sorteio % 2;
                xTaskCreate(arfagem, "arfagem", 1000, (void*) arfagemOpts[i], 1, NULL);
                break;
            }
            case 1: {
                int i = sorteio % 2;
                xTaskCreate(guinada, "guinada", 1000, (void*) guinadaOpts[i], 1, NULL);
                break;
            }
            case 2: {
                int i = sorteio % 2;
                xTaskCreate(rolagem, "rolagem", 1000, (void*) rolagemOpts[i], 1, NULL);
                break;
            }
        }

        vTaskDelay(10);
    }
}


char *printMotores(){
    static char msg[64];

    // montando a string com os valores dos motores
    snprintf(msg, sizeof(msg), "Motor 0: %d\nMotor 1: %d\nMotor 2: %d\nMotor3: %d\n", motor0, motor1, motor2, motor3);

    return msg;
}

void arfagem(void *param){
    // salvo os valores originais do motor
    int temp0 = motor0;
    int temp1 = motor1;
    int temp2 = motor2;
    int temp3 = motor3;

    if(strcmp(param, "para frente") == 0){
        // aumentar velocidade dos motores 2 e 3
        motor2 *= 25;
        motor3 *= 25;

        // diminuir velocidade dos outros para empuxo constante
        motor0 /= 25;
        motor1 /= 25;
    } else{
        // aumentar velocidade dos motores 0 e 1
        motor0 *= 25;
        motor1 *= 25;

        // diminuir velocidade dos outros para empuxo constante
        motor2 /= 25;
        motor3 /= 25;
    }

    // print do sistema
    vPrintString("==================\n");
    vPrintString("[MANOBRA] ARFAGEM\n");

    vPrintString("[AÇÃO] ");
    vPrintString(param);

    vPrintString("\n[MOTORES]\n");
    char *msg = printMotores();
    vPrintString(msg);

    vPrintString("==================\n");

    // volto os valores dos motores ao original
    motor0 = temp0;
    motor1 = temp1;
    motor2 = temp2;
    motor3 = temp3;

    vTaskDelay(40);

    vTaskDelete(NULL);
}

void guinada(void *param){
    // salvo os valores originais do motor
    int temp0 = motor0;
    int temp1 = motor1;
    int temp2 = motor2;
    int temp3 = motor3;

    if(strcmp(param, "horário") == 0){
        // aumentar velocidade dos motores 0 e 2
        motor0 *= 100;
        motor2 *= 100;

        // diminuir velocidade dos outros para empuxo constante
        motor1 /= 100;
        motor3 /= 100;
    } else{
        // aumentar velocidade dos motores 1 e 3
        motor1 *= 100;
        motor3 *= 100;

        // diminuir velocidade dos outros para empuxo constante
        motor0 /= 100;
        motor2 /= 100;
    }

    // print do sistema
    vPrintString("==================\n");
    vPrintString("[MANOBRA] GUINADA\n");

    vPrintString("[AÇÃO] ");
    vPrintString(param);

    vPrintString("\n[MOTORES]\n");
    char *msg = printMotores();
    vPrintString(msg);

    vPrintString("==================\n");

    // volto os valores dos motores ao original
    motor0 = temp0;
    motor1 = temp1;
    motor2 = temp2;
    motor3 = temp3;

    vTaskDelay(10);
    
    vTaskDelete(NULL);
}

void rolagem(void *param){
    // salvo os valores originais do motor
    int temp0 = motor0;
    int temp1 = motor1;
    int temp2 = motor2;
    int temp3 = motor3;

    if(strcmp(param, "direita") == 0){
        // aumentar velocidade dos motores 0 e 3
        motor0 *= 50;
        motor3 *= 50;

        // diminuir velocidade dos outros para empuxo constante
        motor1 /= 50;
        motor2 /= 50;
    } else{
        // aumentar velocidade dos motores 1 e 2
        motor1 *= 50;
        motor2 *= 50;

        // diminuir velocidade dos outros para empuxo constante
        motor0 /= 50;
        motor3 /= 50;
    }

    // print do sistema
    vPrintString("==================\n");
    vPrintString("[MANOBRA] ROLAGEM\n");

    vPrintString("[AÇÃO] ");
    vPrintString(param);

    vPrintString("\n[MOTORES]\n");
    char *msg = printMotores();
    vPrintString(msg);

    vPrintString("==================\n");

    // volto os valores dos motores ao original
    motor0 = temp0;
    motor1 = temp1;
    motor2 = temp2;
    motor3 = temp3;

    vTaskDelay(20);

    vTaskDelete(NULL);
}
