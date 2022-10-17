import numpy as np
import json

with open('goemotions.json') as f:
	dataset = np.array(json.load(f))

# Splitting the information into posts, emotions, and sentiments.
posts = dataset[:, 0]
emotions = dataset[:, 1]
sentiments = dataset[:, 2]