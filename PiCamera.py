from datetime import datetime
#from picamera import PiCamera()
from time import sleep

camera = Picamera()
dateStamp = "{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}-{0:%S}".format(datetime.now())
#type(dateStamp)
camera.capture('home/pi/selfie'+dateStamp+'.png'
camera.close()
