from ffmpy import FFmpeg
import os

os.chdir('video')

folders = os.listdir(os.getcwd())
print folders

for video in folders:
	 if not os.path.isfile(str(video) + '/output.mp4'): 
	 	continue
	 ff = FFmpeg(
	 	inputs={str(video) + '/output.mp4': None},
	 	outputs={str(video) + '/img%03d.jpg': '-vf fps=4'})
	 print ff.cmd
	 ff.run()