from machine import Pin, PWM
import time

# Create a pwm4 object on GPIO4
pwm4 = PWM(Pin(4))
pwm3 = PWM(Pin(3))

wave3 = [0,0,20,40,60,80,60,40,20,0]
wave4 = [100,90,80,70,60,50,40,30,20,10]
index3 = 0
index4 = 0

# Set the pwm4 frequency (e.g., 1000 Hz)
pwm4.freq(1000)
pwm3.freq(16)

# Duty cycle is between 0 (all off) and 1023 (all on) for ESP32
while True:
    for percentage in range(100):
        pwm4.duty(percentage * 3)  # Increase duty cycle
        pwm3.duty(percentage * 10)  # Increase duty cycle
        if percentage % 10 == 0:  # Check if divisible by 10% (102.3 in terms of 0-1023 scale)
            print("Duty cycle: {:.0f}%".format(percentage))
        time.sleep(0.01)  # Short delay

    for percentage in range(100, -1, -1):
        pwm4.duty(percentage * 3)  # Increase duty cycle
        pwm3.duty(percentage * 10)  # Decrease duty cycle
        if percentage % 10 == 0:  # Check if divisible by 10% (102.3 in terms of 0-1023 scale)
            print("Duty cycle: {:.0f}%".format(percentage))
        time.sleep(0.01)  # Short delay
    print("wavy~~~")
