import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8935586994:AAHdm73I8XF-aHW3BkBMtm57mfhMfcUZDOs"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

START_TEXT = "Xush kelibsiz!"

def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            "Dukonga kirish",
            web_app=WebAppInfo(url="https://mavo-miniapp.vercel.app")
        )
    )
    return keyboard

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        START_TEXT,
        reply_markup=start_keyboard()
    )

print("Bot ishga tushdi...")
bot.infinity_polling()