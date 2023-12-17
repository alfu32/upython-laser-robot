from machine import Pin, PWM
import time

# Create a PWM object on GPIO4
pwm4 = PWM(Pin(4))
# Set the PWM frequency (e.g., 1000 Hz)
pwm4.freq(1000)
wave4 = [100,90,80,70,60,50,40,30,20,10,0,0,0,0,10,20,30,40,50,60,70,80,90]
wave4 = [0,20,40,80,100,80,40,20]
l4 = len(wave4)
index4 = 0


# Create a PWM object on GPIO3
pwm3 = PWM(Pin(3))
# Set the PWM frequency (e.g., 16 Hz)
pwm3.freq(1000)
wave3 = [0,0,40,80,100,80,40]
l3 = len(wave3)
index3 = 0

# Create a PWM object on GPIO1
pwm1 = PWM(Pin(1))
# Set the PWM frequency (e.g., 16 Hz)
pwm1.freq(1000)
wave1 = [0,20,60,100,60,20]
l1 = len(wave1)
index1 = 0


# Create a PWM object on GPIO1
pwm0 = PWM(Pin(0))
# Set the PWM frequency (e.g., 16 Hz)
pwm0.freq(1000)
wave0 = [0,10,20,80,100,80,20,10]
l0 = len(wave0)
index0 = 0

timing = 0.1


# Duty cycle is between 0 (all off) and 1023 (all on) for ESP32
while True:
    # print("i3[{:.0f}],i4[{:.0f}]".format(index3,index4))

    percentage0 = wave0[index0]
    percentage1 = wave1[index1]
    percentage3 = wave3[index3]
    percentage4 = wave4[index4]
    if index1 == 0 or index3 == 0 or index4 == 0:
        print("wavy ~~~ :: p0: {:.0f}%,p1: {:.0f}%,p3: {:.0f}%,p4: {:.0f}%".format(percentage0,percentage1,percentage3,percentage4))
    pwm4.duty(percentage4 * 10)  # Increase duty cycle
    pwm3.duty(percentage3 * 10)  # Increase duty cycle
    pwm1.duty(percentage1 * 10)  # Increase duty cycle
    pwm0.duty(percentage0 * 10)  # Increase duty cycle
    index0=(index0+1)%l0
    index1=(index1+1)%l1
    index3=(index3+1)%l3
    index4=(index4+1)%l4
    
    time.sleep(timing)  # Short delay
