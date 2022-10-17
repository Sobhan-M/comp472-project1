# Testing the idea of using Word2Vec in a separate file to speed up performance compared to Jupyter Notebooks.
import gensim.downloader as api

w2v = api.load('word2vec-google-news-300')

print("Done")