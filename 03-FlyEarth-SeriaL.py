import sys
import time
import serial
global port
global cmd_string
try:
  #port = serial.Serial('COM3',115200,None,'EIGHTBITS','STOPBITS_ONE')
  port = serial.Serial(port = "COM3", baudrate=115200,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
except:
  sys.stdout.write("Cannot open Port COM3")
  sys.exit()
while True :
  try:
    # request command
    port.write(17) # XON
    req = "req\r\n".encode("utf-8")
    port.writelines(bytes(req))
    # get command 
    cmd_string = port.readline().decode("utf-8") 
    sys.stdout.write(cmd_string)
    #port.write(19) # XOFF

  except  Exception as e:
    sys.stdout.writelines(str(e))
    break