# Functions for compiling the final videos

# import cv2
import config as cfg
import pyodbc
from pytube import YouTube
from ffmpy import FFmpeg
import os
import urlparse
import subprocess

vsdir = '../final_videos/'

def _seconds_to_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)

def dbConnect():
    dbc = cfg.DB
    # cnxn = pyodbc.connect('DRIVER='+dbc['driver']+';PORT=1433;SERVER='+dbc['server']+';PORT=1443;DATABASE='+dbc['database']+';UID='+dbc['username']+';PWD='+ dbc['password'], autocommit = False)
    # cursor = cnxn.cursor()
    
def getVideoGroupFromDb(vg_id):
    # TO DO - Make this work with the DB
    dbConnect()
    return[
        {'url':'https://www.youtube.com/watch?v=ZbZSe6N_BXs', 'start':5, 'end':15},
        {'url':'https://www.youtube.com/watch?v=sZVB_zCBlCU', 'start':1, 'end':11},
        {'url':'https://www.youtube.com/watch?v=MOWDb2TBYDg', 'start':6, 'end':16},
        {'url':'https://www.youtube.com/watch?v=kOkQ4T5WO9E', 'start':5, 'end':15},
        {'url':'https://www.youtube.com/watch?v=kJQP7kiw5Fk', 'start':20, 'end':30},
        {'url':'https://www.youtube.com/watch?v=PT2_F-1esPk', 'start':45, 'end':55}
    ]

def getVideoFile(vid_data, vdir):
    yt = YouTube(vid_data["url"])
    vid_url_data = urlparse.urlparse(vid_data["url"])
    vid_query = urlparse.parse_qs(vid_url_data.query)
    video_yt_id = vid_query["v"][0]
    vfl_name = 'tmp_'+video_yt_id
    yt.set_filename(vfl_name)
    video = yt.get('mp4', '720p')
    if not os.path.exists(vdir):
        os.makedirs(vdir)
    if os.path.exists(vdir + '/' + vfl_name + '.mp4'):
        os.remove (vdir + '/' + vfl_name + '.mp4')
    video.download(vdir + '/')
    parseVideo(vdir + '/' + vfl_name + '.mp4', 
                vdir + '/' + vfl_name+'_cut.mpg',
                str(_seconds_to_time(vid_data['start'])),
                str(_seconds_to_time(vid_data['end']-vid_data['start'])))
    return vfl_name+'_cut.mpg'
    
def parseVideo(in_file, out_file, s_time, e_time):
    if os.path.exists(out_file):
        os.remove (out_file)
    ff = FFmpeg(
        inputs={in_file: None},
        outputs={out_file: '-ss '+s_time+ ' -t '+e_time + ' -async 1 -qscale:v 1' })
    ff.run()
    os.remove(in_file)
    
def compileVideoGroup(vg_id):
    videos = getVideoGroupFromDb(vg_id)
    vg_id = str(vg_id)
    ccstr = '"concat:'
    vdir = vsdir + vg_id
    for vid_data in videos:
        fl = getVideoFile(vid_data, vdir)
        ccstr += fl + '|'
        vid_data['fl_name'] = fl
    ccstr = ccstr[:-1] + '"'
    os.chdir(vdir)
    subprocess.call('ffmpeg -i '+ccstr+' -c copy output.mpg', shell=True)
    for vid_data in videos:
        os.remove(vid_data['fl_name'])
        

def makeVideo(vg_id):
    compileVideoGroup(vg_id)

makeVideo(1)
