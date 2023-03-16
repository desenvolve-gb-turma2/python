# Twitetive

## Intro
The goal of this project is to create a bot capable of analyzing sentiments using Twitter. Sentiment analysis can make it possible to detect issues very fast, by detecting an increase in negative feelings. This way companies can better answer problems, and detect what their customers are liking the most.

## How to
### Downloading repository and making sure it will work
**Follow the steps below and make sure you are using the same libraries in the same version as I am using. Some time ago Twitter changed how third-party libraries interact with its API, and many stopped working. You can have many bugs and unforeseen problems if you use different versions.**

To clone repository
```bash
$ git clone repository
```

Enter inside the repository and download all the libraries needed. This will download the right libraries. **Follow this step, don't install by hand**
```bash
$ cd repository && pip install -r requirements.txt
```

Create .env file to store keys
```bash
$ touch .env
```

Now you need to create a BotFather API key if you don't have it already. Go to Telegram and find this bot:
<br>
<image src="utils/Images/bofather.png">
<br>
BotFather is a special Telegram account that allows users to manage their own bots.
<br>
To create a new bot, users need to chat with the BotFather account and follow the prompts to set up the bot's name, username, description, and other details.
<br>
Follow all the steps, you will get an API key at the end. Make sure to **NEVER SHARE YOUR API KEY**.
<br>
To store your API Key go to .env and paste it there following this format: 
```
BOTFATHER_API_KEY = 'API_KEY_HERE'
```
**You will need '** change only API_KEY_HERE

<br>
Start bot

```bash
$ python3 app.py
```

Now your bot is running, to access it go to Telegram and search for your bot (You have created it before)

### Passing Queries
**You need to pass lang:en always. Otherwise, this bot can get results in all languages, but currently, it only supports English**

<br>
Gets the last 500 tweets from the company sales force and analyzes its replies to understand if users are positive, negative or neutral when interacting with the company

```
(from:salesforce) lang:en filter:replies
