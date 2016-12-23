import Image
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

class Invoice(object):

    filename = 'D:\\02_code_program\\05_python\\image\\temp1.jpg'
    def __init__(self):
        self.filename = 'D:\\02_code_program\\05_python\\image\\temp1.jpg'
        self.image_size = 28


    def digitPicDiv(self,filename,saveDir='D:\\02_code_program\\05_python\\image\\divs\\'):
        if(filename != None):
            self.filename = filename
        im = Image.open(self.filename)
        width = im.size[0]
        height = im.size[1]
        print "/* width:%d */"%(width)
        print "/* height:%d */"%(height)
        step = width/8.0
        divFileName = filename.split("\\")[-1]
        for i in range(8):
            box = (int(step * i), 0, int(step * (i+1)), int(height))
            region = im.crop(box)
            region.save(saveDir+str(i)+"_"+divFileName)
        print "over"


    def digitPicDivDir(self,dir):
        a = os.listdir(dir)
        b = [x for x in a if os.path.isfile(dir + x)]
        print b
        for tempfile in b:
            self.digitPicDiv(dir+tempfile)


    def singleDigitPicNormalized(self,filename):
        region = Image.open(filename)
        region = region.convert('L')
        region = np.array(region)
        height, width = np.shape(region)
        w_surplus = self.image_size - width
        w_append_left = np.ceil(w_surplus / 2)
        w_append_right = w_surplus - w_append_left
        region = np.hstack((np.zeros((height, w_append_left)) + 255, region, np.zeros((height, w_append_right)) + 255))
        region = np.reshape(region, 784)
        print 'test'

def plot(region):
    fig = plt.figure();
    fig.add_subplot(1, 1, 1);
    plt.imshow(region, cmap='gray');
    plt.show()

if __name__ == '__main__':
    test = Invoice()
    # test.singleDigitPicNormalized()
    dir = "D:\\02_code_program\\05_python\\image\\orgSeries\\"
    filename = "D:\\02_code_program\\05_python\\image\\0265.jpg"
    filenames = filename.split("\\")
    print filenames[-1]
    test.digitPicDivDir(dir)

