import os
import random
import time
os.system('clear')
id = -1
lis = ["🥰","😍","😁","🥺","😷","😺","🤠","😎","🧐","🤓","🎰"]
for _ in lis:
   id +=1
s1 = 0
s2 = 0
s3 = 0
slt1 = 0
slt2 = 0
slt3 = 0
din = 50.00
def dinhe():
   print(f"                                                    [${din}]")

dinhe()
print(input("COMEÇAR? [$0.50]"))
while True:
   wt = 0.04
   din = din - 0.50
   for _ in range(random.randint(10,50)):
      os.system('clear')
      s1 = random.randint(0,id)
      s2 = random.randint(0,id)
      s3 = random.randint(0,id)
      slt1 = lis[s1]
      slt2 = lis[s2]
      slt3 = lis[s3]
      dinhe()
      print(f" {lis[s1-1]}{lis[s2-1]}{lis[s3-1]} ")
      print(f"[{slt1}{slt2}{slt3}]")
      if s1 == id:
         s1 = -1
      if s2 == id:
         s2 = -1
      if s3 == id:
         s3 = -1
      print(f" {lis[s1+1]}{lis[s2+1]}{lis[s3+1]} ")  
      time.sleep(wt)
      wt += wt/5
      if wt > 0.85:
          break
   if slt1 == "🎰" and slt1 == slt2 and slt1 == slt3:
      print ("🎰🎰JACKPOT🎰🎰")
      print("🎉🎉$100.00🎉🎉")
      din = din + 100.00
   elif slt1 == slt2 and slt1 == slt3:
      print("⭐🌟GANHOU🌟⭐")
      print("🎉🎉$25.00🎉🎉")
      din = din + 25.00
   else:
      print ("😁QUASE😁")
      print("+$0.50🎉")
      din = din + 0.50
   print(input("DENOVO? [$0.50]"))
