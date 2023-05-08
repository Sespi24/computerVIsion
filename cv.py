import os
import numpy as np
import cv2 as cv
import pandas as pd
import matplotlib.pyplot as plt

#Figure out a way to check against a list of known directories and let user know errors before execution

'''def enterFolder():
    folder = input("Enter image folder name:")
    dir = os.chdir(folder)
    return(dir)'''

#filename = 'checkerboard.png'

'''img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]

cv.imwrite('subpixel5.png',img)'''

def getItDone():
    #enterFolder()
    try:
        #imgList = os.listdir()
        img = cv.imread('andrew.PNG')
            #cv.imwrite(x, cv.cvtColor(img, cv.COLOR_RGB2BGR)) <= Rewrites the images in the folder to BGR
        rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #Converts BGR to RGB
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        #Plotting
        plt.subplot_mosaic([[rgb, img, gray]])

        plt.show()
    except:
        print("Error 404. Folder not found.\nPlease enter another folder.")
getItDone()

'''def getItDone():
    enterFolder()
    try:
        imgList = os.listdir()
        for x in imgList:
            img = cv.imread(x)
            #cv.imwrite(x, cv.cvtColor(img, cv.COLOR_RGB2BGR)) <= Rewrites the images in the folder to BGR
            rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #Converts BGR to RGB

            #Plotting
            
            plt.imshow(rgb)
            plt.show()
    except:
        print("Error 404. Folder not found.\nPlease enter another folder.")
#getItDone()'''
