def run(numero):
    bandera = False
    counter = 0
    if numero < 2:
        bandera = False
    elif numero == 2:
        bandera = True
    elif numero>2:
        for i in range(1,numero+1):
            if numero%i == 0:
                counter = counter + 1
        if counter > 2:
            bandera = False
        else:
            bandera = True             
    else:
        bandera = True
    return bandera    
      
               
    
if __name__ == "__main__":
    numero = int(input("ingresa numero :"))
    if run(numero):
        print("el {} es primo".format(numero))
    else:
        print("el {} no es primo".format(numero))    
