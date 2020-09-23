import random

def run():
    aleatorio = random.randint(1,100)
    print(aleatorio)
    bandera= True
    while bandera:
        numero = int(input("Ingresa u numero entre 1 y 100 :"))
        if numero  < 1 or numero > 100:
            print("el numero no esta en el rango")
            bandera = False
            break;
        if numero == aleatorio:
            print("se encontro el numero")
            bandera = False
        elif numero > aleatorio:
            print("Ingresa un numero mas pequeño")
        else:
            print("Ingresa un numero mas grande")        



if __name__ == "__main__":
    run()