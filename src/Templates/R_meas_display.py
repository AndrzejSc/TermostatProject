import board
import time
import busio
import digitalio
import adafruit_max31865
import tm1637
tm1 = tm1637.TM1637(clk=21, dio = 20)
tm1.numbers(88, 88)     # Test wyświetlacza
tm2 = tm1637.TM1637(clk=16, dio = 12)
tm2.numbers(88, 88)     # Test wyświetlacza

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor1 = adafruit_max31865.MAX31865(spi, cs1, wires=3,rtd_nominal=100.53)

cs2 = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board.
sensor2 = adafruit_max31865.MAX31865(spi, cs2, wires=3,rtd_nominal=100.53)

while True:
    T1 = sensor1.temperature
    T2 = sensor2.temperature
    
    print('Tempe 1: {0:0.3f}C'.format(T1)+ ' \tTemp 2: {0:0.3f}C'.format(T2))
    temp1 = int('{0:0.0f}'.format(T1))
    temp2 = int('{0:0.0f}'.format(T2))
    tm1.temperature(temp1)
    tm2.temperature(temp2)

    time.sleep(1)

    # Wyświetlenie temperatury oraz dwukropka
    T1_arr=str(round(sensor1.temperature))
    T2_arr=str(round(sensor2.temperature))
    secondDigitColon1 = tm1.encode_digit(int(T1_arr[1])) + 128
    secondDigitColon2 = tm2.encode_digit(int(T2_arr[1])) + 128
    #print(bin(int(aaa[1])))
    #print(bin(secondDigitColon1))
    #print(tm1.encode_digit(int(aaa[0])))
    tm1.write([tm1.encode_digit(int(T1_arr[0])), secondDigitColon1, 99, 57])
    tm2.write([tm2.encode_digit(int(T2_arr[0])), secondDigitColon2, 99, 57])
    
    time.sleep(1)
