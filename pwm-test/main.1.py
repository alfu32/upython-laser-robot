from machine import Pin, PWM
import time

class PinWaveform:
    """A simple example class"""
    i = 0
    l = 2
    wave=[0,100]
    frequency=1000
    pwm=""
    def __init__(self,pinNumber,frequency,wave):
        self.wave = wave
        self.frequency=frequency
        self.l=len(wave)
        self.pwm=PWM(Pin(pinNumber))
    def next(self):
        percentage = self.wave[self.i]
        self.i=(self.i+1)%self.l
        self.pwm.duty(percentage * 10)
        return percentage

# Create a PWM object on GPIO4
p4 = PinWaveform(4,32000,[0,3,10,35,50,90,100,90,50,35,10,3])
# Create a PWM object on GPIO3
p3 = PinWaveform(3,1000,[0,0,100,0,100,0,0,30,0,30,0,30])
# Create a PWM object on GPIO4
p2 = PinWaveform(2,16,[0,0,10,0,10,0,10,0,0,0,100,0,100,0,80,0,0,10,0,10,0,10])
# Create a PWM object on GPIO4
p1 = PinWaveform(1,1000,[0,100,100,100,100,0])
# Create a PWM object on GPIO4
p0 = PinWaveform(0,16,[0,100,100,100,0,0,100,100,100])

timing = 0.1


# Duty cycle is between 0 (all off) and 1023 (all on) for ESP32
while True:
    percentage0 = p0.next()
    percentage1 = p1.next()
    percentage2 = p2.next()
    percentage3 = p3.next()
    percentage4 = p4.next()
    if p0.i == 0 or p1.i == 0 or p3.i == 0 or p4.i == 0:
        print("wavy ~~~ :: p0: {:.0f}%,p1: {:.0f}%,p2: {:.0f}%,p3: {:.0f}%,p4: {:.0f}%".format(percentage0,percentage1,percentage2,percentage3,percentage4))
    
    time.sleep(timing)  # Short delay
