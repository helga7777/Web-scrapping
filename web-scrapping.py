# поиск с главной страницы
# from requests_html import HTMLSession
# import re
#
# KEYWORDS = ['дизайн', 'фото', 'web', 'Python']
#
# session = HTMLSession()
# url = 'https://habr.com'
# r = session.get(url)
# link = ''
# about = r.html.find('article', first=False)
# for hubs in about:
#     hub = hubs.text
#     for name in KEYWORDS:
#         if name in hub:
#             text = hubs.html
#             # находим ссылку поста
#             w = hubs.find('a')
#             # print(w)
#             for i in w:
#                 i1 = i
#                 i2 = i
#                 i1.find('post')
#                 i11 = str(i)
#                 i2.find('blog')
#                 i22 = str(i)
#                 if (('post' in i11) and not('comments' in i11)) or ('blog' in i22):
#                     str1 = i11[19:]
#                     p = str1.find("'")
#                     href = i11[19:19+p]
#                     link = url + href
#             pattern2 = r'title-link\"\>\<(span\>(\w*\s*)*)(\<)*'
#             result = re.findall(pattern2,text)
#
#             pattern3 = r'datetime=\"(\w*-\w*-\d*)\w*:\w*:\w*.\w*\"'
#             result2 = re.findall(pattern3, text)
#
#             pattern4 = r'(title-link\"\>\<span\>)((\w*\s*[,:;?]*)*)'
#             result3 = re.findall(pattern4, text)
#             print(f'Дата - {result2[0]},  заголовок - {result3[0][1]}, ссылка - {link}')






# поиск с введенной страницы,  открывает каждую статью и ищет текст там
from requests_html import HTMLSession
import re

def poisk(url):
    KEYWORDS = ['дизайн', 'фото', 'web', 'Python']

    session = HTMLSession()
    r = session.get(url)
    link = ''
    about = r.html.find('article', first=False)
    for hubs in about:
        hub = hubs.text
        for name in KEYWORDS:
            if name in hub:
                text = hubs.html
                pattern2 = r'title-link\"\>\<(span\>(\w*\s*)*)(\<)*'
                result = re.findall(pattern2,text)

                pattern3 = r'datetime=\"(\w*-\w*-\d*)\w*:\w*:\w*.\w*\"'
                result2 = re.findall(pattern3, text)

                pattern4 = r'(title_h1\"\>\<span\>)((\w*\s*[,:;?]*)*)'
                result3 = re.findall(pattern4, text)

                final = f'Содержит текст {name}. Дата - {result2[0]},  заголовок - {result3[0][1]}, ссылка - {url}'
                print(final)


session = HTMLSession()
url_text = str(input('Введите номер страницы: '))
if url_text == '1':
    url = 'https://habr.com'
else:
    url = f'https://habr.com/en/all/page{url_text}'
url_start = 'https://habr.com'
r = session.get(url)
link = ''
about = r.html.find('article', first=False)
for hubs in about:
    hub = hubs.html
    w = hubs.find('a')
    text_w = str(w[2])
    str1 = text_w[19:]
    p = str1.find("'")
    href = text_w[19:19 + p]
    link = url_start + href
    # print(link)
    try:
        poisk(link)
    except:
        ...



