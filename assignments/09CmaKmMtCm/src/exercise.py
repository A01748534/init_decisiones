def main():
    # Escribe tu código abajo de esta línea
    cm = int(input("Introduce los cm:"))
    me=int(cm*1//100)
    km= int(cm*1//100)*1//1000
    if cm>=1 and cm<=99:
        print(str(cm)+"cm")
    elif cm>=100 and cm<=1000:
        print(str(me)+" m")
    elif cm>=1001:
        print ((str((km)+" km")))
if __name__ == '__main__':
    main()
