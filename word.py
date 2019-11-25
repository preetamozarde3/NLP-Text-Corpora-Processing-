from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string

xml_urls = os.listdir("The Blog Authorship Dataset")
df_words = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    word_data = {}
    for i in range(len(posts)):
        words = nltk.word_tokenize(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)))
        word_data.update({dates[i].string: words})
    df_words.append(pd.DataFrame(list(word_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_words, axis=1, join='outer').to_csv('word.csv', index = None, header = True)
