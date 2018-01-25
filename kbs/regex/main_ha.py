# Settings -> project interpreter ->

import re

melon_f = open('melon.txt', 'rt')
melon_t = melon_f.read()
melon_f.close()

# pattern_div_rank = re.compile(r'')
#
#
# source = '''<td><div class="wrap">
# <div class="wrap_song_info">
#     <div class="ellipsis rank01"><span>
#         <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
#     </span></div><br>
#     <div class="ellipsis rank02">
#         <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
#     </div>
# </div>
# </div></td>'''

pattern_div_rank01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
div_rank01 = re.findall(pattern_div_rank01, melon_t)

pattern_a_content = re.compile(r'<a.*?>(.*?)</a>')

for i in range(len(div_rank01)):
    title = re.search(pattern_a_content, div_rank01[i]).group(1)
    print(title)


# source = '''<td><div class="wrap">
# <div class="wrap_song_info">
#     <div class="ellipsis rank01"><span>
#         <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
#     </span></div><br>
#     <div class="ellipsis rank02">
#         <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
#     </div>
# </div>
# </div></td>'''
#
# # 위의 소스에서 <div class="ellipsis rank01> ~ </div>부분의 텍스트를
# # div_rank01 변수에 할당
# pattern_div_rank01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# div_rank01 = re.search(pattern_div_rank01, source).group()
# print(div_rank01)
#
# # div_rank01 변수에 있는 문자열에서
# # <a href=....>(내용)</a>
# # 위의 (내용)그룹에 해당하는 부분을 title변수에 할당
# pattern_a_content = re.compile(r'<a.*?>(.*?)</a>')
# title = re.search(pattern_a_content, div_rank01).group(1)
# print(title)




# # html = (멜론 사이트로부터 받은 HTML 문자열)
# response = requests.get('https://www.melon.com/chart/index.htm')
# print(response.text)
# '<a\s.*title="'
# source = """<td><div class="wrap">
#     <div class="wrap_song_info">
#         <div class="ellipsis rank01"><span>
#             <a href="javascript:melon.play.playSong('19030101',30851703);" title="다른사람을 사랑하고 있어 재생">다른사람을 사랑하고 있어</a>
#         </span></div><br>
#         <div class="ellipsis rank02">
#             <a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('514741');" title="수지 (SUZY) - 페이지 이동">수지 (SUZY)</a></span>
#         </div>
#     </div>
# </div></td>"""
#
# # DOTALL은 줄바꿈 문자까지 포함하고 싶으면 쓴다
#
# p1 = re.compile(r'<div class="ellipsis rank01">([\w\W]*?)</div>', re.DOTALL)
# p = re.compile(r'<a.*?</a>')
# # result = re.findall(p, source)
# # for index, item in enumerate(result):
# #     print(index, item)
#
