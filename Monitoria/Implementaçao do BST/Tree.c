#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node {
    int valeur;
    struct node *left;
    struct node *right;
};
typedef struct node Node;

// Node *criaEmployee(int valeur, char name[], double income, int ano, int mes, int dia){

// }

Node *creerNoeud(int valeur) {
    Node *nouveauNoeud;
    nouveauNoeud = (Node *)malloc(sizeof(Node));
    nouveauNoeud->valeur = valeur;
    nouveauNoeud->left = NULL;
    nouveauNoeud->right = NULL;
    return nouveauNoeud; // Você esqueceu de retornar o ponteiro para o primeiro funcionário
}

Node *additionerNoeud(Node *raiz, Node *nouveauNoeud) {
    if (raiz == NULL){
        return nouveauNoeud;
    } else {
        if (raiz->valeur >= nouveauNoeud->valeur){
            raiz->left = additionerNoeud(raiz->left, nouveauNoeud);
        } else {
            raiz->right = additionerNoeud(raiz->right, nouveauNoeud);
        }
    }
    return raiz;
    
}


void imprimirTreePreOrder(Node *raiz) {
    if (raiz == NULL) return;

    printf("%d ", raiz->valeur);
    imprimirTreePreOrder(raiz->left);
    imprimirTreePreOrder(raiz->right);
    
}

void imprimirTreeInOrder(Node *raiz) {
    if (raiz == NULL) return;

    imprimirTreeInOrder(raiz->left);
    printf("%d ", raiz->valeur);
    imprimirTreeInOrder(raiz->right);
}

void imprimirTreePosOrder(Node *raiz) {
   if (raiz == NULL) return;
    
    printf("%d ", raiz->valeur);
    imprimirTreePosOrder(raiz->right);
    imprimirTreePosOrder(raiz->left);
}

void imprimerArvore(Node *raiz, int nivel) {
    if (raiz == NULL) {
        return;
    }

    // Incrementa o nível antes de imprimir o nó atual
    nivel += 1;

    // Recursivamente imprime a subárvore direita
    imprimerArvore(raiz->right, nivel);

    // Imprime o nó atual com indentação proporcional ao nível
    for (int i = 0; i < nivel - 1; i++) {
        printf("    ");
    }
    printf("%d\n", raiz->valeur);

    // Recursivamente imprime a subárvore esquerda
    imprimerArvore(raiz->left, nivel);
}
int main() {
    Node *tree = NULL;

    tree = creerNoeud(30);
    tree = additionerNoeud(tree, creerNoeud(51));
    tree = additionerNoeud(tree, creerNoeud(14));
    tree = additionerNoeud(tree, creerNoeud(43));
    tree = additionerNoeud(tree, creerNoeud(82));
    tree = additionerNoeud(tree, creerNoeud(21));
    tree = additionerNoeud(tree, creerNoeud(9));
    tree = additionerNoeud(tree, creerNoeud(3));
    tree = additionerNoeud(tree, creerNoeud(27));
    tree = additionerNoeud(tree, creerNoeud(99));

    imprimerArvore(tree, 0);
    printf("Impressão de pre-order  🤷🏾🤷🏾🤷🏾\n");
    imprimirTreePreOrder(tree);     

    printf("\n\nImpressão de in-order🤷🏾🤷🏾🤷🏾\n");
    imprimirTreeInOrder(tree);    
      
    printf("\n\nImpressão de pos-order🤷🏾🤷🏾🤷🏾\n");
    imprimirTreePosOrder(tree);
    printf("\n");

    return 0;
}
