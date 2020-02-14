import json
import time

import requests
from pyquery import PyQuery as pq
from tqdm import tqdm


class main(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://www.xnxx.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        self.session = requests.session()
        self.session.headers = self.headers
        self.session.get('https://www.xnxx.com/')
        self.Id = []
        print("Welcome Work Download")
        self.incate = input('请输入关键字:')


    def requests_url(self,url,headers,proxy):
        try:
            response = self.session.get(url=url,headers=headers,proxies=proxy)
            return response.text
        except Exception as e:
            print(e)
            return None

    def parse_html(self,url,k):
        kk = int(k)
        url = url
        headers = {
            'Referer': 'https://www.xnxx.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }
        proxy = self.proxyIp()
        pqhtml = self.requests_url(url,headers,proxy)
        if pqhtml == None:
            print('响应错误')
        else:
            html = pq(pqhtml)
            items = html(".mozaique .thumb-inside div a img").items()
            for i in items:
                self.Id.append(i.attr('data-videoid'))
            if kk >33:
                self.next_url(url,kk)
            return self.Id

    def next_url(self,url,k):
        page = int(k/33)
        for i in range(page):
            p = '/{}/'
            ul = url+p.format(i+1)
            self.parse_html(ul,page)

    def down(self,items,k):
        print('请求链接网站...')
        headers = {
            'Origin': 'https://www.xnxx.com',
            'Host':'www.xnxx.com',
            'Cookie': 'wpn_ad_cookie=18a505122b5753f0e33c67839ef0791a; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1581489202; html5_pref=%7B%22SQ%22%3Afalse%2C%22MUTE%22%3Afalse%2C%22VOLUME%22%3A1%2C%22FORCENOPICTURE%22%3Afalse%2C%22FORCENOAUTOBUFFER%22%3Afalse%2C%22FORCENATIVEHLS%22%3Afalse%2C%22PLAUTOPLAY%22%3Atrue%2C%22CHROMECAST%22%3Afalse%2C%22EXPANDED%22%3Afalse%2C%22FORCENOLOOP%22%3Afalse%7D; X-Backend=13|XkOgU|XkOcT; xv_nbview=-1; html5_networkspeed=6508; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1581579003; thumbloadstats_vthumbs=%7B%222%22%3A%5B%7B%22s%22%3A2%2C%22d%22%3A0%7D%2C%7B%22s%22%3A2%2C%22d%22%3A0%7D%2C%7B%22s%22%3A2%2C%22d%22%3A13%7D%5D%2C%223%22%3A%5B%7B%22s%22%3A2%2C%22d%22%3A88%7D%2C%7B%22s%22%3A2%2C%22d%22%3A13%7D%2C%7B%22s%22%3A2%2C%22d%22%3A0%7D%5D%2C%22last%22%3A%7B%22s%22%3A2%2C%22v%22%3A%5B0%2C13%2C0%5D%7D%7D; multi_accounts=91f741755b367f56mhltSdlhXAIcnqbq82-FfLcHMq77crT3S_GbkI8Ba19ZAtSpUqF7xqnYPNaWU4o8; last_views=%5B%2251327097-1581490735%22%2C%2228377857-1581492316%22%2C%2249125517-1581492787%22%2C%2252101981-1581506558%22%2C%2235852691-1581506557%22%2C%2252219927-1581511550%22%2C%2253063159-1581511550%22%2C%2252957939-1581511717%22%2C%2228226929-1581511960%22%2C%2228212819-1581513190%22%2C%2224093289-1581513904%22%2C%2220989793-1581514539%22%2C%2248271134-1581514735%22%2C%2248147749-1581515376%22%2C%2248067619-1581518310%22%2C%2235086417-1581519943%22%2C%2230848709-1581520046%22%2C%2252267837-1581520888%22%2C%2239702747-1581525066%22%2C%2251861457-1581525954%22%2C%2249518569-1581526176%22%2C%2247428105-1581562137%22%2C%2241693493-1581564174%22%2C%2223281353-1581564634%22%2C%2225062153-1581565613%22%2C%2252316311-1581571446%22%2C%2228579629-1581574405%22%2C%2240823343-1581579349%22%2C%2248914819-1581615839%22%5D; session_token=f588a71a93933368hNtJF7T9kvplth-YGb3RxzFeE0p8YBge2nI6UiDTIHOM_1B4qg8y8YxbJvXQ6JtRbgj7SSciUg8AQ42DNlD4-qjgIsXHtcJGmwUG4QI-UQiugs3ZYH4EoXyXFT8xWSWZEgEfy90rv57XOSvgBtvrd0skQmm_Z2_X0iDDn9gr2eYDOwgtzvDG8EV1SEYUokZd5Dz61GDc0z1Mj-QyqaPG4-bA2hAn-35KNetTJimxr_QNaKF-91PrvcsZ9rSlFprOk8_y4jhHSBOqhfq2RnFuNTWNnizwdcQpdnObCrJ7XmTKfjpDrrtb8tExoB1UxI8zEde9Ml9Jzf0uahYaUSIP6QFA4Jovht37dyHkZCm8367ssgZndCLFY2Zb6P7Gj8DSMFYkOAncAf1pZ011tcRIruMS97uNqg9zsVBJAVKJIn7nn7pBQIs863nwwR_hBFhhZ4HTV6XZ4rTIhrPyCp5wIUDsq2XKKvXl5MeVaEst8sY3HmA7WzpC92D2XjuuKPTU'
        }
        item = []
        proxy = self.proxyIp()
        progress = tqdm(items)
        number = 0
        try:
            for i,j in (enumerate(items)):
                progress.set_description('Progress{}'.format(self.incate))
                time.sleep(1)
                url = 'https://www.xnxx.com/video-download/{}/'
                if int(i) >= int(k):
                    break
                url = url.format(j)
                if number == 50:
                    proxy = self.proxyIp()
                    number =0
                dataText = self.session.get(url=url,headers = headers,proxies = proxy)
                item.append(json.loads(dataText.text,encoding='utf-8'))
        except Exception as e:
            print('下载过多，休息一下。。。')
        return item

    def getURL(self,text):
        print('获取高清链接...')
        item = []
        for i in text:
            URL_HIGH = i['URL']
            item.append(URL_HIGH)
        return item


    def main(self):
        category_url = self.initAction()
        k = input('请输入下载个数:')
        Id = self.parse_html(category_url,k)
        text = self.down(Id,k)
        downUrl = self.getURL(text)
        self.save_url(downUrl)

    def save_url(self,text):
        print('保存链接中...')
        data = json.dumps(text,ensure_ascii=False)
        name = '{}.txt'.format(self.incate)
        print(data)
        with open(name,'a+') as fp:
            fp.write(data)

    def initAction(self):
        ul = 'https://www.xnxx.com/search/{}'
        url = ul.format(self.incate)
        return url

    def proxyIp(self):
        ipurl = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=0&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
        response = requests.get(ipurl)
        try:
            time.sleep(1)
            ipdata = json.loads(response.text, encoding='utf-8')['data'][0]
            proxy = {
                'http:': 'http://{}'.format(str(ipdata['ip']) + ':' + str(ipdata['port'])),
                'https:': 'https://{}'.format(str(ipdata['ip']) + ':' + str(ipdata['port']))
            }
            print('获取代理IP', proxy,'此代理用于爬取50个链接')
            return proxy
        except IndexError as e:
            caution = json.loads(response.text, encoding='utf-8')['msg']
            addIp = 'wapi.http.cnapi.cc/index/index/save_white?neek=71463&appkey=fc6feee4f4c37dc85fb14ebe673b4a51&white='
            print('未将IP添加到白名单,复制以下链接到浏览器,添加IP到代理IP白名单：\n')
            print(addIp + caution[6:])


if __name__ == '__main__':
    c = main()
    c.main()