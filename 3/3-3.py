import random, time

ball = 100000000
superduper = 1

start = time.time()

while True:
    dd = float(superduper / ball) * 100
    
    print(superduper, "/", ball)
    print(dd, "%")
    
    if ball == 0 or superduper == 0:
        print("ball ran out!")
        end = time.time()
        print(round(end - start, 2), 'seconds')
        break
    
    numnum = random.randint(1, ball)
    if numnum <= superduper:
        print("Success")
        superduper -= 1
        ball -= 1
    else:
        print("Failed")
        ball -= 1
