import requests
from bs4 import BeautifulSoup
import operator


# Create a list of words
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    # loop through each post and get text
    for post_text in soup.findAll('a', {'class': 'title text-semibold'}):
        content = post_text.string
        # break each post up into a list of words
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


# Lowercase and remove odd symbols
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}|:<>?,./;'[]\=-\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols, "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


# Create dictionary with word counts
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort this dictionary by (0 for key, 1 for values)
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://thenewboston.com/forum/search_topics.php?s=word%20frequency&orderby=recent&page=2')