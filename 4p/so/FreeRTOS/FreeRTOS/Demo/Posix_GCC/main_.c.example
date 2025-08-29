
#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"
#include "time.h"

/*
 1 - O protÛtipo da funÁ„o de uma tarefa deve sempre retornar void, ou seja, a tarefa n„o possui retorno.
 2 - A funÁ„o de uma tarefa deve receber um par‚metro de ponteiro void. 
*/
void vTask1(void *pvParameters);
void vTask2(void* pvParameters);
void taskNome(void *pvParameters);
void taskSobrenome(void *pvParameters);
void taskTempo(void *pvParameters);

/*
 DeniÁ„o da estrutura da funÁ„o
*/
void vTask1(void *pvParameters)
{
	const char *msg = "Task 1\n";

	for (;; )
	{
		vPrintString(msg);
		vTaskDelay(500);
	}

	vTaskDelete(NULL);
}

void vTask2(void* pvParameters)
{
	const char* msg = "Task 2\n";

	for (;; )
	{
		vPrintString(msg);
		vTaskDelay(500);
	}

	vTaskDelete(NULL);
}

void main_(void)
{

	// xTaskCreate(vTask1, "Task 1", 1000, NULL, 1, NULL);
	// xTaskCreate(vTask2, "Task 2", 1000, NULL, 1, NULL);

	// Prática
	// xTaskCreate(taskNome, "Task Nome", 1000, NULL, 1, NULL);
	// xTaskCreate(taskSobrenome, "Task Sobrenome", 1000, NULL, 1, NULL);
	xTaskCreate(taskTempo, "Task Tempo Local", 1000, NULL, 1, NULL);

	// Inicia o escalonador de tarefas
	vTaskStartScheduler();

	for (;; );
}

void taskNome(void *pvParameters) {
	const char* nome = "Fernando ";

	for(;; ){
		vPrintString(nome);
		vTaskDelay(500);
	}

	vTaskDelete(NULL);
}

void taskSobrenome(void *pvParameters){
	const char* sobrenome = "Alonso\n";

	for(;; ){
		vPrintString(sobrenome);
		vTaskDelay(750);
	}

	vTaskDelete(NULL);
}

#include <stdio.h>

void taskTempo(void *pvParameters) {
    char msg[64];
    time_t segundos;

    for (;;) {
        time(&segundos);                          
        struct tm* currentTime = localtime(&segundos);

        snprintf(msg, sizeof(msg), "Tempo Local: %02d:%02d:%02d\n", 
                 currentTime->tm_hour, 
                 currentTime->tm_min, 
                 currentTime->tm_sec);

        vPrintString(msg);
        vTaskDelay(1000);
    }

    vTaskDelete(NULL);
}
