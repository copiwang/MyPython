import requests
from bs4 import BeautifulSoup
import random
import re

############豆瓣图书榜单#############
strurl='https://book.douban.com/chart?subcat=all'
#num=str(float(random.randint(500,600)))
strheader={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 \
Safari/537.36'}
req_doubanbook=requests.get(strurl,headers=strheader)
#后面参数表示解析器： lxml  xml   html5lib   html.parser
Bsoup=BeautifulSoup(req_doubanbook.text,"lxml")

#乱码的话可以修改成 req_doubanbook.content

#获取标题
str_first_title=Bsoup.find_all('h2',class_='clearfix')
for i in range(len(str_first_title)):
    title_book=str_first_title[i].a.text.strip()
    print(f'第{i+1}名：书名-{title_book}')

#代码美化 soup.prettify()
strhtml="""
<body>
<header id="header">
    <h1 id="name">Santos Tang</h1>
    <div class="sns">
                <a href="https://weibo.com/santostang" target="_blank" rel="nofollow" data-toggle="tooltip" data-placement="top" title="Weibo">
                <i class="fab fa-weibo"></i></a>        
                <a href="https://www.linkedin.com/in/santostang" target="_blank" rel="nofollow" data-toggle="tooltip" data-placement="top" title="Linkedin">
                <i class="fab fa-linkedin"></i></a>        <a href="https://www.zhihu.com/people/santostang" target="_blank" rel="nofollow" 
                data-toggle="tooltip" data-placement="top" title="Zhihu"><i class="fab fa-zhihu"></i></a>        
                <a href="https://github.com/santostang" target="_blank" rel="nofollow" 
                data-toggle="tooltip" data-placement="top" title="GitHub"><i class="fab fa-github-alt"></i></a>    </div>
    <div class="nav">
        <ul><li><a href="http://www.santostang.com/">首页</a></li>
<li><a href="http://www.santostang.com/aboutme/">关于我</a></li>
<li><a href="http://www.santostang.com/python%e7%bd%91%e7%bb%9c%e7%88%ac%e8%99%ab%e4%bb%a3%e7%a0%81/">爬虫书代码</a></li>
<li><a href="http://www.santostang.com/%e5%8a%a0%e6%88%91%e5%be%ae%e4%bf%a1/">加我微信</a></li>
<li><a href="https://santostang.github.io/">EnglishSite</a></li>
</ul>    </div>
        <div class="weixin">
        <img src="http://www.santostang.com/wp-content/uploads/2019/06/qrcode_for_gh_370f70791e19_258.jpg" alt="微信公众号" width="50%">
        <p>微信公众号</p>
    </div>
    </header>
"""
mh_soup=BeautifulSoup(strhtml,'lxml')
#print(mh_soup.prettify())

#############遍历文档树 ##############
#soup.header.h1
print('获取h1',mh_soup.header.h1)
print('获取divcontents',mh_soup.header.div.contents)
print('='*60)
print('获取第一个divcontents',mh_soup.header.div.contents[0])
print('='*60)
for child in mh_soup.header.div.children: #子节点
    print(child,'子节点循环一次')
print('='*60)
for child in mh_soup.header.div.descendants: #所有子层级的节点
    print(child,'子孙节点循环一次')
print('='*60)

a_tag=mh_soup.header.div.a
atp=a_tag.parent
print('儿子节点:',a_tag)
print('父节点:',atp)

#############搜索文档树--find   find_all#############
print('='*30,'搜索文档树','='*30)
for tag in mh_soup.find_all(re.compile('^h')):
    print('css搜索文档树：'+tag.name)

############# css 选择器 select #############
print('='*30,'css选择器','='*30)
soup_cs=BeautifulSoup(open('test.html','r', encoding='utf-8'),'lxml')
#也可以多重选择  div > h1 > a
print('选择子：',soup_cs.select('div > div'))  #div 里面的DIV
items=soup_cs.select('title')
print('提取数列：')
for item in items:
    print(item.name)
    print(item.string)
#标签作为选择对象
#id作为选择对象
items=soup_cs.select('#s-top-left')
#选择div的id是fist的内容  select('div#first')
print('id选择：',items)

#属性选择标签 class=mnav1
items=soup_cs.select('span.title-content-title')
for item in items:
    print('属性标签',item)
    print('属性内容',item.string)
    print('属性属性',item.attrs)
    print('属性值',item.get('class'))
items=soup_cs.select('#wrapper > div > a')
for item in items:
    #item.get('href') 获取链接   item.string 获取内容
    print('父子多重选择：',item.get('href'))   
#空格 标识不具有直接父子关系的标签
items=soup_cs.select('body li span')
for item in items:
    print('空格的使用：',item)

#选择链接href
items=soup_cs.select('[href]')      #或者 select('a[href]')
for item in items:
    print('选择链接：',item) #或者 item.get('href')

items = soup_cs.select('[href="https://haokan.baidu.com/?sfrom=baidu-top"]')
for item in items:
    print('选择具体一个:',item)

#选择多个标签
items = soup_cs.select('div#s-top-left, ul#hotsearch-content-wrapper')
for item in items:
    print('选择多个a:',item)

#多种链接选择的方式
items = soup_cs.select('a[href^="https"]')  #https开通
items = soup_cs.select('a[href$="hao123.com"]') #hao123.com 结尾
items = soup_cs.select('a[href*="www"]')  #包含 wwww
items = soup_cs.select('a[class]') #含class 属性 



############太平洋汽车轿车销售榜单#############
'''
strurlcar='https://price.pcauto.com.cn/top/sales/s1-t1.html'
#num=str(float(random.randint(500,600)))
strcarheader={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 \
Safari/537.36'}
req_car=requests.get(strurlcar,headers=strcarheader)
#后面参数表示解析器： lxml  xml   html5lib   html.parser
Bsoup=BeautifulSoup(req_car.text,"lxml")
#获取标题
str_cname=Bsoup.find_all('td',class_='col2 brand')
str_compname=Bsoup.find_all('td',class_='col4 relBrand')
str_price=Bsoup.find_all('td',class_='col3 price')
for i in range(len(str_cname)):
    title_car=str_cname[i].a.text.strip()
    title_comp=str_compname[i].a.text.strip()
    title_price=str_price[i].text.strip()
    print(f'第{i+1}名：汽车-{title_car}-\
        厂家-{title_comp}-价格-{title_price}')
'''

######################## lxml 解析网页 #########
from lxml import etree
link='http://www.santostang.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 \
Safari/537.36'}
r=requests.get(link,headers)
html=etree.HTML(r.text)
title_list=html.xpath('//*[@id="main"]/div/div[1]/article[2]/div/p/text()')
print('lxml解析网页：',title_list)
