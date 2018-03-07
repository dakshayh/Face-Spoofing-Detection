import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import get_pixel
import lbp_calculate


def main():
    imageDir = "/home/ubuntu/Desktop/Face Spoofing/data_normal/test_normal/001" #specify your path here
    image_path_list = []
    for file in os.listdir(imageDir):
        image_path_list.append(os.path.join(imageDir, file))
    out_list=[]
    outDir = "/home/ubuntu/Desktop/Face Spoofing/dataset/test_lbp/001"	#specify the directory where the images should be stored
    d=1

#loop through image_path_list to open each image
    for imagePath in image_path_list:
        img_bgr = cv2.imread(imagePath)
        
        height, width, channel = img_bgr.shape
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        
        img_lbp = np.zeros((height, width,3), np.uint8)
        for i in range(0, height):
            for j in range(0, width):
                img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
                hist_lbp = cv2.calcHist([img_lbp], [0], None, [256], [0, 256])
                output_list = []
        
        output_list.append({
        "img": img_lbp,
        "xlabel": "",
        "ylabel": "",
        "xtick": [],
        "ytick": [],
        "title": "LBP Image",
        "type": "gray"
        })    
        
        
        cv2.imwrite(os.path.join(outDir,'001_%d.jpg'%d),img_lbp) #numbering the images
        d+=1

if __name__ == '__main__':
        main()
