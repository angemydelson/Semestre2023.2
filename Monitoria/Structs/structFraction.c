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

int mmc(Fraction fraction)
{
    int div;
    if(b == 0) return a;
    else
     div = (a*b)/(mdc(a,b));
    return (div); 
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

int main(){
    Fraction fraction1, fraction2, fraction3;
    fraction1 = setFraction(1, 2);
    fraction2 = setFraction(3, 4);
    fraction3 = MultFraction(fraction1, fraction2);
    printFraction(fraction1);
    printFraction(fraction2);
    printFraction(fraction3);
    fraction3 = SubFraction(fraction1, fraction2);
    printFraction(fraction3);
    fraction3 = AddFraction(fraction1, fraction2);
    printFraction(fraction3);
    fraction3 = DivFraction(fraction1, fraction2);
    printFraction(fraction3);
   

    return 0;
}