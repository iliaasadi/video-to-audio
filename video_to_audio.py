from moviepy.editor import *

# Alert
print("Alert:\nBefore you do the conversion, you should put your video near this file.\n\nPress enter to continue...")
input()

# Enter Video Name
video_name = input("Enter your video name (with format): ")

# Enter Audio Output Name
audio_output_name = "Audio.mp3"

video = VideoFileClip(video_name)
audio = video.audio

print("Please wait!")
audio.write_audiofile(audio_output_name)

video.close()
audio.close()

print("Done!")
input()
