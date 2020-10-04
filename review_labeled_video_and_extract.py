#!/usr/bin/env python3
"""
See the repo for general information.
https://github.com/kevin-allen/review_labeled_video_and_extract

The script takes 3 arguments which are 3 file names.

f: forward
b: backward
s: save frame

"""

import argparse
import os
import cv2
import numpy as np
from math import trunc


parser = argparse.ArgumentParser()
parser.add_argument("labeled_video_name",help="A video with labels on the tracked objects")
parser.add_argument("unlabeled_video_name",help="The same video but without the label")
parser.add_argument("output_video_name",help="The output video with the selected frames")

args = parser.parse_args()

print(args.labeled_video_name)
print(args.unlabeled_video_name)
print(args.output_video_name)


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(args.labeled_video_name)

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# read one frame to get the size
ret, frame = cap.read()
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float


# move back so that the user can see this frame
current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)-1
cap.set(cv2.CAP_PROP_POS_FRAMES,current_frame)


frame_list=[]
while cap.isOpened():
  # Read video capture
  ret, frame = cap.read()

  if ret == False:
    break
  next_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
  current_frame = next_frame - 1
  previous_frame = current_frame - 1
  
  # add frame number to video
  cv2.putText(frame,  
              "{0}".format(current_frame),  
              (50, 50),  
              cv2.FONT_HERSHEY_SIMPLEX, 1,  
              (255, 255, 255),  
              2,  
              cv2.LINE_AA) 
  
  
  # Display each frame
  cv2.imshow("video", frame)
  
  # show one frame at a time
  key = cv2.waitKey(0)
  while key not in [ord('q'), ord('f'), ord('b'), ord('s')]:
    key = cv2.waitKey(0)
    # Quit when 'q' is pressed
    if key == ord('q'):
      break
    if key == ord('b'):
      if previous_frame >= 0:
        cap.set(cv2.CAP_PROP_POS_FRAMES, previous_frame)
    if key == ord('s'):
      print("frame {} selected".format(int(current_frame)))
      frame_list.append(current_frame)
   
cap.release()


if(len(frame_list)>0):
  print("Creating video with {} selected frames".format(len(frame_list)))
  print("File name {}".format(args.output_video_name))

  cap = cv2.VideoCapture(args.unlabeled_video_name)
  # Check if camera opened successfully
  if (cap.isOpened()== False): 
    print("Error opening video stream or file")
    
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(args.output_video_name, fourcc , 30.0, (int(width),int(height)))
        
    for index in frame_list:
      cap.set(cv2.CAP_PROP_POS_FRAMES, index)
      ret, frame = cap.read()
      out.write(frame)

    # When everything done, release the video capture object   
    out.release()
    cap.release()
      
# Closes all the frames
cv2.destroyAllWindows()
