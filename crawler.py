from bs4 import BeautifulSoup
from urllib import request


# 获取知乎某一条答案的数据
def zhihuAn(url):
    # 伪造一个代理浏览器(windows的chrome浏览器)
    headerList = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}

    # 构建一个请求
    req = request.Request(url, headers=headerList)

    # 根据请求获取请求结果
    result = request.urlopen(req).read()

    # 使用BS解析HTML字符串
    soup = BeautifulSoup(result, "html5lib")

    # 打印标题
    print(soup.title.string)

    # 获取知乎问题的答案标签
    anList = soup.select(".RichContent-inner")

    # 打印答案内容文本
    for an in anList:
        print(an.get_text())


# 获取知乎推荐中所有的答案
def zhihuQuestions():
    questionUrl = "https://www.zhihu.com/explore/recommendations"

    headerList = {"User-Agent": "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}

    req = request.Request(questionUrl, headers=headerList)

    result = request.urlopen(req).read()

    soup = BeautifulSoup(result, "html5lib")

    quList = soup.select(".question_link")

    for qu in quList:
        zhUrl = "https://www.zhihu.com" + qu.attrs['href']
        print(zhUrl)
        zhihuAn(zhUrl)


# 调用函数
zhihuQuestions()