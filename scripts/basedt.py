import trainingset as ts

# Importing the classifiers.

from sklearn import tree

baseDTClassifier_emotions = tree.DecisionTreeClassifier()
baseDTClassifier_sentiments = tree.DecisionTreeClassifier()

# Fitting and predicting emotions.

baseDTClassifier_emotions.fit(ts.postsForEmotions_train, ts.emotions_train)
baseDT_emotions_results = baseDTClassifier_emotions.predict(ts.postsForEmotions_test)

# Fitting and predicting sentiments.

baseDTClassifier_sentiments.fit(ts.postsForSentiments_train, ts.sentiments_train)
baseDT_sentiments_results = baseDTClassifier_sentiments.predict(ts.postsForSentiments_test)