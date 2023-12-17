from machine import Pin
import time

# Create an LED object on GPIO4, set as output
led = Pin(4, Pin.OUT)

while True:
    led.value(1)  # Turn LED on
    time.sleep(1)  # Wait for 1 second
    led.value(0)  # Turn LED off
    time.sleep(1)  # Wait for 1 second
    print("blinky")
