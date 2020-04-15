import requests
import lxml.html
import sys



target_url = "https://p.eagate.573.jp/game/jubeat/festo/information/music_list2.html"
r = requests.get(target_url)
html = lxml.html.fromstring(r.text)
# x = html.xpath("//*[@id=\"music_list\"]/div[3]/table/tr[1]/*")
# print(x[1].text)

# //*[@id="list_menu"]
# //*[@id="music_list"]/div[2]/table/tbody/tr[1]/td[2]
#//*[@id="music_list"]/div[3]/table/tbody/tr[1]/td[2]

"""
メンテナンスがある時間帯は実行しない
もしくは取得できなかった場合スケージュールを作成し３時間後に取得
"""

if html.xpath("//*[@id=\"music_list\"]/*") == []:
    print("エラー: サイトにアクセスができません。　5:00~7:00の場合は接続先サイトがメンテナンスの場合があります。")
    sys.exit(1)


"""
メインコード

メモ：モジュール化しろ。

文字化け対応
"""

def fetchSongdata(html):
    cnt = len(html.xpath("//*[@id=\"music_list\"]/div/*"))
    song_data = []
    for i in range(cnt):
        i += 2
        if i > 51:    cnt = len(html.xpath("//*[@id=\"music_list\"]/div/*"))
    song_data = []
    for i in range(cnt):
        i += 2
        if i > 51:
            break
        #曲名    
        song_name = html.xpath(f"//*[@id=\"music_list\"]/div[{i}]/table/tr[1]/*")
        song_name = song_name[1].text
        song_data.append(song_name)
        print(song_name.encode)
        
        #アーティスト
        song_art = html.xpath(f"//*[@id=\"music_list\"]/div[{i}]/table/tr[2]/*")
        song_art = song_art[0].text
        song_data.append(song_art)
        
        #レベル
        song_lv = html.xpath(f"//*[@id=\"music_list\"]/div[{i}]/table/tr[3]/td/ul/*")
        cnt_lv = 1
        lv_list = []
        while cnt_lv < 6:
            lv_list.append(song_lv[cnt_lv].text)
            cnt_lv += 2
        song_data.append(lv_list)
        
        #画像
        song_img = html.xpath(f"//*[@id=\"music_list\"]/div[{i}]/table/tr[1]/td[1]/*")
        song_data.append(song_img[0].attrib["src"])

    return song_data

"""
[要素数]
//*[@id=\"music_list\"]/div/*
基本は50
前２つはヘッダー


[画像パス]
//*[@id=\"music_list\"]/div[2から始まる連番]/table/tr[1]/td[1]/*
attrib

[曲名]
//*[@id=\"music_list\"]/div[2]/table/tr[1]/*
text

[アーティスト]
//*[@id=\"music_list\"]/div[2]/table/tr[2]/*
text

[レベル]
//*[@id=\"music_list\"]/div[2]/table/tr[3]/td/ul/li/*
x[1,3,5].text
ba ad ex

"""
