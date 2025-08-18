
#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"

/*
 1 - O protÛtipo da funÁ„o de uma tarefa deve sempre retornar void, ou seja, a tarefa n„o possui retorno.
 2 - A funÁ„o de uma tarefa deve receber um par‚metro de ponteiro void. 
*/
void vTask1(void *pvParameters);
void vTask2(void* pvParameters);

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

	xTaskCreate(vTask1, "Task 1", 1000, NULL, 1, NULL);
	xTaskCreate(vTask2, "Task 2", 1000, NULL, 1, NULL);

	// Inicia o escalonador de tarefas
	vTaskStartScheduler();

	for (;; );
//	return 0;
}

