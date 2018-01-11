from digitalio import DigitalInOut, Direction, Pull
import board
import time

button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
 
relay1 = DigitalInOut(board.D1)
relay1.direction = Direction.OUTPUT
 
relay2 = DigitalInOut(board.D2)
relay2.direction = Direction.OUTPUT

relay3 = DigitalInOut(board.D3)
relay3.direction = Direction.OUTPUT

relay4 = DigitalInOut(board.D4)
relay4.direction = Direction.OUTPUT

start_time = 0
end_time = 0
duration = 400
elapsed = 0
timerstarted = False

def funct1():
            
    if elapsed = 0
        start_time = time.monotonic()
        end_time = start_time + duration
        print("Timer Started At: ", start_time)
        relay1.value = True
        relay2.value = True
        relay3.value = True
        relay4.value = True
        time.sleep(.5)
        elapsed = time_monotonic() - start_time
                
    elif elapsed > 0 < duration
        print("Elapsed Time: ", elapsed)
        relay1.value = True
        relay2.value = True
        relay3.value = True
        relay4.value = True
        time.sleep(.5)
        elapsed = time_monotonic() - start_time
                
    elif time_monotonic >= end_time    
        print("Started at: ", time_monotonic())
        print("Completed at: ", elapsed)
        print("Duration: ", duration)
        relay1.value = False
        relay2.value = False
        relay3.value = False
        relay4.value = False
        elapsed = 0
        start_time = 0
        end_time = 0
        time.sleep(.5)
                    
time.sleep(.01)

   
while True:
    if button.value:
        print("Timer Stopped at: ", time.monotonic())
        print("Duration: ", duration)
        elapsed = 0
        start_time = 0
        end_time = 0
        time.sleep(.5)
    else
        timerstarted = True
        funct1()
    
