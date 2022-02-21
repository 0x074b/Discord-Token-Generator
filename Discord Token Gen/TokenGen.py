import random
import string
import sys
import os
from datetime import date
import datetime
print("(1Loop = 6TokenType)")
Loop = input("How many Tokens loop?: ")
print("\n\n")
count = 0
path = os.path.dirname(os.path.realpath(__file__))
while(int(count)<int(Loop)):
    Gen1 = random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+ random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    Gen2 = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    Gen3 = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    Gen4 = "MD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    Gen5 = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    Gen6 = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    f = open(path+"/"+str("output")+str("")+".txt","a")
    f.write(Gen1+"\n"+Gen2+"\n"+Gen3+"\n"+Gen4+"\n"+Gen5+"\n"+Gen6+"\n")
    print(Gen1)
    print(Gen2)
    print(Gen3)
    print(Gen4)
    print(Gen5)
    print(Gen6)
    count+=1
print("\n\nTokens has been save in output.txt")
