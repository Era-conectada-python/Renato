import random

arquivo = open("texto.txt", "r")

palavras = arquivo.readlines()

tam = len(palavras)

for index, palavra in enumerate(palavras):
	palavras[index] = palavra.replace("\n", "")


palavra = (palavras[random.randrange(tam)])

fim = False
palavra_completa = False
erros = 0
palavra_forca = []

for x in palavra:
	palavra_forca.append("_")

while not fim:
	letra = input("Digite uma letra: ")

	if len(letra) > 1 and letra != palavra:
		erros +=1
		print("Voce errou pela {0}å vez, tente de novo!")

	if letra in palavra:
		for index, l in enumerate(palavra):
			if l == letra:
				palavra_forca[index] = l
	
		print("A palavra é: {0}".format(" ".join(palavra_forca)))

		if not "_" in palavra_forca:
			palavra_completa = True
		

	if erros == 6:
		fim = True
		print("Game Over")
	elif palavra_completa:
		fim = True
		print("Ganhou!")			

