import json
import requests
import re
from requests.exceptions import RequestException
from multiprocessing import Pool
from selenium import webdriver


def get_one_page(url):                  # 获取网页源码
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        return browser.page_source
    finally:
        browser.close()


def  parse_one_page(html):                 # 利用正则表达式提取内容
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                        +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }


def write_to_file(content):                 # 写入文件
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url="http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
    #多线程写法，实测不是很好用，因为同时打开多个网页，抓取结果容易乱序
    """
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    """