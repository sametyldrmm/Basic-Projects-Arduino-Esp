from machine import Pin
from time import sleep

led1 = Pin(14, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(13, Pin.OUT)

while True:
  led1.value(1)
  sleep(15)
  led1.value(0)
  led2.value(1)
  sleep(5)
  led2.value(0)
  led3.value(1)
  sleep(10)
  led3.value(0)