#include <stdio.h>
#include <math.h>
int Expoente( int b, int e){
    if (e == 0) return e;
    if (e == 1) return b;
    e = e - 1;
    return (b * Expoente(b, e));

}

int main(){
    printf("%d\n",Expoente(2, 5));
    return 0;
}