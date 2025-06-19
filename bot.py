from dotenv import load_dotenv
import telebot
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'começar'])
def start(msg):
    bot.reply_to(msg, 'Olá! Como posso ajudar? Escrava /comandos para saber os comandos do bot')

@bot.message_handler(commands=['comandos'])
def comandos(msg):
    texto = (
        "/lang – Fala quais são as melhores linguagens de programação.\n\n"
        "/langyt – Mostra os melhores canais de programação no YouTube.\n\n"
        "➡️ Após usar o /lang, clique no nome da linguagem listada para acessar uma aula sobre ela."
    )
    bot.reply_to(msg, texto, parse_mode='Markdown')

@bot.message_handler(commands=['lang'])  # Fala quais são as melhores linguagens de programação de 2025
def lang(msg):
    texto = (
        "🌟 *Melhores linguagens de programação de 2025:*\n\n"
        "*/Python*: Versátil e popular, reina em áreas como IA, aprendizado de máquina, ciência de dados e automação. "
        "Sua sintaxe clara e vasta gama de bibliotecas a tornam atraente para iniciantes e projetos complexos.\n\n"
        "*/JavaScript*: Indispensável para desenvolvimento web, com frameworks como React, Angular e Vue impulsionando "
        "a criação de aplicações web dinâmicas e interativas.\n\n"
        "*/Go (Golang)*: Desenvolvida pelo Google, destaca-se pela sua performance e concorrência, sendo excelente para "
        "sistemas distribuídos e aplicações backend de alta performance.\n\n"
        "*/Java*: Continua sendo uma linguagem robusta e amplamente utilizada em aplicações corporativas.\n\n"
        "*/PHP*: Popular no desenvolvimento web, especialmente em aplicações legadas."
    )
    bot.reply_to(msg, texto, parse_mode='Markdown')

@bot.message_handler(commands=['langyt'])
def langyt(msg):
    texto = (
        "🎥 Um otimo canal de progamação é o https://www.cursoemvideo.com/cursos/ \n\n"
        "Junto com o https://www.youtube.com/@HashtagProgramacao \n\n"
        "Todos os dois tem uma didatica unica e de facil aprendizado."
        )
    bot.reply_to(msg, texto, parse_mode='Markdown')

@bot.message_handler(commands='Python')
def Python(msg):
    bot.reply_to(msg, 'https://www.cursoemvideo.com/curso/python-3-mundo-1/')

@bot.message_handler(commands='JavaScript')
def JavaScript(msg):
    bot.reply_to(msg, 'https://www.cursoemvideo.com/curso/javascript/')

@bot.message_handler(commands='Go')
def Go(msg):
    bot.reply_to(msg, 'https://www.youtube.com/watch?v=_MkQLDMak-4&list=PL5aY_NrL1rjucQqO21QH8KclsLDYu1BIg')

@bot.message_handler(commands='Java')
def Java(msg):
    bot.reply_to(msg, 'https://www.cursoemvideo.com/curso/java-basico/')

@bot.message_handler(commands='PHP')
def PHP(msg):
    bot.reply_to(msg, 'https://www.cursoemvideo.com/curso/curso-de-php-moderno-modulo-01/')

bot.infinity_polling()