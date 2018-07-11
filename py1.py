from bs4 import BeautifulSoup


soup = BeautifulSoup(open("home.html", encoding="UTF-8"), "html5lib")

# print(soup.prettify())

# print(soup.title.string)
#
# print(soup.title.get_text())


# print(soup.div.attrs['id'])


divList = soup.find_all("div")

# print(divList)

# elList = soup.find_all(True)
#
# print(elList)
print("=====================================")
idEls = soup.find_all(id="div1")
# print(idEls)


clsList = soup.find_all(class_="kkk")

atList = soup.find_all(attrs={"class":"kkk"})


divList = soup.select("div")

print(divList)












