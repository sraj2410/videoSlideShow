import os
from moviepy.editor import VideoFileClip


def play_slideshow(folder_path):
    # Get all video files in the folder
    video_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') or f.endswith('.avi') or f.endswith('.mov')]

    for video in video_files:
        video_path = os.path.join(folder_path, video)
        clip = VideoFileClip(video_path)
        clip.preview()
        clip.close()  # Close the video after preview


if __name__ == "__main__":
    folder_path = '/Users/rajeev/Desktop/Temp'  # Change this to the path of your folder
    play_slideshow(folder_path)
