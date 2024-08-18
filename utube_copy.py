import cv2
# import cvzone

cap = cv2.VideoCapture(0)
custom_width = 1280
custom_height = 720
cap.set(3, custom_width)
cap.set(4, custom_height)

while True:
    imgBG = cv2.imread("Resources/MTC_bg.png")
    imgBG = cv2.resize(imgBG, (custom_width, custom_height))
    success, img = cap.read()
    imgScaled = cv2.resize(img,(0,0),None,0.625,0.625)
    imgScaled = imgScaled[:,229:491]

    imgBG[160:610,868:1130] =imgScaled

    cv2.imshow("Image",img)
    cv2.imshow("BG",imgBG)
    cv2.waitKey(1)