import cv2
#-----------------------#
frameWidth = 640
frameHeight = 480
minArea = 500
color = (255, 0, 255)
woodCascade = cv2.CascadeClassifier("cascade_wood.xml")
#-----------------------#
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()

    #cascade classifier method
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tastyWood = woodCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in tastyWood:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, "Mmmmmh Tasty", (x, y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = img[y:y+h,x:x+h]
            cv2.imshow("ROI", imgRoi)


    cv2.imshow("Result", img)

    #press the 's' key to save a Morsel to the WoodChips folder in Resources
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/WoodChips/morselNo."+str(count)+".jpg", imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(255,255,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count += 1

    #press q after clicking on the 'Result' video feed to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
