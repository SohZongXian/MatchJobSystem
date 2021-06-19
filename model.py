from similarity import Similarity
from keras.preprocessing.text import Tokenizer
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import re
import gensim
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Load pre-trained Word2Vec model.
#model = gensim.models.Word2Vec.load(r"word2vec_trained_model.model")

#model = gensim.models.KeyedVectors.load_word2vec_format(
#    r"GoogleNews-vectors-negative300.bin.gz", binary=True)

model = gensim.models.KeyedVectors.load_word2vec_format(datapath(r'C:\Users\Inspiron 7000\system\MatchJobSystem\w2v_model.txt'), binary=False)

stopwords = set(stopwords.words('english'))
ds = Similarity(model, stopwords=stopwords)

#description_df = pd.DataFrame(data[1])
#user_df = pd.DataFrame(data2)

def calculateSim(source_doc, target_docs):
    sim_scores = ds.calculate_similarity(source_doc, target_docs)
    print(sim_scores)
    return sim_scores