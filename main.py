
import smbus
from time import sleep

class PCF8591:

  def __init__(self,address):
    self.bus = smbus.SMBus(1)
    self.address = address

  def read(self,chn): #channel
      try:
          self.bus.write_byte(self.address, 0x40 | chn)  # 01000000
          self.bus.read_byte(self.address) # dummy read to start conversion
      except Exception as e:
          print ("Address: %s \n%s" % (self.address,e))
      return self.bus.read_byte(self.address)

  def write(self,val):
      try:
          self.bus.write_byte_data(self.address, 0x40, int(val))
      except Exception as e:
          print ("Error: Device address: 0x%2X \n%s" % (self.address,e))

# create Joystick class
class Joystick:

  def __init__(self, address):
    # instantiation code
    # extend PCF8591 class to Joystick class through composition
    self.address = PCF8591(address)
  # class methods to read and return analog pins 0 and 1 of ADC
  def getX(self):
    return self.address.read(0)
  def getY(self):
    return self.address.read(1)

# loop to continuously read the x and y positions of joystick
# use exception handling 
try:
  while True:
    # create object with defined instance variable
    Joystick_position = Joystick(0X48)
    # access class methods and print x and y positions of joystick
    x_position = Joystick_position.getX()
    y_position = Joystick_position.getY()
    print('{:d}, {:d}'.format(x_position,y_position))
    sleep(.1)
except KeyboardInterrupt:
  print('\nExiting')
except Exception as e:
  print('\e')