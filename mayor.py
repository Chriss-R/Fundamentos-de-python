#El mayor de 3
num1 = 24
num2 = 7
num3 = 14
num_mayor = 0
if num1 > num2:
    if num1 > num3:
        num_mayor=num1
    else:
        num_mayor = num3 
elif num2 > num3:
    num_mayor = num2
else:
    num_mayor = num3

print("El mayor es", num_mayor)