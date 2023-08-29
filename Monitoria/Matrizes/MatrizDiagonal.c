# include <stdio.h>
int main(){
    int matriz[4][4];
    for (int i = 0; i < 4; i++){
        for (int j = 0; j< 4; j++){
            if (i == j){
                matriz[i][j] = 1;
            } else {
                matriz[i][j] = 0;
            }
            
        }
    }


    for (int i = 0; i < 4; i++){
            for (int j = 0; j< 4; j++){
                printf("%d ", matriz[i][j]);
            }
            printf("\n");
    }

    


    return 0;
}

