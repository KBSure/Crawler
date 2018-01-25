import requests
import re

# response = requests.get("https://www.melon.com/chart/index.htm")

# with open("melon.html", "w") as f:
#     f.write(response.text)

source = open("melon.html", "rt").read()
# print(source)
# 타이틀 있는 영역 패턴찾기 위해
PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# 타이틀 패턴찾기 위
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

match_list = PATTERN_DIV_RANK01.finditer(source)

title_list = list()
for i in match_list:
    result = PATTERN_A_CONTENT.search(i.group())
    title_list.append(result.group(1))


PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)

found_list = PATTERN_DIV_RANK02.finditer(source)

artist_list = list()
for i in found_list:
    result = PATTERN_A_CONTENT.search(i.group())
    artist_list.append(result.group(1))


PATTERN_DIV_RANK03 = re.compile(r'<div class="ellipsis rank03">.*?</div>', re.DOTALL)

found_list_03 = PATTERN_DIV_RANK03.finditer(source)

album_list = list()
for i in found_list_03:
    result = PATTERN_A_CONTENT.search(i.group())
    album_list.append(result.group(1))

result_list = list(zip(title_list, artist_list, album_list))
# print(result_list)

final_list = list()

count = 1

for i in result_list:
    result_dict = dict()
    result_dict["rank"] = count
    result_dict["title"] = i[0]
    result_dict["artist"] = i[1]
    result_dict["album"] = i[2]
    final_list.append(result_dict)
    count += 1

for i in final_list:
    print(i)

"""
[
    {"rank": 1, "title": "제목", "artist": "가수", "album": "앨범이름"},
    .
    .
    .
]
"""