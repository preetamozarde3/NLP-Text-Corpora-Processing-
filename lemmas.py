from bs4 import BeautifulSoup
import os
import nltk
import pandas as pd
import string
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

xml_urls = os.listdir("The Blog Authorship Dataset")
lemmatizer = nltk.stem.WordNetLemmatizer()
df_lemmas = []

for xml_url in xml_urls:
    xml_file = open("The Blog Authorship Dataset/"+xml_url).read()
    xml_data = BeautifulSoup(xml_file, "xml")
    dates = xml_data.find_all(name='date')
    posts = xml_data.find_all(name='post')
    lemmas_data = {}
    for i in range(len(posts)):
        words = nltk.word_tokenize(posts[i].string.strip().translate(str.maketrans('', '', string.punctuation)))
        lemmas_words = {}
        for word in words:
            lemmas_words.update({word: lemmatizer.lemmatize(word, get_wordnet_pos(word))})
        lemmas_data.update({dates[i].string: lemmas_words})
    df_lemmas.append(pd.DataFrame(list(lemmas_data.items()), columns=['Date', 'Posts']))
export_csv = pd.concat(df_lemmas, axis=1, join='outer').to_csv('lemmas.csv', index = None, header = True)
