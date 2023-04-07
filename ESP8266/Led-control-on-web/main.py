try:
  import usocket as socket
except:
  import socket

from machine import Pin , ADC
from time import sleep
import network
import esp
import gc

esp.osdebug(None)
gc.collect()

ssid = 'TTNET_ZyXEL_KFRK'
password = 'a457a8c2a8848'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

pot = ADC(0) 
led = Pin(2, Pin.OUT)
