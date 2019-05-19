from random import randint
import time
s = randint(1, 10)
p = randint(1, 10)
e = randint(1, 10)
c = randint(1, 10)
i = randint(1, 10)
a = randint(1, 10)
L = randint(1, 10)
try_again = True
while try_again:
    if s + p + e + c + i + a + L == 21:
        print("stats")
        print("strength", s)
        print("perception", p)
        print("endurance", e)
        print("charisma", c)
        print("intelligence", i)
        print("agility", a)
        print("luck", L)
        time.sleep(120000)
        try_again = False
    else:
        s = randint(1, 10)
        p = randint(1, 10)
        e = randint(1, 10)
        c = randint(1, 10)
        i = randint(1, 10)
        a = randint(1, 10)
        L = randint(1, 10)
        print(s + p + e + c + i + a + L)