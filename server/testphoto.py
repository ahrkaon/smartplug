from socket import *
from os.path import exists
import os
import sys
from picamera2 import Picamera2, Preview
import time
#import testClient
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import imgsend

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size":(640,480)}, lores={"size":(640, 480)}, display="lores")
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
for i in range(10):
    i = i + 1
    time.sleep(0.5)
    picam2.capture_file(f"test{i}.jpg")
picam2.stop()
#testClient.recieve()
imgsend.imgSend()
