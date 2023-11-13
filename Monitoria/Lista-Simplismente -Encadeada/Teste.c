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

int existeElemento(Employee *lista, int valor) {
    Employee *aux;
    for (aux = lista; aux != NULL; aux = aux->next) {
        if (aux->id == valor) {
            return 1; // O elemento já existe na lista
        }
    }
    return 0; // O elemento não foi encontrado na lista
}

Employee *intersectionList(Employee *lista1, Employee *lista2){
    Employee *aux, *aux2, *lista3 = NULL, *elementoLista3;
    int valor, verificador;
    aux2 = lista2;
    for (aux = lista1; aux != NULL; aux = aux->next){
        for (aux2 = lista2; aux2 != NULL; aux2 = aux2->next){
            if (aux->id == aux2->id){
                verificador = existeElemento(lista3, aux->id);
                if(verificador == 0){
                    valor = aux->id;
                    elementoLista3 = criarEmployee(valor);
                    lista3 = incluirElementosFim(lista3, elementoLista3);
                    break;
                }
                
            }
        }
    }
    return lista3;
}



Employee *UnionList(Employee *lista1, Employee *lista2){
    Employee *aux, *aux2, *lista3 = NULL, *lista4, *elementoLista3;
    int valor, verificador;
    for (aux = lista1; aux != NULL; aux = aux->next){
        verificador = existeElemento(lista3, aux->id);
        if (verificador == 0){
            elementoLista3 = criarEmployee(aux->id);
            lista3 = incluirElementosFim(lista3, elementoLista3);
        }
        
    }
   for (aux = lista2; aux != NULL; aux = aux->next){
        verificador = existeElemento(lista3, aux->id);
        if (verificador == 0){
            elementoLista3 = criarEmployee(aux->id);
            lista3 = incluirElementosFim(lista3, elementoLista3);
        }
        
    }
   
    return lista3;
}
int main() {
    Employee *first = NULL, *lista2 = NULL, *lista3, *lista4; // Inicialmente, a lista está vazia
    Employee *funcionario;
    
    // Criar o primeiro funcionário
    first = criarEmployee(6);

    // Adicionar um segundo funcionário

    funcionario = criarEmployee(6);
    first = incluirElementosFim(first, funcionario);

    funcionario = criarEmployee(8);
    first = incluirElementosFim(first, funcionario);
    // imprimirLista(first);

    funcionario = criarEmployee(6);
    first = incluirElementosPosId(first, funcionario, 1);

    lista2 = criarEmployee(7);

    // Adicionar um segundo funcionário

    funcionario = criarEmployee(2);
    lista2 = incluirElementosFim(lista2, funcionario);

    funcionario = criarEmployee(8);
    lista2 = incluirElementosFim(lista2, funcionario);
    // imprimirLista(first);

    funcionario = criarEmployee(6);
    lista2 = incluirElementosPosId(lista2, funcionario, 2);

    imprimirLista(first);
    imprimirLista(lista2);
    printf("Interseção entre lista 1 e 2 😏:\n");
    lista3 = intersectionList(first, lista2);
    imprimirLista(lista3);
    printf("Union entre lista 1 e 2 😏:\n");
    lista4 = UnionList(first, lista2);
    imprimirLista(lista4);
    return 0;
}
