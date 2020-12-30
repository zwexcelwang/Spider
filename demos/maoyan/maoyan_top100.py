import requests
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        response = requests.get(url,  headers=headers)
        if response.status_code == 200:        # 通过状态码判断成功了吗
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'http://cc.cmbchina.com/card/?WT.mc_id=N17PCGW100AY689100ZH'
    # http: // cc.cmbchina.com / card / list_3.htm?WT.mc_id = N17PCGW100AY689100ZH
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()
