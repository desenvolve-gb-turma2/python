import re
from requests import get 
from telegram.ext import Updater, MessageHandler, Filters

# API address
CHUCKNORRIS_API_URL = "https://api.chucknorris.io/jokes/random"


def joke() -> str:
    """
    This function gets a call from user by writing "!joke" text and it
    returns a random joke provided by the ChuckNorris public API
    """
    msg = str()
    try:
        msg = get(CHUCKNORRIS_API_URL).json()["value"]
    except:
        msg = "Sorry but chuck API doesn't calls me back, seems like someone's dead :/"

    return msg



def parse_msg(update, context) -> None:
    """
    This function reads the text input and if it matches the defined regex then the user
    gets the joke he/she might want to read :)
    """
    if re.search("^(!joke)", update.message.text, re.IGNORECASE | re.DOTALL):
        update.message.reply_text(joke())



def main() -> None:
    updater = Updater("6128121833:AAFq4G-yvg-BF9qw9kVdpF2hq-1-xJhx5Zg")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(MessageHandler(Filters.text, parse_msg)) # parses all text messages
 
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()



if __name__ == '__main__':
    main()