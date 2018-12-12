import unittest

def fizz_buzz():
	lista = criar_lista()
	for numero in lista:
		if check_fizz_buzz(numero):
			print("FizzBuzz")
		elif check_buzz(numero):
			print("Buzz")
		elif check_fizz(numero):
			print("Fizz")
		else print(numero)			

def criar_lista():
	lista = []
	for numero in range(1,100):
		lista.append(numero)
	return lista	

def check_fizz(numero):
	if numero %3 == 0:
	return True

def check_buzz(numero):
	if numero %5 == 0:
	return True	

def check_fizz_buzz(numero):
	if numero %3 == 0 and numero%5 == 0:
	return True		

class TestFizzBuzz(unittest.TestCase):

	def test_criar_lista(self):
		self.assertEqual(len(criar_lista)), 100)

	def test_Fizz_3(self):
		self.assertEqual(check_fizz(3), True)

	def test_Fizz_9(self):
		self.assertEqual(check_fizz(9), True)

	def teste_Buzz_5(self):
		self.assertEqual(check_buzz(5), True)	