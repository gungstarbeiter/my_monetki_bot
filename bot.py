#!/usr/bin/python3
import telebot
from telebot.types import Message
from telebot import types
import requests

TOKEN = '1040156296:AAF_laopxr9kUmgcyXbW_J20CxjwuwGVPnk'

bot = telebot.TeleBot(TOKEN)
api = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=EDC,DOGE&tsyms=USD,RUR&api_key=c178d4730110d00770f3362944c77b0b6caf2bee7dbb1b3b07bb780210d999bb"


markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('💰Курсы монеток💰')
markup.row(itembtn1)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет!☺️', reply_markup=markup, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def send_table(message: Message):
    if '💰Курсы монеток💰' in message.text:
        bot.reply_to(message, 'Ща!️', reply_markup=markup, parse_mode='HTML')

        raw_data = requests.get(api).json()
        json_edc = raw_data['EDC']
        json_doge = raw_data['DOGE']

        json_edc_usd = json_edc ['USD']
        json_edc_rur = json_edc ['RUR']
        json_doge_usd = json_doge ['USD']
        json_doge_rur = json_doge ['RUR']

        edc_usd = str(json_edc_usd)
        edc_rur = str(json_edc_rur)
        doge_usd = str(json_doge_usd)
        doge_rur = str(json_doge_rur)

        bot.send_message(message.chat.id, text="🤓 Курсы такие:\n\n"
           +" <b> EDC </b>\n"
           +edc_usd+" $\n"
           +edc_rur+" ₽\n\n"
           +"<b> DOGE </b>\n"
           +doge_usd+" $\n"
           +doge_rur+" ₽", parse_mode='HTML', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Чего?😳', parse_mode='HTML', reply_markup=markup)


bot.polling()
