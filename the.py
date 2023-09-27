import argparse
import random
import socket
import threading
import telebot
from telebot import types

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", type=str, help="Host ip")
ap.add_argument("-p", "--port", type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

proxies = [
    "socks5://41.65.103.27:1976",
    "http://89.43.31.134:3128",
    "http://80.190.74.13:8000",
    "http://115.132.32.91:8080",
    "http://15.204.161.192:18080",
    "http://201.91.82.155:3128",
    "http://103.17.77.5:3128",
    "http://43.133.136.208:8800",
    "http://34.154.161.152:80",
    "http://115.127.23.130:8674"
]

bot = telebot.TeleBot("6229938354:AAH3I0u4httA0ERatlFY1cY_JI-pr8UAtsE", proxy=random.choice(proxies))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_udp = types.KeyboardButton('UDP Flood')
    btn_tcp = types.KeyboardButton('TCP Flood')
    markup.add(btn_udp, btn_tcp)
    bot.send_message(message.chat.id, "PROTOCOL:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.text == 'UDP Flood':
        bot.send_message(message.chat.id, "Введите IP адрес:")
        bot.register_next_step_handler(message, get_ip_udp)
    elif message.text == 'TCP Flood':
        bot.send_message(message.chat.id, "Введите IP адрес:")
        bot.register_next_step_handler(message, get_ip_tcp)
    else:
        bot.send_message(message.chat.id, "error")

def get_ip_udp(message):
    global ip
    ip = message.text
    bot.send_message(message.chat.id, "Введите PORT:")
    bot.register_next_step_handler(message, get_port_udp)

def get_port_udp(message):
    global port
    port = int(message.text)
    run_threaded_attack('udp')
    bot.send_message(message.chat.id, "done")

def get_ip_tcp(message):
    global ip
    ip = message.text
    bot.send_message(message.chat.id, "Введите PORT:")
    bot.register_next_step_handler(message, get_port_tcp)

def get_port_tcp(message):
    global port
    port = int(message.text)
    run_threaded_attack('tcp')
    bot.send_message(message.chat.id, "done")

def run_udp_attack():
    # Ваш код для атаки UDP
    pass

def run_tcp_attack():
    # Ваш код для атаки TCP
    pass

def run_threaded_attack(attack_type):
    # Ваш код для многопоточной атаки
    pass

bot.polling()
