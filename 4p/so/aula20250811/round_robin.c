#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int id;
    int tempo_execucao;
    bool terminou; 
} processo;

processo start_process(int id, int tempo_execucao){
    processo p = {id, tempo_execucao, 0};
    return p;
}

void round_robin(int quantum, processo processos[]){
    bool continue_loop;
    do{
        continue_loop = false; 
        printf("\nExecutando ciclo...\n");

        for (int i = 0; i < 8; i++){
            if(processos[i].tempo_execucao > 0){
                processos[i].tempo_execucao -= quantum;

                printf("Subtraindo %d (quantum) do processo %d (Tempo de execução restante: %d)\n", quantum, processos[i].id, processos[i].tempo_execucao);

                if (processos[i].tempo_execucao <= 0){
                    processos[i].terminou = true;
                    printf("Processo %d finalizado!\n", processos[i].id);
                } else{
                    continue_loop = true;
                }
            }
        }
    } while (continue_loop == 1);
}

int main(){
    processo processos[] = {
        start_process(1, 5),
        start_process(2, 3),
        start_process(3, 2),
        start_process(4, 4),
        start_process(5, 6),
        start_process(6, 8),
        start_process(7, 1),
        start_process(8, 4)
    };

    int quantum = 2;

    round_robin(quantum, processos);

    return 0;
}