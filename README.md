# Python抓取并分析豆瓣电影top250

Python3实现豆瓣电影TOP250抓取，然后对爬取的数据进行分析。

使用的库：
- requests
- BeautifulSoup
- csv
- pandas
- matplotlab

爬取数据生成的**csv**文件在Windows中用Excel打开是乱码，因为用的是**UTF-8**格式进行编码，想要正常显示就在**movies_spider.py**文件中把 **open()** 里面的格式改为**gb18030**。

**具体分析可以看博客**：https://blog.csdn.net/weixin_44613063/article/details/87646619
