import requests

youtube_url = 'https://www.youtube.com/watch?v='

url_endpoint = 'https://www.googleapis.com/youtube/v3/search/'

query = ["happy", "nice", "fun", "nice"]

out_file = open('url.txt', 'a')

for q in query:
    payload = {'part': 'snippet', 'q': q, 'maxResults': 30, 'key': 'AIzaSyBnVHKbVsAm7wLxo8h6rbyhoDLIodZRW2c'}

    r = requests.get(url_endpoint, params=payload)

    print(r.json())



    for item in r.json()['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            out_file.write(str(youtube_url) + str(video_id) + "\n")