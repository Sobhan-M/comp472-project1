import trainingset as ts

# Importing the classifiers.

from sklearn.naive_bayes import MultinomialNB

baseMNBClassifier_emotions = MultinomialNB()
baseMNBClassifier_sentiments = MultinomialNB()

# Training emotions classifiers.

baseMNBClassifier_emotions.fit(ts.postsForEmotions_train, ts.emotions_train)
baseMNB_emotions_results = baseMNBClassifier_emotions.predict(ts.postsForEmotions_test)

# Training sentiments classifiers.

baseMNBClassifier_sentiments.fit(ts.postsForSentiments_train, ts.sentiments_train)
baseMNB_sentiments_results = baseMNBClassifier_sentiments.predict(ts.postsForSentiments_test)