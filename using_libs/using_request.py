import json
import requests

def main1():
    '''
    示例
    :return:
    '''
    response = requests.get('https://www.baidu.com/')
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(response.cookies)

def main2():
    '''
    各种请求方式
    :return:
    '''
    requests.post('http://httpbin.org/post')
    requests.put('http://httpbin.org/put')
    requests.delete('http://httpbin.org/delete')
    requests.head('http://httpbin.org/get')
    requests.options('http://httpbin.org/get')

def main3():
    '''
    get请求
    :return:
    '''
    response = requests.get('http://httpbin.org/get')
    print(response.text)

def main4():
    '''
    带参数的get请求
    :return:
    '''
    response = requests.get("http://httpbin.org/get?name=germey&age=22")
    print(response.text)

def main5():
    data = {
        'name': 'germey',
        'age': 22
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.text)

def main6():
    '''
    json解析
    :return:
    '''
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print(response.json())
    print(json.loads(response.text))
    print(type(response.json()))

def main7():
    '''
    二进制数据
    :return:
    '''
    response = requests.get("https://github.com/favicon.ico")
    print(type(response.text), type(response.content))
    print(response.text)
    print(response.content)

def main8():
    response = requests.get("https://github.com/favicon.ico")
    with open('favicon.ico', 'wb') as f:
        f.write(response.content)
        f.close()

def main9():
    '''
    跟10对比
    :return:
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get("https://www.zhihu.com/explore", headers=headers)
    print(response.text)


def main10():
    response = requests.get("https://www.zhihu.com/explore")
    print(response.text)

def main11():
    data = {'name': 'germey', 'age': '22'}
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)

def main12():
    data = {'name': 'germey', 'age': '22'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.post("http://httpbin.org/post", data=data, headers=headers)
    print(response.json())


def main13():
    response = requests.get('http://www.jianshu.com')
    print(type(response.status_code), response.status_code)
    print(type(response.headers), response.headers)
    print(type(response.cookies), response.cookies)
    print(type(response.url), response.url)
    print(type(response.history), response.history)

def main14():
    response = requests.get('http://www.jianshu.com/hello.html')
    exit() if not response.status_code == requests.codes.not_found else print('404 Not Found')

def main15():
    response = requests.get('http://www.jianshu.com')
    exit() if not response.status_code == 200 else print('Request Successfully')

def main16():
    files = {'file': open('favicon.ico', 'rb')}
    response = requests.post("http://httpbin.org/post", files=files)
    print(response.text)

def main17():
    response = requests.get("https://www.baidu.com")
    print(response.cookies)
    for key, value in response.cookies.items():
        print(key + '=' + value)

def main18():
    requests.get('http://httpbin.org/cookies/set/number/123456789')
    response = requests.get('http://httpbin.org/cookies')
    print(response.text)

def main19():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    response = s.get('http://httpbin.org/cookies')
    print(response.text)
def main20():
    response = requests.get('https://www.12306.cn')
    print(response.status_code)
def main21():
    requests.packages.urllib3.disable_warnings()
    response = requests.get('https://www.12306.cn', verify=False)
    print(response.status_code)
def main22():
    response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
    print(response.status_code)
def main23():
    proxies = {
        "http": "http://127.0.0.1:9743",
        "https": "https://127.0.0.1:9743",
    }

    response = requests.get("https://www.taobao.com", proxies=proxies)
    print(response.status_code)
def main24():
    proxies = {
        "http": "http://user:password@127.0.0.1:9743/",
    }
    response = requests.get("https://www.taobao.com", proxies=proxies)
    print(response.status_code)

def main25():
    proxies = {
        'http': 'socks5://127.0.0.1:9742',
        'https': 'socks5://127.0.0.1:9742'
    }
    response = requests.get("https://www.taobao.com", proxies=proxies)
    print(response.status_code)
def main26():
    from requests.exceptions import ReadTimeout
    try:
        response = requests.get("http://httpbin.org/get", timeout=0.5)
        print(response.status_code)
    except ReadTimeout:
        print('Timeout')
def main27():
    from requests.auth import HTTPBasicAuth

    r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
    print(r.status_code)
def main28():
    r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
    print(r.status_code)
def main29():
    from requests.exceptions import ReadTimeout, ConnectionError, RequestException
    try:
        response = requests.get("http://httpbin.org/get", timeout=0.5)
        print(response.status_code)
    except ReadTimeout:
        print('Timeout')
    except ConnectionError:
        print('Connection error')
    except RequestException:
        print('Error')

main16()