import threading
import telebot
from funcoes import CategoriaProdutos
from scrapping import dados_produtos
import telebot
from telebot import types
import schedule
import time
import logging
from funcoes import CategoriaProdutos
from telebot.types import ReplyKeyboardMarkup
from scrapping import Extrair


#tags
Batman = CategoriaProdutos('BATMAN')
Superman = CategoriaProdutos('SUPERMAN')
Maravilha = CategoriaProdutos('MULHER-MARAVILHA')
Lanterna_Verde = CategoriaProdutos('LANTERNA VERDE')
Constantine = CategoriaProdutos('HELLBLAZER')
LigadaJustiça = CategoriaProdutos('LIGA DA JUSTIÇA')
Sandman = CategoriaProdutos('SANDMAN')
Lucifer = CategoriaProdutos('LÚCIFER')
Alvo_Humano = CategoriaProdutos('ALVO HUMANO')
Mulher_Gato = CategoriaProdutos('MULHER GATO')
Asa_Noturna = CategoriaProdutos('ASA NOTURNA')
Aquaman = CategoriaProdutos('AQUAMAN')

Extrair()

def l():
    for produto in dados_produtos:
        nome = produto['Nome'].upper()
        if "BATMAN" in produto["Nome"]:
         Batman.adicionar_tags(produto)
        elif "SUPERMAN" in produto["Nome"]:
            Superman.adicionar_tags(produto)
        elif "MULHER MARAVILHA" in produto["Nome"]:
            Maravilha.adicionar_tags(produto)
        elif "LANTERNA VERDE" in produto["Nome"]:
            Lanterna_Verde.adicionar_tags(produto)
        elif "HELLBLAZER" in produto["Nome"]:
            Constantine.adicionar_tags(produto)
        elif "LIGA DA JUSTIÇA" in produto["Nome"]:
            LigadaJustiça.adicionar_tags(produto)
        elif "SANDMAN" in produto["Nome"]:
            Sandman.adicionar_tags(produto)
        elif "LUCIFER" in produto["Nome"]:
            Lucifer.adicionar_tags(produto)
        elif "ALVO" in produto["Nome"]:
         Alvo_Humano.adicionar_tags(produto)
        elif "MULHER GATO" in produto["Nome"]:
            Mulher_Gato.adicionar_tags(produto)
        elif "ASA NOTURNA" in produto["Nome"]:
         Asa_Noturna.adicionar_tags(produto)
        elif "AQUAMAN" in produto["Nome"]:
            Aquaman.adicionar_tags(produto)

l()

bot = telebot.TeleBot('7773874902:AAHvKjQ-Ifb2WtsyBiHjeYGL-lWtY4nf70s') 
dados = dados_produtos
@bot.message_handler(commands=['start'])
def start(msg:telebot.types.Message): # type: ignore
  texto =  f'Olá seja bem vindo, Gostaria de ver todas as promoções ou usar tags?'
  bot.send_message(msg.chat.id, texto)
  time.sleep(1)
  texto = '''
/Todas
/Tags
  '''
  bot.reply_to(msg, texto)

   

@bot.message_handler(commands=['Todas'])
def Todas(msg:telebot.types.Message): # type: ignore
  mensagem = ''
  for produto in dados_produtos:
      mensagem += f"{produto['Nome']} | Preço: {produto['Preço']} | Preço Antigo:{produto['Preço Antigo']} \n {produto['Link']} \n"
  bot.send_message(msg.chat.id, mensagem)

@bot.message_handler(commands=['Tags'])
def Tags(msg:telebot.types.Message): # type: ignore
   texto = f'Abaixo a Lista de Tags Disponiveis'
   bot.send_message(msg.chat.id, texto)
   time.sleep(1)
   texto = '''
/Batman
/Superman
/Mulher_Maravilha
/Lanterna_Verde
/Constantine
/LigaDaJustiça
/Sandman
/Lucifer
/Alvo_Humano
/Mulher_Gato
/Asa_Noturna
/Aquaman
'''
   bot.send_message(msg.chat.id, texto)
   

@bot.message_handler(commands=['Batman'])
def mostrar_batman(msg:telebot.types.Message): # type: ignore
    texto = Batman.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Superman'])
def mostrar_Superman(msg:telebot.types.Message): # type: ignore
    texto = Superman.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Mulher_Maravilha'])
def mostrar_Mulher_Maravilha(msg:telebot.types.Message): # type: ignore
    texto = Maravilha.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Lanterna_Verde'])
def mostrar_Lanterna_Verde(msg:telebot.types.Message): # type: ignore
    texto = Lanterna_Verde.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Constantine'])
def mostrar_Constantine(msg:telebot.types.Message): # type: ignore
    texto = Constantine.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Liga_da_Justiça'])
def mostrar_Liga_da_Justiça(msg:telebot.types.Message): # type: ignore
    texto = LigadaJustiça.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Sandman'])
def mostrar_Sandman(msg:telebot.types.Message): # type: ignore
    texto = Sandman.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Lucifer'])
def mostrar_Lucifer(msg:telebot.types.Message): # type: ignore
    texto = Lucifer.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Alvo_Humano'])
def mostrar_Alvo_Humano(msg:telebot.types.Message): # type: ignore
    texto = Alvo_Humano.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Mulher_Gato'])
def mostrar_Mulher_Gato(msg:telebot.types.Message): # type: ignore
    texto = Mulher_Gato.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Asa_Noturna'])
def mostrar_Asa_Noturna(msg:telebot.types.Message): # type: ignore
    texto = Asa_Noturna.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)

@bot.message_handler(commands=['Aquaman'])
def mostrar_Aquaman(msg:telebot.types.Message): # type: ignore
    texto = Aquaman.mostrar()
    bot.send_message(msg.chat.id, texto)
    time.sleep(1)
    texto = '/start'
    bot.send_message(msg.chat.id, texto)


    

if __name__ == '__main__':
    bot.infinity_polling()