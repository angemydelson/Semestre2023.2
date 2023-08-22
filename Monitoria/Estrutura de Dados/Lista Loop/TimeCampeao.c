#include <stdio.h>
#include <string.h>

int main (){
    int A = 0, B = 0, C = 0, D = 0, gols; 
    int pontos = 0, time1 = 0, time2 = 0;
    char time, aux1, aux2;
    for (; ;){
        time1 = 0, time2 = 0;
        for (int i = 1; i <3; i++){
            printf("Time%d: ", i);
            scanf(" %c", &time);
            if (time != 'A' && time != 'B' && time != 'C' &&  time != 'D'){
                pontos = 1;
                break;
            }
            printf("Gols: ");
            scanf("%d", &gols);
            if (i == 1){
                time1 += gols;
                aux1 = time;
            } else if (i == 2) {
                time2 += gols;
                aux2 = time;
            }
        }
        if (pontos == 1){
            break;
        }
        if (time1 > time2){
            if (aux1 == 'A'){
                A += 3;
            } else if (aux1 == 'B'){
                B += 3;
            } else if (aux1 == 'C'){
                C += 3;
            } else if (aux1 == 'D'){
                D += 3;
            }
        } else if( time1 < time2){
            if (aux2 == 'A'){
                A += 3;
            } else if (aux2 == 'B'){
                B += 3;
            } else if (aux2 == 'C'){
                C += 3;
            } else if (aux2 == 'D'){
                D += 3;
            }
        } else if (time1 == time2){
            if (aux1 == 'A'){
                A += 1;
            } else if (aux1 == 'B'){
                B += 1;
            } else if (aux1 == 'C'){
                C += 1;
            } else if (aux1 == 'D'){
                D += 1;
            }
            if (aux2 == 'A'){
                A += 1;
            } else if (aux2 == 'B'){
                B += 1;
            } else if (aux2 == 'C'){
                C += 1;
            } else if (aux2 == 'D'){
                D += 1;
            }
        }
        
            
    }
    printf("A: %d\n", A);
    printf("B: %d\n", B);
    printf("C: %d\n", C);
    printf("D: %d\n", D);  
        
        

    
    return 0;
}