__author__ = 'besimaltnok'

import requests

urllist=["http://www.besimaltinok.com",
         "http://bilaldurnagol.com",
         "http://www.hayvanlariyi.com",
         "http://www.pytr.com",
         "https://www.nsa.gov"]



for url in urllist:
    try:
        r = requests.get(url)
        print("{} {} {}").format(r.url, "-", r.headers['Server'])
    except:
        print("Not Found Server")
