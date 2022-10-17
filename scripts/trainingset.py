import loadingdata as ld

# Vectorizing our posts.

from sklearn import feature_extraction

vectorizer = feature_extraction.text.CountVectorizer()
vectorizedPosts = vectorizer.fit_transform(ld.posts)

# Encoding our classes.

from sklearn import preprocessing

emotionsLabelEncoder = preprocessing.LabelEncoder()
sentimentsLabelEncoder = preprocessing.LabelEncoder()

encodedEmotions = emotionsLabelEncoder.fit_transform(ld.emotions)
encodedSentiments = sentimentsLabelEncoder.fit_transform(ld.sentiments)

# Splitting data for training and testing.

from sklearn.model_selection import train_test_split

postsForEmotions_train, postsForEmotions_test, emotions_train, emotions_test =  train_test_split(vectorizedPosts, encodedEmotions, test_size=0.20)
postsForSentiments_train, postsForSentiments_test, sentiments_train, sentiments_test =  train_test_split(vectorizedPosts, encodedSentiments, test_size=0.20)