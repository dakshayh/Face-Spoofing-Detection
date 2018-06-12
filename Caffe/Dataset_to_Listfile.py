import numpy as np
import os
 
CURRENT_DIR = os.path.abspath(os.path.dirname('/home/ubuntu/caffe/data/DogsCats/'))
DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'train'))
TXT_DIR = CURRENT_DIR
DATA_DIR1 = os.path.abspath(os.path.join(CURRENT_DIR,'train/dog'))
DATA_DIR2 = os.path.abspath(os.path.join(CURRENT_DIR,'train/cat'))

dog_images = [image for image in os.listdir(DATA_DIR1)]
cat_images = [image for image in os.listdir(DATA_DIR2)]
 
dog_train = dog_images[:5601]
dog_test = dog_images[5601:]
 
cat_train = cat_images[:5601]
cat_test = cat_images[5601:]
 
with open('{}/train.txt'.format(TXT_DIR), 'w') as f:
    for image in range(0,5601):
        f.write('/dog/{}.jpg 0\n'.format(image))
    for image in range(0,5601):
        f.write('/cat/{}.jpg 1\n'.format(image))
 
with open('{}/text.txt'.format(TXT_DIR), 'w') as f:
    for image in range(5601,8002):
        f.write('/dog/{}.jpg 0\n'.format(image))
    for image in range(5601,8002):
        f.write('/cat/{}.jpg 1\n'.format(image))
