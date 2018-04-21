import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup


def main():
    headers = {
'Host': 'vmmo.vten.ru',
'Connection': 'keep-alive',
'Origin': 'http://vmmo.vten.ru',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
               }
    r_get = requests.get('http://vmmo.vten.ru/login?19-1.IFormSubmitListener-loginPanel-loginForm-loginForm',headers = headers)

    cookie = r_get.cookies['JSESSIONID']

    data = {
        'loginForm_hf_0': '',
        'login': login,
        'password': pass
            }

    r_post = requests.post('http://vmmo.vten.ru/login;jsessionid='+cookie+'?0-1.IFormSubmitListener-loginPanel-loginForm-loginForm',
                            headers=headers,data=data)

    return r_post.text

def chek(html):
    soup = BeautifulSoup(html,'lxml')
    valid = soup.find_all('a',class_='minor')[-1]
    print(valid)



if __name__ == '__main__':
    html = main()
    chek(html)