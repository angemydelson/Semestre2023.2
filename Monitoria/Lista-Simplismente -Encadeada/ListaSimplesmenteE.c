#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct date {
    int dia;
    int mes;
    int ano;
};
typedef struct date Date;

struct employee {
    int id;
    char name[41];
    double income;
    Date dbirth;
    struct employee *next;
};
typedef struct employee Employee;

// Employee *criaEmployee(int id, char name[], double income, int ano, int mes, int dia){

// }

Employee *criarEmployee(int id, char name[], double income, int ano, int mes, int dia) {
    Employee *funcionario;
    funcionario = (Employee *)malloc(sizeof(Employee));
    strcpy(funcionario->name, name);
    funcionario->income = income;
    funcionario->id = id;
    funcionario->dbirth.ano = ano;
    funcionario->dbirth.mes = mes;
    funcionario->dbirth.dia = dia;
    funcionario->next = NULL;
    return funcionario; // Você esqueceu de retornar o ponteiro para o primeiro funcionário
}

Employee *incluirElementosFim(Employee *first, Employee *funcionario) {
    Employee *aux;
    if (first == NULL){
        first = funcionario;
        return first;
    } else {
        for(aux = first; aux->next != NULL; aux = aux->next);
        aux->next = funcionario;
    }
    return first;
    
}

Employee *incluirElementosPosId(Employee *first, Employee *funcionario, int id) {
    Employee *aux;
    if (first == NULL){
        first = funcionario;
        return first;
    }
    for(aux = first; aux->next != NULL; aux = aux->next){
        if (aux->id == id) break;
    };
        
    funcionario->next = aux->next;
    aux->next = funcionario;
    return first;
        
}

Employee *incluirElementosAntId(Employee *first, Employee *funcionario, int id) {
    Employee *aux, *aux2;
    if (first == NULL){
        first = funcionario;
        return first;
    }
    for(aux = first; aux->next != NULL; aux = aux->next){
        if (aux->id == id) break;
        aux2 = aux;
    };
   
    if (aux == first){
        funcionario->next = first;
        first = funcionario;
        return first;
    }
    
    aux2 = aux;
    funcionario->next = aux->next;
    aux->next = funcionario;
    return first;
        
}
   
Employee *excluirElemento(Employee *first, int id){
    Employee *aux, *previous;
    for (aux = first; aux != NULL; aux = aux->next){
        if (aux->id == id){
            if (aux == first){
                first = first->next;
                break;
            }
            previous->next = aux->next;
            break;
        }
        previous = aux;

    }
    if (aux != NULL) free(aux);
    return first;

}


void imprimirLista(Employee *first) {
    Employee *atual = first;
    while (atual != NULL) {
        printf("-=====================================================-\n");
        printf("ID: %d\n", atual->id);
        printf("Nome: %s\n", atual->name);
        printf("Renda: %.2lf\n", atual->income);
        printf("Data de Nascimento: %d/%d/%d\n", atual->dbirth.dia, atual->dbirth.mes, atual->dbirth.ano);
        printf("\n");
        printf("-=====================================================-\n");
        atual = atual->next;
    }
}


void desalocarLista(Employee *first) {
    if (first == NULL) return;
    desalocarLista(first->next);
    free(first);
}


int main() {
    Employee *first = NULL; // Inicialmente, a lista está vazia
    Employee *funcionario;
   
    // Criar o primeiro funcionário
    first = criarEmployee(1, "John", 50000.0, 1990, 5, 15);

    // Adicionar um segundo funcionário
    funcionario = criarEmployee(2, "Angemy", 60000.0, 1985, 8, 25);
    first = incluirElementosFim(first, funcionario);

    funcionario = criarEmployee(3, "Jane", 70000.0, 1685, 8, 55);
    first = incluirElementosFim(first, funcionario);

    funcionario = criarEmployee(4, "Mireille", 7005400.0, 2685, 10, 3);
    first = incluirElementosFim(first, funcionario);
    // imprimirLista(first);

    funcionario = criarEmployee(3, "Midelta", 7005400.0, 2685, 11, 3);
    first = incluirElementosPosId(first, funcionario, 3);

    funcionario = criarEmployee(5, "Patricia", 7005400.0, 2685, 11, 3);
    first = incluirElementosPosId(first, funcionario, 4);

    funcionario = criarEmployee(5, "Delva", 7005400.0, 2685, 11, 3);
    first = incluirElementosAntId(first, funcionario, 1);
    // Imprimir a lista de funcionários
    imprimirLista(first);
    // imprimirListarecursivo(first);
    // excluirElemento(first, 5);
    // imprimirLista(first);

    return 0;
}
