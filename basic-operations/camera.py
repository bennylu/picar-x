import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    
    try:
        time.sleep(2)
        camera.capture('foo.jpg')
    finally:
        camera.stop_preview()
