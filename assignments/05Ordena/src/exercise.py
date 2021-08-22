"""
Weordenar tres númeroos de  forma acendente;
Dame tres numeros;
recibo número x;
recibo número y;
recibo número z;
if (x menor que y and x menor que z and y menor que z)
{
imprimir 
x
y
z;
}
else if (y menor que x and y menor and xmenor que z and z mayor que x)
{
  imprimir
  y
  x
  z;
}
else if(z menor que x and z menor que y and x menor que y and y menor que x:)
{
  z
  x
  y;
}
else if(z menor que x and z menor que y and y menor que x and x mayor que y)
{
  imprimir
  z
  y
  x;
}
else if(y menor que x and y menor que z and z mqneor que x and x mayor que z)
{ 
imprimir
y
z
x;
}
else if(x menor que  y and x menor que  z and z menor que y and y mayor que z)
{
  imprimir
  x
  z
  y;
}
else if (x igual que y and x igual que z and zigual que y)
{
  imprimir
  x
  y
  z;
}
else if (xigual que y and x menor que z and z mayor que y)
{
  imprimir
  x
  y
  z;
}
else if(x igual que y and x mayor que z and z menor que y)
{ imprimir
z
x
y;
}
else if(y igual qeu x and y menor que z and z mayor que x)
{
  imprimir
  y
  x
  z;
}
else if(y igual que x and y mayor que z and z menor que x)
{
  imprimir
  z
  y
  x;
}
else if(z igual que x and z menor que y and y mayor que x)
{imprimir
  z
  x
  y;
}
else if(z igual que x and z mayor que y and y menor quex)
{imprimir
  y
  z
  x;
}
"""
def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    z = int(input("Ingresa el tercer número:"))
 
    if(x < y and x < z and y<z) and z>y:
    
        print(x)
        print(y)
        print(z)

        
    elif  y<x and y<z and x<z and z>x:
        print(y)
        print(x)
        print(z)    
        
    elif z<x and z<y and x<y and y>x:
    
        print(z)
        print(x)
        print(y)

    elif z<x and z<y and y<x and x>y:
        print(z)
        print(y)
        print(x)
            
        
    elif  y<x and y<z and z<x and x>z:
        print(y)
        print(z)
        print(x)
        
    elif x < y and x < z and z<y and y>z:
        print(x)
        print(z)
        print(y)
        
    elif x==y and x==z and z==y:
        print(x)
        print(y)
        print(z)
        
        
    elif x==y and x<z and z>y:
        print(x)
        print(y)
        print(z)
        
    elif x==y and x>z and z<y:
        print(z)
        print(x)
        print(y)
        
    elif y==x and y<z and z>x:
        print(y)
        print(x)
        print(z)
        
    elif y==x and y>z and z<x:
        print(z)
        print(y)
        print(x)

    
    elif z==x and z<y and y>x:
        print(z)
        print(x)
        print(y)
    
    elif z==x and z>y and y<x:
        print(y)
        print(z)
        print(x)
    
if __name__=='__main__':
    main()
