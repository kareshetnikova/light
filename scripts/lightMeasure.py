import time
import picamera 

experiment_number = 0
lamps = ['mercury','tungsten', 'tungsten', 'tungsten','tungsten', 'tungsten']
paper = ['white', '2', '3', '4','5','6']

def prepare_camera():
    with picamera.PiCamera() as camera:
        camera.resolution=(1024, 768)
        camera.start_preview()
        time.sleep(10)
def photo(experiment_name):
    with picamera.PiCamera() as camera:
        camera.resolution=(1024, 768)
        camera.capture('/home/b03-203/Desktop/'+experiment_name+'.png')
print('--for srupe type y--')
a = input()
if a == 'y':
    print('preparing the camera')
    prepare_camera()
    print('camera is ready')
for i in range(6):
    print('--type y')
    a = input()
    if a == 'y':
        print('taking photo for', paper[i],'paper and', lamps[i], 'lamps')
        photo(paper[i]+'-'+lamps[i])
    else:
        break
print('--end the experiment--')
