# Error Correction
# CSE1010 Homework 7, Fall 2018
# Kevin Cayo
# 10/28/2018
# TA: Nila Mandel
# Section: 015L
# Instructor: Ahmad Jbara

from errordetection import *

def string2bin(d):
    "'Converts a string to a list of lists of binary numbers. frame=string2(str)'"
    binlist = []
    for t in d:
        binlist.append(char2bin(t))
    return binlist

def segmentString(string, fillchar):
    "'Converts a string into an 8 character list, any extra space will be filled by the fillchar variable. frame=string2frames(string, fillchar)'"
    segmentString= []
    n = 0
    while n<len(string):
        h=string[n:n+8]
        if len(h)<8:
            h = h.ljust(8, fillchar)
            segmentString.append(h)
        else:
            segmentString.append(h)
        n=n+8
    return segmentString

def printFrames(frames):
    "'Converts the frame list to show the bits in each row, then decodes each bit into a character. frame=printFrames(frames)'"
    frameN = 0
    for frame in frames:
        charN = 0
        for bin in frame:
            char = bin2char(bin)
            print(f"{charN:2}", bin, char)
            charN += 1
        frameN += 1
        print()

def string2frames(string, char):
    "'Converts a string of any length and a fill character, and cuts the string into 8-character segments. frames=string2frames(s, ' ')'"
    framelist= []
    s = segmentString(string, char)
    k = 0
    while k<len(s):
        f=string2bin(s[k])
        framelist.append(f)
        k = k + 1
    return framelist

def appendParityColumn(frame, desiredParity):
    "'Appends a buit to each list in the frame. h=appendParity Column(frame, desiredParity)'"
    l = frame
    k = 0
    y = []
    while k<len(l):
        j = appendParity(l[k], desiredParity)
        y.append(j)
        k = k + 1
    return y 

def transpose(lst):
    "'Rotates the list around the diagonal. transpose([1,2,3]):'"
    lst = list(map(list, zip(*lst)))
    return lst

def appendParityRow(frame, desiredParity):
    "'Adds a 9th row of bits that are the parity bits the columns of the frame. frames=appemdParityRow(frame, desiredParity):'"
    t = transpose(frame)
    t1 = appendParityColumn(t, desiredParity)
    t2 = transpose(t1)
    return t2

def appendParityToFrame(frame, desiredParity):
    "'Converts an 8x8 frame and a desired parity to a 9x9 frame that. frame=appendParityToFrame(frame, desiredParity'"
    h1 = appendParityColumn(frame, desiredParity)
    h2 = appendParityRow(h1, desiredParity)
    return h2

def appendParityToFrames(frames, desiredParity):
    "'Converts takes frames and a desired parity and appends a parity row and column to each frame in the list and returns the new list of frames. frames=appendParityToFrames(frames, desiredParity)'"
    p = []
    o = 0
    while o<len(frames):
        fo = frames[o]
        p1 = appendParityToFrame(fo, desiredParity)
        p.append(p1)
        o = o+1
    return p

def transmitFrames(frames, errorProbability):
    "'Takes a list of frames and an error probability from 0 to 1. frame=transmitFrames(frames, errorProbability)'"
    x = 0
    y = []
    n = 0
    while n<len(frames):
        z = frames[n]
        w = 0
        nF = []
        while w<len(z):
           zw = z[w]
           (newRow, bitsFlipped) = addNoise(zw, errorProbability)
           nF.append(newRow)
           x = x + bitsFlipped
           w = w + 1
        y.append(nF)
        n = n + 1
    print("Number of flipped bits:", x)
    return y

def splitFrame(frame):
    "'Splits frame into 3 equal pieces. frame1=splitFrame(frame)'"
    payload = []
    parityColumn = []
    x = 0
    while x<len(frame)-1:
        y = frame[x][:8]
        payload.append(y)
        z = frame[x][8]
        parityColumn.append(z)
        x = x + 1
    parityRow = frame[8]
    return payload, parityColumn, parityRow

