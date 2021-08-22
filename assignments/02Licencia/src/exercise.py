
from typing import Sized
def main():
    edad= int(input("Ingresa tu edad:"))
    identificacion =(input("¿Tienes identificación oficial?(s/n):" ))
   
    if edad>0 and identificacion == "s" or "n" :
        print("yay")
    elif edad<=0 and identificacion != "s" or "n" :
        print("respuesta incorrecta")

    

        
         
if __name__ == '__main__':
    main()
