import os
import cv2

img_root = 'DATA/images'
img_files = 'DATA/imglist.txt'
fps = 24    

videoWriter = cv2.VideoWriter('kitti.avi', -1, fps, (1248,384))

f = open(img_files)

for i in f:
    frame = cv2.imread(img_root+'/'+i.split('\n')[0])
    videoWriter.write(frame)

videoWriter.release()
