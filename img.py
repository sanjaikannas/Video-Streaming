import cv2
from datetime import datetime
def start(frame):
    '''framesize = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("video.mp4", fourcc, 20, framesize)'''
    #_, frame = cap.read()
    time = datetime.now().strftime(' %Y-%b-%d-%H-%S-%f')
    cv2.imwrite('img'+str(time)+".jpg", frame)