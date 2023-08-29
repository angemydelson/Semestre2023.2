# include <stdio.h>
int main(){
    int matriz[4][4];
    for (int i = 0; i < 4; i++){
        for (int j = 0; j< 4; j++){
            scanf("%d", &matriz[i][j]);
            
        }
        printf("\n");
    }


    for (int i = 0; i < 4; i++){
            for (int j = 0; j< 4; j++){
                printf("%d ", matriz[i][j]);
            }
            printf("\n");
    }

    int maior = 0;
    for (int i = 0; i < 4; i++){
            for (int j = 0; j< 4; j++){
                if (maior < matriz[i][j]){
                    maior = matriz[i][j];
                }
            }
    }

    printf("Maior valor é: %d\n", maior);


    return 0;
}

