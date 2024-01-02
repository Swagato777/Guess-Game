import random
jackpot=random.randint(1,100)
G=int(input("Guess any number"))
count=1
while G !=jackpot:
    if G<jackpot:
     print("Guess higher")
    else:
       print("Guess lower")
    G=int(input("Guess any number"))
    count=count+1

print("Correct Answer")
print("you took",count,"attempts")
