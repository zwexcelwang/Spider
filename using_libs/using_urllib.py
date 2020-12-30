'''
urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False,context=None)
'''

import socket
import urllib.parse
import urllib.request
import urllib.error
import http.cookiejar


def main1():
    '''
    get请求
    :return: none
    '''
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.read().decode('utf-8'))      #base类型，需要解码

def main2():
    '''
    post请求
    :return:
    '''
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    response = urllib.request.urlopen("http://httpbin.org/post", data=data)
    print(response.read())

def main3():
    '''
    设置超时
    :return:
    '''
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
    print(response.read())

def main4():
    try:
        response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("TIME OUT")

def main5():
    response = urllib.request.urlopen("http://python.org")
    print(type(response))
    print(response.status)      # 状态码
    print(response.headers)     # 响应头
    print(response.getheader("Server"))
    print(response.read().decode("utf-8"))      # 响应体的内容

def main6():
    request = urllib.request.Request("http://python.org")
    response = urllib.request.urlopen(request)
    print(response.read().decode("utf-8"))

def main7():
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
    }
    dict = {
        'name': 'Germey'
    }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

def main8():
    url = 'http://httpbin.org/post'
    dict = {
        'name': 'Germey'
    }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, method='POST')
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

def main9():
    '''
    代理设置，我还没有成功
    :return:
    '''
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743'
    })
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open('http://www.baidu.com')
    print(response.read())

def main10():
    '''
    维持登录状态
    :return:
    '''
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)

def main11():
    '''
    将cookie保存在文件里
    :return:
    '''
    filename = "cookie.txt"
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

def main12():
    filename = 'cookie.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

def main13():
    '''
    cookie读取，怎么读怎么取
    :return:
    '''
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))

def main14():
    '''
    error处理
    :return:
    '''
    try:
        response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
    except urllib.error.URLError as e:
        print(e.reason)

def main15():
    try:
        response = urllib.request.urlopen('http://cuiqingcai.com/index.htm')
    except urllib.error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        print('Request Successfully')

def main16():
    try:
        response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

def main17():
    result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    print(type(result), result)


def main18():
    result = urllib.parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(result)

def main19():
    result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    print(result)

def main20():
    result = urllib.parse.urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    print(result)

def main21():
    result = urllib.parse.urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    print(result)

def main22():
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urllib.parse.urlunparse(data))

def main23():
    print(urllib.parse.urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urllib.parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
    print(urllib.parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
    print(urllib.parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
    print(urllib.parse.urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
    print(urllib.parse.urljoin('http://www.baidu.com', '?category=2#comment'))
    print(urllib.parse.urljoin('www.baidu.com', '?category=2#comment'))
    print(urllib.parse.urljoin('www.baidu.com#comment', '?category=2'))

def main24():
    '''
    urlencode
    :return:
    '''
    params = {
        'name': 'germey',
        'age': 22
    }
    base_url = 'http://www.baidu.com?'
    url = base_url + urllib.parse.urlencode(params)
    print(url)

main24()