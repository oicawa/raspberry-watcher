import RPi.GPIO as GPIO
import time
import os
#
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_UP)

status_26 = 1
count_pressed_26 = 0
 
try:  
 
  while True:
    status_26 = GPIO.input(26)
 
    if (status_26):
      count_pressed_26 = 0
    else:
      count_pressed_26 += 1
 
    print('status_26={}, count_pressed_26={}'.format(status_26, count_pressed_26))

    if(5 <= count_pressed_26):
      os.system("sudo shutdown -h now")
      #print("sudo shutdown -h now")
      break
 
    time.sleep(1.0)
 
except KeyboardInterrupt:  
  GPIO.cleanup()
 
GPIO.cleanup()
