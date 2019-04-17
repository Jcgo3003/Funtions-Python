#include<stdio.h>

int main(void)
{
    int numero;
    printf("Dame un numero ");
    scanf("%d", &numero);

    while(numero != 0 ){
        printf("Dame otro numero ");
        scanf("%d", &numero);
    }
    return 0;
}
/* Este while si funciona en c pero si este mismo lo
    pero si este mismo lo hago en python no lo reconoce y
    explota

    Para que funcione se tiene que utilizar
    tu_variable = int(input('Dame un numero ')
    de otra manera python no sabra como interpretar la variable y
    no la interpretara correctamente haciendo un while infinito
    */