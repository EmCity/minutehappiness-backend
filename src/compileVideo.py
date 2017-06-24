# Functions for compiling the final videos

# import cv2
import config as cfg
import pyodbc
from pytube import YouTube
from ffmpy import FFmpeg
import os
import urlparse

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
        {'url':'https://www.youtube.com/watch?v=sZVB_zCBlCU', 'start':3, 'end':10},
        {'url':'https://www.youtube.com/watch?v=MOWDb2TBYDg', 'start':6, 'end':16},
    ]

def getVideoFile(vid_data, vg_id):
    vdir = '../final_videos/' + vg_id
    yt = YouTube(vid_data["url"])
    vid_url_data = urlparse.urlparse(vid_data["url"])
    vid_query = urlparse.parse_qs(vid_url_data.query)
    video_yt_id = vid_query["v"][0]
    vfl_name = 'tmp-'+video_yt_id
    yt.set_filename(vfl_name)
    video = yt.get('mp4', '720p')
    if not os.path.exists(vdir):
        os.makedirs(vdir)
    if os.path.exists(vdir + '/' + vfl_name + '.mp4'):
        os.remove (vdir + '/' + vfl_name + '.mp4')
    video.download(vdir + '/')
    parseVideo(vdir + '/' + vfl_name + '.mp4', 
                vdir + '/' + vfl_name+'_cut.mp4',
                str(_seconds_to_time(vid_data['start'])),
                str(_seconds_to_time(vid_data['end']-vid_data['start'])))
    
def parseVideo(in_file, out_file, s_time, e_time):
    if os.path.exists(out_file):
        os.remove (out_file)
    ff = FFmpeg(
        inputs={in_file: None},
        outputs={out_file: '-ss '+s_time+ ' -t '+e_time + ' -async 1' })
    ff.run()
    os.remove(in_file)
    
def compileVideoGroup(vg_id):
    videos = getVideoGroupFromDb(vg_id)
    vg_id = str(vg_id)
    for vid_data in videos:
        getVideoFile(vid_data, vg_id)

def makeVideo(vg_id):
    compileVideoGroup(vg_id)

makeVideo(1)
