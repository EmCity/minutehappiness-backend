import runFacesApi
import json

images = ['../images/video1/00-01-13_f1.jpg',
'../images/video2/00-02-13_f2.jpg',
'../images/video3/00-03-15_f3.jpg',
'../images/video4/00-01-16_f4.jpg']

result = runFacesApi.returnTimestamps(images)
att = result[0][1]
d = json.loads(att)
#attJson = json.loads(att)
#print(att)
smile = d[0]['faceAttributes']['smile']
#print(type(d[0]))
#print(json.loads(att))
		

