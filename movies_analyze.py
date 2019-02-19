import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


df = pd.read_csv('movies.csv', encoding='utf-8')
matplotlib.rcParams['font.family'] = 'SimHei'   #配置中文字体
matplotlib.rcParams['font.size'] = 15   # 更改默认字体大小

#################################################################
# 数据分析及可视化操作
# 每一部分用空行隔开，可以单独操作，互不影响。想要显示信息就单独打印
#################################################################

# 重复值检查（展示用print()打印）
df.duplicated().value_counts()
len(df.名称.unique())

# 上映年份分析（展示用print()打印）
df["年份"].value_counts().head()

# 国家地区排名
area_split = df['国家'].str.split(' ').apply(pd.Series)
all_country = area_split.apply(pd.value_counts).fillna('0') 
all_country.columns = ['area1', 'area2', 'area3', 'area4', 'area5', 'area6']
all_country['area1'] = all_country['area1'].astype(int)
all_country['area2'] = all_country['area2'].astype(int)
all_country['area3'] = all_country['area3'].astype(int)
all_country['area4'] = all_country['area4'].astype(int)
all_country['area5'] = all_country['area5'].astype(int)
all_country['area6'] = all_country['area6'].astype(int)
all_country['all_counts'] = all_country['area1'] + all_country['area2']\
                        + all_country['area3'] + all_country['area4']\
                        + all_country['area5'] + all_country['area5']
all_country.sort_values(['all_counts'], ascending=False)    # 降序
country = pd.DataFrame({'国家':all_country['all_counts']})
country.sort_values(by='国家', ascending=False).plot(kind='bar', figsize=(10,7))
plt.show()

# 电影类型统计
all_type = df['类型'].str.split(' ').apply(pd.Series)
all_type = all_type.apply(pd.value_counts).fillna('0')
all_type.columns = ['tpye1', 'type2', 'type3', 'type4', 'type5']
all_type['tpye1'] = all_type['tpye1'].astype(int)
all_type['type2'] = all_type['type2'].astype(int)
all_type['type3'] = all_type['type3'].astype(int)
all_type['type4'] = all_type['type4'].astype(int)
all_type['type5'] = all_type['type5'].astype(int)
all_type['all_counts'] = all_type['tpye1'] + all_type['type2']\
                        + all_type['type3'] + all_type['type4'] + all_type['type5']
all_type = all_type.sort_values(['all_counts'], ascending=False)
movie_type = pd.DataFrame({'数量':all_type['all_counts']})
movie_type.sort_values(by='数量', ascending = False).plot(kind ='bar', figsize = (10,6))
plt.show()

# 上榜次数最多的导演（展示用print()打印）
director = df['导演'].value_counts()

# 评分和排名的关系散点图
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.scatter(df['评分'],df['0'])
plt.xlabel('评分')
plt.ylabel('排名')
plt.gca().invert_yaxis()    #修改y轴为倒序
# 评分数量直方图
plt.subplot(1,2,2)
plt.hist(df['评分'], bins=14)
plt.xlabel('评分')
plt.ylabel('出现次数')
plt.show()

# 评分与评价人数的关系散点图
plt.figure(figsize=(14,6)) 
plt.subplot(1,2,1)
plt.scatter(df['评价人数'], df['0'])
plt.xlabel('评价人数')
plt.ylabel('排名')
plt.gca().invert_yaxis()
# 评价人数直方图
plt.subplot(1,2,2)
plt.hist(df['评价人数'], bins=14)
plt.xlabel('评价人数')
plt.ylabel('出现次数')
plt.show()
