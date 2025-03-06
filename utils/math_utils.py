print("Calcular a idade")
def calcula_idade(ano_atual, ano_nascimento):
    """
    Calcula a idade conforme o ano atual e ano de nascimento.

    :param ano_atual: O ano atual
    :param ano_nascimento: O ano de nascimento
    :return: A idade conforme ano de nascimento.
    """
    idade = ano_atual - ano_nascimento
    return idade



print("Conversor de Temperatura: digite a temperatura em Celcius e após isso retornaremos o valor convertido para Fahrenheit e Kelvin.")
def solicite_temperatura():
    temperatura_celsios = int(input("Digite a temperatura em celsius: "))
    return temperatura_celsios



def exibir_fahrenheit(temperatura_celsios):
    fahrenheit = temperatura_celsios * 1.8 + 32
    return fahrenheit



def exibir_kelvin(temperatura_celsios):
    kelvin = temperatura_celsios + 273
    return kelvin



def menu_calculadora():
    print("calculadora")
    print("1 - soma")
    print("2 - subitraçao")
    print("3 - multiplicaçao")
    print("4 - divisao")


def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def divisao(numero1, numero2):
    return numero1 / numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def resultado_funcoes(numero1, numero2):
    resultado_soma = soma(numero1, numero2)
    print(f"o resultado da soma foi {resultado_soma}")

    resultado_subtracao = (numero1, numero2)
    print(f"o resultado da subtracao foi {resultado_subtracao}")

    resultado_divisao = (numero1, numero2)
    print(f"o resultado da divisao foi {resultado_divisao}")

    resultado_multiplicacao = (numero1, numero2)
    print(f"o resultado da multiplicacao foi {resultado_multiplicacao}")


def escolha_do_usuario():
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        resultado_soma = soma(numero1(), numero2())
        print(f"o resultado da soma foi {resultado_soma}")

    elif escolha == 2:
        resultado_subtracao = subtracao(numero1(), numero2())
        print(f"o resultado da subtracao foi {resultado_subtracao}")

    elif escolha == 3:
        resultado_multiplicacao = multiplicacao(numero1(), numero2())
        print(f"o resultado da multiplicacao foi {resultado_multiplicacao}")

    elif escolha == 4:
        resultado_divisao = divisao(numero1(), numero2())
        print(f"o resultado da divisao foi {resultado_divisao}")

        return escolha


def numero1():
    numero1 = int(input("Digite o primeiro numero: "))
    return numero1

def numero2():
    numero2 = int(input("Digite o segundo numero: "))
    return numero2



print("Calculadora IMC: digite seu peso e altura para calcular o imc")
def imc(peso, altura):
    return peso / (altura * altura)


def peso():
    peso = float(input('Digite seu peso: '))
    return peso


def altura():
    altura = float(input('Qual a sua altura: '))
    return altura
