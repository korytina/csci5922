# GOAL: scripted version of jupyter notebook of the same name (as per project reqs)
#   - loads data, parts into 20x20 patches, downscales to 5x5 and then attempts to upscale back to 20x20 
#   - compares loss: original vs cv2.resize vs. sklearn 
# EXAMPLE RUN:
#   python3 baseline.py
# NOTE: close pop-up windows to progress throught the script

import cv2
import numpy as np

# load precip
d = np.load('pr.npy')
print(d.shape)
import matplotlib.pyplot as plt
#plt.imshow(d[0])
#plt.show()

def mse(pic1, pic2):
    ny = len(pic1)
    nx = len(pic1[0])
    a = pic1.reshape(ny*nx)
    b = pic2.reshape(ny*nx)
    #c = np.power(b-a, 2).sum()
    c = np.abs(b-a).sum()
    return c

# break up into many samples
osamples = []    # 20x20 samples
isamples = []   # 5x5 input samples
for t in range(365):
    # rescale to dims divisible by 20, i.e. (166,138)-> (180,140)
    or_img = cv2.resize(d[t],(180,140))
    #plt.imshow(or_img)
    #plt.show()
    for y in range(0,140,20):
        for x in range(0,180,20):
            osample = or_img[y:y+20, x:x+20]
            isample = cv2.resize(osample,(5,5))
            osamples.append(osample)
            isamples.append(isample)
            print ("X,Y:",x, y)
            print (mse(osample, cv2.resize(isample,(20,20))))
            #plt.imshow(osample)
            #plt.show()

# train simple linear model and compare to cv2 NN interpolation
from sklearn import linear_model
regr = linear_model.LinearRegression(normalize=True)
regr.fit(np.reshape(isamples,(len(isamples),5*5)), np.reshape(osamples,(len(osamples),20*20)))

# predict
srs = np.reshape(regr.predict(np.reshape(isamples[0:63],(63,5*5))), (63,20,20))
ii = 0
for iss, sr, orig in zip(isamples[0:63], srs[0:63], osamples[0:63]):
    ii +=1
    print ("PATCH#",ii)
    print ("mse 5x5: n/a")
    print ("mse cvs2:", mse(cv2.resize(iss,(20,20)), orig))
    print ("mse intr:", mse(sr, orig))
    print ("mse orig:", mse(sr, sr))
    f, axarr = plt.subplots(1, 4)
    axarr[0].imshow(iss)
    axarr[1].imshow(cv2.resize(iss,(20,20)))
    axarr[2].imshow(sr)
    axarr[3].imshow(orig)
    plt.show()
