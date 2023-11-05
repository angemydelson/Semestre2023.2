#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct employee {
    int id;
    struct employee *next;
};
typedef struct employee Employee;

// Employee *criaEmployee(int id, char name[], double income, int ano, int mes, int dia){

// }

Employee *criarEmployee(int id) {
    Employee *funcionario;
    funcionario = (Employee *)malloc(sizeof(Employee));
    funcionario->id = id;
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
    
    aux = aux2;
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
    printf("[");
    while (atual != NULL) {
        // printf("-=====================================================-\n");
        printf("%d ,", atual->id);
        // printf("\n");
        // printf("-=====================================================-\n");
        atual = atual->next;
    }
    printf("]\n");
}


void desalocarLista(Employee *first) {
    if (first == NULL) return;
    desalocarLista(first->next);
    free(first);
}

Employee *diferencaList(Employee *lista1, Employee *lista2){
    Employee *aux, *aux2, *lista3 = NULL, *elementoLista3;
    int diff;
    aux2 = lista2;
    for (aux = lista1; aux != NULL; aux = aux->next){
        diff = aux2->id - aux->id;
        elementoLista3 = criarEmployee(diff);
        lista3 = incluirElementosFim(lista3, elementoLista3);
        aux2 = aux2->next;
    }
    return lista3;
}

int main() {
    Employee *first = NULL, *lista2 = NULL, *lista3; // Inicialmente, a lista está vazia
    Employee *funcionario;
    
    // Criar o primeiro funcionário
    first = criarEmployee(1);

    // Adicionar um segundo funcionário

    funcionario = criarEmployee(2);
    first = incluirElementosFim(first, funcionario);

    funcionario = criarEmployee(3);
    first = incluirElementosFim(first, funcionario);
    // imprimirLista(first);

    funcionario = criarEmployee(4);
    first = incluirElementosPosId(first, funcionario, 3);

    lista2 = criarEmployee(2);

    // Adicionar um segundo funcionário

    funcionario = criarEmployee(7);
    lista2 = incluirElementosFim(lista2, funcionario);

    funcionario = criarEmployee(8);
    lista2 = incluirElementosFim(lista2, funcionario);
    // imprimirLista(first);

    funcionario = criarEmployee(6);
    lista2 = incluirElementosPosId(lista2, funcionario, 3);



    // funcionario = criarEmployee(5);
    // first = incluirElementosPosId(first, funcionario, 4);

    // funcionario = criarEmployee(5);
    // first = incluirElementosAntId(first, funcionario, 1);
    // Imprimir a lista de funcionários
    imprimirLista(first);
    imprimirLista(lista2);
    lista3 = diferencaList(first, lista2);
    imprimirLista(lista3);
    // imprimirListarecursivo(first);
    // excluirElemento(first, 5);
    // imprimirLista(first);

    return 0;
}
