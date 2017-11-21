import requests
from bs4 import BeautifulSoup
import subprocess, sys

http_proxy = "proxy:8080"


proxyDict = {
              "http"  : http_proxy,
            }

url = "http://status.catchpoint.com"

def crawl(url):

        source_code = requests.get(url, proxies=proxyDict)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.find_all('a', {'class':'actual-title'}):
                title = link.string
                p = subprocess.Popen(["powershell.exe","C:\\Scripts\\ToastNotif.ps1 \"" + str(title) + "\""],stdout=sys.stdout)
                p.communicate()
                print(title)

crawl(url)

