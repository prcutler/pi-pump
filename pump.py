from gpiozero import OutputDevice
from time import sleep
import sentry_sdk


# TODO: Add code comments to make it easier for a user to add additional pumps

sentry_sdk.init("https://dfe1f1ad68ac4df8abe1479c6dedb280@sentry.io/1492008")

# Assign the pump based on what pin the Raspberry Pi is using
pump1 = OutputDevice(4)


# Set the pump toggle as off and toggle the pump on and running
def pump_on():
    pump1.active_high = False
    pump1.toggle()


# Pump is now running - Define how long the pump should run in the on position from run_pump above:
def pump_time():
    sleep(60)


# Toggle the pump into the off position
def pump_stop():
    pump1.toggle()


# Define how many times (cycles) the pump should turn on, then pause, and then turn off again:
cycles = 4


# This function will turn the pump and and off based on how many cycles above.  Do not changes this code:
def pump_series():
    for cycle in range(cycles):
        pump_on()
        pump_time()
        pump_stop()
        print("Cycle " f"{cycle} " "completed.")


if __name__ == '__main__':
    pump_series()
    print("All done!  Good-bye!")

