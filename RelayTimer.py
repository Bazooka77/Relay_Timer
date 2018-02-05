# Relay Timer
# For Trinket M0
# Power from USB
# Pushbutton on D0
# Relay drivers on D1-D4


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

last_press = None

while True:
    if not button.value:
        if last_press:  # The relay is already on so turn it off.
            relay1.value = False
            relay2.value = False
            relay3.value = False
            relay4.value = False
            last_press = None
            print("timer stoppped at:")
            print(time.monotonic())
            time.sleep(.5)
        else:  # Turn on the relay
            relay1.value = True
            relay2.value = True
            relay3.value = True
            relay4.value = True
            last_press = time.monotonic()
            timeout = 60
            print("Timer started at:", last_press)
            print("Timer will complete at:", timeout + last_press)
            time.sleep(.5)
    
    if last_press and time.monotonic() - last_press > timeout:
        relay1.value = False
        relay2.value = False
        relay3.value = False
        relay4.value = False
        last_press = None
        print("Timer Completed At:", time.monotonic())
    
    else:
        print("Watching for button press:", time.monotonic())
        time.sleep(.5)
        
        