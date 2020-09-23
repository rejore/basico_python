import hashlib
import random

def generar_cadena():
    CHOICE = "abcdefghijklmn"
    TAMAÑO = 6
    COUNT = 0
    cadena = []
    while COUNT<=TAMAÑO:
        caracter = random.choice(CHOICE)
        cadena.append(caracter)
        COUNT = COUNT + 1
    return "".join(cadena) 


def run(cadena):
    h = hashlib.sha256(cadena.encode('utf-8')).hexdigest()
    return h


if __name__ == "__main__":
    print(run(generar_cadena()))
    
