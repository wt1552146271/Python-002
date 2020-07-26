'''
作业一：安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
'''

import requests
from bs4 import BeautifulSoup
import time
import lxml.etree
import pandas

headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
cookie = '__mta=252515894.1595667498447.1595732685289.1595733395907.17; uuid_n_v=v1; uuid=FB195EA0CE5411EA9D9027CAB3F025F89C79D47F3379449CA2E11E0FAC975724; _csrf=45c38877ce51919f8abf60513453ab19e86566004a2d68b660e595c8536f5bf0; mojo-uuid=ed1143214d7015c29c24bc0f961a2786; _lxsdk_cuid=1738531c4ecc8-0cfbe1c05acc0c-3962420d-e1000-1738531c4ecc8; _lxsdk=FB195EA0CE5411EA9D9027CAB3F025F89C79D47F3379449CA2E11E0FAC975724; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595669384,1595669468,1595688236,1595722823; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595735273; __mta=252515894.1595667498447.1595733395907.1595735273785.18; _lxsdk_s=1738a2ecc49-1c6-1fe-083%7C%7C1'
headers = {'User-Agent': headers, 'Cookie': cookie}

def get_film_link():

    url = "https://maoyan.com/films?showType=3"
    res = requests.get(url=url, headers=headers)
    # print(res.text)
    # 使用BeautifulSoap解析猫眼网页
    bs_info = BeautifulSoup(res.text, "html.parser")
    time.sleep(20)
    movie_list = bs_info.find_all('div',attrs = {'class':'channel-detail movie-item-title'})
    link_item=[]
    for movie in movie_list:
        link = "https://maoyan.com"+movie.find('a').get('href')
        link_item.append(link)
    return link_item

def get_film_link_top10():
    return get_film_link()[0:10]


# def film_detail_info():
for link in get_film_link_top10():
    # headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    # headers = {'User-Agent': headers}
    res = requests.get(url=link, headers= headers)
    selector = lxml.etree.HTML(res.text)
    file_name = selector.xpath('//div[@class="movie-brief-container"]/h1/text()')
    film_type = selector.xpath('//a[contains(@href, "/films?catId=")]/text()')
    release_time = selector.xpath('//li[@class="ellipsis"][3]/text()')
    movie_list= [file_name,film_type,release_time]
    print(movie_list)

    movie_info = pandas.DataFrame(data=movie_list)
    movie_info.to_csv("./movie.csv",mode= "a+",encoding="utf8",index=False,header= False)