import cv2
import glob
import random
import time

from core.send_to_cloud import send_image_to_cloud, get_image_base64

#read images from the camera and display them on the screen
def read_images():
    # initialize the camera
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:    # frame captured without any errors
        cv2.namedWindow("cam-test", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("cam-test", img)
        cv2.waitKey(0)
        cv2.destroyWindow("cam-test")
        cv2.imwrite("filename.jpg",img) #save image


# load imgages from test_images folder and display them on the screen
def load_images():
    # load all the images from the test_images folder
    folders = glob.glob('test_images/*')
    for folder in folders:
        images = glob.glob(folder + '/*')
        for file in images:
            img = cv2.imread(file)
            cv2.namedWindow(file, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(file, img)
            cv2.waitKey(0)
            cv2.destroyWindow(file)

# load images from the images folders and display a rendom images every 5 seconds
def load_random_image():
    # load all the images from the test_images folder
    folders = glob.glob('test_images/*')
    all_images = []
    for folder in folders:
        images = glob.glob(folder + '/*')
        # load a random image from the folder
        file = random.choice(images)
        all_images.append(file)

    random_image = random.choice(all_images)
    return random_image

if __name__ == '__main__':
    while True:

        random_image = load_random_image()
        send_image_to_cloud(random_image)
        print(random_image)
        time.sleep(5)
