nota_final = float(input("ingrese nota"))
if  nota_final < 3.0 :
    print ("Insuficiente")
elif 3.5 >= nota_final >= 3.0 :
    print("Aceptable")
elif 3.5 < nota_final <= 4.0 :
    print ("Sobresaliente")
elif 4.0 < nota_final <= 5.0 :
    print ("Excelente")
else:
    print ("Esta nota no existe")