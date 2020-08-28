import os
import ptbot
from pytimeparse import parse

def reply(text):
    bot.create_countdown(parse(text), notify_progress, message_id=bot.send_message(chat_id, 'Таймер запущен на {} секунд(ы)'.format(parse(text))), total_sec=parse(text))
    bot.create_timer(parse(text), notify)

def notify():
    bot.send_message(chat_id, 'Время вышло.')

def notify_progress(secs_left, message_id, total_sec):
    new_message = 'Осталось {} секунд(ы) \n'.format(secs_left) + render_progressbar(total_sec, secs_left)
    bot.update_message(chat_id, message_id, new_message)
    
def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)    

if __name__ == "__main__":
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")
    bot = ptbot.Bot(token)
    bot.send_message(chat_id, 'Бот запущен! \nНа сколько ставить таймер?')
    bot.reply_on_message(reply)
    bot.run_bot()