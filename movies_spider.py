import requests
from bs4 import BeautifulSoup
import csv


# 提取电影信息
def movies_spider():
    movie_url = "https://movie.douban.com/top250?start={}&filter="
    movie_num = 0
    movie_name = '名称'
    movie_year = '年份'
    movie_country = '国家'
    movie_type = '类型'
    movie_director = '导演'
    movie_assess = '评价人数'
    movie_score = '评分'
    f = open('movies.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow([
        movie_num, movie_name, movie_year, movie_country, movie_type,
        movie_director, movie_assess, movie_score
    ])
    for list in range(10):
        movie_content = requests.get(movie_url.format(list * 25)).text
        soup = BeautifulSoup(movie_content, 'lxml')
        for li in soup.select('ol li'):
            movie_num = li.select('em')[0].string
            movie_name = li.select('.title')[0].string
            movie_info = li.select('.bd .')[0].get_text().strip().split('\xa0/\xa0')    # 电影信息
            movie_year = movie_info[0].split()[-1]
            movie_country = movie_info[1]
            movie_type = movie_info[2]
            movie_director = movie_info[0].split()[1]
            movie_assess = li.select('.star span')[-1].string[:-3]
            movie_score = li.select('.star span')[1].string
            writer.writerow([
                movie_num, movie_name, movie_year, movie_country, movie_type,
                movie_director, movie_assess, movie_score
            ])
    f.close()


if __name__ == '__main__':
    movies_spider()
