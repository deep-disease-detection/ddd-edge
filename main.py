import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import QTimer
import cv2
import glob
import random
import time
from core.send_to_cloud import send_image_to_cloud, get_image_base64
from core.utils_images import load_random_image, read_images, load_images
import threading



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title
        self.setWindowTitle("Image Processing")
        # set the geometry of the window
        self.setGeometry(0, 0, 600, 600)

        # Create a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, 300, 300)
        self.image_label.setPixmap(QPixmap("image.jpg"))

        # Create a button to trigger a function
        self.button = QPushButton("Process Image", self)
        self.button.setGeometry(50, 400, 100, 50)
        self.button.clicked.connect(self.process_image)

        # create a timer to update the image
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_image)
        self.timer.start(5000)



    def process_image(self):
        # Add your image processing code here
        random_image = load_random_image()
        #send_image_to_cloud(random_image)
        # display the image on the label
        self.image_label.setPixmap(QPixmap(random_image))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
