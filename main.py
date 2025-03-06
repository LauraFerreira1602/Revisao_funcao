from utils.math_utils import *

ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))


print("Voce tem ",calcula_idade(ano_atual=ano_atual,ano_nascimento=ano_nascimento), "anos")
print("")


temperatura_celsios = int(input("Digite a temperatura em celsius: "))

temperatura_fahrenheit = exibir_fahrenheit(temperatura_celsios)
print('A temperatura em fahrenheit é', temperatura_fahrenheit)

temperatura_kelvin = exibir_kelvin(temperatura_celsios)
print('A temperatura em kelvin é', temperatura_kelvin)
print("")


menu_calculadora()
escolha_do_usuario()
print("")


peso = peso()
altura = altura()
imc = imc(peso, altura)
print('Seu imc é',round(imc, 2))



