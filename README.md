# dlc_review_labeled_video
Python script allowing you to review a video labelled from DeepLabCut and created a new video with mislabeled frames to improve your model.

I often find that DeepLabCut does a very good job at tracking my target objects but there are always mislabeled frames. These are often associated with relatively rare events that were not included in the training set. 

The main goal of the script is to create videos of challenging rare events for your network. You can then use frames of this video to retrain your network to improve it.


## Instruction

1. Label some frames from videos using DeepLabCut.
1. First train your network using DeepLabCut as described on the DeepLabCut website.
2. Use your trained network to analyze and label a video. 
3. Use dlc_review_labeled_video to identify mislabeled frames and store them in a new video.
4. Add the new videos to your DeepLabCut project, extract some frames to be labeled from these new videos.
5. Label the new frames.
6. Retrain you network and hopefully get better results!

## Example case

I train a network with DeepLabCut 
