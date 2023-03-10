import telebot
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

#o usuario do bot é animerandomquote_bot
nome_anime = ""
nome_personagem =""

def quote_check (mensagem): #confirma se é pra mandar frase
    if mensagem.text == "!frase":
        return True
    else:
        return False

@bot.message_handler(func=quote_check)
def frase(mensagem):
    response = requests.get('https://animechan.vercel.app/api/random') #chamada da api aleatória
    jsonquote = response.json()
    quote = ('Anime: '+ jsonquote['anime']+'\n'
             'Personagem: '+ jsonquote['character']+'\n'
             'Frase: '+ jsonquote['quote']+'\n')    
    bot.send_message(mensagem.chat.id, quote)


def help_check (mensagem): #comando de ajuda
    if mensagem.text == "!help":
        return True
    else:
        return False

@bot.message_handler(func=help_check)
def help(mensagem):
    bot.reply_to(mensagem, "Digite !frase para receber uma frase de um anime aleatório. \nDigite !anime e o nome do anime para receber uma frase daquele anime. \nDigite !nome e o nome do personagem para receber uma frase daquele personagem.")

def title_check (mensagem): #confirmando se é pra procurar por título usando split na mensagem
    try:
        a,b = mensagem.text.split(' ', 1)
        if a == "!anime":
            global nome_anime
            nome_anime = b
            return True
    except:
        return False
        
@bot.message_handler(func=title_check)
def frase_anime(mensagem):
    try:
        response = requests.get('https://animechan.vercel.app/api/random/anime?title='+nome_anime) #chamada da api usando a segunda parte do split
        jsonquote = response.json()
        quote = ('Anime: '+ jsonquote['anime']+'\n'
                'Personagem: '+ jsonquote['character']+'\n'
                'Frase: '+ jsonquote['quote']+'\n')             
        bot.send_message(mensagem.chat.id, quote)
    except:
        bot.send_message(mensagem.chat.id, "Título não encontrado, use um título existente ou digite de forma diferente")

def name_check (mensagem): #semelhante ao title check
    try:
        a,b = mensagem.text.split(' ', 1)
        if a == "!nome":
            global nome_personagem
            nome_personagem = b
            return True
    except:
        return False
        
@bot.message_handler(func=name_check)
def frase_personagem(mensagem):
    try:
        response = requests.get('https://animechan.vercel.app/api/random/character?name='+nome_personagem)
        jsonquote = response.json()
        quote = ('Anime: '+ jsonquote['anime']+'\n'
                'Personagem: '+ jsonquote['character']+'\n'
                'Frase: '+ jsonquote['quote']+'\n')      
        bot.send_message(mensagem.chat.id, quote)
    except:
        bot.send_message(mensagem.chat.id, "Nome não encontrado, use um nome existente ou digite de forma diferente")

@bot.message_handler(func= lambda m: name_check or title_check or help_check or quote_check == False) #manda a mensagem abaixo caso qualquer coisa diferente seja usada
def msg_erro(mensagem):
    bot.send_message(mensagem.chat.id,"Digite !help e veja os comandos existentes, qualquer comando diferente não irá funcionar.")


bot.infinity_polling()