import random
import os
import time
os.system('cls')


opçoes = ["arroz","feijao","cachorro","carro", "nuvem", "livro", "janela", "abajur","caderno", "teclado", "espelho", "montanha", "cachorro","dinheiro", "floresta", "elefante", "bicicleta", "chocolate"]


while True:
   chave = random.choice(opçoes)
   letras = []
   chan=random.randint(6,7)
   for i in chave:
       letras.append("_")




   while chan > 0:
       os.system('cls')
       print(f"Você tem {chan} chances")
       print(letras)
       per = input("Seu palpite:  ").lower()
       ind = 0
       if per in chave:
           for i in chave:
               if i == per:
                letras[ind] = per
               ind +=1
       else:
           chan -= 1


       if "_" not in letras or per == chave:
           os.system('cls')
           print(f"A resposta era: {chave}" )
           print("Parabéns você ganhou :)")
           time.sleep(4)
           break
       elif chan <= 0:
           os.system('cls')
           print(f"A resposta era: {chave}" )
           print ("você perdeu :(")
           time.sleep(4)