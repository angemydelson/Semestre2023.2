#include <stdio.h>
#include <math.h>
int SomaVet( int n, int vetor[]){
    if (n == 0) return vetor[0];
    return vetor[n] + SomaVet(n - 1 , vetor);

}

int main(){
    int n = 4;
    int vetor[4] = {3, 5, 4, 6};
    printf("%d\n",SomaVet(n -1, vetor));
    return 0;
}