# Part 4 - Analysis
In this part we will analyze the results of the project.
## 4.1 - Dataset Analysis

To better analyze our data, let us look at it in parts.

### Emotions

![Emotions](emotions.png)

Let us first look at the dataset of emotions and analyze the information present.

By looking at the bar-graph we can tell that emotions are not evenly distributed amongst the posts. In fact, the "neutral" emotion is by far the most common at over 50,000 instances. Whereas all other emotions barely surpass 10,000 if they even get close. This can severely affect our accuracy.

Besides the uneven distribution of emotions in our data, there is an intrinsic problem with the data classification itself. The current database assumes that emotions can be neatly categorized into buckets, but that is not the case in real life. Emotions tend to be very complex and we can feel multiple emotions at once. It's entirely possible for a post to invoke both "joy" and "curiosity". Similarly, some emotions blend into one another. "Anger" and "annoyance" can be very similar emotions. As can "sadness" and "grief". How does our dataset distinguish this information in a meaningful capacity? Because the lack of distinction simply blends a lot of information together, giving us a messy result.

### Sentiments

![Sentiments](sentiments.png)

The distribution of the sentiments is much more even than that of our emotions. That said, there are still some problems.

While the two largest values ("neutral" and "positive") have similar proportions. The "negative" sentiment has roughly 3/4ths  of their proportions. The "ambiguous" sentiment is even worst at under half the proportion of the others. Therefore we again lack an even distribution.

Furthermore, there's again the issue of semantics. While "positive" and "negative" are easy to understand, what about "neutral" and "ambiguous"? These two categories seem very semantically similar, so our data classification is flawed. Especially since there are so few classes.

## 4.2 - Result Analysis

### Metrics

By looking at the general performance of all our models, we can tell the accuracy and macro f1 scores are very low in all cases.
```
EMOTIONS:
			BMNB	BDT		BMLP	TMNB	TDT		TMLP	EBMLP		ETMLP			
accuracy	0.38	0.36	0.43	0.39	0.37	0.43	0.39		0.39
macro f1	0.16	0.27	0.24	0.22	0.27	0.26	0.18		0.18

avg accuracy		0.3925
avg macro f1 		0.2225

```

```
SENTIMENTS:
			BMNB	BDT		BMLP	TMNB	TDT		TMLP	EBMLP		ETMLP			
accuracy	0.55	0.55	0.57	0.55	0.55	0.56	0.51		0.50
Macro F1	0.50	0.53	0.53	0.50	0.53	0.51	0.47		0.47

avg accuracy		0.5425
avg macro f1 		0.505

```

### Accuracy Versus Macro F1

First let us note the discrepancy between the accuracy and macro f1 scores for the emotions. The average accuracy is almost double that of the average macro f1 score.

This lines up with the analysis made in part 4.1, where we noted that the classes of the emotions were very imbalanced. This means the accuracy is a poor metric in this instance so we will be relying on the macro f1 scores.

We also notice that this discrepancy exists in the sentiments as well, but to a much smaller degree. This is due to the same reason as the above and as was mention in part 4.1, since our "ambiguous" class has too few instances which leads to imbalance.

### Low Scores - Emotions

The very low scores in our models indicate a fundamental problem with the design and implementation of the models and the dataset.

As we can see in the emotions table, the macro f1 score is around 25%. This suggests the model is incredibly ineffective at correctly labeling the Reddit post.

Looking at the confusion matrix of our Base Multinomial Naive Bayes model
![Confusion Matrix](confusion-matrix.png)






