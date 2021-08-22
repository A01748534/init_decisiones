def main():
    # Escribe el código adecuado para completar el programa
    year = int(input("Año:"))
    if year <=0:
        print("Dato incorrecto")
    else:

        if year % 4 != 0:
            print("False")
        else:
            if year % 4 == 0 and year %100 != 0:
                print("True")
            else:
                if year % 4 == 0 and year % 100 == 0 and year  % 400 != 0: 
	                print("False")
                else:
                    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
	                    print("True")  
            

if __name__ == '__main__':
    main()
