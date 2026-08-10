import random

escolhaC = ["pedra", "papel", "tesoura"]
sorteio = random.choice(escolhaC)
escolhaP = input("pedra papel tesoura")
print(escolhaC)
if escolhaC == escolhaP:
    print("EMPATE")

