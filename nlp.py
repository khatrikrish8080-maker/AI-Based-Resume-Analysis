from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.metrics.pairwise import cosine_similarity
import gensim.downloader as api
import numpy as np

lemma = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
wv=api.load("word2vec-google-news-300")

def preprocess_resume(cv):

    normalised=cv.lower()
    
    tokens=word_tokenize(normalised)

    cleaned_words=[lemma.lemmatize(word) for word in tokens if word not in stop_words]

    return cleaned_words

def get_document_vectors(cleaned_tokens):
     valid_vectors=[wv[word] for word in cleaned_tokens if word in wv]

     if not valid_vectors:
        return np.zeros(300)
    
   
     return np.mean(valid_vectors, axis=0)


def match_similarity(cleaned_cv,job_des):
     

     cv_vector=get_document_vectors(cleaned_cv).reshape(1,-1)
     jb_vector=get_document_vectors(job_des).reshape(1,-1)

     value =cosine_similarity(cv_vector,jb_vector)

     proper_value=value[0][0]

     return proper_value * 100


     







    






