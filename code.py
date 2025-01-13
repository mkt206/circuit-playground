# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("hello")
print("-----------------")
print(dir(board))
print("-----------------")
print(dir(digitalio))
print("-----------------")
print(dir(digitalio.DigitalInOut))
print("-----------------")
print(dir(led))
print("-----------------")
while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)