def palindromo(palabra):
    return palabra == palabra[::-1]
    

if __name__ == "__main__":
    bandera = palindromo(input("ingrese palabra :"))
    if bandera == True:
        print("La palabra si es palindromo")
    else:
        print("La palabra no es palindromo")    