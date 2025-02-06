import telebot
import json

api = "7709844145:AAG4IPlA9j6W-QwlCwR3K8SiAyCY_TPMxFE"
bot = telebot.TeleBot(api)

startm = """Welcome to Bot! 

Use the buttons to see more."""

# Function to load JSON data
def load_json(filename):
    with open(filename, "r") as file:
        return json.load(file)["getaway"]

@bot.message_handler(commands=['start'])
def start_msg(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton('Futures', callback_data='btn1')
    btn2 = telebot.types.InlineKeyboardButton('Help', callback_data='btn2')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, startm, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "btn1":
        markup = telebot.types.InlineKeyboardMarkup()
        auth_btn = telebot.types.InlineKeyboardButton('Auth', callback_data='auth')
        charged_btn = telebot.types.InlineKeyboardButton('Charged', callback_data='charged')
        back_btn = telebot.types.InlineKeyboardButton('⬅ Back', callback_data='back')
        markup.add(auth_btn, charged_btn)
        markup.add(back_btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="How Can I Assist You Today?", reply_markup=markup)

    elif call.data == "btn2":  
        markup = telebot.types.InlineKeyboardMarkup()
        back_btn = telebot.types.InlineKeyboardButton('⬅ Back', callback_data='back')
        markup.add(back_btn)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text="Help section is under development. Please visit @CarderClubSupportBot for assistance.", reply_markup=markup)

    elif call.data == "auth":
        auth_gates = load_json("authgates.json")
        auth_text = "**Available Authentication Gateways:**\n"
        for gate in auth_gates:
            auth_text += f"/{gate['cmd']} - {gate['gate']}\n"
        
        bot.send_message(call.message.chat.id, auth_text, parse_mode="Markdown")

    elif call.data == "charged":
        charge_gates = load_json("chargegates.json")
        charge_text = "**Available Charged Gateways:**\n"
        for gate in charge_gates:
            charge_text += f"/{gate['cmd']} - {gate['gate']}\n"
        
        bot.send_message(call.message.chat.id, charge_text, parse_mode="Markdown")

    elif call.data == "back":
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton('Futures', callback_data='btn1')
        btn2 = telebot.types.InlineKeyboardButton('Help', callback_data='btn2')
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                              text=startm, reply_markup=markup)

bot.polling()
