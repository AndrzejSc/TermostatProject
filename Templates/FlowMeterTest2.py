import time
import math
import RPi.GPIO as GPIO

boardRevision = GPIO.RPI_REVISION
GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)

pouring = False
lastPinState = False
pinState = 0
lastPinChange = int(time.time() * 1000)
pourStart = 0
pinChange = lastPinChange
pinDelta = 0
hertz = 0
flow = 0
litersPoured = 0
pintsPoured = 0

# main loop
while True:
    currentTime = int(time.time() * 1000)
    if GPIO.input(23):
        pinState = True
        #print("PIN 23 True")
    else:
        pinState = False
        #print("PIN 23 False")

    # If we have changed pin states low to high...
    if(pinState != lastPinState and pinState == True):
        if(pouring == False):
            pourStart = currentTime
        pouring = True
        # get the current time
        pinChange = currentTime
        pinDelta = pinChange - lastPinChange
        #print ('LastPinChange: '+str(lastPinChange)+'PinChange: '+str(pinChange))
        print ("Delta Pin Change: "+str(pinChange-lastPinChange))
        if (pinDelta < 1000 and pinDelta != 0):
            # calculate the instantaneous speed
            hertz = 1000.0000 / pinDelta
            flow = hertz / (60 * 7.5) # L/s
            litersPoured += flow * (pinDelta / 1000.0000)
            pintsPoured = litersPoured * 2.11338

    if (pouring == True and pinState == lastPinState and (currentTime - lastPinChange) > 2000):
    # set pouring back to false, tweet the current amt poured, and reset everything
        pouring = False
        if (pintsPoured > 0.01):
            pourTime = float((currentTime - pourStart)/1000) - 2
            tweet = 'Poured ' + str(round(litersPoured,2)) + ' liters in ' + '%.2f'%pourTime + ' s'
            print(tweet)
            litersPoured = 0
            pintsPoured = 0
    lastPinChange = pinChange
    lastPinState = pinState
