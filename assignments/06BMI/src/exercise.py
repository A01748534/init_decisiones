"""""
Índice de masa corporal;
Dame el peso;
recibo el peso;
Damel la altura;
recibo la altura;
if(peso<=0 or altura <=0 )
{
  print(Revisa tus datos, alguno de ellos es erróneo);
}
else;
sacar IMC;
IMC=peso/altura**2;
recibo resultado;
if(índice>0 and índice<20)
{
imprimir("PESO BAJO");
}
else if(índice>=20 and índice< 25)
{
  imprimir ("NORMAL");
}
else if (índice>=25 and índice< 30)
{
  imprimir ("SOBREPESO");
}
else if (índice>= 30 and índice < 40)
{
  imprimir ("OBESIDAD");
}
else if (índice >= 40)
{
  imprimir ("OBESIDAD MORBIDA")
}
"""
def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))
    if  peso<=0 or altura <=0 :
        
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:

        índice= peso/altura**2

        if índice>0 and índice<20:
            print("PESO BAJO")
        elif índice>=20 and índice< 25:
            print("NORMAL")
        elif índice>=25 and índice< 30:
            print("SOBREPESO")
        elif índice>= 30 and índice < 40:
            print("OBESIDAD")
        elif índice >= 40:
            print 
    

if __name__=='__main__':
    main()