import server

images = [ 'https://www.photocase.de/fotos/1384797-badewanne-mensch-kind-nackt-photocase-stock-foto-gross.jpeg',
     'http://image.afcdn.com/dossiers/D20090902/Psycho-Frage5-192807_L.jpg',
     'http://www.laltraitalia.it/wp-content/uploads/2015/10/michelle-hunziker_1-251x170.jpg',
     'https://cd6.aponet.de/uploads/pics/9629_senior_froehlich_main.jpg'
    ]

print('timestamps: ', server.returnTimestamps(images))