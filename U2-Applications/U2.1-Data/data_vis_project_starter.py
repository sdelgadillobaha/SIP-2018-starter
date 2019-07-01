'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    # print(tweet.keys())
    # tweettext.append(tweet['text'])
    tweetstring += tweet['text']
# print(tweettext)
print(tweetstring)
polarity = []
subjectivity = []

for tweet in tweettext:
    tb = TextBlob(tweet)
    subjectivity.append(tb.subjectivity)
    polarity.append(tb.polarity)

# print(polarity)
# print(subjectivity)


# avg_p = sum(polarity) / len(polarity)
# avg_s = sum(subjectivity) / len(subjectivity)
# print(avg_p)
# print(avg_s)

# import matplotlib.pyplot as plt

# plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.xlabel('Values')
# plt.ylabel('Number of Items')
# plt.title('Histogram')
# plt.axis([-1.1, 1.1, 0, 106])
# plt.grid(True)
# plt.show()


# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.sentiment)


# tweettext = []
# tweetstring = ''
# for tweet in tweetData:
#     tweetstring += tweet['text']

# print(tweeststring)
tweetBlob = TextBlob(tweetstring)
word_dict = {}
for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]

print(word_dict)