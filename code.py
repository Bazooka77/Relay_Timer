from digitalio import DigitalInOut, Direction, Pull
import board
import time

button = DigitalInOut(board.D0)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
 
relay1 = DigitalInOut(board.D1)
relay2 = DigitalInOut(board.D2)
relay3 = DigitalInOut(board.D3)
relay4 = DigitalInOut(board.D4)
relays = [relay1, relay2, relay3, relay4]    

start_time = 0
end_time = 0
duration = 400
elapsed = 0
buttonpress = 0
ticks = time_monotonic()
timerstarted = False

for r in relays:
    r.direction = Direction.OUTPUT

def funct1():
    if buttonpress == 0:
        butonpress = 1
        funct2()
        
    else:
        buttonpress = 0
        print("Started at: ", ticks)
        print("Stopped at: ", elapsed)
        print("Duration: ", duration)
        for r in relays:
            r.value = False
        elapsed = 0
        start_time = 0
        end_time = 0
        time.sleep(.5)

def funct2():
            
    if elapsed == 0:
        start_time = ticks
        end_time = start_time + duration
        print("Timer Started At: ", start_time)
        for r in relays:
            r.value = True
        time.sleep(.5)
        elapsed = ticks - start_time
                
    elif elapsed > 0 < duration:
        print("Elapsed Time: ", elapsed)
        for r in relays:
            r.value = True
        time.sleep(.5)
        elapsed = ticks - start_time
                
    elif ticks >= end_time:    
        print("Started at: ", ticks)
        print("Completed at: ", elapsed)
        print("Duration: ", duration)
        for r in relays:
            r.value = False
        elapsed = 0
        start_time = 0
        end_time = 0
        time.sleep(.5)
                    
time.sleep(.01)

   
while True:
    if button.value:
        funct1()
        time.sleep(.5)
        
    else:
        print("Elapsed Time: ", elapsed, "/", duration)
        time.sleep(.5)
    
