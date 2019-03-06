import urllib.request

from bs4 import BeautifulSoup


class SpiderMan:
    def crawl(self,url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        response = urllib.request.urlopen(req)
        html = response.read().decode('gbk')
        #print(html)
        soup = BeautifulSoup(html,'html.parser')
        b = soup.find_all('a')
        print(b[68:201])
        j = 1
        for i in b[68:201]:
            c = 'http://www.biqugecom.com'+i['href']
            req = urllib.request.Request(c)
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
            response = urllib.request.urlopen(req)
            html = response.read().decode('gbk')
            soup = BeautifulSoup(html, 'html.parser')
            d = soup.find_all('div',attrs={'id':'content'})
            e = soup.find_all('h1')
            g = e[0].text

            with open(r'C:\Users\傲\Desktop\稻香.txt','a',encoding='utf-8') as f:
                f.write(str(g)+'\n')
                f.write(str(d[0]))
            print(j)
            j=j+1





if __name__=='__main__':
    url = 'http://www.biqugecom.com/22/22385/'
    a = SpiderMan()
    a.crawl(url)
