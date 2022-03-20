'''
Author: Egrt
Date: 2022-03-19 10:23:48
LastEditors: Egrt
LastEditTime: 2022-03-20 13:41:53
FilePath: \Luuu\app.py
'''

from gis import GIS
import gradio as gr
import os
os.system('pip install requirements.txt')
from zipfile import ZipFile
gis = GIS()


# --------模型推理---------- #
def inference(filepath):
    filename, file_list = gis.detect_image(filepath)
    with ZipFile("result.zip", "w") as zipObj:
        zipObj.write(file_list[0], "{}.tif".format(filename+'mask'))
        zipObj.write(file_list[1], "{}.tif".format(filename))
        zipObj.write(file_list[2], "{}.pdf".format(filename))
        zipObj.write(file_list[3], "{}.cpg".format(filename))
        zipObj.write(file_list[4], "{}.dbf".format(filename))
        zipObj.write(file_list[5], "{}.shx".format(filename))
        zipObj.write(file_list[6], "{}.shp".format(filename))
        zipObj.write(file_list[7], "{}.prj".format(filename))
    return "images/result.zip"


# --------网页信息---------- #  
title = "基于帧场学习的多边形建筑提取"
description = "目前最先进图像分割模型通常以栅格形式输出分割，但地理信息系统中的应用通常需要矢量多边形。我们在遥感图像中提取建筑物的任务中，将帧场输出添加到深度分割模型中，将预测的帧场与地面实况轮廓对齐，帮助减少深度网络输出与下游任务中输出样式之间的差距。  @Luuuu🐋🐋"
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/2004.14875' target='_blank'>Polygonization-by-Frame-Field-Learning</a> | <a href='https://github.com/JingyunLiang/SwinIR' target='_blank'>Github Repo</a></p>"
example_img_dir  = 'images'
example_img_name = os.listdir(example_img_dir)
examples=[[os.path.join(example_img_dir, image_path)] for image_path in example_img_name if image_path.endswith('.png')]
gr.Interface(
    inference, 
    [gr.inputs.Image(type="filepath", label="待检测图片")], 
    gr.outputs.File(label="检测结果"),
    title=title,
    description=description,
    article=article,
    enable_queue=True,
    examples=examples
    ).launch(debug=True)