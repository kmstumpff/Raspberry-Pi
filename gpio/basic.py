#!/usr/bin/python

from imgproc import *

Res_Width = 320
Res_Height = 240

my_camera = Camera(Res_Width,Res_Height)

my_image = my_camera.grabImage()

my_view = Viewer(mt_image.width, my_image.height, "Basic image processing")

my_view.displayImage(my_image)

waitTime(5000)


