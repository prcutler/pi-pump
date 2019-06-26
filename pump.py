from gpiozero import OutputDevice
from time import sleep

pump1 = OutputDevice(4)

def run_pump:
    pump1.on()
    sleep(5)
    pump1.off()


if __name__ == '__main__':
    run_pump()
    print("All done!  Good-bye!")

