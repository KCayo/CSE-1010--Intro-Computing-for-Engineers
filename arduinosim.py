import digital
import analog
import time

class ArduinoSim: 

    numAnalogs = 6 #these are the class member variables
    numDigitals = 14

    def __init__(self): #creates a list of digital pins
       list_digitalp = []
       list_analogp = []
       self.list_digitalp = list_digitalp
       self.list_analogp = list_analogp
       for x in range(self.numDigitals):
           d = digital.Digital()
           self.list_digitalp.append(d)
       for x in range(self.numAnalogs):
            a = analog.Analog()
            self.list_analogp.append(a)

    def ar(self, pin_num): #returns the read value of Analog
        if pin_num >= 0 and pin_num < self.numAnalogs:
            return self.list_analogp[pin_num].read()
        else:
            return None

    def dr(self, pin_num):#returns read value of Digital
        if pin_num >= 0 and pin_num < self.numDigitals:
            return self.list_digitalp[pin_num].read()
        else:
            return None

    def aw(self, pin_num, value): #returns write value of Analog
        if pin_num >= 0 and pin_num < self.numAnalogs:
            self.list_analogp[pin_num].write(value)
        else:
            None

    def dw(self, pin_num, value): #returns write value of Digital 
        if pin_num == 13:
            if value == 1:
                print("LED is on")
            else:
                print("LED is off")
        elif pin_num >= 0 and pin_num < self.numDigitals:
            self.list_digitalp[pin_num].write(value)
        else:
            None

    def dm(self, pin_num, mode): #sets mode value
        if pin_num >= 0 and pin_num < self.numDigitals:
            self.list_digitalp[pin_num].write(mode)
        else:
            None

    def blink(simulator): #simulates light blinking
        simulator.dm(13, 1)
        for x in range(5):
            simulator.dw(13, 1)
            time.sleep(1)
            simulator.dw(13, 0)
            time.sleep(1)

import threading
def start_potentiometer(arduino): #simulates potentiometer being turned endlessly
    def run(): 
        delay = 0.002
        while True:
            for n in range(1024):
                arduino.list_analogp[0].set_value(n)
                time.sleep(delay)
            for n in range(1023, -1, -1):
                arduino.list_analogp[0].set_value(n)
                time.sleep(delay)
    thread = threading.Thread(target = run)
    thread.start()

def main(): #samples potentiometer value on analog
    ard = ArduinoSim()
    start_potentiometer(ard)
    for n in range(10):
        print (n, ':', ard.ar(0))
        time.sleep(1)
            
        
