#include <stdio.h>

int pertenceFibonacci(int numero) {
    int a = 0, b = 1;

    if (numero == 0 || numero == 1) {
        return 1;
    }

    int c;
    while (b <= numero) {
        c = a + b;  
        a = b;      
        b = c;      

        if (b == numero) {  
            return 1;
        }
    }

    return 0;  
}

int main() {
    int numero;

    printf("Informe um numero: ");
    scanf("%d", &numero);

    if (pertenceFibonacci(numero)) {
        printf("%d pertence a sequência de Fibonacci.\n", numero);
    } else {
        printf("%d nao pertence a sequência de Fibonacci.\n", numero);
    }

    return 0;
}
