import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
from os import listdir, walk
from os.path import isfile, join
import csv
# img_list = [f for f in listdir('./data/') if isfile(join('./data/', f))]
# print(img_list)
with open('ic.csv', "w+") as csvFile:
    spamwriter = csv.writer(csvFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    print(walk('~/Dynamic-Vision-Transformer/data/val/1/'))
    for a in walk('~/Dynamic-Vision-Transformer/data/val/1/'):
        print(a)
    for (dirpath, dirnames, filenames) in walk('~/Dynamic-Vision-Transformer/data/val/1/'):
        print(1)
        print(dirpath, dirnames, filenames)
        index = 0
        for img in filenames:
            img = cv.imread(dirpath + img, index)
            edges = cv.Canny(img,224,224)
            ic = -1 * math.log2(sum(sum(edges)))
            spamwriter.writerow(ic)
            index += 1
            print(ic)
    for (dirpath, dirnames, filenames) in walk('~/Dynamic-Vision-Transformer/data/val/2/'):
        print(dirpath, dirnames, filenames)
        index = 0
        for img in filenames:
            img = cv.imread(dirpath + img, index)
            edges = cv.Canny(img,224,224)
            ic = -1 * math.log2(sum(sum(edges)))
            spamwriter.writerow(ic)
            index += 1
            print(ic)
    for (dirpath, dirnames, filenames) in walk('~/Dynamic-Vision-Transformer/data/val/3/'):
        print(dirpath, dirnames, filenames)
        index = 0
        for img in filenames:
            img = cv.imread(dirpath + img, index)
            edges = cv.Canny(img,224,224)
            ic = -1 * math.log2(sum(sum(edges)))
            spamwriter.writerow(ic)
            index += 1
            print(ic)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()