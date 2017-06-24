from pytube import YouTube
import re 
import os
import ffmpy

videos = []

input_file = open('url.txt', 'r')
for line in input_file:
	videos.append(line.rstrip('\n'))

print(videos)

os.chdir('video')


for counter, item in enumerate(videos):
	yt = YouTube(item)
	yt.set_filename('output')
	video = yt.get('mp4', '720p')

	url =  videos[counter]
	regex = re.compile('\=')
	start = regex.search(url).end()
	end =  len(url)
	video_id = url[start:end]
	print(video_id)
	if not os.path.exists(video_id):
		os.makedirs(video_id)
	video.download(str(video_id) + '/')
