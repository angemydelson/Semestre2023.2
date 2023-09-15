#include <stdio.h>

typedef struct {
    double numerador;
    double denomidador;
} Fraction;

Fraction setFraction(double num, double den);
Fraction MultFraction(Fraction fraction1, Fraction fraction2);
Fraction AddFraction(Fraction fraction1, Fraction fraction2);
Fraction SubFraction(Fraction fraction1, Fraction fraction2);
Fraction DivFraction(Fraction fraction1, Fraction fraction2);
void printFraction(Fraction fraction);