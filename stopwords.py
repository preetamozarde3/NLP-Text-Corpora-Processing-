from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string

xml_urls = os.listdir("The Blog Authorship Dataset")
stop_words = set(nltk.corpus.stopwords.words('english'))
df_stopwords = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    stopwords_data = {}
    for i in range(len(posts)):
        words = nltk.word_tokenize(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)))
        stopwords = [w for w in words if w in stop_words]
        stopwords_data.update({dates[i].string: stopwords})
    df_stopwords.append(pd.DataFrame(list(stopwords_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_stopwords, axis=1, join='outer').to_csv('stopwords.csv', index = None, header = True)
