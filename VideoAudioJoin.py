#pip install moviepy

from moviepy.editor import VideoFileClip,AudioFileClip
from datetime import datetime

#path
videopath='/content/test video.mp4'
audiopath='/content/my_result.mp3'


#read
video=VideoFileClip(videopath)
audio=AudioFileClip(audiopath)

#join
video=video.set_audio(audio)

#write
current_time=str(datetime.now())
video.write_videofile(f"videoAudiojoin{current_time}.mp4")
