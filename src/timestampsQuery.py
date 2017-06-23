import runFacesApi
'''
images = [ 'https://www.photocase.de/fotos/1384797-badewanne-mensch-kind-nackt-photocase-stock-foto-gross.jpeg',
     'http://image.afcdn.com/dossiers/D20090902/Psycho-Frage5-192807_L.jpg',
     'http://www.laltraitalia.it/wp-content/uploads/2015/10/michelle-hunziker_1-251x170.jpg',
     'https://cd6.aponet.de/uploads/pics/9629_senior_froehlich_main.jpg'
    ]
'''

images = ['../images/video1/00-01-13_f1.jpg',
'../images/video2/00-02-13_f2.jpg',
'../images/video3/00-03-15_f3.jpg',
'../images/video4/00-01-16_f4.jpg']

'''
images = ['video1/00-01-13-f1.jpg',
'video2/00-02-13-f2.jpg',
'video3/00-03-15-f3.jpg',
'video4/00-01-16-f4.jpg']
'''
print('timestamps: ', runFacesApi.returnTimestamps(images))