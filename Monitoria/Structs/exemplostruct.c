#include <stdio.h>
#include <string.h>

// struct tdata
// {
//     char nome[51];
//     int idade;
//     int media;
// }; 
// struct tdata data1 = {"Angemy", 10, 10}, data2;

typedef struct {
  int dia;
  int mes;
  int ano;
} Data;

Data controiData(int ano, int mes, int dia){
    Data data;
    data.ano = ano;
    data.mes = mes;
    data.dia = dia;
    return data;
}

int extraiData(Data data){
    return data.dia;
}

int diferençaDatas(Data data1, Data data2){
    if (data1.ano < data2.ano){
        return -1;
    } else if (data1.ano == data2.ano && data1.mes < data2.mes){
        return -1;
    } else if (data1.ano == data2.ano && data1.mes == data2.mes && data1.dia < data2.dia){
        return -1;
    } else if (data1.ano == data2.ano && data1.mes == data2.mes && data1.dia == data2.dia){
        return 0;
    } else {
        return 1;
    }
    
}

void printData(Data data){
    printf("Ano = %d \n", data.ano);
    printf("Mês = %d \n", data.mes);
    printf("Dia = %d \n\n", data.dia);
}
int main(){
    Data data1, data2, data3;
    data1 = controiData(2013, 11, 11);
    data2 = controiData(2013, 11, 9);
    data3 = controiData(2003, 4, 24);

    printData(data1);
    printData(data2);
    printData(data3);

    printf("O retorno é: %d \n", extraiData(data1));
    printf("O retorno é: %d \n", diferençaDatas(data1, data2));
    return 0;
}


