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
    struct employee *prev;
};
typedef struct employee Employee;

struct tsent {
    Employee *first;
    Employee *last;
};
typedef struct tsent Sentinela;

Sentinela *initialisation(Sentinela *lista){
    lista->first = NULL;
    lista->last = NULL;
}


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
    funcionario->prev = NULL;
    return funcionario; 
}

Employee *incluirElementosComeco(Sentinela *lista, Employee *funcionario) {
    if (lista->first == NULL){
        lista->first = funcionario;
        lista->last = funcionario;
    } else {
        funcionario->next = lista->first;
        lista->first->prev = funcionario;
        lista->first = funcionario;
    }
    
}

Employee *incluirElementosFinal(Sentinela *lista, Employee *funcionario) {
    if (lista->first == NULL){
        lista->first = funcionario;
        lista->last = funcionario;
    } else {
        funcionario->prev = lista->last;
        lista->last->next = funcionario;
        lista->last = funcionario;
    }
    
}

Employee *incluirElementosMeio(Sentinela *lista, Employee *funcionario, int id) {
    Employee *aux;
    if (lista->first == NULL){
        lista->first = funcionario;
        lista->last = funcionario;
    } else {
        for (aux = lista->first; aux!=NULL; aux = aux->next){
            if (id == aux->id){ // VERIFICAR SE AUX APONTA PARA O PRIMEIRO
                funcionario->next = aux;
                funcionario->prev = aux->prev;
                aux->prev->next = funcionario;
                aux->prev = funcionario;
            }
        }
    }
    
}


void excluirElemento(Sentinela *lista, int id){
    Employee *aux;
    for (aux = lista->first; aux != NULL; aux = aux->next){
        if (aux->id == id){
            if (aux == lista->first){
                lista->first = aux->next;
                lista->first->prev = NULL;
            }else if (aux == lista->last){
                lista->last = aux->prev;
                lista->last->next = NULL;
            }else{
                aux->prev = aux->next->prev;
                aux->next->prev = aux->prev;
            }
            if (aux != NULL) free(aux);
            break;
        }
    }
   
}


void imprimirLista(Sentinela *lista) {
    Employee *atual = lista->first;
    printf("Impressão normal\n");
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

void impressaoInverso(Sentinela *lista) {
    Employee *atual = lista->last;
    printf("Impressão inverso\n");
    while (atual != NULL) {
        printf("-=====================================================-\n");
        printf("ID: %d\n", atual->id);
        printf("Nome: %s\n", atual->name);
        printf("Renda: %.2lf\n", atual->income);
        printf("Data de Nascimento: %d/%d/%d\n", atual->dbirth.dia, atual->dbirth.mes, atual->dbirth.ano);
        printf("\n");
        printf("-=====================================================-\n");
        atual = atual->prev;
    }
}


void desalocarLista(Employee *first) {
    if (first == NULL) return;
    desalocarLista(first->next);
    free(first);
}


int main() {
    Sentinela lista;
    initialisation(&lista);
    // lista = initialisation(lista);  // Inicialmente, a lista está vazia

    Employee *funcionario;
   
    // Criar o primeiro funcionário
    // funcionario = criarEmployee(1, "John", 50000.0, 1990, 5, 15);

    // Adicionar um segundo funcionário
    funcionario = criarEmployee(2, "Angemy", 60000.0, 1985, 8, 25);
    incluirElementosFinal(&lista, funcionario);
    
    funcionario = criarEmployee(3, "Jane", 70000.0, 1685, 8, 55);
    incluirElementosFinal(&lista, funcionario);

    funcionario = criarEmployee(4, "Mireille", 7005400.0, 2685, 10, 3);
    incluirElementosComeco(&lista, funcionario);
    // // imprimirLista(first);

    funcionario = criarEmployee(5, "Midelta", 7005400.0, 2685, 11, 3);
    incluirElementosMeio(&lista, funcionario, 3);

    // funcionario = criarEmployee(5, "Patricia", 7005400.0, 2685, 11, 3);
    // first = incluirElementosPosId(first, funcionario, 4);

    // funcionario = criarEmployee(5, "Delva", 7005400.0, 2685, 11, 3);
    // first = incluirElementosAntId(first, funcionario, 1);
    // // Imprimir a lista de funcionários
    // imprimirLista(lista);
    // // imprimirListarecursivo(first);
    // // excluirElemento(first, 5);
    imprimirLista(&lista);
    excluirElemento(&lista, 3);
    impressaoInverso(&lista);
    return 0;
}
