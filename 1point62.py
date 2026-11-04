from transformation import *
try:
    list = ['A)', 'Б)', 'B)', 'Г)', 'Д)', 'Е)']
    print('A)a^3 & a^10, Б)a^4 & a^20, B)a^5 & a^13, Г)a^5 & a^19 Д)a^2, a^5 & a^17, Е)a^5 & a^19, Д)a^4, a^12 & a^28')
    permx = transform(float(input('Insert a number: ')))
    aNd = 'and'
    x = permx
    x*=x
    tempx = x
    x*=permx
    x1 = x
    x*=tempx
    x*=x
    print(list[0], x1, aNd, x)
    x=permx
    x*=x
    x*=x
    x1 = x
    x*=permx
    x*=x
    x*=x
    print(list[1], x1, aNd, x)
    x = permx
    x*=x
    x*=x
    x*=permx
    x1 = x
    
except ValueError:
    print('Not a number!')