import logging
import os
import random
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup as BeautifulSnoop

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROBA = 0.1

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Lecture de la clé
key = os.environ["CLE_TG"]


def liberer_la_culture(sp_url):
    """
        GROS ! TA VIE PRIVEE !
    """
    sp_response = urlopen(sp_url)
    sp_html = sp_response.read()
    sp_soup = BeautifulSnoop(sp_html, "lxml")
    title = re.sub('on Spotify', '', re.sub(', a song by', ' - ', sp_soup.title.text))

    yt_url = "https://www.youtube.com/results?search_query=" + title.replace(' ', '+')
    yt_response = urlopen(yt_url)
    yt_html = yt_response.read()
    yt_soup = BeautifulSnoop(yt_html, "lxml")
    urls = yt_soup.findAll(attrs={'class': 'yt-uix-tile-link'})

    return 'Tiens gros ! Ça reste entre nous. \n\nhttps://www.youtube.com' + urls[0]['href']

def start(bot, update):
    """
        Dadadadam !
        C'est le maman baisant D O double G qui rentre sur ton groupe !
    """
    chat_id = update.message.chat_id
    message = "SALUT MON P'TIT COCO ! QU'EST CE QUE JE TE SERS ?!"
    bot.sendMessage(chat_id, text=message)


def suisjeouvert(bot, update):
    """
        GROS ! REGARDE LES PUTAINS D'HORAIRES SI T'AS FAIM !
    """
    # TODO : Réimplémenter quand il sera ouvert, en récupérant ses horaires
    chat_id = update.message.chat_id
    message = "Désolé gros ! J'ai fermé à cause du FN.\nT'inquiète, je reviens bientôt avec des LONG BURGERS !!!!"
    bot.sendMessage(chat_id, text=message)


def musique(bot, update):
    """
        OK LES P'TITS PÉPÈRES Y'A UNE CANETTE À GAGNER !
    """
    chat_id = update.message.chat_id

    url = "https://www.youtube.com/results?search_query=snoop+dogg"
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSnoop(html, "lxml")
    urls = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
    message = 'SBREEEEEEEEEH !\n\nhttps://www.youtube.com' + random.choice(urls)['href']

    bot.sendMessage(chat_id, text=message)


def ecouter(bot, update):
    """
        QU'EST CE QU'IL Y A ?! J'AI PAS LE DROIT DE M'INCRUSTER DANS LES
        CONVERSATIONS ?! PARDON MADAME !
    """
    # TODO : Ajouter plus de répliques gros !
    options = {'végé': "T'aimes ça hein ? SODOMITE !",
               'racisme': "Le mec il avait une noix de coco, y'a un noir qui s'est ramené et SBREEEEH !!! J'te mens pas gros !",
               '24': "DES BUS JUSQU'À FOURVIERE GROS ! J'TE MENS PAS GROS !",
               'tacos': "Un sodovégé supplément foutre, comme d'hab ?",
               'drogue': "PARDON MADAME !!! DÉFORMATION PROFESSIONNELLE !",
               'direct': 'DIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIRECT !!!',
               'virilité': '3 trucs pour être viril :  \n- Se battre\n- Manger de la viande\n- Péter'}

    for mot in update.message.text.split():
        if "open.spotify.com/track/" in mot:
            update.message.reply_text(liberer_la_culture(mot))
            return

    if random.random() < PROBA:
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', update.message.text,
                      flags=re.MULTILINE)
        lower_text = [mot.lower() for mot in text.split()]
        for mot in lower_text:
            if mot in options.keys():
                update.message.reply_text(options[mot])
                break


updater = Updater(key)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('musique', musique))
dispatcher.add_handler(CommandHandler('suisjeouvert', suisjeouvert))
dispatcher.add_handler(MessageHandler(Filters.text, ecouter))


updater.start_polling()
updater.idle()
