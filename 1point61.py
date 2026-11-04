#UNFINISHED
from transformation import *
try:
    list = ['A)', 'Б)', 'B)', 'Г)', 'Д)', 'Е)', 'Ж)', '3)', 'И)', 'K)', 'Л)']
    print('A)a^4, Б)a^6, B)a^7, Г)a^8, Д)a^9, Е)a^10, Ж)a^13, 3)a^15, И)a^21, K)a^28, Л)a^64')
    permx = transform(float(input('Insert a number: ')))
    x = permx
    x*=x
    x*=x
    print(list[0], x)
    x = permx
    x*=x
    x*=permx
    x*=x
    print(list[1], x)
    x = permx
    x*=x
    x*=permx
    x*=x
    x*=permx
    print(list[2], x)
    x = permx
    x*=x
    x*=x
    x*=x
    print(list[3], x)
    x = permx
    x*=x
    x*=x
    x*=x
    x*=permx
    print(list[4], x)
    x = permx
    x*=x
    x*=x
    x*=permx
    x*=x
    print(list[5], x)
    x = permx
    x*=x
    x*=x
    tempx = x
    x*=x
    x*=tempx
    x*=permx
    print(list[6], x)
    x = permx
    x*=x
    x*=x
    x*=permx
    tempx = x
    x*=x
    x*=tempx
    print(list[7], x)
    x = permx
    x*=x
    x*=permx
    x*=x
    x*=permx
    tempx = x
    x*=tempx
    x*=tempx
    print(list[8], x)
    x = permx
    x*=x
    x*=permx
    x*=x
    x*=permx
    x*=x
    x*=x
    print(list[9], x)
    x = permx
    for i in range(6):
        x*=x
    print(list[10], x)
except ValueError:
    print('Not a number!')