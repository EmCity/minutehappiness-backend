from ffmpy import FFmpeg
import os
from multiprocessing import Pool


os.chdir('video')

folders = os.listdir(os.getcwd())
print(folders)

def convert_to_picture(video_id):
    if not os.path.isfile(str(video_id) + '/output.mp4'):
        return
    ff = FFmpeg(
        inputs={str(video_id) + '/output.mp4': None},
        outputs={str(video_id) + '/img%03d.jpg': '-qscale:v 4 -vf fps=1'})
    print(ff.cmd)
    ff.run()
    os.remove(str(video_id) + '/output.mp4')


if __name__ == '__main__':
    p = Pool(6)
    p.map(convert_to_picture, folders)