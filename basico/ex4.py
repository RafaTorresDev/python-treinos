#Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
#descrito, exiba a saudação apropriada. Ex. 
#Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

try: 
    hora = int(input("Digite somente a hora de agora (h): "))

    if hora >= 0 and hora <= 11:
        print("Tenha um ótmo dia!")

    elif hora >= 12 and hora <= 17:
        print("Tenha uma ótima tarde!!")

    elif hora >= 18 and hora <= 23:
        print("Tenha uma ótima noite!!!")

    else:
        print("Valor inválido")

except:
    print("Digite um valor inteiro!")

