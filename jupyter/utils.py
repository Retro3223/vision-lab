import numpy
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

def imshow(bgr):
    if len(bgr.shape) == 2:
        imshowgray(bgr)
    else:
        rgb = numpy.fliplr(bgr.reshape(-1,3)).reshape(bgr.shape)
        plt.imshow(rgb)
    
def imshowgray(gray):
    plt.imshow(gray, cmap=cm.gray)
