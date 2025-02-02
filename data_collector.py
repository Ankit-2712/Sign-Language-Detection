import os
import cv2
import time
import uuid

image_path = "Collected_Image"

labels = ['Hello','Yes','no','Thanks','I_love_U','please']

no_of_images = 10

for label in labels:
    img_path = os.path.join(image_path, label)
    os.makedirs(img_path, exist_ok=True)
    
    # OPEN CAMERA

    cap = cv2.VideoCapture(0)
    print(f"Collecting image for {label}")
    time.sleep(5)

    for imgnum in range(no_of_images):
        ret , frame = cap.read()
        image_name = os.path.join(image_path,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(image_name, frame)
        cv2.imread('frame', frame)
        time.sleep(2)

    cap.release()


                                  





 