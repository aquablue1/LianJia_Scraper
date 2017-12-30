#-*- coding：utf-8 -*-
# lib import
from bs4 import BeautifulSoup
import urllib3
import urllib.parse


def pageQuote(url_string):

    # You’ll need a PoolManager instance to make requests
    https = urllib3.PoolManager()
    page = https.request('GET', url_string)
    print(page.data.decode())


if __name__ == '__main__':
    search_target = '春江新城'
    search_target_parsed = urllib.parse.quote(search_target)
    print(search_target_parsed)
    url_string = "https://nj.lianjia.com/ershoufang/rs" + search_target_parsed + "/"
    pageQuote(url_string)