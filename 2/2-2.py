import time, random
ll = str()
while True:
    for l in range(random.randint(2, 5)):
        llll = random.randint(1, 100)
        if llll > 5:
            for i in range(random.randint(1, 7)):
                for k in range(i):
                    ll += "0"
                print(ll)
                time.sleep(0.1)
                ll = str()
        elif llll < 5:
            for i in range(random.randint(1, 1000)):
                for k in range(i):
                    ll += "0"
                print(ll)
                time.sleep(0.001)
                ll = str()
                