def checkParityOfFrame(frame, desiredParity):
    "'Recalculates the 8x8 payload and compares it to the 9x9 frame. frames=checkParityOfFrame(frames, desiredParity)'"
    (payloadA, parityColumnA, parityRowA) = splitFrame(frame)
    nF = appendParityToFrame(payloadA, desiredParity)
    (payloadB, parityColumnB, parityRowB) = splitFrame(nF)
    y = 0
    x = 0
    parityColumnE = []
    parityRowE = []
    while y<len(parityColumnA):
        if parityColumnA[y] != parityColumnB[y]:
            parityColumnE.append(y)
        y = y + 1
    while x<len(parityRowA):
        if parityRowA[x] != parityRowB[x]:
            parityRowE.append(x)
        x = x + 1
    return parityRowE, parityColumnE

def repairFrame(frame, eColumns, eRows):
    "'Takes the 9x9 frame, error columns, error rows, and tries to repair the frame. frame=(frame, eColumns, eRows):'"
    if eColumns == [] and eRows == []:
        return "NO ERRORS"
    elif len(eColumns) == 2 and len(eRows) == 1 and eColumns[len(eColumns)-1] == 8:
        e = frame[eRows[0]][eColumns[0]]
        if e == 0:
            e = 1
        else:
            e == 0
        frame[eRows[0]][eColumns[0]] = e
        return "CORRECTED"
    elif eColumns == [] or eRows == []:
        return "PARITY ERROR"
    else:
        return "NOT CORRECTED"
    
def repairFrames(frames, desiredParity):
    "'Repairs each frame of the 9x9 frame and the desired parity. frame=(frames, desiredParity):'"
    x = 0
    nFL = []
    sL = []
    for frame in frames:
        (parityRowE, parityColumnE) = checkParityOfFrame(frame, desiredParity)
        nF = repairFrame(frame, parityRowE, parityColumnE)
        if nF == "NO ERRORS":
            print("Frame", x, "has no errors")
            sL.append(nF)
        elif nF == "CORRECTED":
            print("Frame", x, "has been repaired")
            sL.append(nF)
        elif nF == "NOT CORRECTED":
            print("Frame", x, "could not be repaired")
            sL.append(nF)
        else:
            print("Parity Error")
            sL.append(nF)
        x = x + 1
        nFL.append(frame)
    return nFL, sL
    
def stripFrames(frames):
    "'Removes the parity row and column of a 9x9 frame. frame=stripFrames(frames)'"
    nFs = []
    for frame in frames:
        (payload, parityColumn, parityRow) = splitFrame(frame)
        nFs.append(payload)
    return nFs

def bin2string(frame, fillchar):
    "'Takes an 8x8 frame and character and returns the string by that frame. frame=bin2string(frame, fillchar):'"
    nchar = []
    for list in frame:
        c = bin2char(list)
        if c != fillchar:
            nchar.append(c)
    string = ''.join(nchar)
    return string

def frames2string(frames, fillchar):
    "'Converts each frame into a string. frame=frames2string(frames, fillchar):'"
    ss = []
    for frame in frames:
        s = bin2string(frame, fillchar)
        ss.append(s)
    ss1 = ''.join(ss)
    return ss1

def main():
    "'Ties all functions together, so they run simultaneously.'"
    eProb = 0.01
    desiredParity = 0
    fillchar = "~"
    s = input("Enter a string:")
    frame = string2frames(s, fillchar)
    tframes = appendParityToFrames(frame, desiredParity)
    rframes = transmitFrames(tframes, eProb)
    (rpframes, sL) = repairFrames(rframes, desiredParity)
    sframes = stripFrames(rframes)
    s = frames2string(sframes, fillchar)
    print(s)
    print(sL)
main()

    
        
    
    
    
   
    

            
    
