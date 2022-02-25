import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import math
from os import listdir, walk
from os.path import isfile, join
import csv
# img_list = [f for f in listdir('./data/') if isfile(join('./data/', f))]
# print(img_list)
def count_average_ic():
    with open('ic.csv', "r") as csvFile:
        spamreader = csv.reader(csvFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        ic_list = []
        for i in spamreader:
            # print(i)
            ic_list.append(float(i[0]))
            if len(ic_list) == 2495:
                print(sum(ic_list)/2495)
            elif len(ic_list) == 1595 + 2495:
                print(sum(ic_list[2495:])/1595)
            elif len(ic_list) == 1595 + 2495 + 985:
                print(sum(ic_list[1595 + 2495:]) / 985)
def count_ic():
    with open('ic.csv', "w+") as csvFile:
        spamwriter = csv.writer(csvFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        img_list_1 = [f for f in listdir('/home/ubuntu/Dynamic-Vision-Transformer/data/val/1/') if isfile(join('/home/ubuntu/Dynamic-Vision'
                                                                                                  '-Transformer/data/val/1/', f))]
        index = 0
        for img in img_list_1:
            img = cv.imread('/home/ubuntu/Dynamic-Vision-Transformer/data/val/1/' + img, index)
            edges = cv.Canny(img, 224, 224)
            ic = [-1 * math.log2(sum(sum(edges)))]
            spamwriter.writerow(ic)
            index += 1
            print(ic)

        img_list_2 = [f for f in listdir('/home/ubuntu/Dynamic-Vision-Transformer/data/val/2/') if isfile(join('/home/ubuntu/Dynamic-Vision'
                                                                                                  '-Transformer/data/val/2/', f))]
        index = 0
        for img in img_list_2:
            img = cv.imread('/home/ubuntu/Dynamic-Vision-Transformer/data/val/2/' + img, index)
            edges = cv.Canny(img, 512, 512)
            ic = [-1 * math.log2(sum(sum(edges)))]
            spamwriter.writerow(ic)
            index += 1
            print(ic)

        img_list_3 = [f for f in listdir('/home/ubuntu/Dynamic-Vision-Transformer/data/val/3/') if isfile(join('/home/ubuntu/Dynamic-Vision'
                                                                                                  '-Transformer/data/val/3/', f))]
        index = 0
        for img in img_list_3:
            img = cv.imread('/home/ubuntu/Dynamic-Vision-Transformer/data/val/3/' + img, index)
            edges = cv.Canny(img, 512, 512)
            ic = [-1 * math.log2(sum(sum(edges)))]
            spamwriter.writerow(ic)
            index += 1
            print(ic)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()
count_ic()
count_average_ic()