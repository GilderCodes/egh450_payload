import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time

# Define the GPIO pin the servo is connected to
SERVO_PIN = 12

# Function to set servo position
def set_servo_duty(angle):
    #duty_cycle = (angle / 18.0) + 2.5 # Convert angle to duty cycle
    servo.ChangeDutyCycle(angle)
    time.sleep(3) # Allow time for the servo to move
    servo.ChangeDutyCycle(7.5) # Stop sending signal to avoid jitter
    time.sleep(1) # Allow time for the servo to move
    servo.ChangeDutyCycle(0) # Stop sending signal to avoid jitter

# Callback function for payload deployment messages
def payload_callback(msg):
    rospy.loginfo("callback called")
    if msg.data == "drop_epipen":
        rospy.loginfo("Deploying EpiPen for human")
        set_servo_duty(2.5)
    elif msg.data == "drop_gps":
        rospy.loginfo("Deploying GPS for backpack")
        set_servo_duty(12.5)
    elif msg.data == "drop_drone":
        rospy.loginfo("Deploying square payload for drone")
        set_servo_duty(11.7)
    elif msg.data == "drop_phone":
        rospy.loginfo("Deploying rectangular payload for phone")
        set_servo_duty(2.5)

def shutdown():
    # Clean up our ROS subscriber if they were set, avoids error messages in logs
    if payload_deployment is not None:
        payload_deployment.unregister()

    # Close down our GPIO
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        # Initialize ROS node
        rospy.init_node('payload_deployment_node')

        # Initialize PWM for servo motor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        servo = GPIO.PWM(SERVO_PIN, 50) # 50Hz frequency
        servo.start(0)

        # Subscribe to the payload deployment topic
        payload_deployment = rospy.Subscriber('/payload_deployment', String, payload_callback)

        # Register shutdown hook to clean up GPIO
        rospy.on_shutdown(shutdown)

        # Keep the node running
        rospy.spin()

    except rospy.ROSInterruptException:
        pass

    finally:
        # Cleanup GPIO on exit
        GPIO.cleanup()
