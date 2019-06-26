from gpiozero import OutputDevice
from time import sleep

pump1 = OutputDevice(4)


def run_pump():
    pump1.active_high = False
    pump1.toggle()

    sleep(60)
    pump1.toggle()


if __name__ == '__main__':
    run_pump()
    print("All done!  Good-bye!")

