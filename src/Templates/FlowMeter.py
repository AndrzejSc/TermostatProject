# Pomiar przepływu w trakcie 1 sekundy lub /TODO [] w czasie określonym przez wywołanie
# Funkcja pomiarowa nie blokuje działania prorgamu (wykorzystanie multitasking)

import multitasking
import RPi.GPIO as GPIO
import time, sys


class FlowMeter:

    def __init__(self, signalPin: int):
        # Instance variables:
        self.signalPin = signalPin  # Pin sygnałowy czujnika przepływu
        self.defaultMeasureTime = 1  # Czas pomiaru w sekundach
        self.startTime = 0  # Czas startu pomiaru
        self.countedSlopes = 0  # Ilosc impulsów w czasie trwania pomiaru

        # Setup commands
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(signalPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    # def measInit(self):
    #     # Włącza wywołanie funkcji countSlopes() zliczającej ilość impulsów
    #     GPIO.add_event_detect(self.signalPin, GPIO.FALLING, callback=self.countSlopes())
    #     # Rozpoczęcie pomiaru, zapis czasu startu
    #     # Gdy minął czas, odłącz funkcję countSlopes()
    #     GPIO.remove_event_detect(self.signalPin)
    #     # self.measFlow(self,self.measureTime)



    #@multitasking.task
    def startMeas(self, defaultMeasureTime=None):
        print(self)
        if defaultMeasureTime is None:
            measTime = self.defaultMeasureTime
        else:
            measTime = defaultMeasureTime
        #print(super(FlowMeter, self).startMeas())
        # gdy opada zbocze sygnału SignalPin, wywołaj funkcję countSlopes()
        # TODO problem z wywołaniem countSlopes()
        GPIO.add_event_detect(self.signalPin, GPIO.FALLING, callback=self.countSlopes())

        # start pomiaru, zapisujemy czas rozpoczącia
        self.startTime = time.time()
        while (time.time() - self.startTime < measTime):
            print('Zliczam... ' + str(time.time() - self.startTime) + " , pulses: " + str(self.countedSlopes))
            pass
        # Wyłącza wywołanie measInit() gdy opada zbocze sygnalu signalPin
        GPIO.remove_event_detect(self.signalPin)
        return self.countedSlopes


    def countSlopes(self):
        countedSlopes = + 1
'''
TODO:
[ ] Ustawialny czas pomiaru
[ ] Flaga ustawiana po zakończeniu pomiaru 
'''
