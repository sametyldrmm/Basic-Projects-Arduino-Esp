from machine import Pin
from time import sleep

ledb = Pin(5, Pin.OUT)
ledg = Pin(4, Pin.OUT)
ledr = Pin(0, Pin.OUT)
buton = Pin(2, Pin.IN)

while True :
  ledb.value(button.value())
 
