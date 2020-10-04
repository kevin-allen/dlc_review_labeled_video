# review_labeled_video_and_extract

Python script allowing you to review a video labelled from a deep neural network (e.g., DeepLabCut) and created a new video with mislabeled frames that can be used to re-train and hopefully improve your model.

I often use DeepLabCut to train neural networks with the aim of tracking animals. The models are often very good most of the time but there are always mislabeled frames. These are often associated with relatively rare events that were not represented in the images used to train the network. 

The main goal of the script is to review your labeled video and create a new video of challenging rare events (possibly mislabeled frames). You can then use the "challenging" video to retrain your network and hopefully improve it.


## Instruction

1. Label some frames from videos using DeepLabCut.
1. First train your network using DeepLabCut as described on the DeepLabCut website.
2. Use your trained network to analyze and label a video. 
3. Use dlc_review_labeled_video to identify mislabeled frames and store them in a new video.
4. Add the new videos to your DeepLabCut project, extract some frames to be labeled from these new videos.
5. Label the new frames.
6. Retrain you network and hopefully get better results!

## Example case

I train a network with DeepLabCut. The object to track was a lever box (a lever for operant conditioning on wheels). After one iteration of training of 226500 iterations, and 90 % of the images in the training set, I got an error of 2.66 and 11.85 pixels for the train and validation set. 

