import string
import time

text = "PLACEHOLDER... change"
texvi = "" 

for L in text:
    for i in string.printable:
        if i == L or L == " ":
            time.sleep(0.02)
            print(texvi+L)
            texvi += L
            break
        else:
            time.sleep(0.015)
            print(texvi+i)