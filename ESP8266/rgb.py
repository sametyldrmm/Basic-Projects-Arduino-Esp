import	machine
import	time

#	OUTPUT	PINS	-	LEDs
pin_D0	=	machine.Pin(14,	machine.Pin.OUT)
pin_D1	=	machine.Pin(12,machine.Pin.OUT)
pin_D2	=	machine.Pin(13,machine.Pin.OUT)


while True:
  pin_D0.value(1)
  pin_D1.value(1)
  pin_D2.value(1)
  sleep(5)