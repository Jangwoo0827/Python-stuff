import random, time
ball = 100000000
superduper = 1
while True: 
    dd = float(superduper/ball)*100
    if True:
        print(superduper, "/", ball)
        print(dd, "%")
        if ball == 0 or superduper == 0:
            print("ball ran out!")
            break
        numnum = random.randint(1, ball)
        if numnum <= superduper:
            print("Success")
            superduper -= 1
            ball -= 1
        elif numnum > superduper:
            print("Failed")
            ball -= 10
