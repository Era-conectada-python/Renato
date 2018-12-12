
a = int(input("Digite o valor de A"))
b = int(input("Digite o valor de B"))
c = int(input("Digite o valor de C"))

def function(a,b,c):
	resultado = b**2 -4*a*c
	return resultado

def valida_positivo_negativo():
	if function(a,b,c) < 0:
		print("Número negativo")

	if	function(a,b,c) > 0:
		print("Número Positivo")

	if	function(a,b,c) == 0:
		print("BINGO")	

def count_d(resultado, d="9"):
	str(resultado)


print(function(a,b,c))

valida_positivo_negativo()			