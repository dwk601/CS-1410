#!/usr/bin/env python
# encoding=utf-8

from urllib2 import Request, urlopen
from BeautifulSoup import BeautifulSoup
import base64
import os
import sys


def gethtml(url, cache=True):
    path = '/tmp/pycache' + base64.b64encode(url)
    s = cache and os.path.exists(path) and 'r' or 'w'
    res = None
    with open(path, s) as f:
        if s == 'r':
            res = f.read()
        else:
            req = Request(url, headers={'User-Agent': 'Not python'})
            res = urlopen(req).read()
            f.write(res)  # cache
    return res


def getcountries():
    url = 'http://en.wikipedia.org/wiki/List_of_countries'
    html = gethtml(url)
    soup = BeautifulSoup(html)
    spans = soup.findAll('span', {'class': 'flagicon'})
    res = []
    href = None
    for span in spans:
        name = [span.nextSibling.string]
        try:
            if hasattr(span.next, 'name'):  # not empty span
                href = 'http:' + span.next['src']
                if ext == 'svg':
                    href = os.path.split(href)[0]
                if size:
                    name.append(size)
                res.append('-o "' + '_'.join(name) + '.' + ext + '" ' + href)
        except:
            print name, sys.exc_info()[0]
            break
    return res


# python dl_country_flags.py.py
# python dl_country_flags.py.py png [size]
if __name__ == '__main__':
    ext = 'svg'
    size = None
    if len(sys.argv) > 1:
        ext = 'png'
        size = '200'
    if len(sys.argv) > 2:
        size = sys.argv[2]

    urls = getcountries()
    url = ' '.join(urls).encode('utf-8')
    if ext == 'svg':
        url = url.replace('/thumb/', '/')
    else:
        import re
        url = re.sub(r'(?<=svg/)\d+(?=px-Flag_of)', size, url)
    # print url
    os.system('curl -#f ' + url)
    print len(urls), 'files done'
