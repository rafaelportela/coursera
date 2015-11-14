import sys
import json

def read_tweets(fp):
    tweets = []
    for line in fp:
        tweets.append(json.loads(line))

    return tweets

def count_words(all_words, words_count, tweet_words):
    for word in tweet_words:
        if word not in all_words:
            all_words[word] = 0
        all_words[word] += 1

        words_count += 1

    return all_words, words_count

def count_tweet_words(tweets):
    words_count = 0
    all_words = {}
    for tweet in tweets:
        if 'text' in tweet:
            all_words, words_count = count_words(all_words, words_count, tweet['text'].split(' '))

    return term_frequency(all_words, words_count)

def print_items(dic):
    for key in dic.keys():
        print key, dic[key]

def term_frequency(all_words, words_count):
    term_frequency = {}
    for word in all_words.keys():
        term_frequency[word] = float(all_words[word]) / words_count
    return term_frequency

def main():
    tweet_file = open(sys.argv[1])
    tweets = read_tweets(tweet_file)

    words_count = count_tweet_words(tweets)
    print_items(words_count)

if __name__ == '__main__':
    main()
