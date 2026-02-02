# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:20:05 2026

@author: mikun
"""

# XML scapping for xml sheet
import os
os.chdir(r"C:\Users\mikun\Downloads") # used to change the directory of the file to read from

import xml.etree.ElementTree as ET

tree = ET.parse("769952.xml")
root = tree.getroot()

root = ET.tostring(root, encoding="utf-8").decode("utf8")
root

import re
import nltk

from bs4 import BeautifulSoup

def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub("\[[^]]&\]", "", text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = re.sub("  ", "", text)
    return text


sample = denoise_text(root)

# TEXT PREPROCESSING

# text cleaning
clean_text = sample.lower()
clean_text = re.sub(r"[^a-z\s]", "", sample)


# sentence tokenization
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(sample)

# word tokenization
from nltk.tokenize import word_tokenize
tokens = word_tokenize(clean_text)


# stop word removal
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Stemming
from nltk.stem import PorterStemmer
stemming = PorterStemmer()
stemmed_words = [stemming.stem(word) for word in filtered_tokens]

# POS (part of Speach) finding the grammers
from nltk import pos_tag
pos = pos_tag(filtered_tokens)
                  
                  
# lammetization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemmatized_words = []
for word, tag in pos:
    if tag.startswith("V"):
        lemmatized_words.append(lemmatizer.lemmatize(word, pos="v"))
    else:
        lemmatized_words.append(lemmatizer.lemmatize(word))
        
# CHUNKING
# Define a chunking grammar using regular expressions
# This pattern defines a Noun Phrase (NP) chunk:
# <DT>? : Optional Determiner (zero or one)
# <JJ>* : Zero or more Adjectives
# <NN.*> : One or more Nouns (any noun type: NN, NNS, NNP, etc.)
grammer =  "NP: {<DT>?<JJ>*<NN.*>+}"
chunk_parser = nltk.RegexpParser(grammer)
chunk_tree = chunk_parser.parse(pos)


# NER (Named Entity Recognition)
from nltk import ne_chunk
ner_tree = ne_chunk(pos)

# BoW (Bag of Words)
from sklearn.feature_extraction.text import CountVectorizer

bow = CountVectorizer()
bow_matrix = bow.fit_transform(sentences)
bow_matrix_array = bow_matrix.toarray()


# TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(sentences)
tfidf_matrix_array = tfidf_matrix.toarray()
                  
# word2vec
sentences_2 = []
for sentence in sentences:
    sentence = re.sub("[^a-zA-Z]", " ", sentence)
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    sentences_2.append(tokens)
    
from gensim.models import Word2Vec

w2v_model = Word2Vec(sentences=sentences_2,
                     vector_size=100,
                     window=5,
                     min_count=2,
                     workers=4,
                     sg=1   # 1 = Skip-gram, 0 = CBOW
                     )    


w2v_model.wv["drug"]
w2v_model.wv.most_similar('drug')    






































