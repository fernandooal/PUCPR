#include <stdio.h>
#include <stdbool.h>

const int quantum = 2;

typedef enum {
    NOVO,
    PRONTO,
    EXECUCAO,
    ESPERANDO,
    TERMINADO
} Estado;

typedef struct {
    int id;
    int tempo_execucao;
    Estado estado; 
} processo;

processo start_process(int id, int tempo_execucao){
    processo p = {id, tempo_execucao, NOVO};
    return p;
}

char* estado_to_str(Estado e) {
    switch (e) {
        case NOVO:      return "[NOVO]";
        case PRONTO:    return "[PRONTO]";
        case EXECUCAO:  return "[EXECUCAO]";
        case ESPERANDO: return "[ESPERANDO]";
        case TERMINADO: return "[TERMINADO]";
        default:        return "[INVÁLIDO]";
    }
}

processo change_state(processo p, Estado novo_estado) {
    printf("\n[ESTADO] Alterando o estado do Processo %d de %s para %s!\n",
           p.id,
           estado_to_str(p.estado),
           estado_to_str(novo_estado));
    p.estado = novo_estado;
    return p;
}

void round_robin(int quantum, processo processos[]){
    bool continue_loop;
    do{
        continue_loop = false; 
        printf("\nExecutando ciclo...\n");

        for (int i = 0; i < 8; i++){
            if(processos[i].estado == ESPERANDO){
                processos[i] = change_state(processos[i], PRONTO);
            }
            if(processos[i].estado == PRONTO){
                processos[i] = change_state(processos[i], EXECUCAO);

                if(processos[i].tempo_execucao > 0){
                    processos[i].tempo_execucao -= quantum;

                    printf("Subtraindo %d (quantum) do processo %d (Tempo de execução restante: %d)\n", quantum, processos[i].id, processos[i].tempo_execucao);

                    if (processos[i].tempo_execucao <= 0){
                        processos[i] = change_state(processos[i], TERMINADO);
                        printf("Processo %d finalizado!\n", processos[i].id);
                    } else{
                        processos[i] = change_state(processos[i], ESPERANDO);
                        continue_loop = true;
                    }
                }
            }
            
        }
    } while (continue_loop == 1);
}

int main(){
    processo processos[] = {
        change_state(start_process(1, 5), PRONTO),
        change_state(start_process(2, 3), PRONTO),
        change_state(start_process(3, 2), PRONTO),
        change_state(start_process(4, 4), PRONTO),
        change_state(start_process(5, 6), PRONTO),
        change_state(start_process(6, 8), PRONTO),
        change_state(start_process(7, 1), PRONTO),
        change_state(start_process(8, 4), PRONTO)
    };

    round_robin(quantum, processos);

    return 0;
}