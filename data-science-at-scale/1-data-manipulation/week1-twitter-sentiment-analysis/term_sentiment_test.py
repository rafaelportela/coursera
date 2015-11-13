from term_sentiment import avarage_new_sentiment_words
from term_sentiment import print_items

def main():
    tweets = [
            {'text': 'this is perfect I really like'},
            {'text': 'really terrible'}
            ]
    sentiments = {'perfect': 2, 'terrible': -3}
    
    new_sentiments = avarage_new_sentiment_words(tweets, sentiments)
    print_items(new_sentiments)

if __name__ == '__main__':
    main()
