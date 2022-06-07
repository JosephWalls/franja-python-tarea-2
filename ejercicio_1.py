# Funcion para contar el caracter contenido en la frase.
def contar_caracteres(letra,frase):
    # Se inicia el contador en 0
    contador = 0

    # Se recorre la cadena o frase letra por letra comparando cada una con la letra ingresada.
    for char in frase:
        if letra == char:
            contador +=1
    
    # Se retorna el contador
    return contador

def main():

    print("EJERCICIO 1\n")

    # Se lee la frase por teclado y se comprueba que tenga contenido.
    while True:
        frase = input('Escriba una frase: ')
        
        if len(frase) > 0:
            break

        print('Por favor, escribe una frase válida...')
    
    # Se lee la letra por teclado y se comprueba que tenga largo 1, es decir, sólo sea 1 caractér.
    while True:
        letra = input('Escriba una letra: ')

        if len(letra) == 1:
            break

        print('Ingrese sólo una letra!!!')

    print('La cantidad de letras "'+ letra +'" es: ',contar_caracteres(letra,frase))

if __name__ == "__main__":
    main()