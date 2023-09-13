#include <stdio.h>

typedef struct {
    double numerador;
    double denomidador;
} Fraction;

Fraction setFraction(double num, double den){
    Fraction fraction;
    fraction.numerador = num;
    fraction.denomidador = den;
    return fraction;
    
}

Fraction MultFraction(Fraction fraction1, Fraction fraction2){
    Fraction fraction3;
    fraction3.numerador = fraction1.numerador * fraction2.numerador;
    fraction3.denomidador = fraction1.denomidador * fraction2.denomidador;
    return fraction3;
}

void printFraction(Fraction fraction){
    printf("Fraction: %.2lf / %.2lf\n", fraction.numerador, fraction.denomidador);
}

int main(){
    Fraction fraction1, fraction2, fraction3;
    fraction1 = setFraction(1, 2);
    fraction2 = setFraction(3, 4);
    fraction3 = MultFraction(fraction1, fraction2);
    printFraction(fraction1);
    printFraction(fraction2);
    printFraction(fraction3);

    return 0;
}