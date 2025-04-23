import unittest  #Importar librería para Tests Unitarios
from charfun import esPalindromo  # Importar función esPalindromo desde charfun.py

class TestEsPalindromo(unittest.TestCase): #Creación de clase utilizando unittest
    
    def test_frase_palindromo(self): #Test que verifica si esta frase es un palíndromo
        resultado = esPalindromo("Anita lava la tina")
        self.assertEqual(resultado, True)

    def test_frase_no_palindromo(self): #Test que verifica si esta frase no es un palíndromo
        resultado = esPalindromo("Programación en Python")
        self.assertEqual(resultado, False)

    def test_caracteres_especiales(self): #Test para verificar que se manejan caracteres no alfanuméricos.
        resultado = esPalindromo("¡A mamá Roma le aviva el amor a mamá!")
        self.assertEqual(resultado, True)

    def test_acentos(self): #Test para verificar que se manejan los acentos.
        resultado = esPalindromo("Anita lavá la tina")
        self.assertEqual(resultado, True)


# Ejecución de las pruebas
if __name__ == "__main__":
    unittest.main()
