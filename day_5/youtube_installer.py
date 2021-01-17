from pytube import YouTube
from day_5.youtube_functions import download_video


video_url = input('Enter Video URL:\t')
video = YouTube(video_url)
video = video.streams.first()
download_video(video)
