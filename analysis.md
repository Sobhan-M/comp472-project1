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

In terms of metrics, this means our accuracy is entirely worthless. Just by always guessing "neutral" in our tests, the model would have a high accuracy (though it doesn't appear to have done that based off of the low metrics).





