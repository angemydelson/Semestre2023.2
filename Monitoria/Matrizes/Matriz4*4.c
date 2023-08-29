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

    for (int i = 0; i < 4; i++){
        for (int j = 0; j< 4; j++){
            if (i == j){
                printf("%d ", matriz[i][j]);
            }
            
        }
        printf("\n");
    }


    return 0;
}

