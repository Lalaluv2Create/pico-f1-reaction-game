from machine import Pin
import time #countdown
import random #random amount of time after countdown

#  = player's button
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

#create 5 led lights with their location
red_led = Pin(20, Pin.OUT)
yellow_led = Pin(21, Pin.OUT)
blue_led = Pin(22, Pin.OUT)
green_led = Pin(16, Pin.OUT)
white_led = Pin(17, Pin.OUT)

#should perint 0 before we start
#print(button.value())
#Game Loop:
while True:
    #1.) Use the press button to start the game
    while True:
        if button.value() == 1:
            print("F1 Race Begins Now!")
            print()
            print("Let the lights turn on one at a time")
            print("Wait for the lights to go out!")
            print("Then press the button as fast as you can!")
            break #only print message once
        
    #wait for the player to release the button    
    while button.value() == 1:
        time.sleep(0.01)

    #2.) lights turning on 1 second after another
    red_led.on() #light 1
    time.sleep(1)

    yellow_led.on() #light 2
    time.sleep(1)

    blue_led.on() #light 3
    time.sleep(1)

    green_led.on() #light 4
    time.sleep(1)

    white_led.on() #light 5
    time.sleep(1)

    #3.) after a random num. of seconds (0.5 & 5.5) turn off all lights off)
    wait_time = random.uniform(0.5, 5.5)

    #remember when the random waiting started
    wait_start = time.ticks_ms()

    #checking if the player hit wait
    false_start = False
    while True:
        #Check if the player pressed the button too early
        if button.value() == 1:
            print("FALSE START!")
            print()
            print("You pressed the button too early!")
            print ("Try again!")
            false_start = True
            break
        
        #Check how much time has passed
        current_time = time.ticks_ms()
        elapsed = time.ticks_diff(current_time, wait_start)
        
        #If enough time has passed, end the waiting
        if elapsed >= wait_time * 1000:
            break
    
    #if the player had a false start, turn off the lights and restart
    if false_start == True:
        red_led.off()
        yellow_led.off()
        blue_led.off()
        #green_led.off()
        white_led.off()
        
        continue

    #turn off the lights after a normal wait
    red_led.off()
    yellow_led.off()
    blue_led.off()
    green_led.off()
    white_led.off()
            
    #5.record the time the lights went off
    lights_off = time.ticks_ms()
    

    #4.)User should press the button as quickly as possible
    while True:
        if button.value() == 1:
            break
    #record when the player pressed the button
    button_pressed = time.ticks_ms()

    #reaction time of the player
    reaction_time = time.ticks_diff(button_pressed, lights_off)
    
    #6.) display 2 results
    print("Reaction time: ", reaction_time, "ms")
    if reaction_time <= 350:
        print("Perfect Timing!")
    else:
        print("Too Late!") 