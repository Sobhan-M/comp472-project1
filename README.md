# COMP 472 - Project 1
## Link
[GitHub](https://github.com/Sobhan-M/comp472-project1)
## Description
This is the COMP 472 project 1 files for my group "Deus Ex Machina". I am the only member of this group.
In this project I train and tested several machine learning models on a Reddit post dataset and compared the different results.
## How To Run
1. Make sure you have Python 3.8 installed.
2. Install all the necessary packages for this project. In retrospect, I should have used a virtual environment to simplify this step.
```
python3.8 -m pip install gensim matplotlib nltk numpy savefig sklearn
```
3. Run each of the files in Jupyter Notebooks in order: `part1.ipynb`, `part2.ipynb`, `part3.ipynb`. You can also run the exploration files in a similar fashion. Running all the cells in order will work.
4. Read the final analysis in the `analysis.md` file.
## Note
When the project was first created I made the mistake of thinking I needed the targets to be numerical values as well, as such the performance files have numbers instead of the class names. They are listed in alphabetical order and I have displayed the indices here.
### Emotions
```
0		admiration
1		amusement
2		anger
3		annoyance
4		approval
5		caring
6		confusion
7		curiosity
8		desire
9		disappointment
10		disapproval
11		disgust
12		embarrassment
13		excitement
14		fear
15		gratitude
16		grief
17		joy
18		love
19		nervousness
20		neutral
21		optimism
22		pride
23		realization
24		relief
25		remorse
26		sadness
27		surprise

```
### Sentiments
```
0		ambiguous
1		negative
2		neutral
3		positive

```