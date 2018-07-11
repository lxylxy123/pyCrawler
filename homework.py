from urllib import request
from bs4 import BeautifulSoup


def crawContent(url):
    # 伪造一个代理浏览器(windows的chrome浏览器)
    headerList = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}

    # 构建一个请求
    req = request.Request(url, headers=headerList)

    # 数据请求获取请求结果
    result = request.urlopen(req).read()

    # 使用BS解析HTML字符串
    soup = BeautifulSoup(result, 'html5lib')
    # 获取标题
    print(soup.title.string)
    a = str(soup.title.string)
    llen = a.index('》')
    rlen = a.index('《')
    rlen += 1
    txtName = a[int(rlen):int(llen)]
    fp = open(txtName + '.txt', 'a', encoding="UTF-8")

    # 获取知乎问题的答案标签
    anList = soup.select("h1")[0].get_text()
    fp.write(anList + '\n')
    # 打印文本内容
    textContent = soup.select("p")
    for textPlist in textContent:
        print(textPlist.get_text())
        fp.write(textPlist.get_text() + '\r\n')
    fp.close()


def craw(url):
    # 伪造一个代理浏览器(windows的chrome浏览器)
    headerList = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}

    # 构建一个请求
    req = request.Request(url, headers=headerList)

    # 数据请求获取请求结果
    result = request.urlopen(req).read()

    # 使用BS解析HTML字符串
    soup = BeautifulSoup(result, 'html5lib')
   
    # 获取知乎问题的答案标签
    anList = soup.select(".book-mulu")

    # 打印文本内容
    for an in anList:
        listmulu = an.find_all('a')
        for indexList in listmulu:
            zhUrl = "http://www.shicimingju.com" + indexList.attrs['href']
            crawContent(zhUrl)


Url = "http://www.shicimingju.com/book"
headerList = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}
req = request.Request(Url, headers=headerList)
result = request.urlopen(req).read()
soup = BeautifulSoup(result, "html5lib")
quList = soup.select("h2")
i = 1
for qu in quList:
    zhUrl = "http://www.shicimingju.com" + qu.find("a").attrs['href']
    craw(zhUrl)
    i += 1
    if i > 2:
        break
