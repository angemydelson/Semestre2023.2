#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
    int ano;
    int mes;
    int dia;
} Data;

Data * setData(int ano, int mes, int dia){
    Data *data = (Data *)malloc(sizeof(Data));
    data->ano = ano;
    data->mes = mes;
    data->dia = dia;
    return data;
}
int main(){
    // int *p;
   
    // p = (int *)malloc(sizeof(int));
    // // int a = 10;
    // // p = &a;
    // // printf("%p\n", (void *)p);
    // *p = 22;
    // printf("%p\n", p);
    // printf("%d\n", *p);

    Data * data = setData(2000, 11, 10);
    printf("%d\n", data->ano);
    
    return 0;
}