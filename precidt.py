'''
Author: Egrt
Date: 2022-03-18 10:12:19
LastEditors: Egrt
LastEditTime: 2022-03-18 11:07:27
FilePath: \Polygonization-by-Frame-Field-Learning\precidt.py
'''
import os
images_dir   = 'images/val/images'
images_path  = os.listdir(images_dir)
for index, image_name in enumerate(images_path):
    if index<100:
        image_path = os.path.join(images_dir, image_name)
        os.system('')