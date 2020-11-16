import requests
from bs4 import BeautifulSoup as bs


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
cookies = "HMACCOUNT_BFESS=B7F55B5B0909010E; BDUSS_BFESS=UwflpGZW1JUn41QlFQcFF1MGlmQ3c5OXM5WFdDZ2NCcVVzanBUTmdUMlBwOTllSVFBQUFBJCQAAAAAAAAAAAEAAADUdFxTt-fUxsG9srvBogAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI8auF6PGrhecV"
url = "https://maoyan.com/films?showType=3"
headers = {"User-Agent" : user_agent,"Cookie" :cookies}
res = requests.get(url,headers = headers)
#print(res.text)
movie_info = bs(res.text,"html.parser")
#print(movie_info)


movie_list = movie_info.find_all('div',attrs={'class':'movie-item-hover'})
#print(movie_list)

movie_info_list =[]
for i in range(0,10):
    #电影名称
    movie_name = movie_list[i].find('span', attrs={'class': 'name'}).text

    #电影类型
    movie_type = str(movie_list[i].find('div').find_next('div').find_next('div').text).strip()
    print(movie_type)

    #上映日期
    movie_date = str(movie_list[i].find('div', attrs = {'class':'movie-hover-title'}).find_next('div').find_next('div').find_next('div').text).strip()
    print(movie_date)

    movie_date_list = [movie_name,movie_type,movie_date]
    movie_info_list.append(movie_date_list)

#保存数据到文件
import pandas as pd
movie_info = pd.DataFrame(movie_info_list)
movie_info.to_csv('./movie_info.csv',encoding='utf-8', index=False, header=False)





