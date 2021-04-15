import random, re
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from ROBOT import dispatcher
from ROBOT.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler

re


@run_async
def copypasta(bot: Bot, update: Update):
    message = update.effective_message
    emojis = ["😂", "😭", "😡", "😂", "👌", "✌", "💞", "👍", "👌", "💯", "🎶", "👀", "😂", "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩", "😏", "👉👌", "👀", "👅", "😩", "🚰"]
    reply_text = random.choice(emojis)
    b_char = random.choice(message.reply_to_message.text).lower() # choose a random character in the message to be substituted with 🅱️
    for c in message.reply_to_message.text:
        if c == " ":
            reply_text += random.choice(emojis)
        elif c in emojis:
            reply_text += c
            reply_text += random.choice(emojis)
        elif c.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(random.getrandbits(1)):
                reply_text += c.upper()
            else:
                reply_text += c.lower()
    reply_text += random.choice(emojis)
    message.reply_to_message.reply_text(reply_text)



@run_async
def bmoji(bot: Bot, update: Update): #🅱️
    message = update.effective_message
    reply_text = re.sub(r'(r|R)', "🅱️", message.reply_to_message.text)
    reply_text = re.sub(r'(p|P)', "🅱️", reply_text)
    reply_text = re.sub(r'(n|N)', "🅱️", reply_text)
    message.reply_to_message.reply_text(reply_text)

@run_async
def clapmoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "👏 "
    for i in message.reply_to_message.text:
        if i == " ":
            reply_text += " 👏 "
        else:
            reply_text += i
    reply_text += " 👏"
    message.reply_to_message.reply_text(reply_text)
    
@run_async
def angrymoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "😡 "
    for i in message.reply_to_message.text:
        if i == " ":
            reply_text += " 😡 "
        else:
            reply_text += i
    reply_text += " 😡"
    message.reply_to_message.reply_text(reply_text)

@run_async
def crymoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "😭 "
    for i in message.reply_to_message.text:
        if i == " ":
            reply_text += " 😭 "
        else:
            reply_text += i
    reply_text += " 😭"
    message.reply_to_message.reply_text(reply_text)
    
    
@run_async
def owo(bot: Bot, update: Update):
    message = update.effective_message
    faces = ['(・`ω´・)',';;w;;','owo','UwU','>w<','^w^','\(^o\) (/o^)/','( ^ _ ^)∠☆','(ô_ô)','~:o',';-;', '(*^*)', '(>_', '(˵ ͡° ͜ʖ ͡°˵)','✺◟( ͡° ͜ʖ ͡°)◞✺', '(≡^∇^≡)', 'o(〃＾▽＾〃)o', 'ヾ(＾-＾)ノ', '(❁´◡`❁)', '(≧∇≦)/', '(๑˃̵ ᴗ ˂̵)و', '(♥_♥)', '*(^O^)*', '((+_+))']
    reply_text = re.sub(r'(r|l)', "w", message.reply_to_message.text)
    reply_text = re.sub(r'(R|L)', 'W', reply_text)
    reply_text = re.sub(r'n([aeiou])', r'ny\1', reply_text)
    reply_text = re.sub(r'N([aeiouAEIOU])', r'Ny\1', reply_text)
    reply_text = re.sub(r'\!+', ' ' + random.choice(faces), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += ' ' + random.choice(faces)
    message.reply_to_message.reply_text(reply_text)

def shrug(bot: Bot, update: Update):
    reply_msg = "¯\_(ツ)_/¯"
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(reply_msg)
    else:
        message.reply_text(reply_msg, quote=True)
        
@run_async
def me_too(bot: Bot, update: Update):
    message = update.effective_message
    if random.randint(0, 100) > 60:
        reply = random.choice(["Me too thanks", "Haha yes, me too", "Same lol", "Me irl"])
        message.reply_text(reply)

__help__ = "many memz"  
__mod_name__ = "Memes"

COPYPASTA_HANDLER = DisableAbleCommandHandler("copypasta", copypasta)
COPYPASTA_ALIAS_HANDLER = DisableAbleCommandHandler("😂", copypasta)
CLAPMOJI_HANDLER = DisableAbleCommandHandler("clapmoji", clapmoji)
CLAPMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("👏", clapmoji)
ANGRYMOJI_HANDLER = DisableAbleCommandHandler("angrymoji", angrymoji)
ANGRYMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("😡", angrymoji)
CRYMOJI_HANDLER = DisableAbleCommandHandler("crymoji", crymoji)
CRYMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("😭", crymoji)
BMOJI_HANDLER = DisableAbleCommandHandler("🅱️", bmoji)
BMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("️b", bmoji)
OWO_HANDLER = DisableAbleCommandHandler("owo", owo)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
ME_TOO_THANKS_HANDLER = DisableAbleRegexHandler(r"(?i)me too", me_too, friendly="me_too")

dispatcher.add_handler(COPYPASTA_HANDLER)
dispatcher.add_handler(COPYPASTA_ALIAS_HANDLER)
dispatcher.add_handler(CLAPMOJI_HANDLER)
dispatcher.add_handler(CLAPMOJI_ALIAS_HANDLER)
dispatcher.add_handler(ANGRYMOJI_HANDLER)
dispatcher.add_handler(ANGRYMOJI_ALIAS_HANDLER)
dispatcher.add_handler(CRYMOJI_HANDLER)
dispatcher.add_handler(CRYMOJI_ALIAS_HANDLER)
dispatcher.add_handler(BMOJI_HANDLER)
dispatcher.add_handler(BMOJI_ALIAS_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(ME_TOO_THANKS_HANDLER)
