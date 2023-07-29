import cv2
import argparse
import os
def start():
    ap = argparse.ArgumentParser()
    ap.add_argument("-ext", '--extension', required=False,default='jpg')
    ap.add_argument('-o', "--output", required=False, default='finalout.mp4')
    args= vars(ap.parse_args())
    path = '.'
    ext = args['extension']
    output = args['output']
    image = []
    for f in os.listdir(path):
        if f.endswith(ext):
            image.append(f)
    imgpath = os.path.join(path, image[0])
    frame = cv2.imread(imgpath)
    height, width, channel = frame.shape
    
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output, fourcc, 10, (width, height))

    for i in image:
        imgpath = os.path.join(path, i)
        frame = cv2.imread(imgpath)
        out.write(frame)