import random
x=random.randint(1,100)
num=0
count=0

while num!=x:
    num=int(input("Enter Your Number: "))
    if(num==x):
      print(f"You Guessed {x} that is Right Number!")
      print("total guesses= ",count)
      
      break
    
    elif(num>x):
      print("Guess a lower number")
      count+=1

    elif(num<x):
        print("Guess a higher number")
        count+=1

with open("highscore.txt","r") as f:
    highscore=int(f.read())

if(count<highscore):
    print("Congrats! You have Broken the highscore!")
    with open("highscore.txt","w") as f:
     f.write(str(count))

