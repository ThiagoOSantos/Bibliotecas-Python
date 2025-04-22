
# import math - metodo de import de bibliotecas de funções no python 
'''
def operacoes_matematicas():
    numero = float(input("Digite um numero: \n"))
    raiz = math.sqrt(numero) - tipo de função de raiz
    potencia = math.pow(numero, 2) - tipo de função de exponenciação

    print("A raiz quadrada do número é: \n", raiz)
    print("A potência do numero é: \n", potencia)

operacoes_matematicas()
'''
'''
import random #biblioteca de numeros aleatorios 

def numero_da_sorte():
    print("Vamos sorter um número de 1 até 10 \n")
    numero = random.randint(1,60) #função dentro da biblioteca numeros aleatorios q chama um numero aleatorio do tipo inteiro, com intervalo específico(45, 40, 20, 22, 31, 33)
    print("O número da sorte é: \n", numero)

numero_da_sorte()
'''

from datetime import datetime

def mostrar_datahora():
    agora = datetime.now()
    print("A dada e hora de agora é: \n")
    print(agora.strftime("%d/%m/%Y %H:%M:%S"))

mostrar_datahora()