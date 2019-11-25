from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string

xml_urls = os.listdir("The Blog Authorship Dataset")
stop_words = set(nltk.corpus.stopwords.words('english'))
df_nonstopwords = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    nonstopwords_data = {}
    for i in range(len(posts)):
        words = nltk.word_tokenize(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)))
        nonstopwords = [w for w in words if not w in stop_words]
        nonstopwords_data.update({dates[i].string: nonstopwords})
    df_nonstopwords.append(pd.DataFrame(list(nonstopwords_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_nonstopwords, axis=1, join='outer').to_csv('nonstopwords.csv', index = None, header = True)
