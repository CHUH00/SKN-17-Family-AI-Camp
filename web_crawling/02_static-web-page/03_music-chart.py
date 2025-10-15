import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime

class MusicEntry:
    def __init__(self, title, artist, img_path):
        self.title = title
        self.artist = artist
        self.img_path = img_path

    def __repr__(self):
        return f'🎵 {self.artist}의 {self.title} | {self.img_path}'

# 1. 노래 제목, 가수, 앨범 커버 이미지 경로 스크래핑
response = requests.get('https://music.bugs.co.kr/chart')
bs = BeautifulSoup(response.text, 'html.parser')

track_list = bs.select('table.trackList tbody tr')

result_list = []

# 2. 앨범 커버 이미지 -> album_images 디렉토리에 저장
for i, song in enumerate(track_list[:30]):
    title = song.select_one('p.title a').text
    artist = song.select_one('p.artist a').text
    # print(title, artist)

    img_src = song.select_one('a.thumbnail img')['src']
    filename = f'album_images/{datetime.now().strftime('%y%m%d_%H%M%S')}_{i + 1}.jpg'
    urlretrieve(img_src, filename)

    music_entry = MusicEntry(title, artist, filename)
    result_list.append(music_entry)

# 3. 30위까지 출력
for result in result_list:
    print(result)