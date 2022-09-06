x = int(input("Primer número: "))
y = int(input("Segundo número: "))
z = int(input("Tercer número: "))

n1 = min(x, y, z)
n3 = max(x, y, z)
n2 = (x + y + z) - n1 - n3
print("Orden mayor a menor: ", n3, n2, n1)