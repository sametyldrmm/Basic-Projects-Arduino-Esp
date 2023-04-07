from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
buton = Pin(0, Pin.IN)

while True :
  led.value(buton.value())
  sleep(1)
  print(buton.value())
  sleep(0.5)
