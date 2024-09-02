import RPi.GPIO as GPIO
import time

# Define the GPIO pin the servo is connected to
SERVO_PIN = 12

# Initialize GPIO and PWM for servo motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50) # 50Hz frequency
servo.start(0)

try:
    while True:
        duty_cycle = float(input("Enter duty cycle (2.5 to 12.5) to set servo angle: "))
        if 2.5 <= duty_cycle <= 12.5:
            servo.ChangeDutyCycle(duty_cycle)                 
            time.sleep(1) # Allow time for the servo to move
           # servo.ChangeDutyCycle(duty_cycle-0.5)
            #time.sleep(0.2) # Allow time for the servo to move
           # servo.ChangeDutyCycle(duty_cycle+0.5)
           # time.sleep(0.2) # Allow time for the servo to move
          #  servo.ChangeDutyCycle(7.5)
           # time.sleep(1) # Allow time for the servo to move
            servo.ChangeDutyCycle(0) # Stop sending signal to avoid jitter
        else:
            print("Please enter a duty cycle between 2.5 and 12.5")
except KeyboardInterrupt:
    pass
finally:
    servo.stop()
    GPIO.cleanup()
