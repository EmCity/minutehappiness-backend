import runFacesApiSlidingWindow as runFacesApi
import writeToDBSlidingWindow as writeToDB
import json
import os
import glob
import operator


'''
images = ['../images/video1/00-01-13_f1.jpg',
'../images/video2/00-02-13_f2.jpg',
'../images/video3/00-03-15_f3.jpg',
'../images/video4/00-01-16_f4.jpg']

images = ['../images/video1/1.jpg',
'../images/video2/2.jpg',
'../images/video3/3.jpg',
'../images/video4/4.jpg']
'''
video_length = 10 #in seconds
folder = '../images/'
tracks = {}
for root, dirs, files in os.walk(folder):
	#print("Hallo")
	if root != '../images/':
		#frames += glob.glob(os.path.join(root, '*.jpg'))
		#print("frames: ", frames)
		print root
		#print dirs
		print files
		frames = []
		frames += glob.glob(os.path.join(root, '*.jpg'))
		tracks[root] = frames
		#for dir in dirs:
			#for root, dirs, files in os.walk(folder+"/"+)
#print(tracks)

for f in tracks:
	#print("folder: ", f)
	#print(type(tracks))
	images = tracks[f]
	
	#for root, dirs, files in os.walk(folder):
	#		frames += glob.glob(os.path.join(root, '*.jpg'))
	#	print("frames: ", frames)
	#print(images)
	result = runFacesApi.returnTimestamps(images)
	#print("result", result)
	#print result
	#att = result[0][1]
	#d = json.loads(att)
	#attJson = json.loads(att)
	#print(att)
	#smile = d[0]['faceAttributes']['smile']
	#print(type(d[0]))
	#print(json.loads(att))
	#writeToDB.writeDB(result, video_length) #write data to DB
	videos = []
	#Get the folder name
	if len(result) >= 10:	
		scores = []
		for r in result:
			video = []
			#att = result[0][1]
			d = json.loads(r[1])
			print("d", d)
			filename = r[0].split('/')
			frames = []
			folder = filename[0]+"/"+filename[1]+"/"+filename[2]+"/"
			print(folder)
			#for root, dirs, files in os.walk(folder):
			#	frames += glob.glob(os.path.join(root, '*.jpg'))
			#print("frames: ", frames)
			print(filename)
			video_url = filename[2]
			start_time = filename[3].split('.')[0]
			#attJson = json.loads(att)
			#print(att)
			if d:
				smile = d[0]['faceAttributes']['smile']
				if(smile > 0.0):
					#video = [video_url, str(start_time), str(int(start_time)+video_length)]
					scores.append(smile)
				#videos.append(video)
		sums = []
		idx = 0
		for score in scores:
			if idx+video_length < len(scores):
				cnt = 0
				for n in range(idx, idx+video_length):
					cnt += scores[n]
			sums.append(cnt)
			idx = idx + 1
		print("sums", sums, type(sums))
		max_index, max_value = max(enumerate(sums), key=operator.itemgetter(1))
		print('max_index', max_index, 'max_value', max_value)
		video = [video_url, str(max_index), str(int(max_index)+video_length)]
		videos.append(video)
		#videos array is an array of (video_url, start_time, end_time) values
		writeToDB.writeDB(videos)