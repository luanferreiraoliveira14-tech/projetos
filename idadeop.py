import os
os.system('cls') 


id = input("Qual é a sua idade: ")


def oi ():
    if id>=18:
        print("voce é maior de idade")
    elif id < 0:
        print("idade invalida")    
    else:
        print("voce é menor de idade")    


try:
    id = int(id)
    oi()
except ValueError:
     print("idade invalida") 
    


