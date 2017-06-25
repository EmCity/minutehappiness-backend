from ffmpy import FFmpeg
import os

os.chdir('video')

folders = os.listdir(os.getcwd())
print(folders)

for video in folders:
    if not os.path.isfile(str(video) + '/output.mp4'):
        continue
    ff = FFmpeg(
        inputs={str(video) + '/output.mp4': None},
        outputs={str(video) + '/img%03d.jpg': '-qscale:v 4 -vf fps=1'})
    print(ff.cmd)
    ff.run()
    os.remove(str(video) + '/output.mp4')
