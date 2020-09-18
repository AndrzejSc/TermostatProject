# Main file
# Imports:
import src.Templates.FlowMeter as FlowMeterClass

#
if __name__ == "__main__":
    print('Hello')

print("Hello from Raspberry !")

# Obiekt do obsługi przepływomierza:
myFLowMeter = FlowMeterClass.FlowMeter(23)
print(myFLowMeter.startMeas())