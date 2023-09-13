// #include <stdio.h>

// int main() {
//     char minhaString[] = "Olá, mundo!";
//     printf("%s\n", minhaString);
//     return 0;
// }


// #include <stdio.h>

// // Função para calcular o tamanho de uma string
// int tamanhoString(const char *str) {
//     int tamanho = 0;
//     while (str[tamanho] != '\0') {
//         tamanho++;
//     }
//     return tamanho;
// }

// int main() {
//     char minhaString[10];
//     scanf("%c" , minhaString);
//     int tamanho = tamanhoString(minhaString);
    
//     printf("Tamanho da string: %d\n", tamanho);
    
//     return 0;
// }





// #include <stdio.h>

// // Função para concatenar duas strings em um array prealocado
// void concatenarStrings(char *resultado, const char *str1, const char *str2) {
//     int i = 0;

//     // Copiar a primeira string para o resultado
//     while (str1[i] != '\0') {
//         resultado[i] = str1[i];
//         i++;
//     }

//     int j = 0;

//     // Adicionar a segunda string ao resultado
//     while (str2[j] != '\0') {
//         resultado[i + j] = str2[j];
//         j++;
//     }

//     resultado[i + j] = '\0'; // Adicionar o caractere nulo ao final
// }

// int main() {
//     const char *string1 = "Hello, ";
//     const char *string2 = "world!";
    
//     char resultado[50]; // Um array grande o suficiente para conter a concatenação
//     concatenarStrings(resultado, string1, string2);
    
//     printf("%s\n", resultado);
    
//     return 0;
// }


#include <stdio.h>
#include <string.h>

// Função para encontrar a interseção entre duas strings
void intersecaoStrings(const char *str1, const char *str2) {
    printf("Interseção: ");

    for (int i = 0; str1[i] != '\0'; i++) {
        for (int j = 0; str2[j] != '\0'; j++) {
            if (str1[i] == str2[j]) {
                printf("%c ", str1[i]);
                break;
            }
        }
    }

    printf("\n");
}

int main() {
    const char *string1 = "abcdef";
    const char *string2 = "cfghij";
    
    intersecaoStrings(string1, string2);
    
    return 0;
}
