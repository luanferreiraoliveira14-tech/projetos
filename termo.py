import random
import os
import time
opçoes = [
    "sagaz", "amago", "negro", "exito", "mexer", "termo", "senso", "nobre",
    "algoz", "afeto", "plena", "fazer", "assim", "vigor", "sutil", "poder",
    "ideia", "cerne", "moral", "justo", "muito", "honra", "sobre", "anexo",
    "etnia", "sonho", "tange", "lapso", "amigo", "expor", "haver", "tempo",
    "seara", "dengo", "pesar", "entao", "avido", "posse", "genro", "bocal",
    "coser", "causa", "dizer", "prole", "dever", "tenaz", "saber", "crivo",
    "graca", "apice", "animo", "brado", "comum", "sendo", "temor", "gleba",
    "assaz", "culto", "mundo", "pauta", "censo", "fugaz", "valha", "coisa",
    "forte", "denso", "vulgo", "pudor", "dogma", "regra", "louco", "criar",
    "jeito", "ordem", "atras", "impor", "saude", "banal", "clava", "mesmo", 
    "pifio", "pedir", "homem", "feliz", "todos", "apuro", "usura", "juizo", 
    "sabio", "servo", "prosa", "forma", "falar", "viril", "ontem", "manso"
    "aureo", "audio", "ideia", "coisa", "noite", "maior", "carne", "termo",
    "saude", "meias", "prato", "canto", "beato", "resto", "suave", "termo"
]
letras = ["_","_","_","_","_"]




while True:
    termo = list(random.choice(opçoes).upper())
    chances = random.randint(6,7)
    os.system('cls')

    while chances > 0:
        chances -=1
        
        per = list(input('Termo:  ').upper())

        ind = 0
        for l in termo:
            if termo[ind] == per[ind]:
                letras[ind] = '🟩'
            elif per[ind] in termo:
                letras[ind] = '🟨' 
            else:
                letras[ind] = '🟥' 
            ind +=1
        if per == termo:
            os.system('cls')
            print(letras)
            print(per)
            print("Parabéns você ganhou :)")
            time.sleep(4)
            break
        elif chances <= 0:
            os.system('cls')
            print(letras)
            print(termo)
            print ("você perdeu :(")
            time.sleep(4)
            break
        print(letras)
        print(f"| {per}")
        print(f"{chances} chances")