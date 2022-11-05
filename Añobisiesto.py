year=int(input("Ingresa un año y te dire si es bisiesto o no"))
if year%400==0 and year%100==0:
       print("El año es bisiesto")
elif year%4==0 and year%100!=0:
       print("El año es bisiesto")
else:
    print("El año no es bisiesto")
