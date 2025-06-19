from dotenv import load_dotenv
import telebot
from telebot import types
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

language_links = {
    'Python': 'https://www.cursoemvideo.com/curso/python-3-mundo-1/',
    'JavaScript': 'https://www.cursoemvideo.com/curso/javascript/',
    'Go': 'https://www.youtube.com/watch?v=_MkQLDMak-4&list=PL5aY_NrL1rjucQqO21QH8KclsLDYu1BIg',
    'Java': 'https://www.cursoemvideo.com/curso/java-basico/',
    'PHP': 'https://www.cursoemvideo.com/curso/curso-de-php-moderno-modulo-01/'
}

# Comando /start
@bot.message_handler(commands=['start', 'começar'])
def start(msg):
    texto = (
        "👋 *Olá!* Seja bem-vindo ao bot!\n\n"
        "Digite /comandos para ver o que posso fazer por você. 🚀"
    )
    bot.reply_to(msg, texto, parse_mode='Markdown')

# comando do "/comandos"
@bot.message_handler(commands=['comandos'])
def comandos(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/lang')
    btn2 = types.KeyboardButton('/langyt')
    btn3 = types.KeyboardButton('/dev')
    markup.add(btn1, btn2, btn3)
    texto = (
        "📌 *Comandos disponíveis:*\n\n"
        "/lang – Melhores linguagens de programação.\n"
        "/langyt – Melhores canais de programação.\n"
        "/dev - Para me conhecer! \n\n"
        "Toque em um comando abaixo para começar 👇"
    )
    bot.send_message(msg.chat.id, texto, reply_markup=markup, parse_mode='Markdown')

# comando para o "lang"
@bot.message_handler(commands=['lang'])
def lang(msg):
    markup = types.InlineKeyboardMarkup()
    for lang, link in language_links.items():
        markup.add(types.InlineKeyboardButton(text=lang, url=link))
    texto = (
        "🌟 *Melhores linguagens de programação de 2025:*\n\n"
        "Toque no nome da linguagem para acessar um curso!"
    )
    bot.send_message(msg.chat.id, texto, reply_markup=markup, parse_mode='Markdown')

# comando para o "langyt"
@bot.message_handler(commands=['langyt'])
def langyt(msg):
    texto = (
        "🎥 *Melhores canais de programação:*\n\n"
        "✅ [Curso em Vídeo](https://www.cursoemvideo.com/cursos/)\n"
        "✅ [Hashtag Programação](https://www.youtube.com/@HashtagProgramacao)\n\n"
        "Ambos com didática clara e ótima para iniciantes! 🚀"
    )
    bot.send_message(msg.chat.id, texto, parse_mode='Markdown')

# comandos individuais 
@bot.message_handler(func=lambda msg: msg.text[1:] in language_links)
def enviar_link(msg):
    linguagem = msg.text[1:]  # Remove o "/"
    bot.reply_to(msg, language_links[linguagem])

#comando para fala mais sobre mim
@bot.message_handler(commands=['dev'])
def dev(msg):
    url = 'https://media.licdn.com/dms/image/v2/D4D03AQGKJsERPgy4WA/profile-displayphoto-shrink_400_400/B4DZdC.MncG8Ag-/0/1749175292579?e=1755734400&v=beta&t=uMuwBPDLREbtIMUss7Iq1rPCRGrN3e0puBX__aPk4AA'
    legenda = (
        "👨‍💻 <b>Ismar Neto</b>\n\n"
        "🤓 Desenvolvedor em formação apaixonado por tecnologia e criatividade digital.\n"
        "👉 <a href='https://linktr.ee/ismar.dev'>Meus links</a>"
    )
    bot.send_photo(msg.chat.id, photo=url, caption=legenda, parse_mode='HTML')

    
# fala que a mensagem nao reconhecida
@bot.message_handler(func=lambda msg: True)
def fallback(msg):
    bot.reply_to(msg, "❌ Comando não reconhecido.\nDigite /comandos para ver a lista disponível.")

# o bot funciona
bot.infinity_polling()
