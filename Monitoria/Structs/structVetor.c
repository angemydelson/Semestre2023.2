#include <stdio.h>
#include <string.h>
 typedef struct{
    char nome[50];
    float notas[3];
 } Aluno;
 
 Aluno setAluno(char nome[50], float notas[3]){
    Aluno aluno;
    strcpy(aluno.nome, nome);
    for (int i = 0; i<3; i++){
        aluno.notas[i] = notas[i];
    }
    
    return aluno;
 }

 Aluno mediaAluno( Aluno alunos[2]){
    float maior = 0;
    for (int i = 0; i < 2; i++ ){
        
        
    }
 }
void maiorNota(Aluno alunos[2]){
    float maior = 0 ;
    char nome[50]; 
    for (int i = 0; i < 2; i++){
        if (alunos[i].notas[0] > maior){
            maior = alunos[i].nome[0];
            strcpy(nome, alunos[i].nome);
        }
    }
    printf("O aluno com maior nota é: %s\n", nome);
    printf("A maior nota é: %f\n", maior);
    
}
 void printAlunos(Aluno alunos[2]){
    for (int i = 0; i < 2; i++ ){
        printf("Nome Aluno: %s\n", alunos[i].nome);
        for(int j = 0; j < 3; j++){
            printf("Nota %d: %.2f\n", j+1, alunos[i].notas[j]);
        }
    }
    
}
 int main(){
    char nome[50];
    float notas[3];
    Aluno alunos[2], aluno;
    for (int i = 0; i < 2; i++){
        printf("Nome aluno: ");
        scanf("%s", nome);
        for (int j = 0; j<3; j++){
            printf("Nota %d: ", j+1);
            scanf("%f", &notas[j]);
            
        }
        printf("\n");
        aluno = setAluno(nome, notas);
        alunos[i] = aluno;
        
    }
    
    printAlunos(alunos);
    maiorNota(alunos);
    
    return 0;
 }