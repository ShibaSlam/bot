import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Ваш токен для бота
TOKEN = '7220141979:AAHKYh3QkNxI7u_Hl7XjztVwH81jp767Wqg'

# Функция для старта
def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    add_user(user_id, username)  # Запишите пользователя в базу данных

    # Сообщение с кнопкой "Play"
    message_text = '''
    🌟 **Hey, everyone!** 🌟  
    🎮 Are you ready for an exciting adventure? Join us in **ShibaSlam**! 🐕💰  
    🌈 Play now and earn amazing rewards! 🌟  
    🚀 Compete with friends, level up, and have a blast! 🎉  
    💸 Don’t miss out on the fun and the chance to earn some cash! 💵  
    👉 Click the button below to get started and let the games begin! 🔗✨  
    '''

    # Кнопка "Play"
    keyboard = [[InlineKeyboardButton("Play", callback_data='play')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message_text,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

# Обработчик нажатия на кнопку "Play"
def play_game(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()  # Подтверждение нажатия на кнопку

    query.edit_message_text(
        text="🎮 Welcome to **ShibaSlam**! Let the game begin! 🕹️"
    )

# Функция для добавления пользователя
def add_user(user_id, username):
    # Логика для добавления пользователя в базу данных
    pass

# Запуск бота
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(play_game, pattern='play'))

updater.start_polling()
updater.idle()