def esPalindromo(texto): #Función que verifica si la cadena de texto es un palíndromo
   
    # Elimina espacios al principio y al final, espacios dentro del texto y convierte a minúsculas
    texto = texto.strip().replace(" ", "").lower()

    # Verifica si no se ha introducido texto o solo se han introducido números
    if not texto or texto.isdigit():
        return None

    # Elimina caracteres no alfanuméricos
    texto = ''.join([char for char in texto if char.isalnum()])

    # Reemplaza letras mayúsculas y minúsculas que tengan acento
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    texto = texto.replace("Á", "a").replace("É", "e").replace("Í", "i").replace("Ó", "o").replace("Ú", "u")
    
    # Comprueba si la cadena introducida es igual a su reverso
    return texto == texto[::-1]

def principal(): #Función que pide al usuario una frase y verifica si es un palíndromo llamando a la función esPalindromo.
 
    while True:
        # Pide una frase al usuario
        cadena = input("Introduce una cadena de texto para comprobar si es palíndroma: ")

        # Utiliza la función esPalindromo para comprobar la frase
        resultado = esPalindromo(cadena)

        # Si el resultado no es válido, se repite el bucle
        if resultado is None:
            continue
        
        # Imprime si la frase es o no un palíndromo 
        if resultado:
            print("La cadena de texto introducida es un palíndromo.")
        else:
            print("La cadena de texto introducida no es un palíndromo.")
        
        # Sale del bucle después de una entrada válida
        break

# Asegura que la función principal() solo se ejecute cuando se ejecute directamente este archivo.
if __name__ == "__main__":
    principal()
