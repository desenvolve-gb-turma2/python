import snscrape.modules.twitter as sntwitter
import os
import pandas as pd
import csv
import uuid
import datetime
from utils.utils import Utils

class ScrapingTweeter:
    # TODO: improve methods to turn tweets into csv's
    def get_unique_filename(self):
        # WARNING: Use get_unique_file_name from utils
        current_time = datetime.datetime.now()
        filename = str(uuid.uuid4()) + current_time.strftime(".%d-%m-%Y_%H_%M_%S") + ".csv"
        return filename

    def write_to_csv(self, tweeter_csv, filename):
        current_file = os.path.abspath(__file__)
        current_path = os.path.dirname(current_file)
        path = current_path + "/../temp/" + filename
        df = pd.read_csv(tweeter_csv)
        df.to_csv(path)

    def form_query(self, raw_query):
        search_Term = raw_query.split()[1]
        return f"(from:{search_Term}) lang:en"

    def turn_tweets_array_into_csv(self, arr, filename):
        df = pd.DataFrame(arr, columns=['Date', 'User', 'Tweet'])
        current_file = os.path.abspath(__file__)
        # WARNING: Use utils get_current path
        current_path = os.path.dirname(current_file)
        path = current_path + "/temp/" + filename
        df.to_csv(path)
        # return filename

    def get_tweets(self, query, limit=10):
        """ 
        Invoke scraper and get tweets
        """
        tweets = []
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            if len(tweets) == limit:
                break
            else:
                tweets.append([tweet.date, tweet.user.username, tweet.rawContent])
        return tweets
