from frequency import count_tweet_words
from frequency import print_items

def main():
    tweets = [
            {'text': 'this is perfect I really like'},
            {'text': 'really terrible'}
            ]

    term_frequency = count_tweet_words(tweets)
    print_items(term_frequency)

if __name__ == '__main__':
    main()
