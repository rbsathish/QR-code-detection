import cv2
from PIL import Image
from pyzbar.pyzbar import decode
import numpy as np
# img = cv2.imread('3.jpg')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

########### for data checking ##############
with open('Data.txt') as f:
    myDataList = f.read().splitlines()
# print(myDataList)
# mycolor = (0,0,255)

while True:
    success,img = cap.read()
    for barcode in decode(img):
        # print("im in loop")
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in myDataList:
            myOutput = 'Authorized'
            mycolor = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            mycolor = (0,0,255)
            
        pts = np.array([barcode.polygon],np.int32)
        # print(pts)
        pts = pts.reshape((-1,1,2))
        # print(pts)
        cv2.polylines(img,[pts],True,mycolor,5)
        pts2 = barcode.rect 
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.9,mycolor,2)
    cv2.imshow("QR",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
        