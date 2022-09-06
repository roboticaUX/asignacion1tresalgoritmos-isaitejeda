def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Ingrese número a calcular su factorial : "))
print("El factorial es: " , factorial(n))