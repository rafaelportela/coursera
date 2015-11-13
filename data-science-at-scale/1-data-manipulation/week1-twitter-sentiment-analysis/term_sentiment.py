import sys
import json

def read_sentiments(fp):
    dict = {}
    for line in fp:
        term, score = line.split("\t")
        dict[term] = int(score)

    return dict

def read_tweets(fp):
    tweets = []
    for line in fp:
        tweets.append(json.loads(line))

    return tweets

def new_words_sentiment(tweet_text, sentiments):
    new_words = []
    tweet_sentiment = 0
    for word in tweet_text:
        if word in sentiments:
            tweet_sentiment += sentiments[word]
        else:
            new_words.append(word)

    return new_words, tweet_sentiment

def update_sentiments(sentiments, new_words, new_words_sentiment):
    for word in new_words:
        if word not in sentiments:
            sentiments[word] = []
        sentiments[word].append(new_words_sentiment)

def avarage(sentiments):
    sentiments_avarage = {}
    for word in sentiments.keys():
        count = len(sentiments[word])
        total = 0.0
        for value in sentiments[word]:
            total += value
        sentiments_avarage[word] = total / count

    return sentiments_avarage

def avarage_new_sentiment_words(tweets, sentiments):
    new_sentiments = {}
    for tweet in tweets:
        if 'text' in tweet:
            new_words, tweet_sentiment = new_words_sentiment(tweet['text'].split(' '), sentiments)
            update_sentiments(new_sentiments, new_words, tweet_sentiment)

    return avarage(new_sentiments)

def print_items(dic):
    for key in dic.keys():
        print key, dic[key]

def main():
    sent_file = open(sys.argv[1])
    sentiments = read_sentiments(sent_file)

    tweet_file = open(sys.argv[2])
    tweets = read_tweets(tweet_file)

    new_sentiments = avarage_new_sentiment_words(tweets, sentiments)
    print_items(new_sentiments)

if __name__ == '__main__':
    main()
