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
#include "semphr.h"
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdio.h>

// ---------------- PROTÓTIPOS ----------------
void task1(void *param);
void task2(void *param);
void task3(void *param);

// ---------------- VARIÁVEIS GLOBAIS ----------------

char display[32];
SemaphoreHandle_t xSemaphore;

int main_(void) {
    srand(time(NULL));

    xSemaphore = xSemaphoreCreateMutex();

    // criacao das tasks
    xTaskCreate(task1, "data", 1000, (void*) 1, 1, NULL);
    xTaskCreate(task2, "horario", 1000, (void*) 2, 1, NULL);
    xTaskCreate(task3, "temp", 1000, (void*) 3, 1, NULL);

    // escalonador
    vTaskStartScheduler();

    for (;;);
}

void task1(void *param){
    int id = (int) param;

    for(;;){
        // Obtendo o tempo em segundos
        time_t data;
        time(&data);
        struct tm* datetime = localtime(&data);
        
        // Obter dia
        int dia = datetime->tm_mday;

        // Obter mês
        int mes = datetime->tm_mon + 1;

        // Obter ano
        int ano = datetime->tm_year + 1900;

        // Adiciona conteúdo na variável display
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            sprintf(display, "Task %d - %d/%d/%d\n", id, dia, mes, ano);    

            vPrintString(display);
            xSemaphoreGive(xSemaphore);
        }

        vTaskDelay(1000);
    }
}

void task2(void *param){
    int id = (int) param;

    for(;;){
        // Obtendo o tempo em segundos
        time_t data;
        time(&data);
        struct tm* datetime = localtime(&data);

        // Obter hora
        int hora = datetime->tm_hour;

        // Obter minutos
        int minutos = datetime->tm_min;

        // Obter segundos
        int segundos = datetime->tm_sec;

        // Adiciona conteúdo na variável display
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            sprintf(display, "Task %d - %d:%d:%d\n", id, hora, minutos, segundos);    

            vPrintString(display);
            xSemaphoreGive(xSemaphore);
        }

        vTaskDelay(1000);
    }
   
}

void task3(void *param){
    int id = (int) param;

    for(;;){
        // Define semente do algoritmo de acordo com o tempo atual do sistema
        const int max_temp = 30;

        // Obtém valor aleatório. Valor máximo definido na constante max_temp
        float temperatura = ((float)rand() / (float)RAND_MAX) * max_temp;

        // Adiciona conteúdo na variável display
        if (xSemaphoreTake(xSemaphore, portMAX_DELAY) == pdTRUE) {
            sprintf(display, "Task %d - Curitiba %.2fºC\n", id, temperatura);
            
            vPrintString(display);
            xSemaphoreGive(xSemaphore);
        }

        vTaskDelay(1000);
    }
}