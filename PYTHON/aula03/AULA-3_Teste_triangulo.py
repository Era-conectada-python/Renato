lado1 = int(input("Digite a medida do lado 1: "))
lado2 = int(input("Digite a medida do lado 2: "))
lado3 = int(input("Digite a medida do lado 3: "))

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1:
    print("triangulo falso")
elif lado1 == lado2 == lado3:
    print("A medida" + lado1 + "Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isóceles")
else:
    print("Escaleno")
