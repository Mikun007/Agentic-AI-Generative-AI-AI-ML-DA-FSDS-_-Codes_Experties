import streamlit as st
import re
import nltk
import pandas as pd

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, RegexpParser, ne_chunk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Streamlit config
st.set_page_config(page_title="NLP Pipeline (NLTK Only)", layout="wide")
st.title("🧠 NLP Text Preprocessing – Step by Step (NLTK)")

# Input
text = st.text_area(
    "Enter a paragraph or more:",
    height=200,
    placeholder="Paste your text here..."
)

if text:

    # ----------------------------------
    st.header("1️⃣ Text Cleaning")
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'[^a-z\s]', '', cleaned_text)
    st.write(cleaned_text)

    # --------------------
    st.header("2️⃣ Sentence Tokenization")
    sentences = sent_tokenize(text)
    st.write(sentences)

    # -------------------------------
    st.header("3️⃣ Word Tokenization")
    tokens = word_tokenize(cleaned_text)
    st.write(tokens)

    # -----------------------------------------
    st.header("4️⃣ Stop Words Removal")
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    st.write(filtered_tokens)

    # --------------------------------------------
    st.header("5️⃣ Stemming (Porter Stemmer)")
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_tokens]
    st.write(stemmed_words)

    # --------------------------
    st.header("6️⃣ Lemmatization (with POS)")
    lemmatizer = WordNetLemmatizer()
    pos_tags = pos_tag(filtered_tokens)

    lemmatized_words = []
    for word, tag in pos_tags:
        if tag.startswith("V"):
            lemmatized_words.append(lemmatizer.lemmatize(word, pos="v"))
        else:
            lemmatized_words.append(lemmatizer.lemmatize(word))

    st.write(lemmatized_words)

    # ----------------------------------
    st.header("7️⃣ POS Tagging")
    pos_df = pd.DataFrame(pos_tags, columns=["Word", "POS Tag"])
    st.dataframe(pos_df)

    # ----------------------------------
    st.header("8️⃣ Chunking (Noun Phrase)")
    grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
    chunk_parser = RegexpParser(grammar)
    chunk_tree = chunk_parser.parse(pos_tags)
    st.text(chunk_tree)

    # ----------------------------------
    st.header("9️⃣ Named Entity Recognition (NER)")
    ner_tree = ne_chunk(pos_tags)
    st.text(ner_tree)

    # ----------------------------------
    st.header("🔟 Bag of Words (BoW)")
    bow = CountVectorizer()
    bow_matrix = bow.fit_transform(sentences)

    bow_df = pd.DataFrame(
        bow_matrix.toarray(),
        columns=bow.get_feature_names_out()
    )
    st.dataframe(bow_df)

    # ----------------------------------
    st.header("1️⃣1️⃣ TF-IDF")
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(sentences)

    tfidf_df = pd.DataFrame(
        tfidf_matrix.toarray(),
        columns=tfidf.get_feature_names_out()
    )
    st.dataframe(tfidf_df)
