import pigpio
import time

# Initialize pigpio and connect to the daemon
pi = pigpio.pi()

if not pi.connected:
    exit()

# Define PWM pin (e.g., GPIO18)
PWM_PIN = 12  # Change to your desired PWM pin

# Set PWM frequency (in Hz) and duty cycle (in range 0-1,000,000)
pi.set_PWM_frequency(PWM_PIN, 50)  # Set PWM frequency to 50Hz (standard for servos)

def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (500-2500 microseconds for typical servos)
    duty_cycle = int((angle / 180.0) * 2000 + 500)
    pi.set_servo_pulsewidth(PWM_PIN, duty_cycle)  # Set duty cycle in microseconds

try:
    while True:
        # Move servo to 0 degrees
        set_servo_angle(0)
        time.sleep(2)

        # Move servo to 90 degrees (midpoint)
        set_servo_angle(90)
        time.sleep(2)

        # Move servo to 180 degrees (max rotation)
        set_servo_angle(180)
        time.sleep(2)

except KeyboardInterrupt:
    pass

# Stop PWM and clean up
pi.set_servo_pulsewidth(PWM_PIN, 0)  # Stop sending PWM signal
pi.stop()  # Stop the connection to pigpiod daemon
