# Función encargada de calcular el total de la entrada con respecto a la edad.
def calcular_total(edad):
    if edad < 4:
        total = 0

    elif edad >=4 and edad < 18:
        total = 3500

    elif edad >= 18:
        total = 8000
    
    # Se retorna el total
    return total

def main():
    
    print('EJERCICIO 3:\n')
    
    while True:

        # Menú mostrado al usuario para calcular ingresar edad del cliente y calcular el total.
        print('Bienvenido a la sala de juegos:\n\n')
        print('1 -> Ingreso de cliente.\n')
        print('2 -> Salir.\n')

        # Se verifica que la opción sea válida.
        try:
            opcion = int(input('Ingrese el número correspondiente a la opción: '))
            print('\n')
        except:
            print('Ingrese una opción válida!!\n')
            continue

        if opcion == 1:
            
            # Se verifica que la edad sea válida.
            try:
                edad = int(input('Ingrese la edad del cliente: '))
            except:
                print('Ingrese una edad válida!!')

            # Se muestra por pantalla el total a pagar por el cliente.
            print('El total a pagar por la entrada es: $ '+str(calcular_total(edad))+'\n')

        # Se verifica la opción que permite salir del programa.
        elif opcion == 2:
            exit()

if __name__ == "__main__":
    main()