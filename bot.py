
import telebot

bot = telebot.TeleBot('6237995977:AAEmGx9UNbXTN6E1_P1oduowkaxJIwwnq40')

@bot.message_handler(func=lambda message: True)
def handle_button(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton('اسيا سيل 🚩 ', callback_data='button1')
    button2 = telebot.types.InlineKeyboardButton(' اثير 🚩', callback_data='button2')
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, 'Please press a button:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'button1':
        bot.answer_callback_query(callback_query_id=call.id, text='You pressed Button 1!')
        bot.send_message(call.message.chat.id, 'البوت مدفوع وليس مجاني ، يرجى مراسلة المطور للاشتراك 🚩 @TFFF_F .')
    elif call.data == 'button2':
        bot.answer_callback_query(callback_query_id=call.id, text='You pressed Button 2!')
        bot.send_message(call.message.chat.id, 'البوت مدفوع وليس مجاني ، يرجى مراسلة المطور للاشتراك 🚩 @TFFF_F.')

bot.polling()