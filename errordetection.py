# Error Detection 
# CSE1010 Homework 6, Fall 2018
# Kevin Cayo
# 10/20/2018
# TA: Nila Mandel
# Lab Section: 015L
# Instructor: Ahmad Jbara

import random 

def getChar():
    x=input('Enter a character:')
    return (x[0])

def char2bin(d):
    h = ord(d)
    g = bin(h)[2:]
    g = g.zfill(8)
    l = list(g)
    for n in range(len(l)):
        l[n] = ord(l[n])-48
    return list(l)

def bin2char(h):
    for n in range(len(h)):
        if h[n] == 0:
            h[n]='0'
        else:
            h[n]='1'
    h = ''.join(h)
    a = int(h, 2)
    i = chr(a)
    return i

def parityOf(h, j):
    k = h.count(1)
    if (k % 2 == 0 and j == 0) or (k % 2 != 0 and j == 1):
        return 0
    else:
        return 1

def appendParity(h, j):
    return h + [parityOf(h, j)]

def addNoise(r, t):
    h = []
    y = 0
    for n in r:
        ran_num= random.random()
        if ran_num< t:
            if n == 0:
                h.append(1)
                y += 1
            else:
                h.append(0)
                y += 1
        else:
            h.append(n)
    return h, y


def checkParity(p, w):
    s = p[0:8]
    d = parityOf(s, w)
    if d == p[8]:
        return True,s
    else: return False,s

def main():
    k = 0.1
    f = 0
    h = getChar()
    r = char2bin(h)
    b = appendParity(r, f)
    m, a = addNoise(b, k)
    z, c = checkParity(m, f)
    y = bin2char(c)
    print('Transmitted Bits: ', b)
    print('Number of Flipped Bits: ', a)
    print('Received Bits: ', m)
    if z is True:
        print('No errors detected,')
    else:
        print('Error detected.')
    print('Received character: ',y)

if __name__ == '__main__':
    main()
            
    
    
    
