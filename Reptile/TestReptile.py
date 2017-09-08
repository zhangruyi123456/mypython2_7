import urllib.request
# import http.cookiejar
#
from bs4 import BeautifulSoup


# cookie = http.cookiejar.CookieJar()
#  cookie = http.cookiejar.MozillaCookieJar("testcookie.txt")
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("https://www.baidu.com")
# cookie.save(ignore_discard = True,ignore_expires= True);
# for item in cookie:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)
#

# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# soup = BeautifulSoup(html)
# print(soup.head.string)
# content = soup.head.title.string
# for parent in content.parents:
#     print(parent)




def writeFile(filename,source):
    f = open(filename,'wb')
    f.write(source)
    f.close()
    
filename = "baidu.html"
url = "http://www.baidu.com/"

#file = open(filename);

response = urllib.request.urlopen(url)
html = response.read()

writeFile(filename,html)
# soup = BeautifulSoup(html)
# for child in soup.children:
#     print(child.name)
#print(html)
# file.write(html)
# file.close()


