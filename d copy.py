import telebot

b = 1
a = """
я хз что надо делать и спамит тоже не интересно поэтому вот

я Андрей Абидулин поэтому если ты не ко мне то можешь идти от сюда и по скорее
ну а если ты всётаки ко мне я тебе очень сожелею

я учусь на программиста так что если ты хочешь что бы я тебе что то ответил то без печенек и кофе можешь даже не писать

мой номер телефона: 8 917 832 66 36

если ты хочешь позвонить мне то даже не пытайся у меня 34/9 беззвучный

"""

token = "6958502682:AAF6IT63Qq9sYUb9GnjrI_QSO80w1LiQC1M"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def main(message):
    global a
    if b == 1:
        bot.send_message(message.from_user.id, a)
        b = 0
    if message.text.lower.find("печеньки")+1:
        if message.text.lower.find("кофе")+1:
            bot.send_message(message.from_user.id, "мы ответим вам после небольшой паузы ту туту туту ту ту-ту-ту абонент временно не доступен")
        else:
            bot.send_message(message.from_user.id, "а кофе где?")
    if message.text.lower.find("кофе")+1:
        if message.text.lower.find("печеньки")+1:
            pass
        else:
            bot.send_message(message.from_user.id, "а печеньки где?")
    if message.text.lower.find("шахматы"):
        bot.send_message(message.from_user.id, "вообще я шахматист и у меня 1479 рейтинг кстати большенство")




bot.polling(none_stop=True, interval=0, timeout=120)