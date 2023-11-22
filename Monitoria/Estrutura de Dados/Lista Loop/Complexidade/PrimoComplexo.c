#include <stdio.h>


void DominanteADireita(int L[], int n) {
    int maxRight = L[n - 1]; 
    int D[n]; 
    int dIndex = 0;

    D[dIndex++] = maxRight; 

    for (int i = n - 2; i >= 0; i--) {
        if (L[i] > maxRight) {
            maxRight = L[i];
            D[dIndex++] = maxRight;
        }
    }

    printf("Elementos dominantes à direita: ");
    for (int i = dIndex - 1; i >= 0; i--) {
        printf("%d ", D[i]);
    }
    printf("\n");
}

int main() {
    int L[] = {10, 9, 5, 13, 2, 7, 1, 8, 4, 6, 3};
    int n = sizeof(L) / sizeof(L[0]);

    DominanteADireita(L, n);

    return 0;
}
