import machine
import time
##  from melopero_vl53l1x import mp


PWM_PINA=4
PWM_PINB=3
#define pwm pin
pwm4=machine.PWM(machine.Pin(PWM_PINA, machine.Pin.OUT, drive=machine.Pin.DRIVE_0))
pwm3=machine.PWM(machine.Pin(PWM_PINB, machine.Pin.OUT, drive=machine.Pin.DRIVE_0))
pwm3.duty(0)
pwm4.duty(0)

# Define the GPIO pins connected to the sensor
TRIG_PIN = 21  # Change to the GPIO pin you connected to the Trig pin on the sensor
ECHO_PIN = 20  # Change to the GPIO pin you connected to the Echo pin on the sensor

# Create objects for the trigger and echo pins
trigger = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# I2C pin configuration
##  i2c = machine.I2C(scl=machine.Pin(9), sda=machine.Pin(8))  # Replace with your SDA and SCL pin numbers

# Create a VL53L1X object
##  tof = mp.VL53L1X(i2c)

# Initialize the VL53L1X sensor
##  tof.open()

# Function to measure distance using the HC-SR04 sensor
def measure_distance_usnd():
    # Generate a 10us pulse on the trigger pin to trigger the sensor
    trigger.value(1)
    time.sleep_us(100)
    trigger.value(0)

    # Wait for the echo pin to go high (start of the pulse)
    while echo.value() == 0:
        #print("echo")
        pass
    
    start_time = time.ticks_us()

    # Wait for the echo pin to go low (end of the pulse)
    while echo.value() == 1:
        #print("read")
        pass
    
    end_time = time.ticks_us()

    # Calculate the duration of the pulse (in microseconds)
    pulse_duration = end_time - start_time
    print(pulse_duration)

    # Speed of sound at 20°C is approximately 343 meters/second or 34300 centimeters/second
    # Divide the pulse duration by 2 to get the one-way distance
    distance_cm = (pulse_duration / 2) / 29.1  # Adjust for your actual speed of sound

    return distance_cm

##def measure_distance_laser():
##    distance_mm = tof.read()
##    print("Distance: {} mm".format(distance_mm))
##    return distance_mm

THA=20
THB=50
THC=100
DC0=768
RANGE=(1024-DC0)
def duty_for_distance
try:
    while True:
        distance_cm = measure_distance_usnd()
        ## distance_mm = measure_distance_mm()
        ## distance=distance_mm/10
        distance=distance_cm
        if distance < THA :
            dc=-(DC0>>1)+int(RANGE/THA*(THA-distance))
            print("back {:.2f}".format(dc))
        elif distance < THB :
            print("stop")
        elif distance < THC :
            dc=(DC0>>1)+int(RANGE/(THC-THB)*(distance-THB))
            print("forward {:.2f}".format(dc))
        else :
            print("no-need")
        print("Distance: {:.2f} cm".format(distance))
        ## time.sleep(1)  # You can adjust the delay as needed
        time.sleep_us(150)
except KeyboardInterrupt:
    pass