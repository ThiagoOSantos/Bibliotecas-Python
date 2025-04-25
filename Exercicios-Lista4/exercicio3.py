from datetime import datetime
def horadia():
    agora= datetime.now()
    print("Hoje é dia: \n", agora.strftime("%d/%m/%Y e agora são: %H:%M:%S"))
    reuniao = input("Deseja agendar algo?\n")
    print(reuniao, agora.strftime("%d/%m/%Y"))

horadia()