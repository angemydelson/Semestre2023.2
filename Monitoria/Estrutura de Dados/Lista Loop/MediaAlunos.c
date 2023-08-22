#include <stdio.h>

int main (){
    long matricula;
    int cont = 0;
    double notas, mediaAluno = 0, mediaTurma, somaTurma = 0;
    for (; ;){
        printf("Matricula do aluno: ");
        scanf("%ld", &matricula);
        if (matricula == 0){
            break;
        }
        for (int i = 1; i<11; i++){
            printf("Nota%d: ", i);
            scanf("%lf", &notas);
            mediaAluno += notas;
        
        }
        mediaAluno /= 10;
        cont++;
        somaTurma += mediaAluno;
        printf("%ld, média: %.2lf\n", matricula, mediaAluno);
    }
    somaTurma /= cont;
    printf("Média geral da turma é: %.2lf\n", somaTurma);
    
    return 0;
}