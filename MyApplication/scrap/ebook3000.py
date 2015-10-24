import re

__author__ = 'ankurkhandelwal'

import requests
from bs4 import BeautifulSoup

# url="http://www.ebook-3000.com/page/1/"
# link=[]
links_array=[]


def ebook_links():
    for i in range(1,2):
        url="http://www.ebook-3000.com/page/" + `i`+ "/"
        print(url)
        scrap_all(url)


def scrap_all(url):
    r=requests.get(url)
    number_of_pages_array=[]
    book_type_array=[]
    ISBN_array=[]
    number_of_pages=None
    book_type=None
    ISBN=None
    soup=BeautifulSoup(r.text)

    header = soup.find_all('h2', attrs={'class': 'entry-title'})
    summary=soup.find_all('div', attrs={'class':'entry-summary'})
    for i in summary:
        description=i.find('p')
        desc_array=description.getText().split('|')
        for desc in desc_array:
            if 'pages' in desc or 'Pages' in desc:
                number_of_pages=desc
                number_of_pages_array.append(desc)
                # print(number_of_pages)
            if 'File' in desc:
                book_type=desc
                book_type_array.append(desc)
                # print(book_type)
            if 'ISBN' in desc:
                ISBN=desc
                ISBN_array.append(desc)
                # print(ISBN)
    print('%s %s %s' %(number_of_pages_array, book_type_array, ISBN_array))

    for h in header:
        book_title=h.text
        print(book_title)
        href=h.find('a', href=True)
        html=href['href']
        soup_html=requests.get(html)
        soup_html=BeautifulSoup(soup_html.text)
        div=soup_html.find_all('div',attrs={'class':'entry-content'})
        for k in div:
            para=k.find_all(['p','h3'])
            link_img=k.find('p')
            for j in link_img:
                book_image_link=j['data-original']
                print(book_image_link)
            start=0
            end=0
            for j, i in enumerate(para):
                if i.text in ('Download:','Download'):
                    start = j+1
                if i.text in ('Related posts:'):
                    end=j

            for p in range(start, end):
                href=para[p].find_all('a',href=True)
                for i in href:
                    links_array.append(i['href'])

            for n in range(0,end):
                para_text=para[n].getText()
                if('pages' in para_text or 'Pages' in para_text):
                    text_array=para_text.split("|")
                    for text_a in text_array:
                        if('Mb' in text_a or 'MB' in text_a or 'mb' in text_a):
                            book_size=text_a
                            book_size.encode('utf-8')
                            print(book_size)
                    break
    print(links_array)

ebook_links()
# def scrap():
#     r=requests.get(url)
#     next_para=[]
#     soup=BeautifulSoup(r.text)
#     header = soup.find('h2', attrs={'class': 'entry-title'})
#     href=header.find('a', href=True)
#     html=href['href']
#     soup_html=requests.get(html)
#     soup_html=BeautifulSoup(soup_html.text)
#     div=soup_html.find_all('div',attrs={'class':'entry-content'})
#     for k in div:
#         para=k.find_all(['p','h3'])
#         start=0
#         end=0
#         for j, i in enumerate(para):
#             if('Download:' in i.text):
#                    start = j+1
#                    print start
#
#             if('Related posts:' in i.text):
#                     end=j
#                     print end
#
#         for p in range(start, end):
#             href=para[p].find_all('a',href=True)
#             for i in href:
#                 next_para.append(i['href'])
#                 print(next_para)
#

