#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct elemStack {
    char lettre[1];
    struct elemStack *next;
};
typedef struct elemStack ElemStack;

typedef struct {		
    ElemStack *top;	
} Stack;	

void initStack(Stack *stack) {
    stack->top = NULL;
}

ElemStack *criarEmployee(char lettre[1]) {
    ElemStack *mot;
    mot = (ElemStack *)malloc(sizeof(ElemStack));
    strcpy(mot->lettre, lettre);
    mot->next = NULL;
    return mot; 
}

ElemStack *push(Stack *stack, ElemStack *mot) {
    if (stack->top == NULL){
        stack->top = mot;
    } else {
        mot->next = stack->top;
        stack->top = mot;
    }   
}


ElemStack *pop(Stack *stack){
    ElemStack *aux, *previous;
    if (stack->top == NULL) return;
    

}


void imprimirLista(ElemStack *stack) {
    ElemStack *atual = stack;
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


void desalocarLista(ElemStack *stack) {
    if (stack == NULL) return;
    desalocarLista(stack->next);
    free(stack);
}

ElemStack *diferencaList(ElemStack *lista1, ElemStack *lista2){
    ElemStack *aux, *aux2, *lista3 = NULL, *elementoLista3;
    int diff;
    aux2 = lista2;
    for (aux = lista1; aux != NULL; aux = aux->next){
        diff = aux2->id - aux->id;
        elementoLista3 = criarEmployee(diff);
        lista3 = push(lista3, elementoLista3);
        aux2 = aux2->next;
    }
    return lista3;
}





int main() {
    ElemStack *stack = NULL, *lista2 = NULL, *lista3, *lista4; // Inicialmente, a lista está vazia
    ElemStack *mot;
    
    // Criar o primeiro funcionário
    stack = criarEmployee(6);

    // Adicionar um segundo funcionário

    mot = criarEmployee(6);
    stack = push(stack, mot);

    mot = criarEmployee(8);
    stack = push(stack, mot);
    // imprimirLista(stack);

    mot = criarEmployee(6);
    stack = incluirElementosPosId(stack, mot, 1);

    lista2 = criarEmployee(7);

    // Adicionar um segundo funcionário

    mot = criarEmployee(2);
    lista2 = push(lista2, mot);

    mot = criarEmployee(8);
    lista2 = push(lista2, mot);
    // imprimirLista(stack);

    mot = criarEmployee(6);
    lista2 = incluirElementosPosId(lista2, mot, 2);

    imprimirLista(stack);
    imprimirLista(lista2);
    printf("Interseção entre lista 1 e 2 😏:\n");
    lista3 = intersectionList(stack, lista2);
    imprimirLista(lista3);
    printf("Union entre lista 1 e 2 😏:\n");
    lista4 = UnionList(stack, lista2);
    imprimirLista(lista4);
    return 0;
}
