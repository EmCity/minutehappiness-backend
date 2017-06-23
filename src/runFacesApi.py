########### Python 2.7 #############
import httplib, urllib, base64, json

def returnTimestamps(images=[]):

    '''
    key2 = b732bb7fff014564b28ee52efb065c8a
    '''

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'a6f69a1966df4dbabe11bfa71138b1d7',
    }

    params = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'smile,emotion',
    })
    '''
    images = [ 'https://www.photocase.de/fotos/1384797-badewanne-mensch-kind-nackt-photocase-stock-foto-gross.jpeg',
     'http://image.afcdn.com/dossiers/D20090902/Psycho-Frage5-192807_L.jpg',
     'http://www.laltraitalia.it/wp-content/uploads/2015/10/michelle-hunziker_1-251x170.jpg',
     'https://cd6.aponet.de/uploads/pics/9629_senior_froehlich_main.jpg'
    ]
    '''

    for img in images: 
        body = {
            'url': img
        }
        bodydata = json.dumps(body)
        try:
            url = 'westeurope.api.cognitive.microsoft.com'
            #body = 'https://cd6.aponet.de/uploads/pics/9629_senior_froehlich_main.jpg'
            #conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn = httplib.HTTPSConnection(url)
            #print("Laeuuft")
            conn.request("POST", "/face/v1.0/detect?%s" % params, bodydata, headers)
            #print('Nach request')
            response = conn.getresponse()
            data = response.read()
            #print('reading response.')
            print('data: ', data)
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        #i = i + 1

