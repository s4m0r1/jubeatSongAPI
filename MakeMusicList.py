
from script import make_musicList
import requests
import lxml.html


if __name__ == "__main__":
  songList = []
  for i in range(3):
    target_url = f"https://p.eagate.573.jp/game/jubeat/festo/information/music_list2.html?page={i}"
    r = requests.get(target_url)
    print(r.text)
    html = lxml.html.fromstring(r.text)
    print(html)
    songList.append(make_musicList.fetchSongdata(html))
    
  print(songList[0][9].encode('cp932', "ignore").decode('utf-8', "ignore"))
