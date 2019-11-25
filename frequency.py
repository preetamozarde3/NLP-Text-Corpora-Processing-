from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string

xml_urls = os.listdir("The Blog Authorship Dataset")
df_freq = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    freq_data = {}
    for i in range(len(posts)):
        freq_dist = nltk.FreqDist(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)).split(' '))
        freq_data.update({dates[i].string: freq_dist.most_common()})
    df_freq.append(pd.DataFrame(list(freq_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_freq, axis=1, join='outer').to_csv('frequency.csv', index = None, header = True)
