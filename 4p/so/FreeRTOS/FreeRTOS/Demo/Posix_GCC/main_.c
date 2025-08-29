#include "FreeRTOS.h"
#include "task.h"
#include "basic_io.h"
#include <time.h>
#include <stdlib.h>

void monitorarBatimentos(void *param);
void monitorarOxigenio(void *param);
void monitorarTemperatura(void *param);

int randint(int min, int max){
    return rand() % (max - min + 1) + min;
}

void monitorarBatimentos(void *param){
	for (;; ){
		int bpm = randint(40,150);
		vPrintStringAndNumber(param, bpm);

		if(bpm < 50 || bpm > 120){
	 		vPrintString("Atenção! Batimentos cardíacos em estado crítico\n");
		}

		vTaskDelay(1000);
	}
	
	vTaskDelete(NULL);
}

void monitorarOxigenio(void *param){
	for (;; ){
		int saturacao = randint(80,100);
		vPrintStringAndNumber(param, saturacao);

		if(saturacao < 90){
	 		vPrintString("Atenção! Saturação em estado crítico\n");
		}

		vTaskDelay(1000);
	}
	
	vTaskDelete(NULL);
}

void monitorarTemperatura(void *param){
	for (;; ){
		int temp = randint(35,38);
		vPrintStringAndNumber(param, temp);

		if(temp < 36 || temp > 37.5){
	 		vPrintString("Atenção! Febre em estado crítico\n");
		}

		vTaskDelay(1000);
	}
	
	vTaskDelete(NULL);
}

void main_(void){
	srand(time(NULL));

	xTaskCreate(monitorarBatimentos, "Monitoramento de Batimentos", 1000, "Batimentos: ", 1, NULL);
	xTaskCreate(monitorarOxigenio, "Monitoramento de Oxigênio", 1000, "Saturação: ", 1, NULL);
	xTaskCreate(monitorarTemperatura, "Monitoramento de Temperatura", 1000, "Temperatura: ", 1, NULL);

	vTaskStartScheduler();

	for (;; );
}

