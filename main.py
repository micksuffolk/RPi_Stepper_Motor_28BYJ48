from threading import Event
import RPi.GPIO as GPIO
from time import sleep

# For GPIO numbering, choose BCM, or for pin numbering, choose BOARD...
GPIO.setmode(GPIO.BCM)

# Generate a variable for the event.wait() function, alternative to sleep() function...
event = Event()

# Used pins of the ULN2003A assigned to the pins of the Raspberry Pi...
IN1 = 23  # IN1
IN2 = 24  # IN2
IN3 = 25  # IN3
IN4 = 16  # IN4

# Waiting time controls the speed of the motor...
time = 0.0025

# Define pins from outputs...
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# All pins are initially set to false. So the stepper motor does not turn immediately...
GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# The stepper motor 28BYJ-48 number of steps per full rotation = 2038...
# Definition of coil sequence (stages 1-8) via pins IN1 to IN4 on the ULN2003...
# Between each movement of the motor there is a short wait when the motor armature has reached its position...
def Step1():
    GPIO.output(IN4, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN4, False)

def Step2():
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def Step3():
    GPIO.output(IN3, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN3, False)

def Step4():
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def Step5():
    GPIO.output(IN2, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN2, False)

def Step6():
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def Step7():
    GPIO.output(IN1, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN1, False)

def Step8():
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
#    sleep(time)
    event.wait(time)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

# Counter Clockwise rotation
def left(step):
    for i in range(step):
        # os.system('clear') # slows the movement of the motor too much.
        Step1()
        Step2()
        Step3()
        Step4()
        Step5()
        Step6()
        Step7()
        Step8()
#        print("Step left: ", i) # slows the movement of the motor too much.

# Clockwise rotation
def right(step):
    for i in range(step):
        # os.system('clear') # slows the movement of the motor too much.
        Step8()
        Step7()
        Step6()
        Step5()
        Step4()
        Step3()
        Step2()
        Step1()
#        print("Step right: ", i) # slows the movement of the motor too much.


######################################################################################################################
# Initialize/Startup (This block will test the excepted error to occur)...
# Nothing of note to go here yet, variables are initialised at the top of the code instead...
try:
    print("Code Initializing...")



######################################################################################################################
# The try section has failed (handle the error)...
except:
    print('Something went wrong with Try block...')
    exit()



######################################################################################################################
# The try section has been successful (If there is no exception then this block will be executed)...
else:
    print('Code Running...')

    # Main Program Loop...
    while True:

        # Here the decision is made whether left or right
        left(512)  # One full turn
        right(512)  # One full turn



######################################################################################################################
# Finally block always gets executed either exception is generated or not...
finally:

    print('Code Stopped...')
    GPIO.cleanup()
    exit()


