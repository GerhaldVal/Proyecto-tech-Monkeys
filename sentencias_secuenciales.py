
"""Este es un ejemplo de una sentencia secuencial de c++ a python
Normalmente en c++ para hacer un ejercicio del area de un cuadrado lo hacemos asi:
include <stdio.h>
int main(){
float base;
float altura;
float area;
printf("Ingrese la base de su cuadrado");
scanf("%f",&base);
printf("Ingrese la altura de su cuadrado");
scanf("%f",&altura);
area = base * altura;
printf( "El area de su cuadrado es:", area);
 return 0;
}
Como se ve, es muy extenso, sin embargo el codigo de python se hace mucho mas versatil y corto
Aqui va el mismo ejemplo: """

base = float(input("Ingrese la base de su cuadrado"))
altura = float(input("Ingrese la altura de su cuadrado"))
area = base * altura
print("El area de su cuadrado es:")
print(area)
