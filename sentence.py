from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd

xml_urls = os.listdir("The Blog Authorship Dataset")
df = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    post_data = {}
    for i in range(len(posts)):
        sentences = nltk.sent_tokenize(posts[i].string.strip())
        post_data.update({dates[i].string: sentences})
    d = pd.DataFrame(list(post_data.items()), columns=['Date', 'Posts'])
    df.append(d)
export_csv = pd.concat(df, axis=1, join='outer').to_csv('sentence.csv', index = None, header = True)
