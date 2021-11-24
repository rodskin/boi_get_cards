# importing required libraries
from multiprocessing import Process
import subprocess
import requests
from bs4 import BeautifulSoup


# target URL
url = "https://foursouls.com/card-search/"

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

for x in range(1, 21):
    page_url = url
    if x > 1:
        page_url = url + 'page/' + "% s" % x
    #print(page_url)

    response = requests.request("GET", page_url, headers=headers)

    data = BeautifulSoup(response.text, 'html.parser')
    # find all with the image tag
    images = data.find_all('img', src=True)

    for image in images:
        #print(image)
        if image['src'].startswith( 'https' ):
            #print(image['src'].replace("-308x420", ""))
            image_src = image['src'].replace("-308x420", "")
            image_src = image_src.replace("-420x308", "")
            print(image_src)
