#include <stdio.h>
#include "tad.h"

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