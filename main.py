import epaper2in9d as epaper2in9
from machine import Pin, SPI
from image import micropython_logo

# SPI1 on ESP8266
spi  = SPI(1, baudrate=80000000, polarity=0, phase=0)

# SPI pins for Badgy
cs   = Pin(15, Pin.OUT)
dc   = Pin(0, Pin.OUT)
rst  = Pin(2, Pin.OUT)
busy = Pin(4, Pin.OUT)

e = epaper2in9.EPD(spi, cs, dc, rst, busy)
e.init()

#w = 128
#h = 296
#x = 0
#y = 0

#e.clear_frame_memory(0xFF)
#e.set_frame_memory(micropython_logo, x, y, w, h)
#e.display_frame()
e.display_frame(micropython_logo)
