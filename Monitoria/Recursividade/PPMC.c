#include <stdio.h>

int ppmc(int n, int m){
    if (n == 0) return m;
    return ppmc(m % n, n);
}

int main(){
    printf("%d\n",ppmc(18, 6));
    return 0;
}