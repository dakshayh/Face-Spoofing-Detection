import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import caffe as cf

cf.set_mode_cpu()
#loading the network
net=cf.Net('conv.prototxt',cf.TEST)
print (net.blobs['conv'].data.shape)
