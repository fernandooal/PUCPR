/*
Curso: Bacharelado em Ciência da Computação
Disciplina: Sistemas Operacionais Ciberfísicos
Período: 4
Turma: U
Aluno: Fernando Alonso Piroga da Silva
*/

#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdio.h>
#include "basic_io.h"
#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"

// ---------------- PROTÓTIPOS ----------------
void arfagem(void *param);
void guinada(void *param);
void rolagem(void *param);
void radioFrequencia(void *param);
char *printMotores();

// ---------------- VARIÁVEIS GLOBAIS ----------------
SemaphoreHandle_t xSemaphore;

volatile long motor0, motor1, motor2, motor3;
volatile char sentido[15];     // guinada
volatile char direcao[15];     // arfagem
volatile char orientacao[15];  // rolagem

#define VALOR_INICIAL_MOTORES 5000

int main_(void) {
    srand(time(NULL));

    motor0 = VALOR_INICIAL_MOTORES;
    motor1 = VALOR_INICIAL_MOTORES;
    motor2 = VALOR_INICIAL_MOTORES;
    motor3 = VALOR_INICIAL_MOTORES;

    xSemaphore = xSemaphoreCreateBinary();
    if (xSemaphore != NULL) {
        // libera o semaforo
        xSemaphoreGive(xSemaphore);
    }

    // criacao das tasks
    xTaskCreate(arfagem, "Arfagem", 1000, "frente", 2, NULL);
    xTaskCreate(guinada, "Guinada", 1000, "horario", 2, NULL);
    xTaskCreate(rolagem, "Rolagem", 1000, "direita", 2, NULL);
    xTaskCreate(radioFrequencia, "RadioFrequencia", 1000, NULL, 1, NULL);

    // escalonador
    vTaskStartScheduler();

    for (;;);
}

char *printMotores() {
    static char msg[128];

    // montando a string com os valores dos motores
    snprintf(msg, sizeof(msg),
             "Motor 0: %ld\nMotor 1: %ld\nMotor 2: %ld\nMotor 3: %ld\n",
             motor0, motor1, motor2, motor3);
    return msg;
}

// ---------------- MANOBRAS ----------------
void arfagem(void *param) {
    sprintf((char*)direcao, "%s", (char*)param);

    for (;;) {
        // espero para pegar o semaforo
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            // salvo os valores originais do motor
            int temp0 = motor0;
            int temp1 = motor1;
            int temp2 = motor2;
            int temp3 = motor3;

            if (strcmp((const char*)direcao, "frente") == 0) {
                // aumentar velocidade dos motores 2 e 3
                motor2 *= 25;
                motor3 *= 25;

                // diminuir velocidade dos outros para empuxo constante
                motor0 /= 25;
                motor1 /= 25;
            } else {
                // aumentar velocidade dos motores 0 e 1
                motor0 *= 25;
                motor1 *= 25;

                // diminuir velocidade dos outros para empuxo constante
                motor2 /= 25;
                motor3 /= 25;
            }

            // prints do sistema
            vPrintString("==================\n");

            vPrintString("[MANOBRA] ARFAGEM\n");

            vPrintString("[AÇÃO] ");
            printf("%s", direcao);

            vPrintString("\n[MOTORES]\n");
            char *msg = printMotores();
            vPrintString(msg);

            vPrintString("==================\n");

            // volto os valores dos motores ao original
            motor0 = temp0;
            motor1 = temp1;
            motor2 = temp2;
            motor3 = temp3;

            // devolvo o semaforo
            xSemaphoreGive(xSemaphore);
        }
        vTaskDelay(portTICK_RATE_MS * 40);
    }
}

void guinada(void *param) {
    sprintf((char*)sentido, "%s", (char*)param);

    for (;;) {
        // espero para pegar o semaforo
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            // salvo os valores originais do motor
            int temp0 = motor0;
            int temp1 = motor1;
            int temp2 = motor2;
            int temp3 = motor3;

            if (strcmp((const char*)sentido, "horario") == 0) {
                // aumentar velocidade dos motores 0 e 2
                motor0 *= 100;
                motor2 *= 100;

                // diminuir velocidade dos outros para empuxo constante
                motor1 /= 100;
                motor3 /= 100;
            } else {
                // aumentar velocidade dos motores 1 e 3
                motor1 *= 100;
                motor3 *= 100;

                // diminuir velocidade dos outros para empuxo constante
                motor0 /= 100;
                motor2 /= 100;
            }

            // prints do sistema
            vPrintString("==================\n");

            vPrintString("[MANOBRA] GUINADA\n");

            vPrintString("[AÇÃO] ");
            printf("%s", sentido);

            vPrintString("\n[MOTORES]\n");
            char *msg = printMotores();
            vPrintString(msg);

            vPrintString("==================\n");

            // volto os valores dos motores ao original
            motor0 = temp0;
            motor1 = temp1;
            motor2 = temp2;
            motor3 = temp3;

            // devolvo o semaforo
            xSemaphoreGive(xSemaphore);
        }
        vTaskDelay(portTICK_RATE_MS * 10);
    }
}

void rolagem(void *param) {
    sprintf((char*)orientacao, "%s", (char*)param);

    for (;;) {
        // espero para pegar o semaforo
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            // salvo os valores originais do motor
            int temp0 = motor0;
            int temp1 = motor1;
            int temp2 = motor2;
            int temp3 = motor3;

            if (strcmp((const char*)orientacao, "direita") == 0) {
                // aumentar velocidade dos motores 0 e 3
                motor0 *= 50;
                motor3 *= 50;

                // diminuir velocidade dos outros para empuxo constante
                motor1 /= 50;
                motor2 /= 50;
            } else {
                // aumentar velocidade dos motores 1 e 2
                motor1 *= 50;
                motor2 *= 50;

                // diminuir velocidade dos outros para empuxo constante
                motor0 /= 50;
                motor3 /= 50;
            }

            // prints do sistema
            vPrintString("==================\n");

            vPrintString("[MANOBRA] ROLAGEM\n");

            vPrintString("[AÇÃO] ");
            printf("%s", orientacao);

            vPrintString("\n[MOTORES]\n");
            char *msg = printMotores();
            vPrintString(msg);

            vPrintString("==================\n");

            // volto os valores dos motores ao original
            motor0 = temp0;
            motor1 = temp1;
            motor2 = temp2;
            motor3 = temp3;

            // devolvo o semaforo
            xSemaphoreGive(xSemaphore);
        }
        vTaskDelay(portTICK_RATE_MS * 20);
    }
}

// ---------------- RADIO FREQUÊNCIA (controlador) ----------------
void radioFrequencia(void *param) {
    for (;;) {
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            // resto da divisão da seed por 100
            int r1 = rand() % 100;
            int r2 = rand() % 100;
            int r3 = rand() % 100;

            // é par? valores da esquerda : valores da direita
            sprintf((char*)sentido,    (r1 % 2 == 0) ? "horario"    : "anti-horário");
            sprintf((char*)direcao,    (r2 % 2 == 0) ? "frente"     : "tras");
            sprintf((char*)orientacao, (r3 % 2 == 0) ? "direita"    : "esquerda");

            // print do sistema
            printf("[RF] Alterou -> Sentido: %s | Direcao: %s | Orientacao: %s\n",
                   sentido, direcao, orientacao);

            // devolvo o semaforo
            xSemaphoreGive(xSemaphore);
        }
        vTaskDelay(portTICK_RATE_MS * 100);
    }
}
