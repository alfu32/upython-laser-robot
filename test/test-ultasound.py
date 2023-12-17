import machine
import time

# Define the GPIO pins connected to the sensor
TRIG_PIN = 3  # Change to the GPIO pin you connected to the Trig pin on the sensor
ECHO_PIN = 4  # Change to the GPIO pin you connected to the Echo pin on the sensor

# Create objects for the trigger and echo pins
trigger = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance using the HC-SR04 sensor
def measure_distance():
    # Generate a 10us pulse on the trigger pin to trigger the sensor
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    # Wait for the echo pin to go high (start of the pulse)
    while echo.value() == 0:
        pass
    start_time = time.ticks_us()

    # Wait for the echo pin to go low (end of the pulse)
    while echo.value() == 1:
        pass
    end_time = time.ticks_us()

    # Calculate the duration of the pulse (in microseconds)
    pulse_duration = end_time - start_time

    # Speed of sound at 20°C is approximately 343 meters/second or 34300 centimeters/second
    # Divide the pulse duration by 2 to get the one-way distance
    distance_cm = (pulse_duration / 2) / 29.1  # Adjust for your actual speed of sound

    return distance_cm

try:
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))
        time.sleep(1)  # You can adjust the delay as needed
except KeyboardInterrupt:
    pass