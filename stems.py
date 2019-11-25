from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string

xml_urls = os.listdir("The Blog Authorship Dataset")
porter = nltk.stem.PorterStemmer()
df_stems = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    stems_data = {}
    for i in range(len(posts)):
        words = nltk.word_tokenize(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)))
        stem_words = {}
        for word in words:
            stem_words.update({word: porter.stem(word)})
        stems_data.update({dates[i].string: stem_words})
    df_stems.append(pd.DataFrame(list(stems_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_stems, axis=1, join='outer').to_csv('stems.csv', index = None, header = True)
