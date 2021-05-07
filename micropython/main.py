from machine import Pin, SPI
import max7219
slt = open('tempsDattente.txt', 'r').read()
spi = SPI(1, baudrate=96000)



# display = max7219.Max7219(width, height, spi, cs, rotate)
  # width = total width of display in pixels
  # height = total height of display in pixels
  # spi = SPI bus
  # cs = cs (Chip Select) pin on ESP8266
  # rotate = rotate display 180 degrees (Optional; default = True)
display = max7219.Max7219(32, 8, spi, Pin(15))

display.show()
# display.marquee(msg_to_display)
display.marquee(slt)
