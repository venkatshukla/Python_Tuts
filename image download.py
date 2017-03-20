import urllib.request
import random

def download_img(url):
    name = random.randrange(1,1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)

download_img("https://media.licdn.com/media/AAEAAQAAAAAAAAxcAAAAJDY2OWYwNzc1LTM2YTQtNDAwMC04MWE2LWUwODJjYTQ0YzRhNA.jpg")
