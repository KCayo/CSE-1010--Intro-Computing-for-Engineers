# Homework 3 Calculator
# CSE 1010
# Kevin Cayo
# Nila Mandel 015L
# September 13, 2018

contin = True
accum = 0.0
import math
while contin:
    print('Accumulator =', accum)
    print('Please choose...')
    print('1) Addition')
    print('2) Subtraction')
    print('3) Multiplication')
    print('4) Division')
    print('5) Squareroot')
    print('6) Clear')
    print('0) Exit')
    opt = int(input("What is your option?"))
    if opt == 0:
        contin = False
    elif opt == 1:
        # do addition
        add = float(input('Enter a number: '))
        accum = add + accum
    elif opt == 2:
        # do subtraction
        sub = float(input('Enter a number: '))
        accum = accum - sub
    elif opt == 3:
        # do multiplication
        mul = float(input('Enter a number: '))
        accum = accum * mul
    elif opt == 4:
        # do division
        if accum == 0:
            print('Not dividing by zero')
        div = float(input('Enter a number: '))
        accum = accum / div
    elif opt == 5:
        # do squareroot
        if accum >= 0:
            accum = math.sqrt(accum)
        elif accum < 0:
            print('Not taking square root of negative number')
        elif opt == 6:
            # do clear
            accum = 0.0
            print('illegal option: ', opt)
        pass
    print('Program finished')
                
            
            
    
