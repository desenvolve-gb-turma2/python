from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
import numpy
import uuid
from scipy.special import softmax
import matplotlib.pyplot as plt
import pandas as pd
from utils.utils import Utils

class Sentiment:
    def __init__(self):
        """ 
        Initializer responsible for initializing:
        roberta => Model traine in more than 120 million tweets.
        model => Classify words
        tokenizer => Break down text in smaller units
        emotion_values => Store values for emotions
        """
        self.roberta = "cardiffnlp/twitter-roberta-base-sentiment"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.roberta)
        self.tokenizer = AutoTokenizer.from_pretrained(self.roberta)
        # BUG: Emotion values can't stay here. I need to restart bot, otherwise it will allways sum the values
        self.emotion_values = { 'Negative': 0, 'Neutral': 0, 'Positive': 0}

    def get_score(self, tweet_input):
        """ 
        Read tweets and give score
        """
        tweet_phrase = (" ").join(tweet_input)
        encoded_tweet = self.tokenizer(tweet_phrase, return_tensors='pt')
        output = self.model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        biggest_value = max(scores)
        position = numpy.where(scores == biggest_value)[0][0]
        match position:
            case 0:
                word = 'Negative'
            case 1:
                word = 'Neutral'
            case 2:
                word = 'Positive'
        self.emotion_values[word] += 1

    def get_emotion_values(self):
        """ 
        Return emotion values
        """
        return self.emotion_values

    # TODO:Pick a better name for this funcion
    def helper_func(self, tweets):
        """ 
        Loop trough all tweets while invoking get score method
        """
        df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
        tweets_array = df['Tweet']
        for tweet in tweets_array:
            self.get_score(tweet)

    def get_words(self, tweets):
        """ 
        Loop trough all tweets changing @user_name to @user and http://site.com to http
        This step is needed for the model
        """
        for tweet in tweets:
            new_text = []
            for word in tweet.split():
                word = '@user' if word.startswith('@') and len(word) > 1 else word
                word = 'http' if word.startswith('http') else word
                new_text.append(word)
            self.get_score(new_text)

    def plot_sentiment(self, data):
        """ 
        Generate plot with unique file name.
        """
        file_name = Utils().get_unique_file_name()
        current_directory = Utils().get_current_directory()
        path = f'{current_directory}/temp/{file_name}.png'
        keys = list(data.keys())
        values = list(data.values())
        plt.bar(keys, values)
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.title('Sentiment Distribution')
        plt.savefig(path)
        return path
