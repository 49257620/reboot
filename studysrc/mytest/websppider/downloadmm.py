# encoding: utf-8
# Author: LW

import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    return  urllib.request.urlopen(req).read()

def get_page(url):

    html = url_open(url).decode('utf-8')
    print(html)
    a = html.find("current-comment-page")+23
    b = html.find(']',a)

    return  html[a:b]


def find_image(url):
    html = url_open(url).decode('utf-8')
    print(html)
    img_addrs = []

    a = html.find("commentlist")
    b = html.find('</ol>',a)

    html = html[a:b]



def save_img(folder,img_addrs):
    pass

def downloadmm(folder="E://OOXX",pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -=i
        page_url = url + 'page-'+str(page_num)+'#comments'
        img_addrs = find_image(page_url)
        save_img(folder,img_addrs)

if __name__ == '__main__':
    #downloadmm()
    find_image('http://jandan.net/ooxx/page-102#comments')