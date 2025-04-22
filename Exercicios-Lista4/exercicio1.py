import math

def calculadora():
    numero = int(input("digite um numero"))
    raiz = math.sqrt(numero)
    seno = math.sin(numero)
    cosseno = math.cos(numero)
    logarit = math.log(numero)
    print(f"Os valores da raiz, seno, cosseno e log de {numero} são: \n")
    print(f"Raiz:\n {raiz} \n Seno: \n {seno} \n Cosseno: \n {cosseno}\n Log: \n {logarit}")

calculadora()