import time
from gpiozero import OutputDevice as stepper

IN1 = stepper(25)
IN2 = stepper(8)
IN3 = stepper(7)
IN4 = stepper(11)
StepPins = [IN1, IN2, IN3, IN4]

# Define sequence as shown in manufactuers data sheet
Seq = [[1, 0, 0, 1],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       ]

StepCount = len(Seq)
StepDir = 1
WaitTime = 0.01
StepCounter = 0

while True:

    print(StepCounter)
    print(Seq[StepCounter])
    for pin in range(0, 4):
        xpin = StepPins[pin]
        if Seq[StepCounter] [pin] !=0:
            xpin.on()
        else:
            xpin.off()

    StepCounter += StepDir

    # If we reach the end of the sequence start again
    if (StepCounter >= StepCount):
        StepCounter = 0
    if (StepCounter < 0):
        StepCounter = StepCount+StepDir

    # Wait Before Moving On
    time.sleep(WaitTime)
