import random
ball = 20
superduped = 5
while True:
    num = int(input("AAAAAAA  "))
    if num >= 1:
        print("wow")
        print(superduped, "/", ball)
        numnum = random.randint(1, ball)
        if ball == 0 or superduped == 0:
            print("ball ran out!")
            break
        elif numnum <= superduped:
            print("you got the thingy!")
            superduped -= 1
            ball -= 1
        elif numnum > superduped:
            print("you failed to get the thingy!")
            ball -= 1
        
        


