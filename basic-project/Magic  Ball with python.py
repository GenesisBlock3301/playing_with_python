import sys;import random;ans=True
count=0
while ans:
    question=input("enter your answer: ")
    answer=random.randint(1,8)
    print(answer)
    if question=="":
        count+=1
        if count==3:
            print("You are failed")
            sys.exit()
    elif int(question)==answer:
        print("You won the game")
        sys.exit()
    elif answer==1:
        print("It is certain")
    elif answer==2:
        print("outlook good")
    elif answer==3:
        print("you may rely on it")
    elif answer==4:
        print("aask again later")
    elif answer==5:
        print("Concentrate and ask again")
    elif answer==6:
        print("Reply hazy ,try again")
    elif answer==7:
        print("My reply is no")
    elif answer==8:
        print("My source say no")
    else:
        sys.exit()
