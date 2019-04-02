year=int(input("Ingresa un año y te dire si es bisiesto o no"))
if year%4==0 or year%400==0 :
       print("El año es bisiesto")
else:
    print("El año no es bisiesto")