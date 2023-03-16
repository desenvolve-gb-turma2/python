import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import os
import pandas as pd
import dotenv
from twiter_scraping.twitter_scraper import ScrapingTweeter
from sentiment_analysis.sentiment import Sentiment

# TODO: Find a way to plot graphics !!DONE!!
# TODO: Find a way to plot prettier graphics
# TODO: Add Sentiment analysis to portuguese
# TODO: Research how to improve precision
# TODO: Delete images from temp when not needed

class TelegramBot:
    """ 
    Telegram bot class. This class is responsible for connecting with Botfather API.
    This is the main class of this project. It connects all the other classes and most
    of the logic goes here.
    """
    def __init__(self):
        """
        Initializer responsible for initializing:
        logging => Will give me info about the processes and errors.
        Sentiment => Allows me to call sentiment class from anywhere.
        ScrapingTweeter => Class responsible for scraping tweeter with given parameters
        """
        logging.basicConfig(
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt = "%d-%m-%Y %H:%M:%S",
                level=logging.INFO
                )
        self.sentiment = Sentiment()
        self.tweet_bot = ScrapingTweeter()

    def _get_api_key(self):
        """ 
        Load my keys in a safe way using dotenv library
        """
        dotenv.load_dotenv(dotenv.find_dotenv())
        return os.getenv('BOTFATHER_API_KEY')

    async def send_message(self, context_obj, update_obj, text):
        """ 
        Send messages to telegram users
        """
        await context_obj.bot.send_message(chat_id=update_obj.effective_chat.id, text=text)

    async def send_graphic(self, context, update, graphic_path):
        """ 
        Receive a path, open image/graphic as binary and send image to telegram user
        """
        with open(graphic_path, 'rb') as photo:
            await context.bot.send_photo(photo=photo, chat_id=update.effective_chat.id)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ 
        Help messages 
        """
        # TODO: Add all help options
        await self.send_message(context, update,
                                "/user twiter_username => Run sentiment analysis for the last tweets of twitter_username")

    # WARNING: Testing delete later
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.send_message(context, update, "Test Message")

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.send_message(context, update, update.message.text)

    async def user(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ 
        Read tweets from any user, analyze them, and show the emotions the user was feeling when he wrote the tweets.
        Emotions can be: Neutral, negative, and positive
        """
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Processing. It can take a while. Please, have patience :)")
        query = self.tweet_bot.form_query(update.message.text)
        tweets = self.tweet_bot.get_tweets(query)
        df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
        self.sentiment.helper_func(tweets)
        emotion_values = self.sentiment.get_emotion_values()
        graphic_path = self.sentiment.plot_sentiment(emotion_values)
        await self.send_graphic(context, update, graphic_path)
        await self.send_message(context, update, f"{emotion_values}")

    async def topic(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ 
        Get tweets from a company and check how that company's clients reacted to the tweets.
        It will analyze if the users where feeling: Neutral, positive or negative 
        """
        query = update.message.text.replace('/topic', '').strip()
        await self.send_message(context, update, "Just a moment")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=query)
        tweets = ScrapingTweeter().get_tweets(query)
        self.sentiment.helper_func(tweets)
        emotion_values = self.sentiment.get_emotion_values()
        graphic_path = self.sentiment.plot_sentiment(emotion_values)
        await self.send_graphic(context, update, graphic_path)
        await self.send_message(context, update, f"{emotion_values}")

    async def unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """ 
        This function is triggered when the user tries to type an unknown command.
        """
        await self.send_message(context, update, "Sorry, I can't understand that. You can type /help to get a list of commands")

    def manage_handlers(self):
        """ 
        Handlers responsible for managing all of class Telegram Bot async methods
        """
        application = ApplicationBuilder().token(self._get_api_key()).build()
        start_handler = CommandHandler('start', self.start)
        user_handler = CommandHandler('user', self.user)
        topic_handler = CommandHandler('topic', self.topic)
        help_handler = CommandHandler('help', self.help)
        echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), self.echo)
        unknown_handler = MessageHandler(filters.COMMAND, self.unknown)
        application.add_handler(start_handler)
        application.add_handler(user_handler)
        application.add_handler(help_handler)
        application.add_handler(topic_handler)
        application.add_handler(echo_handler)
        application.add_handler(unknown_handler)
        application.run_polling()

if __name__ == '__main__':
    TelegramBot().manage_handlers()
