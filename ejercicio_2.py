# Declaración de variable global PI con sólo 2 decimales.
pi = 3.14

# Función encargada de calcular el área del circulo.
def calcular_area_circulo(radio):
    
    area =  pi * radio**2
    
    # Se retorna el área redondeada a 2 decimales.
    return round(area,2)

def calcular_area_cilindro(radio,altura):

    # Se calcula el área del cilindro reutilizando la función para calcular el área del círculo.
    area = 2 * pi * radio * altura + 2 * calcular_area_circulo(radio)
    
    # Se retorna el área redondeada a 2 decimales.
    return round(area,2)

def main():
    
    print('EJERCICIO 2:\n')
    
    while True:

        # Menú mostrado al usuario para calcular áreas.
        print('1 -> Calcular área de un círculo.\n')
        print('2 -> Calcular área de un cilindro.\n')
        print('3 -> Salir.\n')


        # Se verifica que la opción sea válida.
        try:
            opcion = int(input('Ingrese el número correspondiente a la opción: '))
            print('\n')
        except:
            print('Ingrese una opción válida!!\n')
            continue

        if opcion == 1:
            
            # Se verifica que el radio ingresado sea válido.
            try:
                radio = float(input('Ingrese el valor del radio en cm: '))
            except:
                print('Ingrese un numero válido para el radio!!\n')

            # Se muestra por pantalla el resultado del cálculo del área del círculo.
            print('El área del circulo es: '+ str(calcular_area_circulo(radio)) +' cm\n')

        elif opcion == 2:
            
            # Se verifica que el radio ingresado sea válido.
            try:
                radio = float(input('Ingrese valor del radio en cm: '))
            except:
                print('Ingrese un numero válido para el radio!!\n')

            # Se verifica que la altura ingresada sea válida.
            try:
                altura = float(input('Ingrese valor de la altura en cm: '))
            except:
                print('Ingrese un numero válido para la altura!!\n')

            # Se muestra por pantalla el resultado del cálculo del área del cilindro.
            print('El área del cilindro es: '+ str(calcular_area_cilindro(radio,altura)) +' cm\n')
        
        # Se verifica la opción que permite salir del programa.
        elif opcion == 3:
            exit()

if __name__ == "__main__":
    main()