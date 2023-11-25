# Calculadora

print(".:CALCULADORA:.")
print("¿A que modo deseas ingresar?")

modo = int(input("[1]. Operaciones \n[#]. Hallar si es par o impar \n>>"))
if modo == 1:
    var1 = int(input("Ingresar el primer numero\n>>"))
    var2 = int(input("Ingesar el segundo numero\n>>"))
    oper = int(input("[1]. Suma\n[2]. Resta\n[3]. Multiplicacion\n[4]. Division\n[5]. Potencia\n"))
    if oper == 1:
        suma = var1 + var2
        print(f"El resultado de la suma es: {suma}")
    elif oper == 2:
        resta = var1 - var2
        print(f"El resultado de la resta es: {resta}")
    elif oper == 3:
        mult = var1 * var2
        print(f"El resultado de la multiplicacion es: {mult}")
    elif oper == 4:
        div = var1 / var2
        print(f"El resultado de la division es: {div}")
    elif oper == 5:
        pot = var1 ** var2
        print(f"El resultado de la potencia es: {pot}")
    
else:
    var = input("Ingresar un numero\n>>")
    if var % 2 == 0:
        print(f"El numero {var} es par")
    else:
        print(f"El numero {var} es impar")