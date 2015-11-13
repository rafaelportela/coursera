import sys
import json
import pdb

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

def tweet_sentiment_number(tweet, sentiments):
    sentiment_sum = 0
    words = tweet['text'].split(' ')
    for word in words:
        if word in sentiments:
            sentiment_sum += sentiments[word]
    return sentiment_sum

def print_tweets_sentiment(tweets, sentiments):
    for tweet in tweets:
        if 'text' in tweet:
            print tweet_sentiment_number(tweet, sentiments)

def main():
    sent_file = open(sys.argv[1])
    sentiments = read_sentiments(sent_file)

    tweet_file = open(sys.argv[2])
    tweets = read_tweets(tweet_file)

    print_tweets_sentiment(tweets, sentiments)

if __name__ == '__main__':
    main()
