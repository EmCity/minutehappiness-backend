import runFacesApi
import json
import pyodbc

'''
images = ['../images/video1/00-01-13_f1.jpg',
'../images/video2/00-02-13_f2.jpg',
'../images/video3/00-03-15_f3.jpg',
'../images/video4/00-01-16_f4.jpg']

result = runFacesApi.returnTimestamps(images)
#print result
att = result[0][1]
d = json.loads(att)
#attJson = json.loads(att)
#print(att)
smile = d[0]['faceAttributes']['smile']
#print(type(d[0]))
#print(json.loads(att))
'''

def writeDB(result, smile):
	server = 'dbhappy.database.windows.net'
	database = 'db_happyness'
	username = 'hackathon_ai'
	password = 'Happynessdbpwd1$'
	driver= '{ODBC Driver 13 for SQL Server}'
	cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password, autocommit = False)
	#cnxn = pyodbc.connect("Driver="+driver+";Server=tcp:dbhappy.database.windows.net,1433;Database=db_happyness;Uid=hackathon_ai@dbhappy;Pwd=Happynessdbpwd1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
	cursor = cnxn.cursor()

	for img in result:
		#print("img: ", img)
		d = json.loads(img[1])
		#print("d: ", img, img)
		if d:
			smile = d[0]['faceAttributes']['smile']
			print("smile: ", smile)
			with cursor.execute("INSERT INTO videos (VIDEO_URL, START_TIME, END_TIME) VALUES ('"+img[0]+"',"+str(img[3])+","+str(smile)+")"): 
			    print ('Successfuly Inserted!')
			cnxn.commit()


	cursor.execute("SELECT VIDEO_URL, START_TIME, END_TIME FROM videos")
	row = cursor.fetchone()
	while row:
	    print str(row)
	    row = cursor.fetchone()
			

