import re
source = """<tr class="lst50" id="lst50" data-song-no="30838076">
								
								
							
							
									<td><div class="wrap t_right"><input type="checkbox" title="주인공 곡 선택" class="input_check " name="input_check" value="30838076"></div></td>
									<td><div class="wrap t_center"><span class="rank ">4</span><span class="none">위</span></div></td>
		
									
										<!-- 차트순위 추가 -->
										<td><div class="wrap">
											
												
												
												
												
												<span title="1단계 하락" class="rank_wrap">
													<span class="bullet_icons rank_down"><span class="none">단계 하락</span></span>
													<span class="down">1</span>
												</span>
												
												
											
										</div></td>
									
		
									<td><div class="wrap">
										<a href="javascript:melon.link.goAlbumDetail('10128855');" title="주인공" class="image_typeAll">
											<img onerror="WEBPOCIMG.defaultAlbumImg(this);" width="60" height="60" src="http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize" alt="주인공 - 페이지 이동">
											<span class="bg_album_frame"></span>
										</a>
									</div></td>
									<td><div class="wrap">
										<a href="javascript:melon.link.goSongDetail('30838076');" title="주인공 곡정보" class="btn button_icons type03 song_info"><span class="none">곡정보</span></a>
									</div></td>
									<td><div class="wrap">
										<div class="wrap_song_info">
											<div class="ellipsis rank01"><span>
												
												
												
												
												
												
												<a href="javascript:melon.play.playSong('19030101',30838076);" title="주인공 재생">주인공</a>
											</span></div><br>
											<div class="ellipsis rank02">
												
												
												<a href="javascript:melon.link.goArtistDetail('22938');" title="선미 - 페이지 이동">선미</a><span class="checkEllipsis" style="display: none;"><a href="javascript:melon.link.goArtistDetail('22938');" title="선미 - 페이지 이동">선미</a></span>
											</div>
											
										</div>
									</div></td>
									<td><div class="wrap">
										<div class="wrap_song_info">
											<div class="ellipsis rank03">
												<a href="javascript:melon.link.goAlbumDetail('10128855');" title="주인공 - 페이지 이동">주인공</a>
											</div>
										</div>
									</div></td>
									<td><div class="wrap">
										<button type="button" class="button_etc like" title="주인공 좋아요" data-song-no="30838076" data-song-menuid="19030101"><span class="odd_span">좋아요</span>
<span class="cnt">
<span class="none">총건수</span>
40,354</span></button>
									</div></td>
									<td><div class="wrap t_center">
										<button type="button" title="듣기" class="button_icons play " onclick="melon.play.playSong('19030101',30838076);"><span class="none">듣기</span></button>
									</div></td>
									<td><div class="wrap t_center">
										<button type="button" title="담기" class="button_icons scrap " onclick="melon.play.addPlayList('30838076');"><span class="none">담기</span></button>
									</div></td>
									<td><div class="wrap t_center">
										<button type="button" title="다운로드" class="button_icons download " onclick="melon.buy.goBuyProduct('frm', '30838076', '3C0001', '','0', '19030101');"><span class="none">다운로드</span></button>
									</div></td>
									<td><div class="wrap t_center">
										<button type="button" title="뮤직비디오" class="button_icons video " onclick="melon.link.goMvDetail('19030101', '30838076','song');"><span class="none">뮤직비디오</span></button>
									</div></td>
									<td><div class="wrap t_center">
										<button type="button" title="링/벨" class="button_icons bell " onclick="melon.buy.popPhoneDecorate('1110000000000000','30838076')"><span class="none">링/벨</span></button>
									</div></td>
								</tr>"""

#image_typeAll
# rank01

def get_tag_attribute(attribute_name, tag_string):
    """

    :param attribute_name:
    :param tag_string:
    :return:
    """
    p_first_tag = re.compile(r'^.*?<.*?>', re.DOTALL)
    first_tag = re.search(p_first_tag, tag_string).group()



    first_tag = re.compile(r'^<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name = attribute_name
    ), re.DOTALL)

    #문자열 포맷에 이름 붙이고, format()에서 키워드 인수로 전달
    p = re.compile(r'')
}

def get_tag_content(tag_string):
    """

    :param tag_string:
    :return:
    """
    p = re.compile(r'')

PATTERN_TD = re.compile(r'<td>.*?</td>', re.DOTALL)
td_list = re.findall(PATTERN_TD, source)

for index, td in enumerate(td_list):
    td_strip = re.sub(r'[\n\t]+|\s{2,}','', td)
    print(f'{index:02}: {td_strip}')

td_img_cover = td_list[3]
PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)

# PATTERN_IMAGE = re.compile(r'<img.*src=()')
# td_list[3]

# pattern_image_ing = test[3]



# print(test[3])