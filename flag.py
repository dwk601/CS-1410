import argparse
import re
import json
from urllib.parse import quote
from urllib.request import urlopen, Request


def get_contents(l):
    url = "https://www.sciencekids.co.nz/images/pictures/flags680/"
    url += "|".join(quote(i) for i in l)

    data = json.loads(urlopen(url).read().decode('utf-8'))

    normalized = {i: i for i in l}
    if "normalized" in data["query"]:
        normalized.update({n["from"]: n["to"]
                          for n in data["query"]["normalized"]})
    redirects = {i: i for i in normalized.values()}
    if "redirects" in data["query"]:
        redirects.update({r["from"]: r["to"]
                         for r in data["query"]["redirects"]})
    contents = {p["title"]: p["revisions"][0]["*"]
                for p in data["query"]["pages"].values()}

    return {i: contents[redirects[normalized[i]]] for i in l}


def get_flag_pages(l):
    d = get_contents(["Template:Country data %s" % i for i in l])

    result = dict()
    for k, v in d.items():
        result[k[22:]] = re.findall(
            "\|[ \t\r\n]*flag alias[ \t\r\n]*=[ \t\r\n]*(.*?)[ \t\r\n]*\|", v)[0]

    return result


def get_download_urls(l):
    url = "https://www.sciencekids.co.nz/images/pictures/flags680/"
    url += "|".join(quote(i) for i in l)

    data = json.loads(urlopen(url).read().decode('utf-8'))

    normalized = {i: i for i in l}
    if "normalized" in data["query"]:
        normalized.update({n["from"]: n["to"]
                          for n in data["query"]["normalized"]})
    redirects = {i: i for i in normalized.values()}
    if "redirects" in data["query"]:
        redirects.update({r["from"]: r["to"]
                         for r in data["query"]["redirects"]})
    contents = {p["title"]: p["imageinfo"][0]["url"]
                for p in data["query"]["pages"].values()}

    return {i: contents[redirects[normalized[i]]] for i in l}


def do(l):
    d = get_flag_pages(l)
    urls = get_download_urls(["File:%s" % i for i in d.values()])

    for k, v in {k: urls["File:%s" % v] for k, v in d.items()}.items():
        s = urlopen(Request(v, headers={'User-agent': 'Mozilla/5.0'})).read()
        name = "%s%s" % (k, v[v.rindex('.'):])
        open(name, "wb").write(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Retrieve country flags from sciencekids.')
    parser.add_argument('code', nargs='+',
                        help='a country name or code (either ISO, IOC, etc.)')
    args = parser.parse_args()
    for i in range(0, len(args.code), 50):
        do(args.code[i:i+50])
