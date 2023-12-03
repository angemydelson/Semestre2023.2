#include <stdio.h>
#include <stdlib.h>

struct node {
    int valeur;
    struct node *left;
    struct node *right;
    int height;  // Adicionamos uma altura ao nó
};
typedef struct node Node;

// Função auxiliar para obter a altura de um nó (retorna 0 para nós nulos)
// int getHeight(Node *n) {
//     return (n == NULL) ? 0 : n->height;
// }

int getHeight(Node *n) {
    if (n == NULL) {
        return 0;
    } else {
        return n->height;
    }
}

// Função auxiliar para calcular o fator de equilíbrio de um nó
int getBalance(Node *n) {
    if (n == NULL) return 0;
    return getHeight(n->left) - getHeight(n->right);
}

// Função auxiliar para atualizar a altura de um nó com base nas alturas dos filhos
// void updateHeight(Node *n) {
//     int leftHeight = getHeight(n->left);
//     int rightHeight = getHeight(n->right);
//     n->height = (leftHeight > rightHeight ? leftHeight : rightHeight) + 1;
// }

void updateHeight(Node *n) {
    int leftHeight = 0;
    int rightHeight = 0;

    if (n->left != NULL) {
        leftHeight = n->left->height;
    }

    if (n->right != NULL) {
        rightHeight = n->right->height;
    }

    if (leftHeight > rightHeight) {
        n->height = leftHeight + 1;
    } else {
        n->height = rightHeight + 1;
    }
}


// Função para realizar uma rotação simples à direita (Rotação Direita)
Node *rotateRight(Node *y) {
    Node *x = y->left;
    Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    // Atualiza as alturas
    updateHeight(y);
    updateHeight(x);

    return x;
}

// Função para realizar uma rotação simples à esquerda (Rotação Esquerda)
Node *rotateLeft(Node *x) {
    Node *y = x->right;
    Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    // Atualiza as alturas
    updateHeight(x);
    updateHeight(y);

    return y;
}

Node *creerNoeud(int valeur) {
    Node *nouveauNoeud;
    nouveauNoeud = (Node *)malloc(sizeof(Node));
    nouveauNoeud->valeur = valeur;
    nouveauNoeud->left = NULL;
    nouveauNoeud->right = NULL;
    nouveauNoeud->height = 1; // Inicializa a altura como 1 para o novo nó
    return nouveauNoeud;
}

Node *additionerNoeud(Node *raiz, Node *nouveauNoeud) {
    int valeur = nouveauNoeud->valeur;
    // Passo de inserção normal
    if (raiz == NULL) {
        return creerNoeud(valeur);
    }

    if (valeur < raiz->valeur) {
        raiz->left = additionerNoeud(raiz->left, valeur);
    } else if (valeur > raiz->valeur) {
        raiz->right = additionerNoeud(raiz->right, valeur);
    } else {
        // Duplicatas não são permitidas, então, se a chave já existe, não fazemos nada
        return raiz;
    }

    // Atualiza a altura do nó atual
    updateHeight(raiz);

    // Obtém o fator de equilíbrio deste nó
    int balance = getBalance(raiz);

    // Realiza as rotações, se necessário
    if (balance > 1 && valeur < raiz->left->valeur) {
        return rotateRight(raiz);
    }
    if (balance < -1 && valeur > raiz->right->valeur) {
        return rotateLeft(raiz);
    }
    if (balance > 1 && valeur > raiz->left->valeur) {
        raiz->left = rotateLeft(raiz->left);
        return rotateRight(raiz);
    }
    if (balance < -1 && valeur < raiz->right->valeur) {
        raiz->right = rotateRight(raiz->right);
        return rotateLeft(raiz);
    }

    return raiz;
}

Node *deleteNode(Node *root, int value) {
    // Passo de exclusão normal
    if (root == NULL) {
        return root;
    }

    if (value < root->valeur) {
        root->left = deleteNode(root->left, value);
    } else if (value > root->valeur) {
        root->right = deleteNode(root->right, value);
    } else {
        // Nó a ser removido encontrado

        // Caso 1: Nó com um ou nenhum filho
        if (root->left == NULL || root->right == NULL) {
            Node *temp = root->left ? root->left : root->right;

            // Caso 1a: Nenhum filho
            if (temp == NULL) {
                temp = root;
                root = NULL;
            } else { // Caso 1b: Um filho
                *root = *temp; // Copia os conteúdos do filho para o nó a ser removido
            }

            free(temp);
        } else {
            // Caso 2: Nó com dois filhos
            Node *temp = minValueNode(root->right); // Encontra o nó com o menor valor na subárvore direita

            // Copia o valor do nó encontrado para este nó
            root->valeur = temp->valeur;

            // Remove o nó encontrado
            root->right = deleteNode(root->right, temp->valeur);
        }
    }

    // Se a árvore tinha apenas um nó, então retorna a árvore atualizada
    if (root == NULL) {
        return root;
    }

    // Atualiza a altura do nó atual
    updateHeight(root);

    // Obtém o fator de equilíbrio deste nó
    int balance = getBalance(root);

    // Realiza as rotações, se necessário
    if (balance > 1 && getBalance(root->left) >= 0) {
        return rotateRight(root);
    }
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }
    if (balance < -1 && getBalance(root->right) <= 0) {
        return rotateLeft(root);
    }
    if (balance < -1 && getBalance(root->right) > 0) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}

// Função auxiliar para encontrar o nó com o valor mínimo em uma subárvore
Node *minValueNode(Node *node) {
    Node *current = node;

    // Percorre a árvore para encontrar o nó com o valor mínimo
    while (current->left != NULL) {
        current = current->left;
    }

    return current;
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
