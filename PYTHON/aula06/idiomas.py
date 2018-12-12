import unittest

# dicionário de idiomas

esp = {1: 'uno', 2: 'dos', 3: 'tres', 4: 'quatro', 5: 'cinco'}
ing = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
por = {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco'}

linguas = {'espanhol' : esp, 'inglês' : ing, 'português' "por"}

def check_numero(numero):
	return int == type(numero)

def check_lingua(lingua):
	return lingua in linguas	


class TestFizzBuzz(unittest.TestCase):

	def test_valida_numero(self):
		self.assertTrue(check_numero(2))

	def teste_valida_lingua(self):
		self.assertTrue(check_lingua('espanhol'))

	def teste_numero_inexistente(self):
		self.assertFalse(check_e)		

if __name__ == '__main__':
	unittest.main()	