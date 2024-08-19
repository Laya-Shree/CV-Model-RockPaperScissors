import cv2
import cvzone
import supervision as sv
from ultralytics import YOLOv10
import os
import time
import random

model = YOLOv10(f'best.pt')

def readPlayer():
    ret, frame = cap.read()
    imgScaled = cv2.resize(frame,(0,0),None,0.625,0.625)
    imgScaled = imgScaled[:,229:491]  
    return ret,imgScaled

timer = 0
stateResult = False
startGame = False
scores = [0,0]

cap = cv2.VideoCapture(0)
custom_width = 1280
custom_height = 720
cap.set(3, custom_width)
cap.set(4, custom_height)

bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

if not cap.isOpened():
    print("Unable to read camera feed")

playerMove=" "
while True:
    imgBG = cv2.imread("Resources/MTC_bg.png")
    imgBG = cv2.resize(imgBG, (custom_width, custom_height))
    ret, player_image=readPlayer()
    if not ret:
        break

    if startGame:
        if stateResult is False:
            timer = int(time.time() - startTime)
            time_count = {0:"Rock",1:"Paper",2:"Scissor",3:" ",4:" "}
            cv2.putText(imgBG,time_count[timer],(620,440),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
            
            if timer > 2:
                stateResult = True
                timer = 0
                
                results = model(player_image)[0]
                detections = sv.Detections.from_ultralytics(results)

                if(detections.data['class_name'].size):

                    playerMove = detections.data['class_name'][0]

                    randomNumber = random.randint(1,3)
                    AImap = {1:"Rock",2:"Paper",3:"Scissor"}
                    aiMove = AImap[randomNumber]
                    if(aiMove == playerMove):
                        pass
                    elif(aiMove == "Rock" and playerMove == "Scissor") or (aiMove == "Paper" and playerMove == "Rock") or (aiMove == "Scissor" and playerMove == "Paper"):
                        scores[0] += 1
                    else:
                        scores[1] += 1

                    imgAI = cv2.imread(f'Resources/{aiMove}.png',cv2.IMREAD_UNCHANGED)
                    annotated_image = bounding_box_annotator.annotate(scene=player_image, detections=detections)
                    player_image = label_annotator.annotate( scene=annotated_image, detections=detections)

                else:
                    playerMove="Unable to Detect"

    imgBG[160:610,868:1130] = player_image

    if stateResult and detections.data['class_name'].size:
        imgBG = cvzone.overlayPNG(imgBG,imgAI,(250,310))

    cv2.putText(imgBG,str(scores[0]),(370,650),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
    cv2.putText(imgBG,str(scores[1]),(1040,655),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
    cv2.putText(imgBG,str(playerMove),(850,700),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)

    cv2.imshow('Webcam', imgBG)
    k = cv2.waitKey(1)

    if k == ord('s'):
        startGame = True
        stateResult = False
        startTime = time.time()
    if k == ord('r'):
        scores=[0,0]

    if k%256 ==27:
        print("Escape hit, closing...")
        break
    
cap.release()
cv2.destroyAllWindows()