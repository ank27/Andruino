__author__ = 'ankurkhandelwal'

import requests
from bs4 import BeautifulSoup

from MyApplication.template.MyApplication import *

# Beautiful soup extract all the html tags and you can traverse through them usign .get to a particular tag
# Either u use soup.find('a') where a is tag in html
# or you can mention tag to it like div in below function, a tag is kind of dictionary where u can find its attribute
# tag.attrs gives all attribute of particular tag
#

def scrap():
    r=requests.get("http://www.pythonforbeginners.com")
    data=r.text
    soup = BeautifulSoup(data)
    soup.prettify()
    tag=soup.div
    split_class=[]
    div_array=[]
    div_all=soup.find_all('div')
    # print(div_all)
    for div in div_all:
        if(div.get('class')):
            split_class=div.get('class')
            # print(split_class)
            for j in split_class:
                if('cf' in j):
                    div_array.append(div)
    print(div_array)
    for i in div_array:
        print(i.text)
        # soup_div=BeautifulSoup(i)
        # comment = soup_div.div.string()
                    # print(split_class)
                    # soup_div=BeautifulSoup(split_class)
                    # soup_div.get('class')
                    # print(soup_div.get('class'))
        #         it gives "post-bodycopy cf"
        #             comment=soup_div.div.string()
        #             print(comment)

                    # above function gives
                    # <div class="post-bodycopy cf">
                    #     The sockets module provides an easy way to look up a host name's ip address. import socket addr1 = socket.gethostbyname('google.com') addr2 = socket.gethostbyname('yahoo.com') print(addr1, addr2) Which will output the following ip addresses: 173.194.121.9 98.138.253.109
                    # </div>
                    # print(div)

        # split_class.split()
        # for c in split_class:
        #     if 'cf' in c:
        #         print(div)
        # if div.get('class') == "'post-bodycopy', 'cf'":
        #     print(div)
    # print(tag)
    # <div id="fb-root"></div>
    # print(tag.attrs)
    # print (tag['id'])
    # fb_root
    # so id is key and fb_root is value
    return tag

    # print(soup.title.string)
    # print soup
    # for l in soup.find_all('a'):
    #     print(l.get("href"))
        # return l.get("href")
    data=[]
    href_data=[]
    link_title=[]
    array=soup.find_all('a')
    data=array
    # print(data[1])
    # print(soup.find_all('a'))
    for j in data:
        # print(j.get('href'))
        # print(j.get('title'))
        href_data.append(j.get('href'))
        link_title.append(j.get('title'))
    # print(href_data)
    # print(link_title)


def parse_doc():
    soup_doc=BeautifulSoup(open('index.html'))
    soup_doc.prettify()
    print((soup_doc))