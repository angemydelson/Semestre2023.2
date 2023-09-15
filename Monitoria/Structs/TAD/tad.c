#include <stdio.h>
#include "tad.h"
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

Fraction AddFraction(Fraction fraction1, Fraction fraction2){
    Fraction fraction3;
    fraction3.denomidador = fraction1.denomidador * fraction2.denomidador;
    // if (fraction1.denomidador % fraction2.denomidador == 0 || fraction2.denomidador % fraction1.denomidador == 0){
        
    // }
    fraction3.numerador = ((fraction3.denomidador / fraction1.denomidador) * fraction1.numerador) + ((fraction3.denomidador / fraction2.denomidador) * fraction2.numerador);
    return fraction3;
}

Fraction SubFraction(Fraction fraction1, Fraction fraction2){
    Fraction fraction3;
    fraction3.denomidador = fraction1.denomidador * fraction2.denomidador;
    fraction3.numerador = ((fraction3.denomidador / fraction1.denomidador) * fraction1.numerador) - ((fraction3.denomidador / fraction2.denomidador) * fraction2.numerador);
    return fraction3;
}

// Fraction SubFraction(Fraction fraction1, Fraction fraction2){
//     Fraction fraction3;
//     fraction3.denomidador = fraction1.denomidador * fraction2.denomidador;
//     fraction3.numerador = ((fraction3.denomidador / fraction1.denomidador) * fraction1.numerador) - ((fraction3.denomidador / fraction2.denomidador) * fraction2.denomidador);
//     return fraction3;
// }

Fraction DivFraction(Fraction fraction1, Fraction fraction2){
    Fraction fraction3;
    fraction3.denomidador = fraction1.denomidador * fraction2.numerador;
    fraction3.numerador = fraction1.numerador * fraction2.denomidador;
    return fraction3;
}

void printFraction(Fraction fraction){
    printf("Fraction: %.2lf / %.2lf\n", fraction.numerador, fraction.denomidador);
}
