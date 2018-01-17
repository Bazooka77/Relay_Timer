from digitalio import DigitalInOut, Direction, Pull
import board
import time

# Set the pushbutton to pin D0 and pull to UP
button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Set the relays to pins D1-D4 and the direction to OUTPUT
relay1 = DigitalInOut(board.D1)
relay1.direction = Direction.OUTPUT

relay2 = DigitalInOut(board.D2)
relay2.direction = Direction.OUTPUT

relay3 = DigitalInOut(board.D3)
relay3.direction = Direction.OUTPUT

relay4 = DigitalInOut(board.D4)
relay4.direction = Direction.OUTPUT

# Variable for the button to start or stop
buttonpressed = 0


def funct1():
    print("Timer Started")
    global buttonpressed
    buttonpressed = 1
    relay1.value = True
    relay2.value = True
    relay3.value = True
    relay4.value = True
    time.sleep(.5)

def funct2():
    print("Timer Stopped")
    global buttonpressed
    buttonpressed = 0
    relay1.value = False
    relay2.value = False
    relay3.value = False
    relay4.value = False
    time.sleep(.5)

    
# While the button has not been pressed if it is pressed goto function1 
# else wait for press
while buttonpressed == 0:
        if button.value is False:
            funct1()
        else:
            print("Waiting for button press")
            time.sleep(.5)
            
# Else button has been pressed if button is pressed goto function2 else 
# print elapsed time
while buttonpressed == 1:
    if button.value is False:
        funct2()
    else:
        print("elapsed time")
        time.sleep(.5)
        