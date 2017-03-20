import requests
from bs4 import BeautifulSoup
import subprocess, sys



url = "http://status.catchpoint.com"

def crawl(url):

        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, "html.parser")

        for link in soup.find_all('a', {'class':'actual-title'}):
                title = link.string
                p = subprocess.Popen(["powershell.exe","C:\\Scripts\\ToastNotif.ps1 \"" + str(title) + "\""],stdout=sys.stdout)
                p.communicate()


crawl(url)

