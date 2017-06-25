import requests

youtube_url = 'https://www.youtube.com/watch?v='

url_endpoint = 'https://www.googleapis.com/youtube/v3/search/'

query = ["happy", "laughting", "fun", "nice", "k pop", "smiling"]

out_file = open('url.txt', 'a')

for q in query:
    payload = {'part': 'snippet', 'q': q, 'type': 'video', 'maxResults': 30, 'videoDuration': 'short', 'key': 'AIzaSyBnVHKbVsAm7wLxo8h6rbyhoDLIodZRW2c'}

    r = requests.get(url_endpoint, params=payload)

    print(r.json())



    for item in r.json()['items']:
        if item['id']['kind'] == 'youtube#video':
            video_id = item['id']['videoId']
            out_file.write(str(youtube_url) + str(video_id) + "\n")
