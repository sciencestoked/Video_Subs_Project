import cv2
import numpy as np

vid_obj = cv2.VideoCapture("touhou-bad-apple-touhou.gif")

go_on = True
while go_on:
    
    success, vid_frame = vid_obj.read()
    go_on=success
    cv2.imshow("win",vid_frame)

    pixcount=0
    whitecount=0
    blackcount=0

    for y in vid_frame :
        for x in y:
            pixcount+=1
            thresh=127
            if ((x[0]>thresh) or ((x[1]>thresh) or (x[2]>thresh))):
                whitecount+=1
            else:
                blackcount+=1

    if (whitecount > pixcount/2):
        print('White')
    if (blackcount > pixcount/2):
        print('Black')
    
    cv2.waitKey(20)

